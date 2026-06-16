#!/usr/bin/env python3
"""Fetch U.S. national + per-state gas & diesel prices from the EIA API and write
data/fuel_prices.json. Run weekly via fuel.yml. Needs a free EIA_API_KEY
(register: https://www.eia.gov/opendata/register.php). Exits clean (keeps seed) if no key.

Granularity: EIA publishes weekly *retail* regular-gas prices for 9 states directly; every
other state falls back to its PADD region price. Diesel is published by PADD region. So each
state is resolved to the best available level (state -> region -> national)."""
import os, json, urllib.request, urllib.parse

KEY = os.environ.get("EIA_API_KEY", "").strip()
OUT = "data/fuel_prices.json"

# States with direct EIA weekly retail regular-gasoline series (duoarea code)
STATE_GAS_AREA = {
    "CA": "SCA", "CO": "SCO", "FL": "SFL", "MA": "SMA", "MN": "SMN",
    "NY": "SNY", "OH": "SOH", "TX": "STX", "WA": "SWA",
}
PADD_AREA = {1: "R10", 2: "R20", 3: "R30", 4: "R40", 5: "R50"}  # PADD region duoareas
PADD_NAME = {1: "East Coast (PADD 1)", 2: "Midwest (PADD 2)", 3: "Gulf Coast (PADD 3)",
             4: "Rocky Mountain (PADD 4)", 5: "West Coast (PADD 5)"}
STATE_PADD = {
    "CT": 1, "DE": 1, "DC": 1, "FL": 1, "GA": 1, "ME": 1, "MD": 1, "MA": 1, "NH": 1, "NJ": 1,
    "NY": 1, "NC": 1, "PA": 1, "RI": 1, "SC": 1, "VT": 1, "VA": 1, "WV": 1,
    "IL": 2, "IN": 2, "IA": 2, "KS": 2, "KY": 2, "MI": 2, "MN": 2, "MO": 2, "NE": 2, "ND": 2,
    "OH": 2, "OK": 2, "SD": 2, "TN": 2, "WI": 2,
    "AL": 3, "AR": 3, "LA": 3, "MS": 3, "NM": 3, "TX": 3,
    "CO": 4, "ID": 4, "MT": 4, "UT": 4, "WY": 4,
    "AK": 5, "AZ": 5, "CA": 5, "HI": 5, "NV": 5, "OR": 5, "WA": 5,
}
STATE_NAME = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "Washington DC", "FL": "Florida",
    "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
    "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri",
    "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio",
    "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont",
    "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
}

if not KEY:
    print("EIA_API_KEY not set - keeping existing data/fuel_prices.json seed")
    raise SystemExit(0)


def latest(product, area):
    q = {"api_key": KEY, "frequency": "weekly", "data[0]": "value",
         "facets[product][]": product, "facets[duoarea][]": area,
         "sort[0][column]": "period", "sort[0][direction]": "desc", "length": "1"}
    url = "https://api.eia.gov/v2/petroleum/pri/gnd/data/?" + urllib.parse.urlencode(q)
    try:
        d = json.loads(urllib.request.urlopen(url, timeout=25).read())
        rows = d.get("response", {}).get("data", [])
        return (round(float(rows[0]["value"]), 2), rows[0]["period"]) if rows else (None, None)
    except Exception as e:
        print(f"  EIA {product}/{area} failed: {e}")
        return (None, None)


# National (keeps existing behaviour + dates the dataset)
nat_gas, gd = latest("EPMR", "NUS")
nat_diesel, dd = latest("EPD2D", "NUS")
if nat_gas is None:
    print("EIA national fetch failed - keeping seed")
    raise SystemExit(0)
date = gd or dd
nat_diesel = nat_diesel or 3.62

# PADD regional gas + diesel (fallback granularity for most states)
padd_gas, padd_diesel = {}, {}
for p, area in PADD_AREA.items():
    g, _ = latest("EPMR", area)
    di, _ = latest("EPD2D", area)
    if g: padd_gas[p] = g
    if di: padd_diesel[p] = di

# Direct state regular-gas (9 states)
state_gas_direct = {}
for st, area in STATE_GAS_AREA.items():
    g, _ = latest("EPMR", area)
    if g: state_gas_direct[st] = g

# Resolve every state to best-available gas/diesel
states = {}
for st, padd in STATE_PADD.items():
    if st in state_gas_direct:
        gas, glevel = state_gas_direct[st], "state"
    elif padd in padd_gas:
        gas, glevel = padd_gas[padd], "region"
    else:
        gas, glevel = nat_gas, "national"
    diesel = padd_diesel.get(padd, nat_diesel)
    states[st] = {
        "name": STATE_NAME[st], "gas": gas, "diesel": round(diesel, 2),
        "level": glevel, "region": PADD_NAME[padd],
    }

data = {
    "title": "U.S. Fuel Prices", "date": date,
    "source": "U.S. Energy Information Administration (EIA)",
    "gas": nat_gas, "diesel": nat_diesel, "states": states,
}
os.makedirs("data", exist_ok=True)
json.dump(data, open(OUT, "w"), indent=2)
print(f"Wrote {OUT}: national gas ${nat_gas}, diesel ${nat_diesel} (week of {date}); "
      f"{len(states)} states resolved ({len(state_gas_direct)} state-level, {len(padd_gas)} PADD regions).")
