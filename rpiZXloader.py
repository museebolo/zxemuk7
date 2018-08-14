#!/usr/bin/env python3

from tkinter import *
import simpleaudio as sa


app_name = "rpiZXloader"

games_library = (
    (
        "Eric and the floaters",
        "/home/romain/Documents/zxSpectrum/games/eric_and_the_floaters/eric.wav"
    ),
    (
        "Boulder Dash",
        "/home/romain/Documents/zxSpectrum/games/boulder_dash/boulder_dash.wav"
    )
)

class MainWin(Frame):
    """
    """
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master.title(app_name)
        #self.master.attributes("-fullscreen", True)

        for x in range(0, len(games_library)):
            but = Button(master,
                         text = games_library[x][0],
                         width = 30,
                         command = lambda:self.playWave(games_library[x][1]))
            but.pack()

        but_help = Button(text = "HELP",
                          command = lambda:self.helpWin(master))
        but_help.pack()

    def playGame(self, wav):
        playWave(wav)

    def playWave(self, wav):
        wave_obj = sa.WaveObject.from_wave_file(wav)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def helpWin(self, master):
        pup = Toplevel(master)
        display = Label(pup, text = "LOAD \"\"")
        display.pack()
        button_quit = Button(pup, text = "Quit", command = pup.destroy)
        button_quit.pack()


if __name__ == '__main__':
    root = Tk()
    win = MainWin(root)
    win.mainloop()


# vim: ft=python ts=8 et sw=4 sts=4
