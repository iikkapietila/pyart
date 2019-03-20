Pyart beta v0.1 by Iikka Pietilä 2019

This is a Python implementation of ART method (Affective Reaction Times) which can be used to e.g. measure semantic distances between symbols or icons or to test/compare other artefacts with a priming expression. Tested on python 3.5, 3.6, 3.7. Libraries used: os, tkinter, time, PIL (aka PILLOW), random and csv.


In this beta version a screen resolution of 1920 x 1080 is assumed. The programme will run on top and in fullscreen. In the beginning of the testing sequence a countdown is displayed. Please click anywhere on this screen to make sure that the testing windows is focused so keyboard input functions correctly.

The programme functions in the following manner:
-A folder named "pictures" (case sensitive) is assumed to be placed in the same folder as the pyart_0_1.py. This "pictures" folder includes the pictures that are wanted to be shown during the test.
-A file named "sentences.txt" (again, case sensitive) is assumed to be placed in the same folder as thee pyart_0_1.py. This "sentences.txt" file includes the priming sentences / expressions that are wanted to be shown during the test. Each expression should be placed on their own line.
-Programme generates an image pair list for each expression so that all of the possible combinable pairs of pictures will be tested against each other for each expression. The order is semi-randomized using random.shuffle() function.
-Procedure consists of iterating all the possible pairs for each expression so that the expression is displayed first for three (3) seconds and the pair is displayed until the selection is made.
-In the beginning of execution the programme asks the csv file name in which user wants to save the output of the selections. File will be named with date and time prefix + user input (+ .csv). 
-On each line of the csv the output is saved including Expression, Pressed Key, Picture 1 filename, Picture 2 filename, Selection starting time, Selection ending time, Selection duration, Selected picture filename. These are separated with a ",", comma.
-Programme runs until all of the possible pairs have been tested for each expression.
-Programme can be aborted by using the Escape key during image display (clean) or for acute exit alt + f4 can be used (unclean).


For comments, bugs, problems and needs for next versions can be sent to: iikka.pietilae@gmail.com

(c) Iikka Pietilä 2019
http://www.iikka.org/
iikka.pietilae@gmail.com

