import requests
import pandas as pd
from pathlib import Path

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url, timeout=30)
response.raise_for_status()

data = response.json()

print("Scheme Name:", data["meta"]["scheme_name"])
print("Latest NAV:", data["data"][0]["nav"])
print("NAV Date:", data["data"][0]["date"])

output_folder = Path(__file__).resolve().parent / "data" / "raw"
output_folder.mkdir(parents=True, exist_ok=True)

df = pd.DataFrame(data["data"])
df.to_csv(output_folder / "sbi_small_cap_nav.csv", index=False)

print("NAV data saved successfully!")

schemes = {
    "sbi_bluechip": 119598,
    "icici_bluechip": 120586,
    "nippon_large_cap": 118632,
    "axis_bluechip": 120465,
    "kotak_bluechip": 120152
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data["data"])
    df.to_csv(output_folder / f"{name}_nav.csv", index=False)

    print(name, "-", data["meta"]["scheme_name"])
    print("Saved successfully!")

response = requests.get(
    "https://api.mfapi.in/mf",
    timeout=30
)
response.raise_for_status()

all_schemes = requests.get("https://api.mfapi.in/mf", timeout=30).json()
keywords = ["ICICI", "AXIS", "KOTAK"]

for scheme in all_schemes:
    name = scheme["schemeName"].upper()

    if any(word in name for word in keywords) and "LARGE CAP" in name and "DIRECT" in name and "GROWTH" in name:
        print(scheme["schemeCode"], scheme["schemeName"])

all_schemes = response.json()

for scheme in all_schemes:
    name = scheme["schemeName"]
    if "SBI"in name.upper() and "LARGE CAP" in name.upper():
        print(scheme["schemeCode"], name)