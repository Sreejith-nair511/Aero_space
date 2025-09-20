import matplotlib.pyplot as plt

# ---- Sample systems with vulnerabilities ----
systems = {
    'Server1': ['CVE-2021-123', 'CVE-2020-999'],
    'Server2': ['CVE-2022-456'],
    'ControlUnit1': ['CVE-2019-789', 'CVE-2020-111', 'CVE-2021-321'],
    'SensorModule1': []
}

# ---- Function to calculate risk score ----
def calculate_risk(vulns):
    """
    Simple scoring:
    - Each vulnerability = 20 points
    - Max score = 100
    """
    score = len(vulns) * 20
    return min(score, 100)

# ---- Compute risk scores ----
system_names = []
risk_scores = []

for system, vulns in systems.items():
    score = calculate_risk(vulns)
    system_names.append(system)
    risk_scores.append(score)
    print(f"{system}: Risk Score = {score}%, Vulnerabilities = {vulns}")

# ---- Visualization ----
plt.figure(figsize=(8,5))
bars = plt.bar(system_names, risk_scores, color='orange')
plt.ylim(0, 100)
plt.ylabel('Risk Score (%)')
plt.xlabel('System')
plt.title('Cyber Risk Scoring for Systems')

# Add risk score labels on top of bars
for bar, score in zip(bars, risk_scores):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{score}%', ha='center', va='bottom')

plt.show()
