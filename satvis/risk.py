import matplotlib.pyplot as plt

# ---- Sample satellite launches ----
launches = [
    {'Satellite': 'SatA', 'Vehicle': 'New', 'Orbit': 'LEO', 'Weather': 'Clear'},
    {'Satellite': 'SatB', 'Vehicle': 'Old', 'Orbit': 'GEO', 'Weather': 'Storm'},
    {'Satellite': 'SatC', 'Vehicle': 'New', 'Orbit': 'LEO', 'Weather': 'Storm'},
    {'Satellite': 'SatD', 'Vehicle': 'Old', 'Orbit': 'MEO', 'Weather': 'Clear'},
    {'Satellite': 'SatE', 'Vehicle': 'New', 'Orbit': 'GEO', 'Weather': 'Clear'}
]

# ---- Function to calculate risk / premium ----
def calculate_risk(vehicle, orbit, weather):
    risk = 50  # base risk score
    if vehicle.lower() == 'new':
        risk += 10
    if orbit.upper() == 'LEO':
        risk += 20
    elif orbit.upper() == 'MEO':
        risk += 10
    if weather.lower() == 'storm':
        risk += 30
    return min(risk, 100)  # cap at 100

# ---- Calculate risk for all launches ----
sat_names = []
risk_scores = []

for launch in launches:
    risk = calculate_risk(launch['Vehicle'], launch['Orbit'], launch['Weather'])
    sat_names.append(launch['Satellite'])
    risk_scores.append(risk)
    print(f"Satellite {launch['Satellite']}: Risk Score = {risk}")

# ---- Visualization ----
plt.figure(figsize=(8,5))
bars = plt.bar(sat_names, risk_scores, color='skyblue')
plt.ylim(0, 100)
plt.ylabel('Risk Score (%)')
plt.xlabel('Satellite')
plt.title('Satellite Launch Risk Simulation')

# Add risk score labels on top of bars
for bar, score in zip(bars, risk_scores):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{score}%', ha='center', va='bottom')

plt.show()
