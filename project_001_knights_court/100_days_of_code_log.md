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