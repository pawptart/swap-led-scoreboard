# swap-led-scoreboard
Python script to swap between led boards (NHL/MLB) and possibly others if developed.

This is pretty basic.  You need the following:
- Python3
- supervisor properly setup to run ALL the boards you want run
- some led boards (NHL https://github.com/riffnshred/nhl-led-scoreboard and MLB https://github.com/MLB-LED-Scoreboard/mlb-led-scoreboard)

All you should need to do is go into the python script, make sure things are set for the names of your supervisor processesfor your led-boards.  

**board_names** - list of the names of your supervisor processes (defaults to the sample config names below)

### Usage

Please refer to the [NHL LED Scoreboard Supervisor setup](https://github.com/riffnshred/nhl-led-scoreboard#method-1-using-supervisor) for specific instructions on setting up Supervisor

It's worth noting you will likely need two program configs:

```
[program:MLB]
command=[SCOREBOARD COMMAND]
directory=[LOCATION OF THE MLB SCOREBOARD DIRECTORY]
autostart=true
autorestart=true

[program:NHL]
command=[SCOREBOARD COMMAND]
directory=[LOCATION OF THE NHL SCOREBOARD DIRECTORY]
autostart=false
autorestart=true
```
