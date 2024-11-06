# Match Attributes

> [!IMPORTANT]  
> CSV file are converted from a dictionary into a DataFrame, using `json` and `pandas` module.
> Due to the unordered nature of Python dictionary, columns in CSV file may not appear in the
> order in the tables below.

## Common attributes

| Count | Attribute | Description |
| --- | --- | --- |
| 1 | match_id | Match ID |
| 2 | season | Season |
| 3 | date | Date and Time |
| 4 | ground | Stadium |
| 5 | duration | Duration (seconds) |
| 6 | outcome | Match Outcome (H/A/D) |

## Team attributes

Home and Away teams have attributes starting with `h_` and `a_` respectively. These prefixes have been stripped
in the making of this table.

| Count | Attribute | Description |
| --- | --- | --- |
| 1 | name | Team Name |
| 2 | team_id | Team ID |
| 3 | score | Team Final Score |
| 4 | formation | Team Formation |
| 5 | players | Player List |
| 6 | possession_percentage | Possession Percentage |
| 7 | backward_pass | Backward Passes |
| 8 | accurate_pass | Accurate Passes |
| 9 | touches | Total Touches |
| 10 | total_back_zone_pass | Total Back Zone Passes |
| 11 | total_pass | Total Passes |
| 12 | accurate_back_zone_pass | Accurate Back Zone Passes |
| 13 | final_third_entries | Final Third Entries |
| 14 | open_play_pass | Open Play Passes |
| 15 | successful_final_third_passes | Successful Final Third Passes |
| 16 | total_cross_nocorner | Total Crosses (Excluding Corners) |
| 17 | rightside_pass | Rightside Passes |
| 18 | won_tackle | Tackles Won |
| 19 | total_cross | Total Crosses |
| 20 | total_contest | Total Contests |
| 21 | total_final_third_passes | Total Final Third Passes |
| 22 | fwd_pass | Forward Passes |
| 23 | leftside_pass | Leftside Passes |
| 24 | long_pass_own_to_opp | Long Passes (Own to Opponent) |
| 25 | put_through | Through Balls |
| 26 | poss_won_att_3rd | Possession Won in Attacking Third |
| 27 | total_chipped_pass | Total Chipped Passes |
| 28 | total_fwd_zone_pass | Total Forward Zone Passes |
| 29 | total_long_balls | Total Long Balls |
| 30 | accurate_fwd_zone_pass | Accurate Forward Zone Passes |
| 31 | total_tackle | Total Tackles |
| 32 | crosses_18yard | Crosses into 18 Yard Box |
| 33 | blocked_pass | Blocked Passes |
| 34 | won_contest | Contests Won |
| 35 | ball_recovery | Ball Recoveries |
| 36 | poss_lost_all | Possession Lost (All) |
| 37 | duel_won | Duels Won |
| 38 | poss_lost_ctrl | Possession Lost (Control) |
| 39 | passes_right | Passes to the Right |
| 40 | pen_area_entries | Penalty Area Entries |
| 41 | successful_put_through | Successful Through Balls |
| 42 | touches_in_opp_box | Touches in Opponent's Box |
| 43 | aerial_won | Aerial Duels Won |
| 44 | total_flick_on | Total Flick-Ons |
| 45 | successful_open_play_pass | Successful Open Play Passes |
| 46 | accurate_chipped_pass | Accurate Chipped Passes |
| 47 | lost_corners | Corners Lost |
| 48 | poss_won_def_3rd | Possession Won in Defensive Third |
| 49 | total_clearance | Total Clearances |
| 50 | unsuccessful_touch | Unsuccessful Touches |
| 51 | effective_clearance | Effective Clearances |
| 52 | outfielder_block | Outfielder Blocks |
| 53 | duel_lost | Duels Lost |
| 54 | goal_kicks | Goal Kicks |
| 55 | challenge_lost | Challenges Lost |
| 56 | fk_foul_lost | Free Kick Fouls Lost |
| 57 | attempts_conceded_ibox | Attempts Conceded Inside Box |
| 58 | attempted_tackle_foul | Attempted Tackle Fouls |
| 59 | effective_head_clearance | Effective Head Clearances |
| 60 | head_clearance | Head Clearances |
| 61 | goals_conceded_ibox | Goals Conceded Inside Box |
| 62 | goals_conceded | Goals Conceded |
| 63 | total_throws | Total Throw-Ins |
| 64 | long_pass_own_to_opp_success | Successful Long Passes (Own to Opponent) |
| 65 | accurate_throws | Accurate Throw-Ins |
| 66 | accurate_long_balls | Accurate Long Balls |
| 67 | dispossessed | Times Dispossessed |
| 68 | attempts_ibox | Attempts Inside Box |
| 69 | att_assist_openplay | Attempt Assists from Open Play |
| 70 | passes_left | Passes to the Left |
| 71 | att_ibox_target | Attempts on Target Inside Box |
| 72 | total_att_assist | Total Attempt Assists |
| 73 | ontarget_scoring_att | On Target Scoring Attempts |
| 74 | att_lf_total | Total Left Foot Attempts |
| 75 | won_corners | Corners Won |
| 76 | att_lf_target | Left Foot Attempts on Target |
| 77 | att_openplay | Attempts from Open Play |
| 78 | total_scoring_att | Total Scoring Attempts |
| 79 | att_bx_left | Attempts from Box Left |
| 80 | poss_won_mid_3rd | Possession Won in Midfield Third |
| 81 | ontarget_att_assist | On Target Attempt Assists |
| 82 | att_bx_centre | Attempts from Box Centre |
| 83 | att_obox_blocked | Blocked Attempts Outside Box |
| 84 | att_rf_total | Total Right Foot Attempts |
| 85 | accurate_cross | Accurate Crosses |
| 86 | attempts_obox | Attempts Outside Box |
| 87 | att_corner | Corner Attempts |
| 88 | att_sv_high_centre | Attempts Saved High Centre |
| 89 | att_sv_low_left | Attempts Saved Low Left |
| 90 | total_corners_intobox | Total Corners into Box |
| 91 | att_rf_target | Right Foot Attempts on Target |
| 92 | corner_taken | Corners Taken |
| 93 | aerial_lost | Aerial Duels Lost |
| 94 | blocked_scoring_att | Blocked Scoring Attempts |
| 95 | accurate_corners_intobox | Accurate Corners into Box |
| 96 | att_obx_centre | Attempts Outside Box Centre |
| 97 | accurate_keeper_throws | Accurate Keeper Throws |
| 98 | keeper_throws | Keeper Throws |
| 99 | crosses_18yardplus | Crosses into 18 Yard Plus |
| 100 | accurate_cross_nocorner | Accurate Crosses (Excluding Corners) |
| 101 | fouled_final_third | Fouled in Final Third |
| 102 | contentious_decision | Contentious Decisions |
| 103 | penalty_won | Penalties Won |
| 104 | fk_foul_won | Free Kick Fouls Won |
| 105 | forward_goals | Goals by Forwards |
| 106 | att_lf_goal | Left Foot Goals |
| 107 | att_ibox_goal | Goals Inside Box |
| 108 | goals | Total Goals |
| 109 | first_half_goals | First Half Goals |
| 110 | att_goal_low_left | Goals Low Left |
| 111 | big_chance_scored | Big Chances Scored |
| 112 | att_pen_goal | Penalty Goals |
| 113 | total_launches | Total Launches |
| 114 | attempts_conceded_obox | Attempts Conceded Outside Box |
| 115 | accurate_goal_kicks | Accurate Goal Kicks |
| 116 | att_ibox_blocked | Blocked Attempts Inside Box |
| 117 | goals_openplay | Goals from Open Play |
| 118 | goal_assist_openplay | Goal Assists from Open Play |
| 119 | att_goal_low_centre | Goals Low Centre |
| 120 | goal_assist | Goal Assists |
| 121 | goal_assist_intentional | Intentional Goal Assists |
| 122 | interception | Interceptions |
| 123 | interception_won | Interceptions Won |
| 124 | effective_blocked_cross | Effective Blocked Crosses |
| 125 | blocked_cross | Blocked Crosses |
| 126 | goals_conceded_obox | Goals Conceded Outside Box |
| 127 | total_offside | Total Offsides |
| 128 | shot_off_target | Shots Off Target |
| 129 | att_miss_high | Missed Attempts High |
| 130 | att_ibox_miss | Missed Attempts Inside Box |
| 131 | big_chance_created | Big Chances Created |
| 132 | big_chance_missed | Big Chances Missed |
| 133 | att_cmiss_high | Missed Chances High |
| 134 | offtarget_att_assist | Off Target Attempt Assists |
| 135 | saves | Total Saves |
| 136 | saved_ibox | Saves Inside Box |
| 137 | subs_made | Substitutions Made |
| 138 | total_high_claim | Total High Claims |
| 139 | att_sv_low_right | Attempts Saved Low Right |
| 140 | good_high_claim | Good High Claims |
| 141 | total_yel_card | Total Yellow Cards |
| 142 | total_pull_back | Total Pull Backs |
| 143 | diving_save | Diving Saves |
| 144 | accurate_layoffs | Accurate Layoffs |
| 145 | total_layoffs | Total Layoffs |
| 146 | freekick_cross | Free Kick Crosses |
| 147 | att_one_on_one | One-on-One Attempts |
| 148 | att_bx_right | Attempts from Box Right |
| 149 | att_miss_high_right | Missed Attempts High Right |
| 150 | accurate_through_ball | Accurate Through Balls |
| 151 | total_through_ball | Total Through Balls |
| 152 | accurate_launches | Accurate Launches |
| 153 | hand_ball | Hand Balls |
| 154 | draws | Total Draws |
| 155 | pts_dropped_winning_pos | Points Dropped from Winning Position |
| 156 | pts_gained_losing_pos | Points Gained from Losing Position |
| 157 | accurate_pull_back | Accurate Pull Backs |
| 158 | shield_ball_oop | Shield Ball Out of Play |
| 159 | att_hd_total | Total Header Attempts |
| 160 | att_miss_right | Missed Attempts Right |
| 161 | att_hd_miss | Missed Header Attempts |
| 162 | att_setpiece | Set Piece Attempts |
| 163 | accurate_freekick_cross | Accurate Free Kick Crosses |
| 164 | att_hd_goal | Header Goals |
| 165 | defender_goals | Goals by Defenders |
| 166 | goal_assist_deadball | Goal Assists from Dead Ball |
| 167 | goal_assist_setplay | Goal Assists from Set Play |
| 168 | att_goal_high_centre | Goals High Centre |
| 169 | interceptions_in_box | Interceptions in Box |
| 170 | penalty_conceded | Penalties Conceded |
| 171 | penalty_faced | Penalties Faced |
| 172 | pen_goals_conceded | Penalty Goals Conceded |
| 173 | att_obox_miss | Missed Attempts Outside Box |
| 174 | att_lg_centre | Long Goals Centre |
| 175 | total_keeper_sweeper | Total Keeper Sweepers |
| 176 | accurate_keeper_sweeper | Accurate Keeper Sweepers |
| 177 | att_obox_goal | Goals Outside Box |
| 178 | att_miss_left | Missed Attempts Left |
| 179 | att_rf_goal | Right Foot Goals |
| 180 | att_cmiss_left | Missed Chances Left |
| 181 | att_sv_low_centre | Attempts Saved Low Centre |
| 182 | att_assist_setplay | Attempt Assists from Set Play |
| 183 | accurate_flick_on | Accurate Flick-Ons |
| 184 | overrun | Overruns |
| 185 | att_hd_target | Header Attempts on Target |
| 186 | midfielder_goals | Goals by Midfielders |
| 187 | att_obox_target | Attempts on Target Outside Box |
| 188 | att_goal_low_right | Goals Low Right |
| 189 | saved_obox | Saves Outside Box |
| 190 | subs_goals | Goals by Substitutes |
| 191 | att_goal_high_right | Goals High Right |
| 192 | total_fastbreak | Total Fast Breaks |
| 193 | att_fastbreak | Fast Break Attempts |
| 194 | shot_fastbreak | Fast Break Shots |
| 195 | wins | Total Wins |
| 196 | att_cmiss_right | Missed Chances Right |
| 197 | att_miss_high_left | Missed Attempts High Left |
| 198 | error_lead_to_goal | Errors Leading to Goal |
| 199 | att_obxd_right | Attempts Outside Box Right |
| 200 | clearance_off_line | Clearances Off the Line |
| 201 | att_freekick_total | Total Free Kick Attempts |
| 202 | att_obxd_left | Attempts Outside Box Left |
| 203 | att_freekick_target | Free Kick Attempts on Target |
| 204 | att_sv_high_left | Attempts Saved High Left |
| 205 | last_man_tackle | Last Man Tackles |
| 206 | losses | Total Losses |
| 207 | att_ibox_post | Attempts Hitting Post Inside Box |
| 208 | post_scoring_att | Scoring Attempts Hitting Post |
| 209 | att_post_high | Attempts Hitting Post High |
| 210 | hit_woodwork | Hit Woodwork |
| 211 | punches | Punches |
| 212 | att_post_left | Attempts Hitting Post Left |
| 213 | clean_sheet | Clean Sheets |
| 214 | att_sv_high_right | Attempts Saved High Right |
| 215 | att_obox_post | Attempts Hitting Post Outside Box |
| 216 | six_yard_block | Six Yard Blocks |
| 217 | error_lead_to_shot | Errors Leading to Shot |
| 218 | att_goal_high_left | Goals High Left |
| 219 | att_post_right | Attempts Hitting Post Right |
| 220 | own_goal_accrued | Own Goals Accrued |
| 221 | total_red_card | Total Red Cards |
| 222 | second_yellow | Second Yellow Cards |
| 223 | att_obx_left | Attempts Outside Box Left |
| 224 | att_ibox_own_goal | Own Goals Inside Box |
| 225 | own_goals | Own Goals |
| 226 | att_freekick_goal | Free Kick Goals |
| 227 | att_hd_post | Header Attempts Hitting Post |
| 228 | foul_throw_in | Foul Throw-Ins |
| 229 | att_cmiss_high_right | Missed Chances High Right |
| 230 | att_cmiss_high_left | Missed Chances High Left |
| 231 | att_freekick_miss | Missed Free Kick Attempts |
| 232 | goal_fastbreak | Fast Break Goals |
| 233 | fifty_fifty | Fifty-Fifty Challenges |
| 234 | successful_fifty_fifty | Successful Fifty-Fifty Challenges |
| 235 | penalty_save | Penalty Saves |
| 236 | att_pen_target | Penalty Attempts on Target |
| 237 | att_obx_right | Attempts Outside Box Right |
| 238 | att_pen_post | Penalty Attempts Hitting Post |
| 239 | att_freekick_post | Free Kick Attempts Hitting Post |
| 240 | att_obp_goal | Goals Outside Box |
| 241 | att_lg_left | Long Goals Left |
| 242 | att_lg_right | Long Goals Right |
| 243 | att_pen_miss | Missed Penalty Attempts |
| 244 | att_obox_own_goal | Own Goals Outside Box |
| 245 | rescinded_red_card | Rescinded Red Cards |

Total number of attributes: $6 + 245 \times 2 = 496$

The number of columns in our crawled data sheet is 495. There is no `h_rescinded_red_card` column, meaning no Home team in the 5 crawled seasons had any red card overturned.