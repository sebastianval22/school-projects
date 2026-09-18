# Assignment 1: DCCavaCava 🏖⛏

**Course:** IIC2233 - Programación Avanzada, Pontificia Universidad Católica de Chile

This is a sanitized showcase version of an individual university assignment. The core algorithmic logic has been redacted, since this course reuses assignments across semesters and publishing a working solution could enable academic dishonesty for future students — see the note at the bottom for details on what was kept vs. redacted.

## Overview
An object-oriented simulation of a digging tournament, driven by a menu-based CLI. Three entity types — `Arena`, `Excavador` (digger, with subtypes), and `Item` (treasure/consumable) — compose into a `Torneo` (tournament) class that orchestrates each simulated day: diggers dig for a yield depending on their type and the arena's difficulty, spend energy and rest when it runs out, and may find items with a type/arena-dependent probability; random events can also change the active arena. Tournaments can be saved to and loaded from disk.

**Design:** the class diagram models diggers as an abstract base type with concrete subtypes (each with its own dig-yield, energy-cost, and consumable-effect formulas), and arenas with a per-type difficulty calculation (including one arena type whose characteristics reshuffle randomly each day). See `DiagramaClasesFinal.png` and `Explicacion_Diagrama.md` for the full class diagram and rationale.

## Tech Stack
* Python 3 (`abc`, `random`, `collections`, `os`, `sys` from the standard library)

## Run
```bash
python3 main.py
```
Saved tournaments live under `Partidas/`; digger/arena/item definitions are loaded from CSV files.

## External references
Per the assignment's collaboration policy, the multi-level menu navigation (options to go back or exit from any menu) was adapted from the course's own help-room reference material ([`IIC2233/Syllabus`](https://github.com/IIC2233/Syllabus)).

---
*Note: This is a sanitized showcase repository derived from a university assignment. The bodies of methods implementing graded formulas (digging yield, energy cost, rest duration, item-find probability, consumable effects, arena difficulty, and the day-simulation/event-resolution logic) have been replaced with descriptive comments; class/attribute scaffolding, menu navigation, and file I/O are unchanged.*
