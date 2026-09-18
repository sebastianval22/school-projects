# Assignment 3: DCCachos 🎲🃏

**Course:** IIC2233 - Programación Avanzada, Pontificia Universidad Católica de Chile

This is a sanitized showcase version of an individual university assignment. The core protocol, encryption, and game-logic implementations have been redacted, since this course reuses assignments across semesters and publishing a working solution could enable academic dishonesty for future students — see the note at the bottom for details on what was kept vs. redacted.

## Overview
A networked, turn-based dice game ("cachos") for four players over TCP sockets, with a PyQt5 GUI on the client. The server hosts a waiting room (backfilling empty seats with bots) and, once full, runs the game: each turn a player can pass, announce a value, use a power, roll, or call doubt, with wrong calls costing a life; the last player with lives remaining wins. Disconnections are handled gracefully — a waiting player takes an empty seat, and a lost connection mid-game continues the match for the rest.

**Architecture:**
- **Networking:** persistent TCP connections per client, handled concurrently on the server (with locks around shared state) and logged server-side.
- **Message protocol:** a custom byte-level framing scheme — a length header and a block-id header (mixing little- and big-endian encoding), splitting content into fixed-size blocks with zero-padding.
- **Encryption:** messages are additionally obfuscated with a lightweight custom cipher seeded by the player's id before being framed for transport.
- **Game logic:** a server-side class models turn order, dice rolls, announcing/doubting rules, and power effects; a matching bot policy plays automatically on empty seats.
- **GUI:** PyQt5 windows (waiting room, game) driven by signals from a thin client-side networking/backend layer — the frontend itself does not implement protocol or game-rule logic.

## Tech Stack
* Python 3, PyQt5, `socket`, `threading`, `pickle`, `json`

## Run
```bash
python3 servidor/main_servidor.py <port>
python3 cliente/main_cliente.py <port>
```

---
*Note: This is a sanitized showcase repository derived from a university assignment. The bodies of functions implementing the graded protocol (message framing), cipher (encrypt/decrypt), and game-rule logic (turn resolution, bot decisions, doubt/announce/power rules) have been replaced with descriptive comments; socket/threading setup and the PyQt GUI architecture are unchanged. The written assignment brief and a redundant submission archive (`T3.zip`) have been removed.*
