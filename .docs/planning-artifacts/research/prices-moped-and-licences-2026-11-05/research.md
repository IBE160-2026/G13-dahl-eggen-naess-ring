# Prices for the moped and driving licences

Researched on 2026-11-05 for issue #29 and OQ-3 in the PRD. The game needs real prices for FR-23, FR-24 and FR-28 to FR-30. The values below are written into the brief addendum's parameter table.

## Summary

| Item | Game value | Confidence |
|---|---|---|
| Moped licence, total | NOK 12,000 | Medium: commercial estimates that agree with each other |
| Car licence (class B), total | NOK 32,500 | Medium: midpoint of a commercial range |
| New moped | NOK 29,000 | Medium: a few dealer ads |
| Used moped, about 7-8 years old | NOK 13,750 | Low: two private ads |
| Moped insurance | NOK 3,000 a year | Low: not verified at a primary source |
| Petrol 95 | NOK 20.64 per litre | High: official statistics |
| Moped repairs | No value | No source found |
| Moped resale value per year | No value | No source found; set when tuning (OQ-8) |
| Fuel use, moped and car | No value | Not researched; set when tuning (OQ-8) |

## Moped licence (AM 146)

**Game value: NOK 12,000, range NOK 8,000-15,000.**

| Part | About |
|---|---|
| Practical training | NOK 5,400 |
| Basic traffic course (trafikalt grunnkurs) | NOK 3,000 |
| Basic moped course | NOK 2,400 |
| State fees | NOK 850 |
| Other (eye test, helmet, equipment) | NOK 350 |

- TeoriPortalen, published 2026-05-01: typically NOK 9,000-15,000, median about NOK 12,000 outside Oslo, with the breakdown above. It does not explain how the median was derived.
- Testen.no, updated 2026-07-24: NOK 8,000-15,000 in total. No method or sources given.
- Støyten Trafikkskolesenter, prices from 2026-08-01: traffic course NOK 4,900, moped course NOK 1,800 and a driving package of NOK 13,400. That comes to NOK 20,100 before state fees, well above the range, so a single school can cost much more.
- ung.no, updated 2026-10-05: the licence requires age 16 and the basic traffic course, and it ends with a theory test.

## Car licence (class B)

**Game value: NOK 32,500, the midpoint of NOK 25,000-40,000.**

- Testen.no, updated 2026-07-24: most people pay NOK 25,000-40,000. No method or sources given.
- Statens vegvesen, valid from 2026-02-01: theory test NOK 480, practical test NOK 1,490 online, and issuing the licence NOK 160 online. These fees are part of the total.
- Støyten lists prices per item and has no total. It lists NOK 6,400 for the track safety course and NOK 10,300 for the road safety course.

A 2013-2017 Klikk article gives an average of about NOK 30,000. It is too old to use.

## Buying a moped

**New: NOK 29,000.** Dealer ads on FINN for 2026 models, seen on 2026-11-05: Peugeot Kisbee 50 at NOK 28,900 and NOK 29,531, and SYM Fiddle at NOK 28,990. One dealer adds NOK 1,900 for registration. Sportier models were NOK 37,900-38,900.

**Used: NOK 13,750.** The midpoint of two Yamaha Aerox 50 ads on FINN: a 2019 model at NOK 12,500 and a 2018 model at NOK 15,000. Other ads ranged from NOK 5,355 to NOK 25,000, depending on model and condition. This isn't market data.

**Resale value:** no Norwegian figures found. The new and used prices above are for different models, so they don't give a reliable rate.

## Moped insurance

**Game value: NOK 3,000 a year, about NOK 250 a month.** This is the weakest figure.

- Search summaries gave NOK 1,500-5,000 a year (Førerkortet.no), and an average of about NOK 3,000 (Finansrådet, cited by Tjenestetorget). Those pages weren't read directly.
- Search results also cited a price table for ages 16-18 on eteo.no. The page itself has no such table, so the figures are not used.
- Gjensidige states no price. It says the price depends on the moped, cover, location and rider's age, and it is lowest in winter.
- The claim that parents must take out the insurance for under-18s was not confirmed by the pages read.

**To check:** get a quote for a 16-year-old from an insurer's price calculator.

## Fuel

**Game value: NOK 20.64 per litre,** the average of January-September 2026 for unleaded 95.

Source: SSB table 09654, read through the SSB API on 2026-11-05 (table updated 2026-10-21).

| Month 2026 | NOK per litre |
|---|---|
| January | 20.47 |
| February | 19.68 |
| March | 23.50 |
| April | 19.32 |
| May | 19.15 |
| June | 18.43 |
| July | 19.59 |
| August | 19.42 |
| September | 26.18 |

September is NOK 6.76 above August, and we haven't found out why. The average is used so that a single month doesn't set the price. It equals the 20.64 that Pengeradar reports for 2026, while the 27.87 from Bensinstation.nu for September does not match SSB.

## Still missing

- Moped insurance from a primary source.
- Moped repair prices.
- Resale value per year, and fuel use for the moped and the car, set when tuning.
