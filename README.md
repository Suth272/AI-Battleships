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
     - You cannot give an blank/empty input

## Future Features
- Allow the computer to fire back against the player and for the player to pick where to place their ships in the grid.
- Remove the limits for turns and instead have a counter on how many turns it takes for the player to hit all the AI battleships.
- Have ships take up more than a 1x1 grid space.

##  Data Model
My project uses a Board class as my model. The game creates two instances of the board class. First to create a board that is hidden from the player and contains the computer's ships that have been randomly generated. Secondly to create an empty board that is used by the player to make guesses of where the AI battleships are. 

The Board class has a print method to help play the game, but is mainly used to store the guesses of the player and where the computer's ships are. The class is also used randomly generate the computer's ships on the board, plots the user's inputs on to the guess grid and keeps track of the ships that have been hit.

## Testing
This site has been tested in all aspects, all of which can be seen below.
## Validation Testing 

This section shows the successful tests from the appropiate code validators.

### Python Validation
No errors or warnings were returned when passing the Python validation test.

The Pythonn validator that was used can be found [here](https://pep8ci.herokuapp.com/).

![Image](https://github.com/user-attachments/assets/a14c295f-e074-491e-add5-303d5ab1a7ff)

## Manual Testing
I have manually tested this project by doing the following:
- [x] Given invalid inputs - Inputting strings when numbers were expected and vice versa, out of bounds inputs, repeating the same inputs and empty inputs return the appropiate error to the user, without crashing the application.
- [x] Tested the error handling of the application - Purposely provided invalid inputs and successfully recieved an error handling message that clearly tells the user on how to provide a valid input.
- [x] Tested the computer created targets for the user to try to hit - Adjusted the code to create a smaller board, so it would be easier to hit the target and see if the computer actually made targets.
- [x] Tested for hit and miss messages, as well as counter - Provided multiple valid inputs to see if the target was hit or not on the board, which was shown on the board by an X or O respectively. The application successfully returned a hit or miss message and provided the updated number of remaining turns as the counter every time.
- [x] Tested to see if win/loss message appeared at end of the game:
     + Tested the loss message by providing random valid inputs until the number of turns ran out. The application successfully displayed a loss messager everytime.
     + Tested the win message by adjusting the code to have the number of turns equal the number of spaces on the board. Valid inputs were then provided until the board was filled, which would mean all ships would have been hit. The application would return a successful win message everytime. I also tested it when the number of turns exceeded the nhumber of spaces on the board and the outcome was the same.


## Defect Tracking
While coding the website, defects have occured throughout the build, which I have fixed as the project progressed. All the defects have been recorded in GitHub Issues. They can also be seen in the screenshots below. (Please note that issue 4 on the github issue tracker is used as an image library for the README file, hence a jump in issue number on the images).

### Issue 1:
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/3ea7f6c5-6b1d-4ee2-9570-78edacf76f7b)

### Issue 2:
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/effe76d3-223e-41cc-938f-d4fc115f31cb)

### Issue 3:
![image](https://github.com/Suth272/AI-Battleships/assets/159195438/73180108-dc3b-440a-a0f1-d3b66f79a305)

### Issue 4:
![Image](https://github.com/user-attachments/assets/78c2d55e-63f3-4cae-b164-3ffc766e1a88)

### Issue 5
![Image](https://github.com/user-attachments/assets/0fa0e310-8cbb-4ebc-8b9a-b8df3666d2e5)

### Issue 6
![Image](https://github.com/user-attachments/assets/6797d666-d37d-441e-bd77-e7914d731bb2)

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
