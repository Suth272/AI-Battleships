# AI Battleship
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/607c7522-f793-46ab-8c50-709593029992)
AI Battleships is a Python terminal game, which runs in the Code Institue mock terminal on Heroku. 

Users can control a virtual battleship and fire shells at a fleet of battleships controlled by AI. The player must find and destroy all the battleships before they run out of shells (turns), with each battleship occupying one space on the board.

## Live Site

You can view the deployed site [here](https://ai-battleship-6bf0fdd14ba3.herokuapp.com/).


## Repository

You can view the repository [here](https://github.com/Suth272/AI-Battleships).

## Author

Sutharshanan Alagarajah

## How to play
AI Battleships is based on classic battleships game, however in this version the user plays against an AI computer instead of another user/player.

In this version, the player is shown an empty grid, where there are hidden AI controlled battleships.

The player then inputs in co-ordinates that corespond to a space on the grid, in attempt to hit a ship.

If the guess successfully hits a ship, it is marked on the grid with a ```X```.

If the guess misses, the co-ordinate that the player guessed will be marked with a ```O```.

## Features
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/66dd44f5-facc-4c6a-80b1-a364ae140dd6)

+ Random board generation - The computer randomly places 5 ships on the board.
+ Play against the computer
+ Accepts user inputs
+ Records user inputs
+ Turn counter - A turn counter that counts down on how many turns the player has left.
+ Data maintained in class instances

![image](https://github.com/Suth272/AI-Battleships/assets/159195438/b4011ac5-af43-46a3-8b3b-ce1cc3b70d47)

- Input validation and error checking
     - You cannot enter co-ordinates outside of the grid
     - You must enter a number for the row
     - You must enter a letter for the column
     - You cannot enter the same guess twice

## Future Features
- Allow the computer to fire back against the player and for the player to pick where to place their ships in the grid.
- Remove the limits for turns and instead have a counter on how many turns it takes for the player to hit all the AI battleships.
- Have ships take up more than a 1x1 grid space.

##  Data Model
My project uses a Board class and a Ships class as my model. The game creates two instances of the board class. First to create a board that is hidden from the player and contains the computer's ships that have been randomly generated. Secondly to create an empty board that is used by the player to make guesses of where the AI battleships are. 

The Board class has a print method to help play the game, but is mainly used to store the guesses of the player and where the computer's ships are. 

The Ship class is used randomly generate the computer's ships on the board, plots the user's inputs on to the guess grid and keeps track of the ships that have been hit.

## Testing
This site has been tested in all aspects, all of which can be seen below.
## Validation Testing 

This section shows the successful tests from the appropiate code validators.

### Python Validation
No errors or warnings were returned when passing the Python validation test, apart from formatting errors. It should be noted that that a double space indentation was used instead a 4 space indentation, as it prevented the code from running properly.

The Pythonn validator that was used can be found [here](https://pep8ci.herokuapp.com/).

![image](https://github.com/Suth272/AI-Battleships/assets/159195438/b34b4fa6-9d0d-4a91-80ec-df42c12a434e)

## Manual Testing
I have manually tested this project by doing the following:
- [x] Given inalid inputs - strings when numbers were expected and vice versa, out of bounds inputs, repeating the same inputs
- [X] Tested it in my local terminal and the Code Institure Heroku terminal

## Defect Tracking
While coding the website, defects have occured throughout the build, which I have fixed as the project progressed. All the defects have been recorded in GitHub Issues. They can also be seen in the screenshots below.

### Issue 1:
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/3ea7f6c5-6b1d-4ee2-9570-78edacf76f7b)

### Issue 2:
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/effe76d3-223e-41cc-938f-d4fc115f31cb)

### Issue 3:
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/73180108-dc3b-440a-a0f1-d3b66f79a305)

## Outstanding Defects
There are no outstanding defects in the code/site.

# Deployment
The site was deployed to Heroku from Github.

## Deploy to Heroku Pages
1. Press the **Create new app** button on the Heroku website.
2. Then type in an app name in my case it is **ai-battleship**, choose your region (in my case it was **Europe**) and then press **Create app**.
3. Navigate to the **Settings** tab then press the **Reveal Config Vars**. Set where it says **KEY** to **PORT**, set where it says **VALUES** to **8000**, and then press the **add** button.
4. Scroll down and press thee **Add buildpack** button, select **python** and press **save changes**. Repeat this for **nodejs**. Make sure the python package is above the noed.js package.
5. Navigate to the **Deploy** tab, click on **Github** for deployment method and press **Connect to Github**.
6. Search up and connect the desired repository.
7. Scroll down and press the **Deploy Branch** button under Manual deploy. Wait a couple minutes and a link to the deployed site should be linked below.

# Credits
## Content
+ Code Institute for the deployment terminal
+ Knowledge Mavens [video](https://youtu.be/tF1WRCrd_HQ?si=SLGftFEWLsGraNo-) for code snippets, but modified for my object oriented project.
