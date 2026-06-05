#!/usr/bin/env python3
"""Fetch latest U.S. national average gasoline + diesel prices from the EIA API
and write data/fuel_prices.json. Run weekly via fuel.yml. Needs a free EIA_API_KEY
(register: https://www.eia.gov/opendata/register.php). Exits clean (keeps seed) if no key."""
import os, json, urllib.request, urllib.parse

KEY = os.environ.get("EIA_API_KEY", "").strip()
OUT = "data/fuel_prices.json"
if not KEY:
    print("EIA_API_KEY not set - keeping existing data/fuel_prices.json seed")
    raise SystemExit(0)

def latest(product):
    q = {"api_key": KEY, "frequency": "weekly", "data[0]": "value",
         "facets[product][]": product, "facets[duoarea][]": "NUS",
         "sort[0][column]": "period", "sort[0][direction]": "desc", "length": "1"}
    url = "https://api.eia.gov/v2/petroleum/pri/gnd/data/?" + urllib.parse.urlencode(q)
    d = json.loads(urllib.request.urlopen(url, timeout=25).read())
    rows = d.get("response", {}).get("data", [])
    return (float(rows[0]["value"]), rows[0]["period"]) if rows else (None, None)

try:
    gas, gd = latest("EPMR")      # regular gasoline, U.S. weekly avg
    diesel, dd = latest("EPD2D")  # No. 2 diesel, U.S. weekly avg
except Exception as e:
    print(f"EIA fetch failed ({e}) - keeping seed")
    raise SystemExit(0)

if gas is None or diesel is None:
    print("EIA returned no data - keeping seed")
    raise SystemExit(0)

data = {"title": "U.S. Average Fuel Prices", "date": gd or dd,
        "source": "U.S. Energy Information Administration (EIA)",
        "gas": round(gas, 2), "diesel": round(diesel, 2)}
os.makedirs("data", exist_ok=True)
json.dump(data, open(OUT, "w"), indent=2)
print(f"Wrote {OUT}: gas ${gas:.2f}, diesel ${diesel:.2f} (week of {data['date']})")
