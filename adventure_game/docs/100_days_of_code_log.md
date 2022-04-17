# 100 Days Of Code - Log

### Day 0: February 13th, 2022
##### The Beginning

**Today's Progress**: 
1. Began work on user_input() function.
2. Worked on help()'s integration with user_input()

**Thoughts:**
I coudln't get user_input() to work properly. I want to be able to call it from anytime in the program. There are two problems. The first is after call, the program continues to prompt the user. 2. How do I call help() from user_input() and return to the prompt from the last question asked to the user.

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

**Thoughts:**
Overall, a productive session. It took some digging to find out I needed a while loop to correctly referrence help() and inventory() from within user_input(). You can now call help() or inventory() at anytime from within the prompt. I did notice that having shorthand commands would be super helpful. I haven't figured out how to do this for yes and no yet. I'm super excited to get the ball rolling on the story. Once I have a save file set up, and the inventory working, I should be able to start working on the first chapter. I want there to be interactables so I for sure need the inventory() command working correctly. Since I'm using this, it'll go hand in hand with getting the savefile to work as well. It'd be worth doing both of them at the same time. I want to be careful that I don't get to side-tracked with features that I don't bother writing the story.

### Day 2: February 15th, 2022
##### Adventerer Name & Research

**Today's Progress:**
1. Investigated pickle module for serializing game save and inventory.
2. Added get_name().
3. Added error handling to get_name()
4. Added a TODO list markdown file.

**Thoughts:**
Today wasn't as productive as yesterday. I spent a little more time researching what modules I wanted to use in the game. We will be using some serializing for the game saves and inventory management. Pickle seems like the way to go. I've decided I want to stick with python for the time being. At some point, i'll need to bulid a GUI for the game. But good news is, it can be done in python. So we're going to give it a shot. Added the get_name() function with error handling. Added a TODO list file.

### Day 3: February 15th, 2022
##### Circular Hell

**Today's Progress:**
1. Started work on save_inventory() and load_inventory() functions.
2. Added game_pickle.py file for data serialization.
3. Encountered a bug with circular imports. Current solution might be classes.

**Thoughts:**
Overall, today was a good learning experience. I spent some time working with the pickle module. But shortly thereafter I realized I had ran into a problem with circular imports. After some further research, it looks like classes are the solution to my problem, which I'll begin implimenting tomorrow.

### Day 4: February 16th, 2022
##### Refactor & Test

**Today's Progress:**
1. Refactored code.
2. Renamed files.
3. Resolved circular import issue.
4. Updated help()
5. Added section labels to main.py
6. Completed get_name() 

**Thoughts:**
The circular import bug was more problematic than I thought. It turns out, if any functions call another function that are in seperate files, a circular import problem will arise. To resolve this, I refactored the code and moved the majoraty of the functions into main.py. This is not exactly how I want to handle the game. I would like to have a chapters.py file to place the main game into. However, this might not be possible. At least, I haven't thought of a solution yet.

For the time being, the only functions that can be placed into a seperate file of their own are functions that do not call other functions. Such as help() and possibly the functions for data_serialization. However, we shall see how data_serialization.py turns out.

### Day 5: February 17th, 2022
##### Data Serialization & Error Handling

**Today's Progress:**
1. Built create_inv()
2. Built save_inv()
3. Modified help() to be more readable and easily modifiable.
4. Created error handling for inv and save commands.

**Thoughts:**
The beginning setup is near complete. All that's left to do is to create an inventory addition and ensure that it saves. Once that's done, we can start working on the main chapter of the game. I'm reasonbly happy with the progress that's been made thus far. It's taken some time to get the setup complete, but having this done early will avoid some major headaches longterm.

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

**Thoughts:**
Today was a productive day. I definitely extended the time I would normally work on the project. There were a number of bugs that needed to be resolved and I want to have the platform ready to start writing the story. The next problem is, I haven't ever written a story before. Not a full fledged one. So this is totally new. I can imagine that I will begin the prologue and end up re-writting the entire first chapter later on down the road as the story becomes more clear with the direction I want to take it. This is okay. At the very least, i'll still be coding and learning how to integrate the items and puzzles around the rooms I'm going to put the character in. On the bright side, I can likely take my time writing the story and drop in small parts as the character moves through the levels. This way I can finish reading Robert McKee's STORY book before finishing my own story. I'm excited. The platform is finally ready to begin writing the chapter_01 prototype.

### Day 7: February 19th, 2022
##### Story Prologue

**Today's Progress:**
1. Added prologue() function.
2. Wrote the introduction to the story.
3. Moved Master Control Panel to the bottom of main.py to let all of the functions get loaded in before they are called.

**Thoughts:**
As far as logic problems goes, today was quite light. It entirely involved story writing and kicking things off to a good start. The prologue is in a first draft stage. I'll have to go over it again on a different day to make sure I like it. But in it's current state, it is going in the correct direction. I'm looking forward to writing more.

### Day 8: February 20th, 2022
##### Character by Character Print

**Today's Progress:**
1. Added delay_print() function to functions.py
2. Removed excessive sleep() functions in main.py
3. Updated story print() statements to delay_print()

**Thoughts:**
This has to be my most favorite feature yet. Delay print essentially prints each character one at a time at a random interval to make the computer look as if it is a real person typing. It's not perfect, but it's close. The game feels a bit more human now than it did before.

### Day 9: February 21st, 2022
##### Second Draft Prologue

**Today's Progress:**
1. Revised prologue() function

**Thoughts:**
This is the second draft for the prologue. In its current state, it is an acceptable kick-start to the adventure. It will go over a final revision upon the rest of the chapters being written for the story.

### Day 10: February 22nd, 2022
##### Bug Fixes & Improvements

**Today's Progress:**
1. Fixed spelling and grammatical errors in prologue() function.
2. Added shorthand commands to yes, no and perhaps.
3. Added an easter egg in user_input()
4. Added some comments explaining code functionality in main.py

**Thoughts:**
Today was a bit rushed. So I focused on bug fixes an performance improvements. Added some shorthand commands for more fun interacting with the computer.

### Day 11: February 23rd, 2022
##### Tutorial

**Today's Progress:**
1. Added skip feature to prologue().
2. Created a tutorial() function to teach the users how to play.
3. Modified prologue() story.
4. Created future logic for master control panel.

**Thoughts:**
I'm often going back to the prologue() function to tweak it. At some point, it might get completely re-written. Depending on the direction the story takes. Added the tutorial() function which only covers the help command right now. It's better than nothing lol. I didn't feel as though it was necessary to cover inventory commands or movement commands. At least, not yet. I'll need to ask someone about this. It might be simple for me to use, but for someone who's never played a text adventure before, it might not be so intuitive.

The prototype is getting closer to completion. I believe I have all of the primary functions created except for save_game() and load_game(). These I'll create once the first 3 puzzles rooms have been completed. I'm ballparking 10 puzzles rooms per chapter would be a good size for a game. With 10 chapters needed to complete the game. I'd like the save_game() and load_game functions to leave the player off at the last puzzle they were attempting to solve. Though, I might make some checkpoints.

We're getting into the territory of story writing now, and I can't say this is my strongest suit. So much of it is new. I'm hoping I can write a really engaging story that will be enjoyable to play through. I'd especially like the puzzles to be challenging, but fair. I'll have to put a lot of time and effort into working out these mechanics and story. But the payoff will be well worth it.

### Day 12: February 24th, 2022
##### Improvements & Bug Fixes

**Today's Progress:**
1. Added lists for positive, negative, undecided and command responses.
2. Updated conditionals to use lists instead of hard coded "yes", "no" and "perhaps" responses.
3. Updated conditional if/else logic to include elif and else statements which were missing previously.
4. Removed logic from prologue() and tutorial() functions and placed them in master control panel.

**Thoughts:**
We made a lot of updates today, and I have no idea if everything is written correctly. In fact, I expect a lot of bugs next session. We'll probably spend a good hour bug fixing all of the lists before moving on. However, The lists we added thanks to Lubos' suggestions will definitely improve the speed of writing the logic and the simplicity of understanding it down the road.

### Day 13: February 25th, 2022
##### Bug Fixes

**Today's Progress:**
1. Fixed bug in global list and start_game() while loop. There was an empty "" field in the list causing the loop to break.
2. Fixed a conditional with the if/elif/else statement for the perhaps easter egg.
3. Removed unecessary pass of user_name to create_inv() function.
4. Removed double error print when an invalid response is given to the prompt.
5. Added clear_buffer() function.

**Thoughts:**
The more I work on this project, the more I realize just how much there is to do. Realistically, I want to have a prototype completed by day 30. Which, is likely still possible, but the project scope is starting to get quite large. I didn't realize just how much work goes into creating interactive fiction. I started doing more reserach on some of the commands many of these games would allow their users to make. It floored me just how many options there are and ways you can interact with the world.

For that reason alone, it feelsl like puzzle rooms and chapters will take a great deal of time to make and craft. Especially if you want them to be challenging. There are a lot of features that these games have that seem basic. Or things you really should have in your game. It wouldn't be considered complete without. When I signed up for this project, I believed I could have a working fully functional interactive fiction game made within 100 days. Although now, this project feels like it could take up to a year to complete. Which is fine. I'm still going to see it through to its end.

The current goal is just to get the prototype done. This means chapter 01 completely written and ready to be played. Then we'll start playtesting. I'll need to find out from my game testers if the game is actually fun. If they're enjoying the experience or if it's not enjoyable at all. That's the one thing I dread. Putting so much work and effort into making something as fun as you can, but then fun doesn't really come about. So hopefully, with enough attention to the most important aspects of what makes the game fun, I can accomplish that.

Here's hoping.

### Day 14: February 26th, 2022
##### Researching Threading

**Today's Progress:**
1. Began chapter_01() function.
2. Wrote introduction to first puzzle.
3. Researched threading.

**Thoughts:**
I encountered a problem while creating the first puzzle. The character falls into water and has a limited time to solve the puzzle before he dies. I wasn't sure how exactly to make this work so I started doing some research. It looks like what I might need will either be threading or multiprocessing.

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

**Thoughts:**
I'm stuck. I'm probably going to need an hour or two dedicated to solving this problem. Although I think I'm on the right track with threading. I'm pretty tired from competing in the CTF this weekend, so today wasn't my best work. But I worked on it nonetheless.

### Day 16: February 28th, 2022
##### Oxygen Progress

**Today's Progress:**
1. Made progress on the oxygen problem.
2. Problem is now 80% solved.

**Thoughts:**
We're close. All that's left to do with this function is get the oxygen remaining to display, and somehow figure out how to allow the program to terminate while requesting user input. If we can do this, we're boolin.

### Day 17: March 1st, 2022
##### Oxygen Solved

**Today's Progress:**
1. Worked with Austin L. Howard to solve the oxygen problem.
2. Full credit to Austin for solving the problem. A big thank you to him.

**Thoughts:**
I'd like to say a big thank you to Austin L. Howard for helping me solve the oxygen problem. I was stuck for quite a few days and starting to feel quite discouraged about the project. It feels like I can start making solid progress again. Looking forward to writing out the puzzle solution and implimenting the movement commands soon.

### Day 18: March 2nd, 2022
##### Writing the First Puzzle

**Today's Progress:**
1. Modified question() and countdown_event().
2. Resolved additional ">" symbol printing upon exit of loop.
3. Wrote the water puzzle.

**Thoughts:**
Today was successful and productive. The first puzzle is almost complete. There are a lot of features to add with the input parsing. I need to come up with a solid system for using commands with items in the user's inventory. However, we're off to a great start. Looking forward to making more puzzles like this one.

### Day 19: March 3rd, 2022
##### Bug Fixes

**Today's Progress:**
1. Fixed scrambled output bug causing two print statements to overlap.

**Thoughts:**
Bug fixes today. There is a problem with the question thread not ending after completing the oxygen puzzle. We'll need to figure out how to properly close the thread before moving on. Force quitting the thread sounds like it's a bad programming practice.

### Day 20: March 4th, 2022
##### Bug Fixes With a Side of: New Bugs to Fix

**Today's Progress:**
1. Fixed delayed_print from running too slow. Added a stop flag to the question() thread.
2. Fixed programming running indefinitely.
3. Enabled threads to run properly.
4. Added a feature to rewrite over the "> " on input() call when doing a timer based delay_print() statement

**Thoughts:**
20 Days! We're going strong. I've got a few more bugs to fix with the threads. They're a bit tricky to wrap your head around at first, but we're making headway.

### Day 21: March 5th, 2022
##### Preparing Actionable Commands

**Today's Progress:**
1. Added directional commands to the input_* lists.
2. Added a resources page to keep track of important links and references.
3. Added descriptive text for the first puzzle room.

**Thoughts:**
The bug causing the swim up command to break is now magically working again. You love to see it. Couldn't tell you why either. The program is getting long enough now that I start getting lost in the sauce. I'm unsure how to handle movement in the game.

### Day 22: March 6th, 2022
##### Building Help

**Today's Progress:**
1. Added move_player() help menu.
2. Added short_hand_commands() help menu.
3. Added movement types for latter parsing by user_input()

**Thoughts:** 
Days are starting to blend together. There is also way too many global variables. I'm not sure if I can move them yet, but I might be able to.

### Day 23: March 7th, 2022
##### Input Parsing

**Today's Progress:**
1. Working on user_input() to parse directional movement

**Thoughts:**
I'm struggling to read through my code. It's getting long. I need a better way to sort all of the functions. Input parsing is far more difficult than I thought it would be. I haven't got a great idea/gameplan in my head how I will do it yet. Need more time to get everything running smoothly.

### Day 24: March 8th, 2022
##### Researching Classes

**Today's Progress:**
1. Viewed: https://youtu.be/hLLaw9BI-EE
2. Viewed: https://youtu.be/pnWINBJ3-yA

**Thoughts:**
Worked on researching classes today. Will look into implimenting them into the user_input() function for parsing the directional movements and additional player commands. 

### Day 25: March 9th, 2022
##### Code Readability

**Today's Progress:**
1. Modified all functions in main.py for readability.
2. Added a credits markdown file.

**Thoughts:**
I need to get more comfortable with reading through my code. The file is pretty large and it's easy to get lost. I dedicated today to working on the readibilty and editing the comments so they all made sense.

### Day 26: March 10th, 2022
##### Command Parsing

**Today's Progress:**
1. Created direction_sort() function for parsing string content from user_input()

**Thoughts:**
Created the direction_sort() function. It is not done yet. Need to work on error handling.
Considering removing the ability to move left/right/forward/backwards and keep it to north/south/east/west. This might make it easier to visualize where the character is. I haven't decided yet. It might make more sense to keep both, and use whatever the users feels is the correct command in the moment.

Say perhaps they're scaling a wall. You wouldn't really want to use east/west to move left and right along the wall. It would work, but it wouldn't make as much sense as saying climb left or climb right.

Moving backwards is tricky. Since it would make more sense to say move south.

### Day 27: March 11th, 2022
##### Direction Input Parsing 

**Today's Progress:**
1. Worked on directional input parsing

**Thoughts:**
Nested for loops get pretty wild. Working on geting the directional input parsing to work. There is currently a bug that prints all lines from the direction to the error console. Need to adjust the program so it only prints the error that the player entered incorrectly.

### Day 28: March 12th, 2022
##### Direction Sort

**Today's Progress:**
1. Made headway on direction_sort()

**Thoughts:**
The function, direction_sort() needs a way to properly parse the buffer string before letting it run through the rest of the function. Currently it takes the buffer and splits it.
"climb up" becomes "climb", "up" and "hello climb forward" becomes "hello", "climb", "forward"
This could be a problem later on. Best sanitize the input now so it doesn't become a game breaking bug later on.

### Day 29: March 13th, 2022
##### Planning & Organizing

**Today's Progress:**
1. Updated format strings to be compliant with python 3.10
2. Removed unecessry code.
3. Started refactoring chapter_01 into a class.

**Thoughts:**
Didn't complete a lot today. Tidied up some code. I'm taking a guess that the chapter_01 function needs to be a class. If we refactor it, we can call the question and countdown_timer threads within it. Then the player can still move around in the room. Parts of the room or the room itself could be an object. I need to figure out how to make the oxygen puzzle run once, then not run again.

As far as user_input() goes, we have for the most part finished the direction_sort function. The user_input fucntion might also work best as a class. Putting the direction_sort() function into the class as a callable method might be a good way of handling the input parsing.

I haven't been giving the project as much attention as I'd like to. 100 Days of Code is no joke. Though we're going to see it through. I often get lost in my own code and unsure where to keep progressing to get the prototype done. But it'll come in time.

### Day 30: March 14th, 2022
##### Code Review & Function Integration

**Today's Progress:**
1. Reviewing Code
2. Working on integrating direction_sort() into user_input()

**Thoughts:**
Tried making chapter_01 into a class, but i'm unsure how it's going to work. I was thinking you could have different funtions within the class that would be rooms. But the problem is the initialize method will always be called each time the class is called. And if I have the oxygen puzzle in there, it will get called multiple times, which shouldn't happen. I'm not sure what to do.

Spent quite a bit more time on the program today than I normally do. I've noticed 1 hour isn't always enough time to really get into the meat of the problems. I might switch to doing 2 hours a day on the weekends to cover some of the harder problems more effecitvely.

I'm a bit bummed out that I don't have the prototype finished yet. I was expecting i'd be pretty close by day 30. But no. On our current rate of progress, we're aiming to have the prototype complete by day 100. Which is fine. Once I have the major commands writen for allowing the player to move around the world, writing the story and puzzles will go faster.

There are some functions like save_game() and interactable commands such as examine that need to be figured out. There are a large number of intereactable commands to create. But I will likely be adding them as we build the puzzles.

Realistically, if I want to finish this game and see it to the full end which I would expect would be roughly around 10 chapters | 100 puzzles, it will be a year. It could be longer depending on how in-depth we go. I really want to finish this project though. We're doing good. Get stuck occasionally, but I just want to get this completed. We might just end up doing 365 Days of code instead of just 100 lol.

I'm buying myself a nice scotch after I finish this project.

### Day 31: March 15th, 2022
##### Directional Movement Parsing is Completed!

**Today's Progress:**
1. Renamed direction_sort() to movement_check()
2. Correctly integrated movement_check() into user_input()

**Thoughts:**
Huzzah! We finally had a breakthrough. I am now correctly parsing directional movement commands. There is error handling for the player so if they try to type an invalid command, the game will inform them that what they tried doesn't work. This took 3 days to solve and it feels good. That is one massive roadblock out of the way. I can probably start writing the sections of the first room out now. We will need to work on creating an examine player command next. Which is probably the next big hurdle. But I should be able to figure it out faster now that i've got the directional movement parsing all sorted out.

### Day 32: March 16th, 2022
##### Testing & Lore

**Today's Progress:**
1. Edited story in chapter_01()
2. Testing chapter_01()
3. Worked on lore and plans for the story.

**Thoughts:**
I may eventually expand movement check into an error_handler function for the majoraty of player input. Worked on some story ideas for the game. Didn't do much coding in this update. Will need to make up for it this weekend.

### Day 33: March 17th, 2022
##### Bug Fixes

**Today's Progress:**
1. Fixed [BUG] where output would not correctly display after entering "swim up" command while restrained.

**Thoughts:**
The wear of an hour a day eventually gets to you. I know i'm a third of the way to my goal, but it's easy to get sidetracked or want to do something else. Although, I know I made the commitment to myself, and I think that's whats really keeping me going. I can't lie, theres been some days where I've only worked on the project from 15 - 30 minutes. But I still logged on and did something. Even if it was something super small. I've also had days where I've gone over and worked on the project for 2 - 2.5 hours. It doesn't entirely balance it out, but at the very least, I'm still doing it daily.

This is my first big project. Part of the discouragement comes from the growing project scope. I started this project with the belief that I would probably be done the prototype roughly around day 30. We're getting closer, but the prototype won't realistically be done till roughly around day 100 at the earliest. Then you have the realization that you're making a very niche game that few people will play. Which is fine. The experience of creating something is still really rewarding.

I may not always have the motivation to code. But at the very least I've had the discipline. Grateful for that.

At this point, what we've created is a game engine. It's nowhere near done, and has a lot of work to do, but I could eventually make this into a library for people to use. That would be pretty sweet.

### Day 34: March 18th, 2022
##### Bug Fix

**Today's Progress:**
1. Fixed [BUG] where program does not correctly exit after the timer runs out on the oxygen puzzle.

**Thoughts:**
On a time crunch today. Didn't have much time to work on the project. However, I fixed an annoying bug that wasn't allowing the program to quit on a game over death.

### Day 35: March 19th, 2022
##### ASCII Art & Planning

**Today's Progress:**
1. Added a game_over() function to display ascii art and quit the program.
2. Prepared plans for future additions of the game and engine.

**Thoughts:**
I probably have a little bit of testing left to do, but the next step is making multiple sections within the room that the player can move around in. I'm fairly certain I'm going to need classes for the chapter() functions. Otherwise there's no way to move back from one room to the next. Especially if room text will change after a player has solved the puzzle in that room.

I'm a bit uneasy about playing around with classes, since I know I'm going to experience enough bugs I will have no idea at first how to fix. I've been avoiding them for as long as I can and now i'm approaching that area where I'm really going to need to start working with them otherwise I'm not going to be making much progress anymore.

As far as player movement goes, I'd like to have a north, south, east and west side of a room. I'd like to make rooms in a grid basis. The first room is a 9x9 grid. The center box is where the water is located. If I do this, it might be beneficial to allow the player to move northwest, northeast, southwest and southeast. But it shouldn't be necessary in order to get the game working. More of an extended feature than anything. And if I did do this, how would I translate those commands as they are translated previously? North = Forward, South = Backward. What would Northwest be? Front left? It might be easier to only allow the player to move left/right forward/back. It would also be pretty cool to suggest to the player to make a map. Or the player could pick up map of the area to see where they are.

I could write the maps like so:

      N
      |
  W --+-- E
      |
      S
 ___ ___ ___
|   |   |   |
|___|___|___|
|   |   |   |
|___|___|___|
|   |   |   |
|___|___|___|

ASCII art for the maps would be super cool. Something a player could pick up after completing a section, or a reward. It would also help with the level design. Rooms wouldn't just be 9x9 boxes, but hallways with smaller rooms, nooks and crannies.

This passion project has become more of an obsession. It used to be something I felt I ought to do, but now it feels like something I want to do. I like that I can move from one problem to another. Take a break on problems that are stumping me to work on another aspect of the project and come back to the roadblock later. I don't feel like I have to intensely think out a solution, but I can take my time to figure out the problems instead.

The learning journey has been very rewarding thus far. I've learned about data serialization, parsing strings, proper code commenting, threading, project organization, and many more little things that are too much to number. Even though it's an interactive fiction game that's going to be very niche, I find it pretty satisfying to build. Enough so that I really want to continue the project after the 100 days of code challenge. Though I might challenge myself to 365 days of code, just so I can keep the momentum going.

I definitely don't write a lot each day. Yesterday I only spent 10 minutes writing code. I had to fly out the door. But I still acomplished something. The routine is helpful to keep the momentum going. I think if I took breaks on the weekdays or weekends, It would be more difficult to keep making progress on the project. It's easier to take one-more break after taking the first one. It's much easier to just say to yourself, I need to get this done today. Where in my schedule can I complete it?

I'm really looking forward to the day I can publish this on steam. It'll be very rewarding, I'm sure. But after that, I'll probably just start on the next project. No sense stopping there.

Also i'm bumping up the scotch date to completing 100 Days of Code. I'm getting that bottle of Oban. We'll get a nicer bottle after we get to our release date.

Side note: There's something just so relaxing about listing to the Legend of Zelda soundtrack while making this game. I do it every session. I really never get sick of the music. I love it.

### Day 36: March 20th, 2022
##### Research

**Today's Progress:**
1. Began planning matrix creation for player movement.
2. Researched Linked lists
3. Researched how 2D/3D movement works within game engines.

**Thoughts:**
Lane provided the solution for the problem of player movement. I need matrices to allow the player to move throughout the world.

I need a translation and transformation matrix for player movement.

A vector is multiplied to the matrix to adjust the position of the player.

  x  y  z  t  
  -----------       ---       ----
| 1  0  0  vx |    | x |     | x1 |
| 0  1  0  vy |    | y |  =  | y1 |
| 0  0  1  vz |    | z |     | z1 |
| 0  0  0  1  |    | 1 |     | 1  |
  ------------      ---       ----

Made up for the shortage on work done this week by working on research for over 2 hours today.

### Day 37: March 21st, 2022
##### Research

**Today's Progress:**
1. Started work on coordinate system.
2. Learned about matrices and working with a transformation matrix.

**Thoughts:**
No programming today. Only research and planning. Worked on a coordinate system. Using the first room in the world as a framework for everything else.

### Day 38: March 22nd, 2022
##### Research

**Today's Progress:**
1. Testing co-ordinate system.
2. Further research on movement systems.

**Thoughts:**
I'm not sure how to handle this aspect of the game engine. There are two lines of thought. The first being a co-ordinate system. The other, a 3D linked list. I'm unsure how i'm going to mark individual boxes and areas as movable and walkable areas. This feels like a complex problem that is quite out of my league of understanding at the moment.

I've found two solutions that involve movement. One is a coordinate system, while the other is a system that seems to be comprised mostly of classes. Ive ordered two books to help me solve this problem. I need some expert guidance. It took some digging to find the books that (hopefully) will help.

### Day 39: March 23rd, 2022
##### Research

**Today's Progress:**
1. Learned about the pygame library.
2. Researched pygame_gui library.
3. Researched classes
4. Worked on custom weapon classes.

**Thoughts:**
It looks like the pygame and pygame_gui libraries are the solution to creating a GUI interface for the game. Along with Sound FX, Music and animations.

Classes:

The __str__ method is used for debugging. Instead of returning a pointer of the object, it returns the object as a string.

### Day 40: March 24th, 2022
##### Research

**Today's Progress:**
1. Learned about the super() function.
2. Learned about class inheritance.

**Thoughts:**
I've been making slow progress on the project this week. Lots of learning. I am starting to better understand classes and class inheritence. I'm going to start using them and I think I'm starting to get an understanding of how to impliment them in the program to make my life easier.

Building your own engine is no joke, though I'm really glad I took on this project.

### Day 41: March 25th, 2022
##### Research

**Today's Progress:**
1. Started reading Make Your Own Python Text Adventure - Phillip Johnson
2. Started reading The LIttle book of Adventure Game Programming in JAVA - Huw Collingbourne
3. Attempted building the groundwork for the class structure.

**Thoughts:**
I have a rough idea how to solve the map, rooms and player movement now. We're going to be using classes. There will be a parent class of map, with subclasses of room and player. The player subclass keeps track of which room the player is currently located in. The room class holds items that are in the room, along with interactables, a description and index for the player to move to.

The map parent class I haven't understood how it will work yet. But we're going to try a rough draft here to get this working.

### Day 42: March 26th, 2022
##### Understanding Classes

**Today's Progress:**
1. Built an experimental Room() subclass and Map() superclass.
2. Starting to understand OOP

**Thoughts:**
I finally made some progress. I am starting to understand classes. I don't have my head wrapped around them entirely just yet, but today we definitely made some serious headway. I was able to create getter and setter methods for the Room() class and properly call them.

### Day 43: March 27th, 2022
##### Instance Variables vs. Class Variables

**Today's Progress:**
1. Started learning about the "self" variable.
2. Learned about the difference between class variables and instance variables.

**Thoughts:**
This is a compilation of today's research involving classes. There is still more to learn before I get a comfortable understanding of what in the world is going on:

================================================================================================================================================

* Attribute
	* An attribute can be defined in one of two ways:
		* Instance Variable
			* Varies from object to object.
		* Class Variable ( Static Variable )
			* Declared within a class, but outside of any instance method or constructor (__init__).


================================================================================================================================================

* Class Variables ( Static Variables )
	* Defined within a class
	* Shared with all instances (objects) of a class.
	* When accessing class variables, it is recommended to use the class name.
		* class Student()
			school_name = 'ABC School'	# Class Variable
			def __init__(self, name):
				self.name = name	# Instance Variable
		* print(Student.school_name)		# Printing Class Variable

* Instance Variables
	* Owned by the instances of a class.
		* For different instances, the instance variables are different.
	* A variable defined inside a class.
		* For which each instantiated object of the class has a seperate copy, or instance.
	* Has similarities with a class variable, but is non-static.
	* An class variable is declared in a class but outside of constructors, methods or blocks.
	* Instance variables are created when an object is instantiated.
		* Instance variables are accessible to all the constructors, methods or blocks in the class.

================================================================================================================================================

* Class Methods
	* Inform about the status of the classs.

* Instance Methods
	* Set or get details about instances or objects.
	* When defining, the foremost parameter of the method must always be self.
	* Can easily access different attributes and methods with the help of the self variable.
	* By using the self.__class__ attribute, instance methods can also access the class.
	* Are able to modify the class state.

================================================================================================================================================

* The self Variable
	* Has the power to modify the state of an object.
	* The self variable is replaced by the object
		* obj = myClass()
		* obj.instance_method()
		* or
		* myClass.instance_method(obj)
	* Not a defined keyword, but a convention
	* Self represents the instance or objects of a class and binds the attributes of a class with specific arguments.
	* The use of the self variable in python helps to differentiate between the instance attributes (and methods) and local variables.

================================================================================================================================================

* __init__
	* The __init__ method is a constructor
	* This method is called when the object is created.
	* It sets up the initial state of the object

* __dict__
	* Contains all variables and their values within them.

### Day 44: March 28th, 2022
##### Namespaces, Method Types and Dunder Methods

**Today's Progress:**
1. Added .gitignore file to prevent __pychache__ from being uploaded to the git repository. Thanks to Trevor Kanten for the suggestion.
2. Learned about built-in, global and local namespaces.
3. Learned about decorator flags.

**Thoughts:**

Compilation of Today's Research:

=================
Types of Methods:
=================

* Instance Method
	* Takes one parameter, self.
	* Can modify instance state.
	* Can also access the class itself through the self.__class__ attribute.
		* Can modify class states.

* Class Method
	* Takes a cls parameter that points to the class.
	* Cannot modify instance state.
	
* Static Method
	* Does not take any self or cls parameter.
	* Can have arbitrary parameters passed to it.
	* Restricted data access.
	* Primarily used to namespace your methods.
	* Have limited use cases.
		* Cannot access the properties of the class.
	* Used when you need a utility function that doesn't access any properties of a class, but makes sense that it belongs to the class.

===========
Namespaces:
===========

* Namespaces
	* A collection of currently defined symbolic names along with information about the object that each name references.
	* Similar to a dictionary in which the keys are the object names and the values are the objects themselves.
	* The python interpreter understands what exact method or variable one is trying to point to in the code, depending upon the namespace.

* Types of Namespaces
	* Built-in namespace
		* print()
		* id()
	* Global namespace
		* Created when a user creates a module
	* Local namespace
		* Created within local functions
	* The built-in namespace encompasses the global namespace.
		* The global namespace encompasses the local namespace.

* What is a namespace?
* What is a namespace used for?

===============
Dunder Methods:
===============

* What is a dunder method?
* What is the purpose of a dunder method?
* How many dunder methods are there?

### Day 45: March 29th, 2022
##### Class Methods & Static Methods

**Today's Progress:**
1. Learned the difference between instance variables and class variables and when to use them.
2. Learned applications for class methods and static methods.

**Thoughts:**

* The self variable is passed because the instance is automatically passed as a parameter.
* Mathods always take the self variable because they are always passed the instance when called.

================
Instance Method:
================

* Frequently used.

=============
Class Method:
=============

* Need a class method decorator at the top.
* @classmethod
* def set_raise_amt(cls, amount);
* 	  pass

* Class methods can also be used as alternative constructors.

==============
Static Method:
==============

* Does not get passed self or cls.
* Does not use the instance or the class.
* Can have custom variables passed to it.
* A method should be a static method if it does not access the class or the instance anywhere in the function.

### Day 46: March 30th, 2022
##### Wrapping Up Classes Research

**Today's Progress:**
1. Learned about class inheritance.
2. Covered dunder methods.
3. Learned about __str__
4. Learned about __repr__

**Thoughts:**

I finished the classes playlist from Corey Shafer today. I have a much better idea how to use and impliment classes into my code now. I am well aware that I still don't know everything there is to know about classes, but I am more aware of what I don't know now. So if I do need to learn something else for implimentation for the game, I should be able to learn it. The time I took to work on the research has been really refreshing, and a nice break from directly programming the game. I feel like tomorrow I'm going to have a much more fresh look at creating the map and room solution.

We haven't got a lot of progress done on the game this week, but I feel like I've grown as a programmer spending the time learning more about classes. I'm glad I did. Looking forward to seeing what all I've accomplished by day 100. Both in the project and what I've learned.

* What is Method resolution order?
	* The order in which python looks for the __init__ method when searching through class inheritence.
* What is builtins.object?
	* 
* What is the super() function?
	* A function that referrences the parent class.
* How do I use NotImplimented?
* How do I use the property decorator?
* How and when should I use decorators?

### Day 47: March 31st, 2022
##### Working With Classes

**Today's Progress:**
1. Created items.py
2. Added a Weapon class
3. Added a handful of item classes.
4. Begun work on code structure.

**Thoughts:**

I'm back in the thick of it again. I'm considering refactoring some of the code.

I think for the room objects, we'll use an (x,y,z) co-ordinate system. It will be a lot easier to keep track of, and I can draw it out on grid paper.

I can pass tuples into the object to observe what locations are connected to each other. I will need another value to pass to indicate the player can not move in that direction. Maybe a False variable.

### Day 48: April 1st, 2022
##### Room / Map Classes

**Today's Progress:**
1. Added rooms.py
2. Worked through thought logic of the map, player position, and how to implement xyz values.

**Thoughts:**

Making progress. Short code today, busy day. I will continue with the project and give it more attention as much as I can.

### Day 49: April 2nd, 2022
##### Room / Map Classes

**Today's Progress:**
1. Outlined player movement in the Player() class.
2. Added Item & Rusty Key as class.

**Thoughts:**
Even though I've done enough research on classes. It's still complex to work with them. This is part because of the coordinate problem. It is a complex problem that is not easy to wrap your head around. I've got a start, and we're going somewhere, but it's also unclear where I should wind up.

I feel like the problem is 80% solved. I'm just tired and not able to see the whole picture clearly.

100 Days of code was no joke. It's not easy programming every day. Some days you really don't want to. But it's nice to see the progress I've made thus far.

I'm not going to give up. There's plenty of work left to do.

### Day 50: April 3rd, 2022
##### 3D Plotting

**Today's Progress:**
1. Working on 3D Plotting the map.
2. Attempting to deconstruct reality.

**Thoughts:**

This is so far out of my comfort zone. I'm pretty sure I need a 3D list to store all of the plotpoints that the player can move to. There is a number of problems. The first is, I'm not sure how to generate this list. Secondly, how do I mentally picture the Z-axis? I have a basic understanding of how a 2D list would work. But once we add the Z-axis, everything gets way more complex.

I'm curious how other people have solved this problem, and how I can figure out how to conceptualize this in my head. Once I can get the visualization of how this should work, writing the code shouldn't be too difficult.

### Day 51: April 4th, 2022
##### 4D Cubes

**Today's Progress:**
1. Worked on 4D addressing cube.

**Thoughts:**

Encountered a problem with the cube. When I go to print the address, it reverses the print statement, printing the coordinates backwards. I'm not sure yet how to fix this. 

### Day 52: April 5th, 2022
##### List Generation

**Today's Progress:**
1. Worked on understanding the xyz generation method provided by Austin L. Howard

**Thoughts:**

I'm a bit lost, sometimes programs can get quite complex and breaking them down to understand them isn't always easy. But we're making progress. Even if it's slow.

### Day 53: April 6th, 2022
##### 

**Today's Progress:**
1. Worked on understanding the grid system.
2. Evaluating if I need a 3D grid or even a grid system in general.

**Thoughts:**

I need to review how I want room creation to work. Because it's a confusing problem that could be tackled in a number of ways.

I want to create an object that is a room. That room knows about it's other nearby rooms, but they are not loaded into memory. The only object that is loaded into memory is the current room the player is standing in. Once a player leaves a room, the previous room should be cleared from memory.

This makes me wonder if I need a grid at all, or if I can just individually create each object as the story progresses. I'm not sure who to ask, or if I should just try it, and if it doesn't work, rework it.

I've been stuck without much progress for a while now. I'd like to get the ball rolling again and make some headway. I keep getting bogged down in this grid system, when I barely understand how I would impliment it. I don't really have a plan for how to make this work. I have rough ideas in my head I'd like to try out but some of these pathways are rather difficult for a novice programmer.

I would like a challenge, but I don't want to put my brain through a meat processor.

I might do a node based system when creating each object so it is aware of the rooms around it. But this had something to do with perhaps storing all objects in memory at once which a bad practice? I'm not sure, I don't know enough to know what are both good and bad practices are, especially when starting out. This is why I find leet code much more frustrating for beginners. It's hard to understand where to even begin when you're told you should be focused on doing it the correct way. While the correct way may be far more complex than simply accomplishing the task itself.

I just want to get this done. I might just start powering through some code ideas. Wether they are best practice or not. I can come back and refactor my code when I have more experience under my belt. Otherwise i'm just going to get far too discouraged to even bother continuing the project. I want to see some results.

### Day 54: April 7th, 2022
##### 

**Today's Progress:**
1. Refactored map.py
2. Removed the Map class.
3. Removed xyz coordinate system.
4. Clarified Room function.
5. Learned about data encapsulation.

**Thoughts:**

I might have found the solution to the mapping problem.

So I do need an index. But I don't necessarily need a grid system. But in a sense, I do. Let me explain.

The solution was explained in The Little Book of Adventure Game Programming in Java: Chapter 2 - The Map.

Essentially, when each room object is created, it is aware of what rooms are connected to it. We will call these room exits. These room exits contain an integer value. This integer value is the index for an array. This array we will call map.

The map array is a list of all room objects. So in order to load a room, the player must move to the index. When the player moves to that index, the object is loaded into memory.

I believe initially I was on course to create the game like this, but got side tracked and stuck in the mud. We're back on track and should soon have this problem solved.

In regards to data encapsulation, I learned that python doesn't have private variables. However, data encapsulation is still possible through a standard convention. Variables with two underscores "__" are not to be called outside of a class. But rather modified and called by the methods within that class.

### Day 55: April 8th, 2022
##### Building the World

**Today's Progress:**
1. Began appending room objects to the map list.
2. Defined the __repr__ method.
3. Working on __str__ method.

**Thoughts:**

Tired today. Made a little bit of progress though. We should be able to try testing moving the player between rooms soon. I need to figure out how to print out __str__ before I keep going though.

### Day 56: April 9th, 2022
##### QoL

**Today's Progress:**
1. Learned how to correctly call the __str__ dunder method.
2. Formatted Room's __str__ output.
3. Began work on player class.

**Thoughts:**
I got the __str__ dunder method to work for the Room class. Now that I have 4 rooms set up, I should be able to create a singular object variable that is loaded in based on conditional logic. We should be able to use a while loop to continually get player input. Then as the player moves, print the index that the player is in. If the player attempts to exit out of the wrong direction, an error message should be displayed to the player.

This is a little bit more in-depth, but I can break these down into more simple problems.

### Day 57: April 10th, 2022
##### Player Movement

**Today's Progress:**
1. Created test environment for moving the player.

**Thoughts:**
Today is a really good day. My first prototype for player movement is done. I can use the map, which is created the room objects. I can reference the object instance variables. Everything works. It's with classes and it works. I'm so happy! It took so long to figure this out hahaha.

### Day 58: April 11th, 2022
##### Adv. Room Creation

**Today's Progress:**
1. Removed unused index variable from Room() class.
2. Worked out thought process for associating puzzles with rooms. 

**Thoughts:**

Ok. So I have a rough outline of how the player can move from one room to another. Now I need a way of creating puzzles inside these rooms. I already have one built puzzle. The oxygen puzzle which uses threading. I'm not sure how I can make this part of the object. Do I want a seperate file just for created rooms? Here I would define the objects i'm creating with their own methods?

Do I need a puzzle class? Or should puzzles still be their own seperate functions that are called when a player is inside a certain room?

If I want to associate a puzzle with a room, how do I do that? Should the puzzle be in its own function? Or should the puzzle be a method within the object?

If the puzzle is a method within the object, can I create methods that are specific to individual objects? Is that a thing?

### Day 59: April 12th, 2022
##### Learning Code Organization

**Today's Progress:**
1. Researched when to use class inheritence.
2. Researched code organization through packages and modules.

**Thoughts:**
Started covering how to organize my program with packages and modules. Getting a bit lost in classes and how to proceed with the next steps. Nothing out of the originary, haha. I find the project very dense and difficult to maneuver. I think I'm at a stage where if I can get my entire program organized and still operational, it will help me to continue building it. Right now, everything feels quite messy. Even though I've done my best to organize it, it's not where it could be.

I still often feel discouraged about just how much there is to learn about programming. I can write a few scripts, but developing a full application is a whole different story. The more you learn, the more you realize how much there is to learn, and how little you really know. Then you wonder how can you ever learn all there is to know? It feels like climbing a never ending mountain, but you can always take a breath to admire the view from wherever you are along the journey.

When I set out to do this project, I thought that I wouldn't run into many hiccups. That there might be some challenges, but it wouldn't ever really be all that hard. But in reality, it was far more challenging than I was expecting. Learning how to teach yourself without the aid of others is perhaps the most difficult. There are of course mentors and friends who are willing to lend a hand when you've been stuck on a problem for a while, but you in a sense have to be your own guru. You have to figure out where your problem is, then work towards the solution for that problem.

This is especially difficult when you don't really know what the problem is. Defining the problem is half the problem. Sometimes the concepts feel so advanced that you have to say: "Ok, I need to go over the fundementals." Which is okay. There's nothing wrong with that. It's a very humbling experience. I don't think I ever want to stop learning how to program. There's something very captivating about it all. It's a challenge I've never really encountered before and I find it very rewarding. But it is no joke. If you ever think programming won't kick your ass, you're dead wrong.

### Day 60: April 13th, 2022
##### Organization

**Today's Progress:**
1. Added docs folder for .md files.
2. Created README.md

**Thoughts:**
I need to place the puzzle mechanic for the starting room outside of the Room object class. Started organizing the program a bit more. I'm not even sure where to start, but we'll get there.

### Day 61: April 14th, 2022
##### Research

**Today's Progress:**
1. Read introduction and chapter 1 of Adventure Game Programming in Java by Huw Collingbourne.

**Thoughts:**
Learned that I need to properly parse input correctly with a delimiter list. The parse should result in a list of words that were used by the user. I can't believe I didn't think of this. I'm going to add this to the user_input function right away.

### Day 62: April 15th, 2022
##### Staying on Track

**Today's Progress:**
1. Changed parent directory from knights_court to adventure_game
2. Created a trello board for keeping track of what is currently being worked on.
3. Created quit functionality for user_input() function.

**Thoughts:**
I need to break the code down further into bite size chucnks. I often look at all of the things I need to do and get overwhelmed and struggle to do anything significantly productive. The primary reason for this comes from the code base being so big and seemingly unorganized, while having a large list of things that need to be fixed or built upon in order to progress.

The map.py code is a great example. I know I need to start incorporating player movement into the main function in side the main.py file, but how do I do this correctly? I know there should be a running while loop in there, and the user should be able to quit the game. Maybe i'm missing functionality before including this?

I'm having a hard time telling if i've lost motivation for the project, and I'm just doing barely enough to qualify this as a submission for each day, or if my head is so busy with life outside this project that it makes the project itself much more difficult to focus on.

I want to continue this project and I want to see it to the end. I also want to do a really great job of making it a game worth playing. Not something i've simply finished for the sake of finishing it. There's 28 days until the challenge is complete. Which is all well and good, but considering how little i've managed to contribute this last month, it hardly feels like im making much of any progress at all.

Maybe i'm being too hard on myself. I just want to make this happen.

### Day 63: April 16th, 2022
##### Game Loop Structure

**Today's Progress:**
1. Worked on solving how the game loop will run.

**Thoughts:**
The game loop is tricky. I think the biggest challenge I've had with learning how to program is structure. Learning how to approach problems to break them down into smaller problems. But there are times when you have to look at the whole and work backwards. Which is a weird line of thinking.

Either way, we have a heading for the game loop. I'm pretty sure referrencing the class index variable for the Player class is a good way to go about filtering what sections of the game to run. I'm not 100% sure if this is the best way to do this, but its a start.

### Day 64: April 17th, 2022
##### 

**Today's Progress:**
1. Started integrating previous code into while loop.

**Thoughts:**

I didn't have much time to program today. My day got flipped topsy turvey. I need to make up for the lack of programming today this week. I wanted to at least add a contribution.

