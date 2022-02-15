# 100 Days Of Code - Log

### Day 0: February 13th, 2022
##### The Beginning

**Today's Progress**: 
1. Began work on user_input() function.
2. Worked on help()'s integration with user_input()

**Thoughts:** I coudln't get user_input() to work properly. I want to be able to call it from anytime in the program. There are two problems. The first is after call, the program continues to prompt the user. 2. How do I call help() from user_input() and return to the prompt from the last question asked to the user.

**TODO:**
1. Solve how to call help() and still be able to resume input from the last user_input() call.
2. Be able to use user_input() as a function call without errors.
3. Fix perhaps easter egg.
4. BUG: Prompt returns after typing an answer. Doesn't progress story.
5. Change program over from Linux to Host.
6. Figure out how to post to git.

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

**TODO:**
1. Build inventory() function
2. Add character_creation() function.
3. Create save file | Referrence save file.
4. Prompt user to continue or select new game.
5. Create a flashing prompt.
6. Add shorthand to yes and no commands.

### Day 2: February 15th, 2022
##### Adventerer Name & Research

**Today's Progress:**
1. Investigated pickle module for serializing game save and inventory.
2. Added get_name().
3. Added error handling to get_name()
4. Added a TODO list markdown file.

**Thoughts:** Today wasn't as productive as yesterday. I spent a little more time researching what modules I wanted to use in the game. We will be using some serializing for the game saves and inventory management. Pickle seems like the way to go. I've decided I want to stick with python for the time being. At some point, i'll need to bulid a GUI for the game. But good news is, it can be done in python. So we're going to give it a shot. Added the get_name() function with error handling. Added a TODO list file.