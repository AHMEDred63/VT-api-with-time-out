import requests
import time
import csv

API_KEY = "YOUR_API_KEY"  # Replace with your key safely
INPUT_FILE = "file_path"          # One hash per line
OUTPUT_FILE = "vt_results.csv"

url = "https://www.virustotal.com/api/v3/files/{}"
headers = {"x-apikey": API_KEY}

def vt_lookup(file_hash):
    response = requests.get(url.format(file_hash), headers=headers)
    if response.status_code == 200:
        data = response.json()
        stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        return stats
    else:
        return {"error": response.status_code}

results = []

with open(INPUT_FILE, "r") as f:
    hashes = [line.strip() for line in f.readlines() if line.strip()]

for i, h in enumerate(hashes, 1):
    print(f"[{i}/{len(hashes)}] Checking {h} ...")
    stats = vt_lookup(h)
    results.append([h, stats])
    time.sleep(20)  # Free API has ~4 requests/minute

# Save results
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Hash", "Stats"])
    writer.writerows(results)

print(f"Done. Results saved in {OUTPUT_FILE}")

