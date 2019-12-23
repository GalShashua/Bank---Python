# Name: Melany Cygiel Gdud      ID: 324442243
# Name: Gal Shashua             ID: 315878397

from tkinter import *
from threading import Timer
import time
import matplotlib.pyplot as plt


'''
#################################################################################
#                              Logic class                                    #
#################################################################################
'''


class Logic(object):
    def __init__(self):
        self.file_name = 'words.txt'
        self.form = 'r'

    def generator(self, letter, flag):
        the_letter = letter.lower()
        if not the_letter.isalpha():
            print("Please enter only letters!")
            return
        with open(self.file_name, self.form) as f:
            for line in f:
                for word in line.split(","):
                    if the_letter in word and flag:
                        yield word
                    if the_letter not in word and not flag:
                        yield word

    def count_letters(self):
        dic_freq = {}
        with open(self.file_name, self.form) as f:
            for char in f.read():
                if char.isalpha():
                    lower = char.lower()
                    for i in lower:
                        for j in i:
                            if j in dic_freq:
                                dic_freq[j] += 1
                            else:
                                dic_freq[j] = 1
        dic_list = list(dic_freq.items())
        sort_d = sorted(dic_list)
        return sort_d[:10]


'''
#################################################################################
#                              Gui class                                    #
#################################################################################
'''


class Gui(object):
    def __init__(self, logic):
        self.logic = logic
        self.root = Tk()
        self.root.title("Words Gui")
        self.root.geometry('350x200')
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None
        self.startButton = None
        self.restartButton = None
        self.graphButton = None
        self.includeCheckButton = None
        self.letterEntry = None
        self.init_frames()
        self.init_bottoms()
        self.init_check()
        self.init_entry()
        self.t = None
        self.root.mainloop()

    def init_bottoms(self):
        self.startButton = Button(self.frame3, text="Start", fg="green", padx=10, pady=10, command=self.start)
        self.startButton.pack(side=LEFT, padx=10, pady=10)
        self.restartButton = Button(self.frame3, text="Restart", fg="blue", padx=10, pady=10, command=self.restart)
        self.restartButton.pack(side=LEFT, padx=10, pady=10)
        self.graphButton = Button(self.frame3, text="Graph", fg="orange", padx=10, pady=10, command=self.graph)
        self.graphButton.pack(side=LEFT, padx=10, pady=10)

    def init_frames(self):
        self.frame1 = Frame(self.root, bd=20)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.root)
        self.frame2.pack(side=TOP)
        self.frame3 = Frame(self.root)
        self.frame3.pack(side=BOTTOM)

    def init_check(self):
        Label(self.frame2, text="Choose the Square if you want to include the letter: ").grid(row=0)
        self.includeCheckButton = IntVar()
        Checkbutton(self.frame2, text="Include", variable=self.includeCheckButton).grid(row=1, column=0, sticky=W)

    def init_entry(self):
        Label(self.frame1, text="Please Enter a letter: ").grid(row=0)
        self.letterEntry = Entry(self.frame1)
        self.letterEntry.grid(row=0, column=1)

    def start(self):
        self.t = Timer(0, self.call_generator)
        self.t.start()

    def call_generator(self):
        get_letter = self.letterEntry.get()
        flag = self.includeCheckButton.get()
        gen = self.logic.generator(get_letter, flag)
        for i in gen:
            time.sleep(1)
            print(i)

    def graph(self):
        count = self.logic.count_letters()
        plt.bar(range(len(count)), [val[1] for val in count], align='center', color="red")
        plt.xticks(range(len(count)), [val[0] for val in count])
        plt.ylabel('Frequency\n')
        plt.xlabel('Letters')
        plt.title('Frequency Graph\n', color='black')
        plt.show()

    def restart(self):
        self.includeCheckButton.set(0)
        self.letterEntry.delete(0, 'end')


if __name__ == "__main__":
    my_logic = Logic()
    Gui(my_logic)
