# Assignment 0: DCCeldas 💣🐢🏰

**Course:** IIC2233 - Programación Avanzada, Pontificia Universidad Católica de Chile

This is a sanitized showcase version of an individual university assignment. The core algorithmic logic has been redacted, since this course reuses assignments across semesters and publishing a working solution could enable academic dishonesty for future students — see the note at the bottom for details on what was kept vs. redacted.

## Overview
Models a castle's turtle-and-bomb defense system as a grid puzzle: bombs have a fixed blast range, turtles must be placed so they're protected, and every board must satisfy a fixed set of validity rules. `main.py` drives two menus — the first lets the user pick and validate a board file, the second offers actions on it (display, validate placements, check a proposed solution, or solve it automatically).

**Approach:** the solver is a recursive backtracking search — starting from a valid board, it tries turtle placements (guided by a set of directional movement permutations to cover as much of the search space as possible), validating each candidate against all of the board's rules (bomb blast ranges, bomb value bounds, cell uniqueness, turtle adjacency, and an "enclosed region" bonus rule) until it finds a fully valid solution or exhausts the search.

## Tech Stack
* Python 3 (standard library only: `sys`, `os`, `copy`)

## Run
```bash
python3 main.py
```

## External references
Per the assignment's collaboration policy, two small pieces were adapted from external sources and cited in the original submission:
* A coordinate-bounds-check helper, adapted from the course's own help-room reference material ([`IIC2233/Syllabus`](https://github.com/IIC2233/Syllabus)).
* The structure of the recursive board-solving search, partly informed by the same reference material.
* A generic list-permutation routine (used since `itertools` wasn't allowed), adapted from a public forum post.

---
*Note: This is a sanitized showcase repository derived from a university assignment. The bodies of functions implementing the graded rule-checking and recursive solving logic have been replaced with descriptive comments; menu navigation, board display, and file I/O are unchanged.*
