# Change log
## 20221113
  *  Change inittime in .glparchis files to played seconds.
  * There is not 10 moves threat if there is no pieces to enter final square with a throw.
  * Improving delays.
  * Fixed lots of bugs.
  * Fixed pip dependencies.

## 20181125
  * Created glparchis_shortcuts.exe in Windows to create Desktop shortcut
  * Fixed update detection system

## 20181115
  * Created a pypi project from glparchis-20181020 with package structure
  * Migrated to github

## 20181020
* Added action to hide/show left panel
* Added automatism to the dice
* Added automatism to pawns when only one can move

## 20180510
* Added 3 players mode
* Now you can report a bug from glParchis

## 20180416
* Windows: Solved annoying bug. User needed to do several clicks to move a piece
* Improved OpenGL code and it's documentation
* Added Doxygen document system for developers
* Windows: Solved bug showing objcts in About menu

## 20180308
* Linux: Fixed bug loading translation files

## 20180307
* Now you can throw the dice pressing ENTER
* Added Zoom IN / Zoom OUT actions to the menu

## 20170726
* Added delay between movements as a settings option
* Added difficult level as a settings option
* Added board zoom  with keys + and -
* Installation statistics added to the game
* Windows distribution file has been upgraded to a msi file. Please uninstall the old glparchis before installing the new one

## 20160812
* Fullscreen state is saved in settings file
* Added statistics system in Sourceforge database
* Added option to do not contribute to world statistics

## 20160801
* Splitter game configuration is saved with fullscreen and normal data

## 20160623
* project_i18n script added to translate project documentation
* Board rotates pressing m key
* Improved performance
* Fullscreen icon error fixed

## 20160325
* Sound configuration is saved now in settings
* Makefile have been changed to compile with make and to install with make install
* Windows sources are not going to be released
* 32 bits and 64 bits windows versions are going to be released
* Phonon support have been droped. Now we use QMultimedia
* We have migrated to PyQt5
* We have added full screen support

## 20130716
* When you eat a piece in the first spacem, this piece is the last in arrive, when both pieces are of different color.
* Change color pink by fuchsia, cyan by darturquise and orange by darkorange 
* Compatibility added with old highscores
* Added autosave support
* Improved user interface
* Solved bug when closing app
* Added option to follow the current player in the user panel
* When saving the current game, it saves now inittime and the number of eaten pieces
* App has been migrated to python3. I have test it with python 3.3

## 20130228
* About menu shows a dice
* cmdDado improved
* Double click on the board to roll the dice
* Solved bug when there's a new game version
* Added support to highscores
* Added 6 and 8 players game

## 20120921
* Bug solved looking for game updates
* Numerical textures added to places
* A sound plays after rolling 3 sixes, if you go home.
* You can save the game even when all the players are IA
* Game sounds updated
* Dice double click bug solved
* The dice is now in 3D

## 20120917
* Bug solved when pressing ESCAPE. Now it exists the game
* Switch off / on sound added
* Screen hyperlinks are now clickable.
* New menu option to look for update manually or each 7 days
* The splitter now shows the board by default
* English is the default language. You can change the language at Settings. Settings will be saved for the next execution
* A game handbook have been added To read press F1
* All popups are now inside the screen

## 20120914
* Windows and Linux binary distribution
* Solved bug when pressing cancel at initial dialog
* Solved several bugs

## 20120910
* Solved bug with saved games directory
* Dice text changes color to the current player color
* Score system added. It uses the number of moved places. 
* A crown is added in statistics table to show the player is winning the game.
* IA first movements are now showed
* Solved several bugs
* IA improved using probabilities.
* A game timer has been added
* User panel logs have been improved

## 20120902
* Initial support to the application
* The app has all the funcionality. We need to improve the virtual players
