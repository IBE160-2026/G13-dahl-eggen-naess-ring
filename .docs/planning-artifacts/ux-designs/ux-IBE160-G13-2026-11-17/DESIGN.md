---
name: LifeMode
description: A life and money game for 15–20-year-olds in Norway. Superseded: round 2 of four candidate visual systems. The group chose in issue #95; the final UX is in ux-IBE160-G13-2026-11-11.
status: superseded
superseded_by: .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/ (final; direction chosen in issue #95)
created: 2026-11-17
updated: 2026-11-18
candidates:
  veien: konsepter/veien/DESIGN.md
  blokka: konsepter/blokka/DESIGN.md
  speilet: konsepter/speilet/DESIGN.md
  basen: konsepter/basen/DESIGN.md
---

## Brand & Style

LifeMode must feel like an actual game, motivating and alive, never like schoolwork or a bank app (PRODUCT.md, NFR-8). It is grown-up, not childish, and every candidate below carries that posture in its own world.

This round ends with four candidate visual systems. They share the same PRD, the same 28 surfaces and the same experience rules (`EXPERIENCE.md`). They differ in metaphor and look:

| Candidate | World | Visual spine |
|---|---|---|
| **Veien** | A level map in perspective; months are milestones on a road, a new age is a gate at New Year | [`konsepter/veien/DESIGN.md`](konsepter/veien/DESIGN.md) |
| **Blokka** | An isometric 3D dollhouse block; each floor is a year of your life | [`konsepter/blokka/DESIGN.md`](konsepter/blokka/DESIGN.md) |
| **Speilet** | A mirror selfie in your own room; the year hangs as a photo garland | [`konsepter/speilet/DESIGN.md`](konsepter/speilet/DESIGN.md) |
| **Basen** | A mountain base camp in a glossy mobile-game style; one camp per year, the summit is your goal | [`konsepter/basen/DESIGN.md`](konsepter/basen/DESIGN.md) |

Sketches for each candidate (28 SVG screens) live in `.working/<concept>/oversikt.html`. The concept spines win on conflict with their sketches.

## Do's and Don'ts

These rules bind every candidate.

| Do | Don't |
|---|---|
| Measure every text and control pair against WCAG 2.2 AA | Rely on color alone for money, state or progress |
| Show time as month, age and "År N av 5" | Show a running month number |
| Keep one clear primary action per screen | Stack competing buttons of equal weight |
| Keep the scene alive: light, people and belongings react to choices | Freeze the hub into a static picture with hotspots |
| Keep the visual style grown-up | Childish mascots, school or bank-app looks |
