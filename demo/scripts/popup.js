document.addEventListener('DOMContentLoaded', function () {
    const alpha = 0.7; // Alpha value for colors

    fetch(chrome.runtime.getURL('data/teams.json'))
        .then(response => response.json())
        .then(teamMap => {
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                var tab = tabs[0];
                var title = tab.title;

                // Preprocess the title: remove special characters and split into words
                var cleanedTitle = title.replace(/[^a-zA-Z0-9\s&]/g, '');
                var titleWords = cleanedTitle.split(/\s+/);

                // Generate n-grams from title words
                var ngrams = [];
                var maxN = 3; // Maximum n-gram length
                for (var i = 0; i < titleWords.length; i++) {
                    for (var n = 1; n <= maxN && i + n <= titleWords.length; n++) {
                        var ngram = titleWords.slice(i, i + n).join(' ');
                        ngrams.push(ngram.toLowerCase());
                    }
                }

                // Look through the teamMap for matching n-grams
                var matchedTeams = [];
                ngrams.forEach(function (ngram) {
                    for (var team in teamMap) {
                        if (teamMap[team].names.includes(ngram)) {
                            matchedTeams.push(team);
                        }
                    }
                });

                // Remove duplicate teams
                matchedTeams = [...new Set(matchedTeams)];

                // Display the matched teams
                if (matchedTeams.length >= 2) {
                    var team1 = matchedTeams[0];
                    var team2 = matchedTeams[1];
                    var message = capitalize(team1) + ' vs ' + capitalize(team2);
                    document.getElementById('message').textContent = message;

                    // Show the Winning Probabilities and Stats cards
                    document.getElementById('winning-probabilities-card').style.display = 'block';
                    document.getElementById('stats-card').style.display = 'block';

                    // Prediction spinner
                    document.getElementById('prediction-spinner').style.display = 'block';
                    document.getElementById('prediction-chart-container').style.display = 'none';

                    // Show the spinner while fetching stats
                    document.getElementById('stats-spinner').style.display = 'block';
                    document.getElementById('stats-boxes-container').style.display = 'none';

                    // Get prediction
                    fetch('http://127.0.0.1:8386/predict', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ team1: team1, team2: team2 })
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        var ctx = document.getElementById('predictionChart').getContext('2d');
                        var chart = new Chart(ctx, {
                            type: 'bar',
                            data: {
                                labels: [capitalize(team1), 'Draw', capitalize(team2)],
                                datasets: [{
                                    label: 'Winning Probability (%)',
                                    data: [
                                        (data.win * 100).toFixed(2), 
                                        (data.draw * 100).toFixed(2), 
                                        (data.lose * 100).toFixed(2)
                                    ],
                                    backgroundColor: [
                                        teamMap[team1].color.replace('ALPHA', alpha), // Win color (team1 color)
                                        'rgba(128, 128, 128, ' + alpha + ')', // Draw color (grey)
                                        teamMap[team2].color.replace('ALPHA', alpha)  // Lose color (team2 color)
                                    ],
                                    borderColor: [
                                        teamMap[team1].color.replace('ALPHA', '1'), // Win color (team1 color)
                                        'rgba(128, 128, 128, 1)', // Draw color (grey)
                                        teamMap[team2].color.replace('ALPHA', '1')  // Lose color (team2 color)
                                    ],
                                    borderWidth: 1
                                }]
                            },
                            options: {
                                layout: {
                                    padding: {
                                        top: 20
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        display: false
                                    }
                                },
                                plugins: {
                                    title: {
                                        display: false,
                                        text: 'Winning Probability (%)',
                                    },
                                    legend: {
                                        display: false
                                    },
                                    tooltip: {
                                        callbacks: {
                                            label: function(context) {
                                                return context.dataset.label + ': ' + context.raw + '%';
                                            }
                                        }
                                    },
                                    datalabels: {
                                        anchor: 'end',
                                        align: 'end',
                                        formatter: function(value) {
                                            return value + '%';
                                        }
                                    }
                                }
                            },
                            plugins: [ChartDataLabels]
                        });
                        // Hide the spinner and show the chart
                        document.getElementById('prediction-spinner').style.display = 'none';
                        document.getElementById('prediction-chart-container').style.display = 'block';
                    })
                    .catch(error => {
                        console.error('Error fetching prediction:', error);
                        document.getElementById('prediction-spinner').style.display = 'none';
                        document.getElementById('prediction-chart-container').textContent = 'Error loading prediction.';
                    });

                    // Get stats
                    fetch('http://127.0.0.1:8386/lookup', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ team1: team1, team2: team2 })
                    })
                    .then(response => response.json())
                    .then(stats => {
                        var statsContainer = document.getElementById('stats-boxes-container');
                        statsContainer.innerHTML = '';

                        var statsLabels = Object.keys(stats[team1]);
                        statsLabels.forEach(stat => {
                            var team1Stat = stats[team1][stat];
                            var team2Stat = stats[team2][stat];

                            var statBox = document.createElement('div');
                            statBox.className = 'mb-3';

                            var canvas = document.createElement('canvas');
                            canvas.height = 50;
                            statBox.appendChild(canvas);
                            statsContainer.appendChild(statBox);

                            var ctx = canvas.getContext('2d');
                            var maxValue = Math.max(Math.abs(team1Stat), Math.abs(team2Stat));
                            new Chart(ctx, {
                                type: 'bar',
                                data: {
                                    labels: [capitalize(stat)],
                                    datasets: [
                                        {
                                            label: capitalize(team1),
                                            data: [-team1Stat],
                                            backgroundColor: teamMap[team1].color.replace('ALPHA', alpha),
                                            borderColor: teamMap[team1].color.replace('ALPHA', '1'),
                                            borderWidth: 1,
                                            stack: "Stack 0",
                                            datalabels: {
                                                anchor: 'start',
                                                align: 'start',
                                                formatter: function(value) {
                                                    return Math.abs(value);
                                                }
                                            },
                                        },
                                        {
                                            label: capitalize(team2),
                                            data: [team2Stat],
                                            backgroundColor: teamMap[team2].color.replace('ALPHA', alpha),
                                            borderColor: teamMap[team2].color.replace('ALPHA', '1'),
                                            borderWidth: 1,
                                            stack: "Stack 0",
                                            datalabels: {
                                                anchor: 'end',
                                                align: 'end',
                                                formatter: function(value) {
                                                    return Math.abs(value);
                                                }
                                            },
                                        }
                                    ]
                                },
                                options: {
                                    indexAxis: 'y',
                                    layout: {
                                        padding: {
                                            left: 30,
                                            right: 30
                                        }
                                    },
                                    scales: {
                                        x: {
                                            beginAtZero: true,
                                            min: -maxValue,
                                            max: maxValue,
                                            ticks: {
                                                callback: function(value) {
                                                    return Math.abs(value);
                                                },
                                                display: false
                                            }
                                        },
                                        y: {
                                            beginAtZero: true,
                                            grid: {
                                                display: false
                                            },
                                            ticks: {
                                                display: false
                                            }
                                        }
                                    },
                                    plugins: {
                                        legend: {
                                            display: false
                                        },
                                        title: {
                                            text: capitalize(stat),
                                            display: true,
                                            padding: {
                                                bottom: -5
                                            }
                                        },
                                        tooltip: {
                                            callbacks: {
                                                label: (c) => {
                                                    const value = Number(c.raw);
                                                    const positiveOnly = value < 0 ? -value : value;
                                                    return `${c.dataset.label}: ${positiveOnly}`;
                                                }
                                            }
                                        },
                                    }
                                },
                                plugins: [ChartDataLabels]
                            });
                        });

                        // Hide the spinner and show the stats boxes
                        document.getElementById('stats-spinner').style.display = 'none';
                        document.getElementById('stats-boxes-container').style.display = 'block';
                    })
                    .catch(error => {
                        console.error('Error fetching stats:', error);
                        document.getElementById('stats-spinner').style.display = 'none';
                        document.getElementById('stats-boxes-container').textContent = 'Error loading stats.';
                    });
                } else {
                    document.getElementById('message').textContent = 'Teams not recognized.';
                }
            });
        })
        .catch(error => console.error('Error loading team data:', error));
});

function capitalize(str) {
    return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}