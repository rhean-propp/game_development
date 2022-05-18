# TO DO:

### In-Progress
1. Complete second puzzle.
2. Write better hints for first puzzle room.
3. Create a callable hint command for puzzle rooms.
4. Instruct player to use "rusty_key" instead of "Rusty Key" when typing the command.

### Prototype Completion
1. Build 10 puzzles for chapter_01
2. Add save_game() and load_game() functions to data_serialization.
3. Add save_game() and load_game() to the help menu.
4. Add actions for the player to use: examine, read, look, etc.
5. Finish help() after creation of all major player commands.
6. After a player death, the game over screen should prompt the player to restore to a previous save.
7. Work integration of items.py into the inventory function.
8. Serialize if player has player has played tutorial or not. Do not prompt on second boot.

### Bugs
1. [BUG] Resolve "." not displaying after a print. Character cursor overlap bug.\
2. [BUG] Circular Imports
3. [BUG] If you type "use rusty_key" just before the timer ends, both the success and failure text prompts collide.
4. [BUG] Torch is not properly added to inventory after picking it up.

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