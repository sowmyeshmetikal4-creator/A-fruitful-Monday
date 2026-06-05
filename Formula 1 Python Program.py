import random
import time

# ─────────────────────────────────────────────
#  Formula 1 Race Simulator  Sowmesh Metikal (n = 52 cars)
# ─────────────────────────────────────────────

N = 52

TEAMS = [
    ("Red Bull Racing",  "🔵"), ("Mercedes",        "⚫"), ("Ferrari",         "🔴"),
    ("McLaren",          "🟠"), ("Aston Martin",    "🟢"), ("Alpine",          "🔵"),
    ("Williams",         "🔵"), ("Haas",            "⚪"), ("Alfa Romeo",      "🔴"),
    ("AlphaTauri",       "🔵"), ("Lamborghini",     "🟡"), ("Maserati",        "🔴"),
    ("Bugatti Racing",   "🔵"), ("Lotus F1",        "🟡"), ("Brabham",         "⚪"),
    ("Tyrrell Racing",   "⚪"), ("Renault Sport",   "🟡"), ("BMW Motorsport",  "🔵"),
    ("Toyota Racing",    "🔴"), ("Honda Racing",    "🔴"), ("Porsche LMR",     "⚪"),
    ("Peugeot Sport",    "🔵"), ("Citroën Racing",  "⚪"), ("Subaru Technica", "🔵"),
    ("Mitsubishi Sport", "🔴"), ("Nissan GT",       "🔴"),
]

FIRST = ["Lewis","Max","Charles","Lando","Carlos","George","Sebastian","Valtteri",
         "Kimi","Daniel","Pierre","Lance","Fernando","Esteban","Yuki","Nicholas",
         "Mick","Kevin","Antonio","Zhou","Alex","Logan","Nyck","Guanyu","Oscar",
         "Pato","Colton","Marcus","Robert","Theo","Jack","Frederik","Clement",
         "Vips","Jehan","Roy","Bent","Calan","David","Juri","Marino","Richard",
         "Seb","Timo","Nico","Romain","Heikki","Jarno","Takuma","Narain","Vitaly"]

LAST  = ["Hamilton","Verstappen","Leclerc","Norris","Sainz","Russell","Vettel",
         "Bottas","Räikkönen","Ricciardo","Gasly","Stroll","Alonso","Ocon","Tsunoda",
         "Latifi","Schumacher","Magnussen","Giovinazzi","Guanyu","Palou","O'Ward",
         "Herta","Drugovich","Shwartzman","Daruvala","Hughes","Vesti","Hauger",
         "Pourchaire","Doohan","Beckmann","Novalak","Lawson","Ahlin-Kottulinsky",
         "Nissany","Viscaal","Fernandez","Vidales","Martins","Belov","Fittipaldi",
         "Senna","Prost","Lauda","Piquet","Mansell","Hill","Clark","Stewart","Hunt"]

random.seed(42)
used_names = set()

def unique_name():
    while True:
        n = f"{random.choice(FIRST)} {random.choice(LAST)}"
        if n not in used_names:
            used_names.add(n)
            return n

cars = []
for i in range(N):
    team, flag = TEAMS[i % len(TEAMS)]
    cars.append({
        "number": i + 1,
        "driver": unique_name(),
        "team":   team,
        "flag":   flag,
        "skill":  random.uniform(0.5, 1.0),   # base skill
        "speed":  random.uniform(180, 230),    # km/h average
        "fuel":   100.0,
        "tire":   random.choice(["Soft","Medium","Hard"]),
        "pit_stops": 0,
        "dnf":    False,
        "dnf_reason": "",
        "time":   0.0,                         # total race time in seconds
    })

CIRCUIT = "Bahrain International Circuit"
LAPS    = 57
LAP_KM  = 5.412
TOTAL_KM = LAPS * LAP_KM

DNF_CHANCE    = 0.06   # 6 % chance of DNF per car
PIT_CHANCE    = 0.65   # 65 % chance of at least one pit stop

DNF_REASONS = [
    "Engine failure", "Gearbox issue", "Hydraulic failure",
    "Brake failure", "Suspension damage", "Collision",
    "Power unit MGU-K failure", "Puncture – unrecoverable",
    "Driver error – wall contact", "Overheating",
]

# ── Simulate race ──────────────────────────────────────────────────────────────
print("=" * 65)
print(f"  🏎️   FORMULA 1 RACE SIMULATOR  Sowmesh Metikal |  {CIRCUIT}")
print(f"       {N} Cars  •  {LAPS} Laps  •  {TOTAL_KM:.1f} km")
print("=" * 65)
print()

for car in cars:
    # Base lap time in seconds (lower skill → slower)
    base_lap = (LAP_KM / car["speed"]) * 3600        # seconds per lap
    noise     = random.gauss(0, 2)                    # natural variation ±2 s
    pit_time  = 0

    # DNF?
    if random.random() < DNF_CHANCE:
        car["dnf"]        = True
        car["dnf_reason"] = random.choice(DNF_REASONS)
        dnf_lap           = random.randint(1, LAPS)
        car["time"]       = base_lap * dnf_lap + noise * dnf_lap
        continue

    # Pit stop?
    if random.random() < PIT_CHANCE:
        car["pit_stops"] = random.randint(1, 3)
        pit_time = car["pit_stops"] * random.uniform(22, 28)   # 22-28 s per stop

    car["time"] = (base_lap + noise) * LAPS + pit_time

# ── Sort: finishers first (by time), then DNFs ────────────────────────────────
finishers = sorted([c for c in cars if not c["dnf"]], key=lambda x: x["time"])
dnf_cars  = [c for c in cars if c["dnf"]]

print(f"{'POS':<4} {'#':<4} {'DRIVER':<26} {'TEAM':<22} {'TIME':>10}  {'TIRE':<7} {'PITS'}")
print("-" * 85)

MEDALS = {1:"🥇", 2:"🥈", 3:"🥉"}

for pos, car in enumerate(finishers, 1):
    medal  = MEDALS.get(pos, "  ")
    mins   = int(car["time"] // 60)
    secs   = car["time"] % 60
    t_str  = f"{mins}m {secs:05.2f}s"
    gap    = "" if pos == 1 else f"+{car['time']-finishers[0]['time']:.3f}s"
    print(f"{medal}{pos:<3} {car['number']:<4} {car['driver']:<26} "
          f"{car['flag']} {car['team']:<20} {t_str:>10}  {car['tire']:<7} {car['pit_stops']}")

print()
print(f"{'─'*85}")
print(f"  💥  DNF — Did Not Finish ({len(dnf_cars)} cars)")
print(f"{'─'*85}")
for car in dnf_cars:
    print(f"  #{car['number']:<3}  {car['driver']:<26} ({car['team']})  —  {car['dnf_reason']}")

# ── Stats ──────────────────────────────────────────────────────────────────────
print()
print("=" * 65)
winner = finishers[0]
print(f"  🏆  WINNER : {winner['driver']}  ({winner['flag']} {winner['team']})")
mins  = int(winner['time'] // 60)
secs  = winner['time'] % 60
print(f"  ⏱️  TIME   : {mins}m {secs:.3f}s")
print(f"  🔢  CARS CLASSIFIED : {len(finishers)} / {N}")
print(f"  💥  RETIREMENTS     : {len(dnf_cars)}")

tire_counts = {}
for c in finishers:
    tire_counts[c["tire"]] = tire_counts.get(c["tire"], 0) + 1
print(f"  🔄  TIRE STRATEGIES : " +
      "  |  ".join(f"{t}: {v}" for t,v in sorted(tire_counts.items())))

avg_pits = sum(c["pit_stops"] for c in finishers) / max(len(finishers), 1)
print(f"  🛠️  AVG PIT STOPS   : {avg_pits:.2f}")
print("=" * 65)
