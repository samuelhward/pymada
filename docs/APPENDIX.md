# Appendix

## 1. Upper Limit For Probability Space

Assuming only discretised units e.g. ships:

- the total number of actions for all ships:
    - each ship has N_s optional commands
    - adding another ship adds N_(s+1) possible commands 
    --> total number of action permutations is now N_s * N_(s+1)... 
    --> all permutations for all ships = multiplied_sum_over_SS'(N_available_actions_per_ship)
- this does not take activation order into account but activation order *is* another independent variable (assuming no special abilities affecting activation order):
    - if each player is isolated and can activate S ships then, over the course of a single turn, each player has S! total options for their activation pathway
    - however player activations alternate but player 1's current activation possibilities are independent of player 2's activation history (assuming no ships destroyed) 
    - thus for each of player 1's activation pathways we can claim it is possible for player 2 to choose any corresponding pathway; they are effectively independent  
    - hence the total number of activation combinatiosn is S!S'!
- N_available_actions_per_ship can be estimated by considering the following number of actions and their possible states:
    - command dial variations = 4
    - command dial activation choice = 2
    - number valid targets N_targets 
    - number valid target defense tokens N_defense_tokens
    - move options = multiplied_sum_over_speed(number_notches_possible)
    - valid upgrade abilities (binary decision) = N_upgrade_cards
    --> 4 * 2 * N_targets * N_defense_tokens * multiplied_sum_over_speed(number_notches_possible) * N_upgrade_cards
- this currently encompasses all possible choices within a single turn - N_turn_choices - but there are 6 turns --> N_turn_choices^6 (assuming that actions within a turn do not affect the probability space of the next turn e.g. no information created or destroyed)


So the total probability space for discrete ships is N_space = (multiplied_sum_over_SS'(4 * 2 * N_targets * N_defense_tokens * multiplied_sum_over_speed(number_notches_possible) * N_upgrade_cards) * S!S'!)^6

For typical game parameters:
- N_targets = 1
- N_defense_tokens = 3
- multiplied_sum_over_speed(number_notches_possible) = 2 * 2 = 4
- N_upgrade_cards = 3
- S = S' = 4 --> S! * S'! ~ 24^2 = 576

and a game with identical ships --> N_space ~ ((4 * 2 * 1 * 3 * 4 * 3)^(S + S') * S!S'!)^6 ~ 2.3e51