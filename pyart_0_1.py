import os
from tkinter import *
import time
from PIL import ImageTk, Image

import random
import csv

r = Tk()

RESOLUTION_X = r.winfo_screenwidth()
RESOLUTION_Y = r.winfo_screenheight()

r.destroy()

FULLSCREEN = True

# This is the function for the launcher window that has the countdown and
# reminder to click on the screen for activation
def launcher_window():
    root = Tk()
    root.lift()
    root.focus_force()
    root.attributes("-fullscreen", FULLSCREEN, "-topmost", True)
    canvas = Canvas(root, width=RESOLUTION_X, height=RESOLUTION_Y)
    canvas.pack()

    secs = 5

    # Countdown here. Above variable "secs" defines the time for the countdown
    while secs >= 0:
        text = "Please click here to activate the windows. \n" \
               "Use the letter F or J to make the selection. \n \n \n" \
               "Your test will begin in " + str(secs)

        c = canvas.create_text(RESOLUTION_X / 2 - 50, RESOLUTION_Y / 2 - 50,
                               text=text, font = "Arial 50")

        canvas.update()
        time.sleep(1)
        canvas.delete("all")
        secs = secs -1

    root.destroy()
    root.mainloop()


# This is the function for displaying the primes / sentences
# Again, variable "secs" defines the time the prime will be shown
def sentence_display(sentence):
    root = Tk()
    root.lift()
    root.focus_force()
    root.attributes("-fullscreen", FULLSCREEN, "-topmost", True)
    canvas = Canvas(root, width=RESOLUTION_X, height=RESOLUTION_Y)
    canvas.pack()

    secs = 3

    while secs >= 0:
        c = canvas.create_text(RESOLUTION_X / 2 - 50, RESOLUTION_Y / 2 - 50,
                               text=sentence, font = "Arial 25")

        canvas.update()
        time.sleep(1)
        secs = secs -1

    root.destroy()
    root.mainloop()
    return


# This is the function for displaying information that the test has ended
def exit_window():
    root = Tk()
    root.lift()
    root.focus_force()
    root.attributes("-fullscreen", FULLSCREEN, "-topmost", True)
    canvas = Canvas(root, width=RESOLUTION_X, height=RESOLUTION_Y)

    canvas.pack()

    secs = 3

    while secs >= 0:
        text = "Test is now over. Thank you. \n" \
               "Software exiting in " + str(secs)

        c = canvas.create_text(RESOLUTION_X / 2 - 50, RESOLUTION_Y / 2 - 50,
                               text=text, font = "Arial 50")

        canvas.update()
        time.sleep(1)
        canvas.delete("all")
        secs = secs -1

    root.destroy()
    root.mainloop()



# The main window for showing the pictures.
def window(picture1, picture2, time_beginning, csv_file, sentence):
    root = Tk()
    root.focus_force()
    root.update()

    root.lift()

    root.attributes("-fullscreen", FULLSCREEN, "-topmost", True)

    canvas = Canvas(root, width = RESOLUTION_X, height = RESOLUTION_Y)

    # Between-function for calling the keypress handler and also destroying the
    # previous window
    def keypressnode(key):
        if key.char == "f" or key.char == "j":
            keypress_handler(key.char, picture1, picture2, time_beginning,
                             csv_file, sentence)
            root.destroy()
        else:
            return

    canvas.bind("<KeyPress>", keypressnode)
    canvas.bind("<Escape>", lambda e: quit())
    canvas.pack()
    canvas.focus_set()

    img1 = ImageTk.PhotoImage(Image.open(picture1))
    img2 = ImageTk.PhotoImage(Image.open(picture2))

    img1_x = (RESOLUTION_X / 2) - (img1.width()) - 60
    img1_y = (RESOLUTION_Y / 2) - (img1.height() / 2)

    img2_x = (RESOLUTION_X / 2)
    img2_y = (RESOLUTION_Y / 2) - (img2.height() / 2)

    canvas.create_image(img1_x, img1_y, anchor=NW, image=img1)
    canvas.create_image(img2_x, img2_y, anchor=NW, image=img2)

    canvas.focus_set()
    root.mainloop()


# This function just takes the input and saving information from mainwindow
# and calls for the saver which actually decides what to write
def keypress_handler(char, picture1, picture2, time_beginning, csv_file,
                     sentence):
    answer = char
    if answer == "f" or answer == "j":
        save_input(answer, picture1, picture2, time_beginning, csv_file,
                   sentence)


# Middlepiece to determine what to write to csv and calls for the csv
# writer
def save_input(answer, picture1, picture2, time_beginning, csv_file,
               sentence):
    if answer == "f":
        print("answer was f, which is 1")
        selection = picture1

    if answer == "j":
        print("answer waas j, which is 2")
        selection = picture2

    selection_writer(sentence, answer, picture1, picture2, time_beginning, csv_file,
                     selection)


# Writing to csv happens here.
def selection_writer(sentence, answer, picture1, picture2, time_beginning, csv_file,
                     selection):

    time_now = time.time()
    attributes_list = [sentence, picture1, picture2, time_beginning, time_now,
                       time_now - time_beginning, answer, selection]
    writables = []
    for item in attributes_list:
        item = str(item)
        writables.append(item)

    writables = ",".join(writables)

    with open(csv_file, "a", newline="") as output:
        writer = csv.writer(output)
        writer.writerow([writables])



# Function for creating a list of image pairs from folder /pictures/
# Returns a list consisting of lists. Each sub list is a pair of two images.

def image_list_getter():
    display_images_list = os.listdir("pictures/")
    display_image_pairs = []

    for item in display_images_list:
        for item2 in display_images_list:
            if item2 != item:
                pair = (item, item2)
                pair_reverse = (item2, item)
                if pair not in display_image_pairs and pair_reverse not in display_image_pairs:
                    display_image_pairs.append(pair)
                    display_image_pairs.append(pair_reverse)

    return display_image_pairs


# Creates nice timestamp that is used in the csv filename
# Is called from csv creator (create_csv)
def timestampcreator():
    time_now = time.localtime()
    year = time_now.tm_year
    month = time_now.tm_mon
    day = time_now.tm_mday
    hour = time_now.tm_hour
    minute = time_now.tm_min
    second = time_now.tm_sec

    stamplist = (year, month, day, hour, minute, second)
    stamplist_strings = []

    for item in stamplist:
        item = str(item)
        if len(item) <= 1:
            item = "0" + item
        stamplist_strings.append(item)
    timestamp = ("".join(stamplist_strings))

    return timestamp


# Csv document creator that returns the filename to be used
# Calls for timestampcreator
def create_csv():

    flag = True
    while flag == True:

        print("What do you want to name the CSV file?")
        file_input = input("Insert name: ")

        if len(file_input) > 0:
            timestamp = timestampcreator()

            if file_input[-4:] != ".csv":
                realfilename = (timestamp + "-" +
                                file_input + ".csv")
                flag = False
            else:
                realfilename = (timestamp + "-" +
                                file_input)
                flag = False

            print("csv file created: ", realfilename)

        else:
            print()
            print("Incorrect name. Name cannot be empty.")
            flag = True

    return realfilename


# Middlepiece ot create loop for displaying each image pair
# Each pair calls for sentence displayer and then main window for displaying
# the pair
def picture_viewer(csv_file, display_list):
    for item in display_list:
        sentence_display(item[0])
        time_beginning = time.time()
        window("pictures/" + item[1], "pictures/" + item[2], time_beginning,
               csv_file, item[0])


# This function loads the sentences to be used as primes form the
# sentences.txt
def sentences_loader():
    sentences_file = open("sentences.txt", "r")
    sentences = sentences_file.readlines()
    sentences_stripped = []
    for item in sentences:
        sentences_stripped.append(item.strip())
    return sentences_stripped


# Main function in which all the other functions are called
def main():
    print("loading image list")
    image_list = image_list_getter()
    print("image list loaded succesfully")
    print("loading sentences")
    sentences = sentences_loader()
    print("sentences loaded succesfully")
    display_list = []
    print("creating list of pairs to display")

    # Create a list of all the pairs to be displayed as following:
    # [sentence, image1, image2]
    for sentence in sentences:
        for image in image_list:
            set = (sentence, image[0], image[1])
            display_list.append(set)

    print("\nlist of pairs to display created succesfully\n")

    for item in display_list:
        print(item)
    print("\nlength of display list / items to display: ", len(display_list),"\n")


    csv_file = create_csv()
    random.shuffle(display_list)

    launcher_window()
    picture_viewer(csv_file, display_list)
    exit_window()

main()
