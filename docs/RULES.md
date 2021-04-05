# Armada

## Features

- 6 rounds max
- S, S' ships per team
- F, F' squadrons per team
- Total number of possible moves in typical discretised 6-turn game ~ 5e111 (see Appendix 1)
- Branching factor per turn ~ 10^19

## Stages

- Deployment 
- 6 turns played each _or_ victory conditon satisfied _or_ all enemy ships destroyed
    - Ship phase (1 per player)
        - Player 1 then player 2 - until all ships activated
    - Squadron phase (2 per player)
        - Player 1 then player 2 - until all squadrons activated

### Deployment

- Terrain set up
    - players alternate placing scenery at least distance 1 apart
- Unit placement
    - players alternate placing ships or groups of 3 squadrons within designated area
    - speed of ship is chosen
- All command dials chosen

### Player Turn

- Ship 
    - Command dial revealed 
    - Dial executed or token stored
    - Activated ship may fire
    - Activated ship _must_ move

## Pieces

### Ships

- three ship classes: small, medium and large
- ships have 4 hull zones: front, left, right and rear
- ship movement direction and speed is discretised
- ship information:
    - card:
        - hull zones:
            - arc shape
            - LoS dot
            - shields per hull zone
            - armament per hull zone
        - anti-squadron armament (all hull zones)
        - movement capabilities
        - points cost
        - upgrade slots
        - command dial values:
            - command value
            - engineering value
            - squadron value
        - defense tokens
    - other:
        - current speed
        - objective markers
        - command tokens
        - defense token states

### Squadrons

- continuous circular range
- move or shoot (both if activated by squadron dial)
- squadron information:
    - anti-ship armament
    - anti-squadron armament
    - defense tokens if any
    - health