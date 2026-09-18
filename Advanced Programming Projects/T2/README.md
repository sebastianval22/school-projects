# Assignment 2: DCCazafantasmas 👻🧱🔥

**Course:** IIC2233 - Programación Avanzada, Pontificia Universidad Católica de Chile

This is a sanitized showcase version of an individual university assignment. The core algorithmic logic has been redacted, since this course reuses assignments across semesters and publishing a working solution could enable academic dishonesty for future students — see the note at the bottom for details on what was kept vs. redacted.

## Overview
A PyQt5 arcade game: the player controls Luigi, aiming to reach and grab a star before running out of lives or time. Ghosts move independently along fixed axes (horizontal/vertical) or, in a bonus mode, actively path toward Luigi; colliding with a ghost or fire costs a life and resets the level, while rocks can be pushed (but not destroyed) and walls block movement entirely. Maps can be loaded from file or built live in a drag-and-drop constructor mode. The app has four windows: start, game, in-game timer/HUD, and end-of-round.

**Architecture:** a `Juego` backend class owns all game state and rule logic (movement resolution, collision detection, ghost behavior, win/lose conditions, scoring), and communicates with the PyQt frontend windows via Qt signals — the frontend itself is pure presentation (layout, sprites, animations, keyboard/mouse input capture) and does not decide game outcomes.

## Tech Stack
* Python 3, PyQt5 (`QtCore`, `QtWidgets`, `QtGui`, `QtMultimedia`)

## Run
```bash
python3 main.py
```
Maps are loaded from the `mapas/` folder, or built via the in-app constructor mode.

---
*Note: This is a sanitized showcase repository derived from a university assignment. The bodies of functions/methods implementing graded game logic (movement resolution, collision detection, each ghost type's movement rule, the follower-ghost pathing heuristic, and scoring) have been replaced with descriptive comments; the PyQt window/widget architecture, signal wiring, and menu flow are unchanged.*
