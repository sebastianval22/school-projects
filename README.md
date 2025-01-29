# Projects
This is a repository containing many of the coding projects I have worked on for university courses. This README also links to external repositories for school projects I have contributed to.

# Index
The courses are listed in chronological order, with the most recent projects closer to the top. You can find more information in the individual README of each project.

## Data Structures and Algorithms ##

### Task T0
The main objectives were to:
- Design simple algorithms in C.
- Understand the differences between arrays and linked lists.
- Familiarize myself with pointers and memory management.  
[Go to repository](https://github.com/IIC2133-PUC/T0-2024-2-sebastianval22)

### Task T1
The focus was on:
- Applying heaps to solve priority-based problems.
- Using linear sorting for efficient solutions.
- Optimizing algorithms to meet specific complexity requirements.  
[Go to repository](https://github.com/IIC2133-PUC/T1-2024-2-sebastianval22)

### Task T2
The objectives included:
- Implementing and applying search trees for efficient problem-solving.
- Using hashing techniques for efficient search and storage solutions.
- Optimizing search and storage algorithms to meet specified time and space complexity constraints.  
[Go to repository](https://github.com/IIC2133-PUC/T2-2024-2-sebastianval22)

### Task T3
The final task involved:
- Exploring graph-based algorithms.
- Employing algorithmic techniques to find optimal solutions.  
[Go to repository](https://github.com/IIC2133-PUC/T3-2024-2-sebastianval22)

## Detailed Design of Software
In this project, I coded and simulated a simplified version of the combat system from *Fire Emblem* in **C#**. The game involves strategic battles between units, each with unique abilities and characteristics, aiming to defeat the opposing team. The project focused on implementing clean code practices, utilizing various design patterns and strategies to ensure scalability and maintainability. The game also includes a graphical interface to enhance the user experience.  
[Go to repository](https://github.com/sebastianval22/Proyecto_Fire-Emblem_DDS)

## Web Development

### Tic-Tac-Goal: Football-Themed Tic Tac Toe
This project is a modern twist on the classic "Tic Tac Toe" game, reimagined with a football theme. Players take turns selecting squares on a 3x3 grid, but instead of simply placing X or O, they must choose a football player whose attributes (e.g., nationality, club, position) match the row and column conditions of the selected square. The game connects to a football player API to validate selections, making it both fun and educational for football enthusiasts.

**Frontend Development**  
The frontend was built using **React**, **HTML**, and **CSS**, providing a responsive and interactive user interface. It integrates with the backend API to fetch and validate player data, enabling seamless gameplay. The application is deployed on **Netlify** for easy access.  
[Frontend Repository](https://github.com/IIC2513/PichangasYa_frontend_24-2)

**Backend Development**  
The backend, developed with **Koa.js** and **Sequelize**, manages all game logic and interactions with a **PostgreSQL** database. It includes features like data loaders, web scrapers for player data, and **WebSocket** integration for real-time multiplayer functionality. The API is deployed on **Render**, ensuring reliable performance.  
[Backend Repository](https://github.com/IIC2513/PichangasYa_backend_24-2)

This project combines strategic gameplay with football trivia, offering a unique experience for players to enjoy while learning about their favorite sport.

## Software Engineering
This is a project that the entire class worked on throughout the duration of the course. It is a web platform designed to facilitate the organization and participation in soccer pickup games. Additionally, it allows the creation of private groups, user communication through chats, and user permission management by administrators. I worked on both the backend and frontend as part of the development team.  
[Go to repository](https://github.com/IIC2143/2024-1-grupo-12)

## Databases
This is a group project where we created a database modeling deliveries, restaurants, and dishes for a food company managing multiple clients. We also built a website demonstrating some of the functionalities and queries supported by the database.  
[Go to repository](https://github.com/ilungenstrass/Proyecto-BD-52)

## Advanced Programming
In this course, I worked on several projects using Python and external libraries.

### Project T0
This submission, specifically the main file: `main.py`, models the defense plan of a castle involving turtles and bombs with a certain range, using recursive functions. The code follows the five rules described in the task 0 instructions to construct and validate board solutions.

First, it models two menus for user interaction. The first menu, the start menu, prompts the user to select a board file to open and verifies its validity. The second menu offers five action options that the code can perform with the provided file, allowing the user to choose.

Finally, based on the user's choice, the program executes the corresponding action using various functions from modules like `functions.py` and `tablero.py`.  
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T0)

### Project T1
The main file, `main.py`, simulates a digging tournament, DCCavaCava, with specific rules and constraints. The tournament is simulated through menus that the user can interact with. The tournament has three main entities essential for its operation, which is why they have a composition relationship with the Tournament in the Class Diagram. These entities are Arena, Digger, and Items. To add these entities to the Tournament, we worked with Objects, creating classes for Tournament, Arena, Item, and Digger. These classes include the main characteristics and functions of each entity (as outlined in the instructions), as well as necessary subclasses, such as digger types and item types. Finally, all user options throughout the game were added to the Tournament class, and these methods are called when requested by the user.

This entire program and simulation of DCCavaCava are based on a folder called "Partidas" (Matches). This folder stores the tournaments and is where tournaments can be loaded.  
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T1)

### Project T2
The main file, `main.py`, simulates an arcade-style game where the player controls Luigi, and the main objective is to reach the position of the final star and grab it. However, Luigi has a limited number of lives and time to achieve this goal. The game includes other entities like ghosts, differentiated by their movement (vertical, horizontal, and "follower"), whose goal is to take lives from Luigi when they collide with him. Additionally, there are other types of blocks, such as walls (immovable), fire (which can also take lives from Luigi), and rocks that can only be moved by Luigi. The program features four game windows: `Ventana_Inicial` (Start Window), `Ventana_Juego` (Game Window), `Ventana_Juego_Timer` (Game Timer Window), and `Ventana_Final` (End Window).

The game map is created based on information stored in the "mapas" (maps) folder or through a constructor mode where the user can place entities on the map using the "Drag and Drop" method.

Finally, the user is notified if they lose (due to running out of time or lives) or win, with the final score calculated based on the instructions.  
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T2)

### Project T3
The main files are `cliente/main_cliente.py` and `servidor/main_servidor.py`, which simulate a dice game (cachos) with a server-client interaction (allowing multiple clients to connect). The main objective is to finish the game with remaining lives. This is achieved through turn-based options, including PASS, ANNOUNCE TURN, USE POWER, ROLL DICE, and DOUBT. The game operates in turns, chosen randomly, with four players. If the room is not filled, it is populated with BOTS, which have a predetermined way of playing. The game features two graphical interfaces: one for the WAITING ROOM, showing the four players, their names, and icons, and notifying any additional players that the room is full and they must wait. Additionally, if a player among the four disconnects, a waiting player joins. If any player (among the four) presses the START button, the game begins, and all players are shown the game interface. If it is the bot's turn, it acts immediately and proceeds to the next player. Finally, if a player loses (runs out of lives) or disconnects, the interface and turns are updated. When only one player remains, they are notified of their victory and must exit the program, while losing players are told to exit the program (as per the instructions).  
[Go to code](https://github.com/sebastianval22/school-projects/tree/main/Advanced%20Programming%20Projects/T3)
