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

### Day 11: February 23rd, 2022
##### Tutorial

**Today's Progress:**
1. Added skip feature to prologue().
2. Created a tutorial() function to teach the users how to play.
3. Modified prologue() story.
4. Created future logic for master control panel.

**Thoughts:** I'm often going back to the prologue() function to tweak it. At some point, it might get completely re-written. Depending on the direction the story takes. Added the tutorial() function which only covers the help command right now. It's better than nothing lol. I didn't feel as though it was necessary to cover inventory commands or movement commands. At least, not yet. I'll need to ask someone about this. It might be simple for me to use, but for someone who's never played a text adventure before, it might not be so intuitive.

The prototype is getting closer to completion. I believe I have all of the primary functions created except for save_game() and load_game(). These I'll create once the first 3 puzzles rooms have been completed. I'm ballparking 10 puzzles rooms per chapter would be a good size for a game. With 10 chapters needed to complete the game. I'd like the save_game() and load_game functions to leave the player off at the last puzzle they were attempting to solve. Though, I might make some checkpoints.

We're getting into the territory of story writing now, and I can't say this is my strongest suit. So much of it is new. I'm hoping I can write a really engaging story that will be enjoyable to play through. I'd especially like the puzzles to be challenging, but fair. I'll have to put a lot of time and effort into working out these mechanics and story. But the payoff will be well worth it.

### Day 12: February 24th, 2022
##### Improvements & Bug Fixes

**Today's Progress:**
1. Added lists for positive, negative, undecided and command responses.
2. Updated conditionals to use lists instead of hard coded "yes", "no" and "perhaps" responses.
3. Updated conditional if/else logic to include elif and else statements which were missing previously.
4. Removed logic from prologue() and tutorial() functions and placed them in master control panel.

**Thoughts:** We made a lot of updates today, and I have no idea if everything is written correctly. In fact, I expect a lot of bugs next session. We'll probably spend a good hour bug fixing all of the lists before moving on. However, The lists we added thanks to Lubos' suggestions will definitely improve the speed of writing the logic and the simplicity of understanding it down the road.

### Day 13: February 25th, 2022
##### Bug Fixes

**Today's Progress:**
1. Fixed bug in global list and start_game() while loop. There was an empty "" field in the list causing the loop to break.
2. Fixed a conditional with the if/elif/else statement for the perhaps easter egg.
3. Removed unecessary pass of user_name to create_inv() function.
4. Removed double error print when an invalid response is given to the prompt.
5. Added clear_buffer() function.

**Thoughts:** The more I work on this project, the more I realize just how much there is to do. Realistically, I want to have a prototype completed by day 30. Which, is likely still possible, but the project scope is starting to get quite large. I didn't realize just how much work goes into creating interactive fiction. I started doing more reserach on some of the commands many of these games would allow their users to make. It floored me just how many options there are and ways you can interact with the world.

For that reason alone, it feelsl like puzzle rooms and chapters will take a great deal of time to make and craft. Especially if you want them to be challenging. There are a lot of features that these games have that seem basic. Or things you really should have in your game. It wouldn't be considered complete without. When I signed up for this project, I believed I could have a working fully functional interactive fiction game made within 100 days. Although now, this project feels like it could take up to a year to complete. Which is fine. I'm still going to see it through to its end.

The current goal is just to get the prototype done. This means chapter 01 completely written and ready to be played. Then we'll start playtesting. I'll need to find out from my game testers if the game is actually fun. If they're enjoying the experience or if it's not enjoyable at all. That's the one thing I dread. Putting so much work and effort into making something as fun as you can, but then fun doesn't really come about. So hopefully, with enough attention to the most important aspects of what makes the game fun, I can accomplish that.

Here's hoping.

### Day 14: February 26th, 2022
##### Researching Threading

**Today's Progress:**
1. Began chapter_01() function.
2. Wrote introduction to first puzzle.
3. Researched threading.

**Thoughts:** I encountered a problem while creating the first puzzle. The character falls into water and has a limited time to solve the puzzle before he dies. I wasn't sure how exactly to make this work so I started doing some research. It looks like what I might need will either be threading or multiprocessing.

I spent the last half-hour learning about how threading works and if i'm not mistaken, multiprocessing might be what I need to make this happen.

I need the oxygen to count down from 60 to 0. WHile this is happening, the user must be able to put in inputs to the cmd terminal without interrupting the countdown timer. While the countdown timer proceeds, I need it to print a ASCII art image of the oxygen that is remaining to the user, that is updated before the prompt is displayed. When it does update, I don't want it to overwrite the prompt. I only want it to display for a period of time until the puzzle is over.

This is a bit of an ambitious first puzzle, but it should set us on the right track. I think it'll be some time before I get the puzzle, and all of the commands working for this oxygen problem. Tomorrow will be more research until we have a rough idea how we are going to accomplish the countdown timer + user input working together at the same time.

### Day 15: February 27th, 2022
##### Solving the Oxygen Problem

**Today's Progress:**
1. Played with the system clock.
2. Worked on solving the threading problem.
3. Researched ncurse library
4. Worked on solving the oxygen problem.

**Thoughts:** I'm stuck. I'm probably going to need an hour or two dedicated to solving this problem. Although I think I'm on the right track with threading. I'm pretty tired from competing in the CTF this weekend, so today wasn't my best work. But I worked on it nonetheless.