# bot
osrs runelite color bot
it only runs in 1920x1080 resolution havent fixed it to run on any pc yet

can see how bot runs here - https://www.youtube.com/watch?v=jdZOW1HxIK4&ab_channel=KyleVerwey 

Hello any and everyone,
this is my botting script written in python with pyautogui and keyboard inputs with win32gui

Firstly id like to say that this is educational and not product ready. I wanna show how im able to write scripts in python for osrs with runelite
and hopefully help others create there own custom scripts for games they love and practice their skills at the same time

when running the script if you try you have to click the compass on minimap to face north then pull the zoom all the way back and look vertical


The script im going to explain here is the trueblood.py script under the runescrafting folder in the blood secondary folder.

firstly, there are some settings we need to change in runelite, dont worry its not a lot

![settings](https://github.com/starzzots/bot/assets/108106818/2dc30d69-eaba-4f02-9871-2760bc89509c)

1)first setting is the enity hider 
![entityhider](https://github.com/starzzots/bot/assets/108106818/3f7342f8-26cb-428b-a203-c42909c15e8e)


we need to change it so it hides everything in the game so you dont click on monsters and players by acciendent

![entitysettings](https://github.com/starzzots/bot/assets/108106818/4248f490-4382-4148-b077-548d11cdae8b)

2)next step is we need to set the zoom for this script to 300 later it can be changed when you get comfortable writing your own scripts but for now lets change this

![zoomsettings](https://github.com/starzzots/bot/assets/108106818/d011ff6f-cb5b-40fc-91fc-365143331a07)

![camerazoom](https://github.com/starzzots/bot/assets/108106818/8d1a8798-64b5-42c9-b218-cca28eea6e26)

3)next step inventory tags. This lets you change color of objects in your inventory and give specific RGB values which is the core to the way I script osrs

![invotags](https://github.com/starzzots/bot/assets/108106818/61687a53-1f50-463b-a25c-c70768912359)

![inventorytagsettings](https://github.com/starzzots/bot/assets/108106818/a7308a36-5225-4311-854e-278df37c7d34)

4) now we need ground and object markers on same concept as before we we be able to mark the ground tiles any color we like and objects such as doors and walls ect

![groundmarker](https://github.com/starzzots/bot/assets/108106818/76fcb190-93e5-4771-973f-a49e2b2ea830)
  ![object marker](https://github.com/starzzots/bot/assets/108106818/8d8adf02-44dc-44fe-986e-27fa7bf8294f)
  


![groundmarkersettings](https://github.com/starzzots/bot/assets/108106818/fee3900a-f0d2-4322-b9f9-f301f39e874e)
  ![objsettingsosrs](https://github.com/starzzots/bot/assets/108106818/0537512a-ba4a-4d83-a1e6-39f66b52edd8)

Now we have that out of the way your 90% of the way there

next we need to mark the ground tiles and give them rgb values these can be changed to any color you want but for the runcrafting script you can either go in and change the rgb values to the ones you picked here in the code otherwise use these rgb values

![rgbvalues](https://github.com/starzzots/bot/assets/108106818/d9d38cdb-421c-4b40-a96a-7bf0f1ebaf12)


![Capture](https://github.com/starzzots/bot/assets/108106818/04acfd87-534f-4d45-8197-257113bd95b3)

![secondtiles](https://github.com/starzzots/bot/assets/108106818/dd0973bd-a2db-466d-a470-55ed67147f85)

![3tileset](https://github.com/starzzots/bot/assets/108106818/d0f3a400-83a1-4cf7-bf8c-dc337f6db114)

![4tileset](https://github.com/starzzots/bot/assets/108106818/a1185d45-d1e5-40a9-bf4e-f3acd95f3da0)

![tilesethouse](https://github.com/starzzots/bot/assets/108106818/d91fa168-b0a1-469b-80cf-eee04292dc4c)

after all this the script is ready to run!

![run](https://github.com/starzzots/bot/assets/108106818/0b097078-08e5-4aa8-9841-240d16047e52)




