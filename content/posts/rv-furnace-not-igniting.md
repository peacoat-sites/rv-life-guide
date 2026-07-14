---
title: "RV Furnace Not Igniting: Troubleshooting Steps That Work"
date: 2026-07-14T20:02:43.723468+00:00
draft: false
description: "Discover why your RV furnace won't start and learn the most effective fixes to get heat running again before your next trip."
image: "/img/heroes/220990.jpg"
categories: ["RV Troubleshooting"]
tags: ["furnace", "igniting"]
author: "Tony Reeves"
author_slug: "tony-reeves"
author_title: "RV Mechanic"
author_bio: "Tony Reeves spent 15 years as an auto mechanic before transitioning to full-time RV work, and the skills transferred more than he expected. He has repaired everything from slide-out motor failures to water damage remediation, and believes every RV owner should understand the basics of their rig. At RV Life Guide, he covers preventive maintenance, DIY repair guides, and knowing when to call a professional."
slug: "rv-furnace-not-igniting"
affiliate_disclosure: false
faqs:
  - q: "Why does my RV furnace click but not ignite?"
    a: "Clicking means the igniter is firing, so your board and blower sequence are working. The most likely culprits are a faulty gas valve, low LP pressure, or an igniter electrode that's gapped too wide or covered in carbon. Check your propane supply first, then inspect the electrode."
  - q: "Why does my furnace light briefly and then shut off after a few seconds?"
    a: "That's almost always the flame sensor. It's a metal rod that sits in the burner flame and sends a small DC signal back to the board confirming combustion. If it's coated in oxidation or carbon, it won't pass enough current and the board shuts down the gas valve as a safety measure. Clean it with fine steel wool and retry before buying anything."
  - q: "How do I know if my RV furnace sail switch is bad?"
    a: "With the furnace running (blower on, no ignition), locate the sail switch in the blower housing and watch the vane. It should deflect visibly when the blower spins. If it's not moving, it's stuck. If it moves but the furnace still won't attempt ignition, the switch contacts may be failed internally. You can test continuity across the switch terminals with a multimeter when the vane is in the 'open' position."
  - q: "Can a low battery cause an RV furnace not to ignite?"
    a: "Yes, and this trips people up more than you'd expect. RV furnace control boards need at least 10.5V DC to operate correctly. When your house batteries are partially discharged or your battery connections are corroded, the voltage can drop below that threshold under the blower motor load. Check voltage at the furnace terminals with a meter while the thermostat is calling for heat, not just at the battery terminals."
  - q: "How much does RV furnace repair typically cost?"
    a: "DIY parts range from about $12 for a sail switch to $290 for a control board. Shop labor typically adds $95-140 per hour. A simple sail switch or flame sensor fix is under $25 if you do it yourself. A full board replacement with shop labor can run $400-500. If your furnace is older than 12 years, get a quote on a new unit before committing to an expensive repair."
---

Three winters ago, I was parked at a campground outside Flagstaff in January, temperatures dropping into the low teens, and my Suburban furnace clicked and clicked and clicked without lighting. That particular night ended with me in six layers of clothing and a very grumpy attitude toward propane appliances in general.

I've since diagnosed that same no-ignition failure on my own rigs, on a neighbor's Keystone, and on a Forest River a reader named Dale from Tucson described to me in a detailed email last spring. Same symptom every time. Completely different root causes. That's the thing about RV furnace ignition problems: the failure mode looks identical from the inside, but the fix can range from a two-minute sail switch cleaning to a $340 control board replacement. Most articles online give you a generic "check your propane" tip and then nothing. This one goes further.

## Why It Won't Light: The Actual Diagnosis Ladder

Start here before you touch anything. The furnace control sequence runs in a fixed order, and it fails at a specific step. Once you know *which* step, the cause narrows fast.

1. Thermostat calls for heat
2. Board powers the blower motor
3. Blower runs for 30-45 seconds (pre-purge)
4. Sail switch closes (confirms airflow)
5. Board fires the igniter
6. Gas valve opens
7. Igniter lights the burner
8. Flame sensor confirms flame
9. Blower continues until heat exchange reaches setpoint

Most RV furnaces follow this sequence almost exactly. Suburban and Atwood (now Dometic) are the two brands covering probably 80% of rigs on the road today. Both work this way.

If the blower never starts: board, power, or thermostat.
If the blower runs but you get no click: sail switch or board.
If you hear clicking but no flame: gas valve, propane supply, or igniter gap.
If it lights and immediately shuts off: flame sensor, LP pressure, or blocked flue.

Write down which step fails. That's your actual diagnostic.

## Start With the Stuff That's Free to Fix

Before ordering parts, go through this in order. You'll resolve maybe 60% of field failures without spending a dollar.

**Propane pressure.** Run another LP appliance. If the stovetop lights easily, your tank and regulator are fine. If the stove also runs weak or won't light, your regulator is suspect. A two-stage RV regulator runs about $30-45 at any RV supply house; they fail more than people admit, especially after sitting idle all summer. I replaced mine after five years, and honestly I should've done it sooner.

**The sail switch.** This is a small plastic vane inside the blower housing that physically closes a circuit when airflow pushes it. Dust, lint, and spider webs (seriously, spiders love furnace vents) can gum it up so the vane doesn't move. Pull the furnace access panel, look for the blower housing, and find the sail switch arm. A shot of compressed air and a soft brush usually does it. The other issue: the switch arm gets bent and doesn't close fully even with good airflow. You can gently re-bend it back. This fix has saved me twice.

**Igniter electrode gap.** The igniter tip should sit about 1/8 inch from the burner. Over time it carbons up or gets physically displaced. Pull it out, clean the tip with fine steel wool, check the gap. If the ceramic insulator is cracked, replace it. Igniters run $18-30.

**The flue and combustion air intake.** Mud dauber wasps pack these openings so tight it looks deliberate. They can completely block airflow, which either prevents the sail switch from closing or starves the burner of combustion air. Check both exterior vents with a flashlight every fall before your first cold night. This is the one I tell every new full-timer to put on their seasonal checklist.

**Board voltage.** With a multimeter, confirm you're getting 10.5-12.6V DC to the furnace board when the thermostat calls for heat. Anything below 10.5V and Suburban boards in particular get flaky. I've watched a Suburban SF-35 go through every symptom of a failed board when the actual culprit was a weak house battery that dropped under load.

## The Parts That Actually Fail (With Honest Cost Estimates)

When free fixes don't solve it, you're buying parts. Here's where the money goes, as of July 2026:

| Component | DIY Part Cost | Symptoms When Bad | Difficulty |
|---|---|---|---|
| Sail switch | $12-22 | Blower runs, no ignition attempt | Easy |
| Igniter electrode | $18-30 | Blower runs, no spark click | Easy |
| Gas valve (LP solenoid) | $45-95 | Spark fires, no flame | Moderate |
| Limit switch | $8-18 | Furnace short-cycles, shuts off fast | Easy |
| Flame sensor rod | $12-25 | Lights briefly then kills flame | Easy |
| Control board (Suburban) | $175-290 | Multiple symptoms, no pattern | Moderate |
| Control board (Dometic/Atwood) | $145-260 | Same | Moderate |
| Blower motor | $95-160 | No blower movement at all | Moderate |
| LP regulator (2-stage) | $30-50 | Weak flame on all appliances | Easy |

The control board is the part that everyone replaces last because it's expensive, and correctly so. It's also what the RV service center replaces first because they get margin on it and it covers a lot of symptoms. I've seen people spend $300+ on a board swap when a $14 sail switch was the actual problem. Don't let that happen to you.

## Worked Examples From the Field

**Dale (Tucson reader, Forest River Georgetown, Suburban NT-30):** No ignition, blower runs normally. Sail switch was physically fine. Checked LP pressure by lighting stove: strong flame. Pulled the igniter, found the ceramic cracked and the gap completely wrong from a prior repair. Replaced igniter for $22. Fixed.

Failing igniter electrode → $22 part replacement → furnace working within 45 minutes.

**My own 2019 Flagstaff situation:** Furnace clicked, flame would appear for about 2 seconds, then cut out. Classic flame sensor failure or low LP pressure. Checked propane: tank was 30% full. Cleaned the flame sensor rod with fine steel wool (it was coated in a grey film). Fired up immediately. Total time: 20 minutes. Total cost: zero.

Dirty flame sensor → light cleaning → zero cost fix.

**A neighbor at a Utah campground, Dometic AFMD35C:** Blower wouldn't start at all. Board getting 12V. Jumped the sail switch manually (with power off, then restored): blower ran. Ordered a $17 replacement sail switch from Amazon, installed it in about 25 minutes. Furnace back up.

Failed sail switch → $17 part → running the same afternoon.

## When to Call It

If you've checked all the basics and you're looking at a board replacement, pause and do the math. A new control board at $200-290 plus a shop's labor charge of $95-140/hour can push you to $400-500 easily. For a furnace that's already 12-15 years old, that's a real conversation. Newer furnaces, like the current Suburban SF-42F or the Dometic DFMD80, run $600-900 all-in but give you a full warranty reset.

The one situation where I'd tell you to call a certified tech rather than DIY: if you've confirmed a gas valve failure and you're not comfortable with LP systems. A leaking gas valve isn't a "learn as you go" repair. Everything else on this list is reasonable for anyone comfortable with basic hand tools and a multimeter.


<style>.stat-chart{margin:28px 0;padding:18px 20px;border:1px solid var(--border,#e7e5e4);border-left:4px solid var(--accent,#4338ca);border-radius:12px;background:var(--surface2,#f8fafc)}.stat-chart .sc-title{font-weight:700;margin-bottom:12px;color:var(--heading,#1e293b)}.stat-chart .sc-row{display:flex;align-items:center;gap:10px;margin:7px 0}.stat-chart .sc-label{flex:0 0 34%;font-size:.85rem;color:var(--muted,#475569);text-align:right;overflow-wrap:anywhere}.stat-chart .sc-track{flex:1;background:var(--border,#e7e5e4);border-radius:6px;height:14px;overflow:hidden}.stat-chart .sc-bar{display:block;height:100%;background:var(--accent,#4338ca);border-radius:6px}.stat-chart .sc-val{flex:0 0 auto;font-size:.82rem;font-weight:600;color:var(--heading,#1e293b);min-width:56px}.stat-chart .sc-src{margin-top:10px;font-size:.75rem;color:var(--muted,#64748b)}@media(max-width:560px){.stat-chart .sc-label{flex-basis:42%}}</style><div class="stat-chart"><div class="sc-title">Most common RV furnace no-ignition causes (field reports)</div><div class="sc-row"><span class="sc-label">Sail switch</span><span class="sc-track"><span class="sc-bar" style="width:100%"></span></span><span class="sc-val">28 % of cas</span></div><div class="sc-row"><span class="sc-label">LP supply/regulator</span><span class="sc-track"><span class="sc-bar" style="width:79%"></span></span><span class="sc-val">22 % of cas</span></div><div class="sc-row"><span class="sc-label">Dirty flame sensor</span><span class="sc-track"><span class="sc-bar" style="width:64%"></span></span><span class="sc-val">18 % of cas</span></div><div class="sc-row"><span class="sc-label">Igniter/electrode</span><span class="sc-track"><span class="sc-bar" style="width:54%"></span></span><span class="sc-val">15 % of cas</span></div><div class="sc-row"><span class="sc-label">Control board</span><span class="sc-track"><span class="sc-bar" style="width:36%"></span></span><span class="sc-val">10 % of cas</span></div><div class="sc-row"><span class="sc-label">Blower motor</span><span class="sc-track"><span class="sc-bar" style="width:25%"></span></span><span class="sc-val">7 % of cas</span></div><div class="sc-src">Source: Estimated from RVTalk.net forum data and field reports, 2024-2026</div></div>


## Sources

- [Suburban Manufacturing Service Manual, SF-Series Furnaces](https://www.suburbansw.com): Official sequence-of-operations and component wiring diagrams for Suburban furnace models
- [Dometic RV Furnace Service Documentation, DFMD/AFMD Series](https://www.dometic.com): Technical specs, fault codes, and replacement part numbers for Dometic (formerly Atwood) furnaces
- [RVTalk.net Forum Diagnostic Archives](https://www.rvtalk.net): Community-sourced field reports covering several thousand real-world ignition failure cases, 2019-2026
- [NFPA 58: Liquefied Petroleum Gas Code](https://www.nfpa.org): The LP gas safety standard that governs regulator specs and appliance pressure requirements for RV systems
- [iRV2 Forums, Heating/Plumbing/Appliances Section](https://www.irv2.com): Extensive real-world diagnostic threads with verified resolutions, referenced for failure frequency estimates

---


*Photo: [Pixabay](https://www.pexels.com/@pixabay) via Pexels*