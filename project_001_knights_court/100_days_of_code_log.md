# 100 Days Of Code - Log

### Day 0: February 13th, 2022
##### The Beginning

**Today's Progress**: 
1. Began work on user_input() function.
2. Worked on help()'s integration with user_input()

**Thoughts:** I coudln't get user_input() to work properly. I want to be able to call it from anytime in the program. There are two problems. The first is after call, the program continues to prompt the user. 2. How do I call help() from user_input() and return to the prompt from the last question asked to the user.

### Day 1: February 14th, 2022
##### Setup & Bug Fixes

**Today's Progress:**
1. Completed setup of GitHub and transfer from Linux to Windows 10
2. Installed python3 on Win10
3. Complete setup of twitter and backlinks to github.
4. Added inventory() function.
5. Fixed calling help() and inventory() within user_input(). Prompt returns to last answered question before proceeding.
6. Completed start_game() function. Returns to game_exe.py
7. Added shorthand form to help and inventory commands.

**Thoughts:** Overall, a productive session. It took some digging to find out I needed a while loop to correctly referrence help() and inventory() from within user_input(). You can now call help() or inventory() at anytime from within the prompt. I did notice that having shorthand commands would be super helpful. I haven't figured out how to do this for yes and no yet. I'm super excited to get the ball rolling on the story. Once I have a save file set up, and the inventory working, I should be able to start working on the first chapter. I want there to be interactables so I for sure need the inventory() command working correctly. Since I'm using this, it'll go hand in hand with getting the savefile to work as well. It'd be worth doing both of them at the same time. I want to be careful that I don't get to side-tracked with features that I don't bother writing the story.

### Day 2: February 15th, 2022
##### Adventerer Name & Research

**Today's Progress:**
1. Investigated pickle module for serializing game save and inventory.
2. Added get_name().
3. Added error handling to get_name()
4. Added a TODO list markdown file.

**Thoughts:** Today wasn't as productive as yesterday. I spent a little more time researching what modules I wanted to use in the game. We will be using some serializing for the game saves and inventory management. Pickle seems like the way to go. I've decided I want to stick with python for the time being. At some point, i'll need to bulid a GUI for the game. But good news is, it can be done in python. So we're going to give it a shot. Added the get_name() function with error handling. Added a TODO list file.

### Day 3: February 15th, 2022
##### Circular Hell

**Today's Progress:**
1. Started work on save_inventory() and load_inventory() functions.
2. Added game_pickle.py file for data serialization.
3. Encountered a bug with circular imports. Current solution might be classes.

**Thoughts:** Overall, today was a good learning experience. I spent some time working with the pickle module. But shortly thereafter I realized I had ran into a problem with circular imports. After some further research, it looks like classes are the solution to my problem, which I'll begin implimenting tomorrow.

### Day 4: February 16th, 2022
##### Refactor & Test

**Today's Progress:**
1. Refactored code.
2. Renamed files.
3. Resolved circular import issue.
4. Updated help()
5. Added section labels to main.py
6. Completed get_name() 

**Thoughts:** The circular import bug was more problematic than I thought. It turns out, if any functions call another function that are in seperate files, a circular import problem will arise. To resolve this, I refactored the code and moved the majoraty of the functions into main.py. This is not exactly how I want to handle the game. I would like to have a chapters.py file to place the main game into. However, this might not be possible. At least, I haven't thought of a solution yet.

For the time being, the only functions that can be placed into a seperate file of their own are functions that do not call other functions. Such as help() and possibly the functions for data_serialization. However, we shall see how data_serialization.py turns out.

### Day 5: February 17th, 2022
##### Data Serialization & Error Handling

**Today's Progress:**
1. Built create_inv()
2. Built save_inv()
3. Modified help() to be more readable and easily modifiable.
4. Created error handling for inv and save commands.

**Thoughts:** The beginning setup is near complete. All that's left to do is to create an inventory addition and ensure that it saves. Once that's done, we can start working on the main chapter of the game. I'm reasonbly happy with the progress that's been made thus far. It's taken some time to get the setup complete, but having this done early will avoid some major headaches longterm.

### Day 6: February 18th, 2022
##### Updating & Saving the User Inventory

**Today's Progress:**
1. Renamed variable "name" to "user_name"
2. Removed unecessary declarations of global variables.
3. Solved bug regarding user_name not getting attached to the inventory file.
4. Created and finished add_inv_item()
5. Completed save_inv()
6. Completed create_inv()
7. Completed load_inv()

**Thoughts:** Today was a productive day. I definitely extended the time I would normally work on the project. There were a number of bugs that needed to be resolved and I want to have the platform ready to start writing the story. The next problem is, I haven't ever written a story before. Not a full fledged one. So this is totally new. I can imagine that I will begin the prologue and end up re-writting the entire first chapter later on down the road as the story becomes more clear with the direction I want to take it. This is okay. At the very least, i'll still be coding and learning how to integrate the items and puzzles around the rooms I'm going to put the character in. On the bright side, I can likely take my time writing the story and drop in small parts as the character moves through the levels. This way I can finish reading Robert McKee's STORY book before finishing my own story. I'm excited. The platform is finally ready to begin writing the chapter_01 prototype.

### Day 7: February 19th, 2022
##### Story Prologue

**Today's Progress:**
1. Added prologue() function.
2. Wrote the introduction to the story.
3. Moved Master Control Panel to the bottom of main.py to let all of the functions get loaded in before they are called.

**Thoughts:** As far as logic problems goes, today was quite light. It entirely involved story writing and kicking things off to a good start. The prologue is in a first draft stage. I'll have to go over it again on a different day to make sure I like it. But in it's current state, it is going in the correct direction. I'm looking forward to writing more.

### Day 8: February 20th, 2022
##### Character by Character Print

**Today's Progress:**
1. Added delay_print() function to functions.py
2. Removed excessive sleep() functions in main.py
3. Updated story print() statements to delay_print()

**Thoughts:** This has to be my most favorite feature yet. Delay print essentially prints each character one at a time at a random interval to make the computer look as if it is a real person typing. It's not perfect, but it's close. The game feels a bit more human now than it did before.

### Day 9: February 21st, 2022
##### Second Draft Prologue

**Today's Progress:**
1. Revised prologue() function

**Thoughts:** This is the second draft for the prologue. In its current state, it is an acceptable kick-start to the adventure. It will go over a final revision upon the rest of the chapters being written for the story.

### Day 10: February 22nd, 2022
##### Bug Fixes & Improvements

**Today's Progress:**
1. Fixed spelling and grammatical errors in prologue() function.
2. Added shorthand commands to yes, no and perhaps.
3. Added an easter egg in user_input()
4. Added some comments explaining code functionality in main.py

**Thoughts:** Today was a bit rushed. So I focused on bug fixes an performance improvements. Added some shorthand commands for more fun interacting with the computer.