# TO DO:

### In-Progress
1. Integrate room movement test code with oxygen puzzle execution.
2. Reorganize code.
3. Correctly parse string input into a list of words against a delimiter string.
4. Create a verb/object parser/error handler for user_input()
5. Write better hints for first puzzle room.
6. Create a callable hint command for puzzle rooms.

### Prototype Completion
1. Build 10 puzzles for chapter_01
2. Add save_game() and load_game() functions to data_serialization.
3. Add save_game() and load_game() to the help menu.
4. Add actions for the player to use: examine, read, look, etc.
5. Add full functionality for validating player input and providing errors when input is invalid.
6. Finish help() after creation of all major player commands.
7. Begin basic movement around the first room in chapter_01()
8. After a player death, the game over screen should prompt the player to restore to a previous save.
9. Refactor code to run inside of a while True loop. AKA the game loop
10. Move all items into items.py
11. Work integration of items.py into the inventory function.
12. Serialize if player has player has played tutorial or not. Do not prompt on second boot.

### Bugs
1. [BUG] Resolve "." not displaying after a print. Character cursor overlap bug.\
2. [BUG] Circular Import bug.

### Puzzle Plans
1. Cryptographic note. | Reference ram journal

### Extended Features
1. Add character_creation() function.
2. Create a flashing prompt.
3. Create an oxygen display for the oxygen puzzle in chapter_01() | Research ncurse library
4. Use pygame for implimenting GUI, cursor and sound effects.

### Long-Term Features
1. CRT Terminal GUI
2. Individual keyboard click sounds for each character appearance.
3. Soundtrack
4. Start Menu
5. Title Screen
6. Options Menu
7. Adjustable Music and Sound FX
8. Colorblind mode for CRT Monitor
9. Change font. Courier new.
10. Create discord release for final version of the game.
11. Create steam release for final version of the game.