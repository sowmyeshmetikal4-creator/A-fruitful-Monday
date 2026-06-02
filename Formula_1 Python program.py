Here's the F1 Race Simulator with all 52 cars! Here's what the program models:
Race Setup

52 cars across 26 teams (Red Bull, Ferrari, McLaren, Mercedes, and many more)
Bahrain International Circuit — 57 laps, 308.5 km total
Each driver gets a unique name, team, tire compound (Soft/Medium/Hard), and a skill rating

Simulation Logic

Lap times are calculated from each car's randomised average speed (180–230 km/h), scaled by skill and natural noise
Pit stops are simulated — 1 to 3 stops, each adding 22–28 seconds
DNF (Did Not Finish) events fire at ~6% probability with realistic failure reasons (engine, gearbox, collision, etc.)

Results from this run
🏆 WinnerTheo Hamilton (Ferrari) — 
79m 6.27sCars Classified47 / 52Retirements (DNF)
5 cars
Avg Pit Stops1.38
Run the file anytime to get a freshly randomised race — change
random.seed(42) to any other number for a different outcome!