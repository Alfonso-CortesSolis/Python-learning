import pandas as pd

# --- Configuration ---
LOG_FILE = "logs.json"  # JSON Lines format
KEYWORDS = [
    "Failed",
    "Delete",
    "Root",
    "Unauthorized",
    "CreateAccessKey",
    "AdministratorAccess",
]

# --- Load Logs ---
df = pd.read_json(LOG_FILE, lines=True)

# Convert entire row to string for broad keyword matching
df["combined"] = df.fillna("").astype(str).agg(" ".join, axis=1)

# --- Search for Keywords ---
pattern = "|".join(KEYWORDS)

matches = df[df["combined"].str.contains(pattern, case=False, na=False)]

# --- Output Results ---
print("\n=== Suspicious Log Entries ===\n")
print(matches.drop(columns=["combined"]))

print(f"\nTotal Matches Found: {len(matches)}")

# Optional: export to CSV
matches.drop(columns=["combined"]).to_csv("alerts.csv", index=False)
