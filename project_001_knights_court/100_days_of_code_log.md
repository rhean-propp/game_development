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

**Today's Progress**: 
1. Started work on save_inventory() and load_inventory() functions.
2. Added game_pickle.py file for data serialization.
2. Encountered a bug with circular imports. Current solution might be classes.

**Thoughts:** Overall, today was a good learning experience. I spent some time working with the pickle module. But shortly thereafter I realized I had ran into a problem with circular imports. After some further research, it looks like classes are the solution to my problem, which I'll begin implimenting tomorrow.