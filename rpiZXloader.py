#!/usr/bin/env python3

from tkinter import *
import simpleaudio as sa


app_name = "rpiZXloader"

games_library = (
    (
        "Boulder Dash",
        "/home/romain/Documents/zxSpectrum/games/boulder_dash/boulder_dash.wav"
    ),
    (
        "Crystal Quest",
        "/home/romain/Documents/zxSpectrum/games/crystal_quest/crystal_quest.wav"
    ),
    (
        "Double Dragon",
        "/home/romain/Documents/zxSpectrum/games/double_dragon/double_dragon.wav"
    ),
    (
        "Elite",
        "/home/romain/Documents/zxSpectrum/games/elite/elite.wav"
    ),
    (
        "Eric and the floaters",
        "/home/romain/Documents/zxSpectrum/games/eric_and_the_floaters/eric.wav"
    ),
    (
        "Sentinel",
        "/home/romain/Documents/zxSpectrum/games/sentinel/sentinel.wav"
    ),
    (
        "Sim City",
        "/home/romain/Documents/zxSpectrum/games/sim_city/sim_city.wav"
    ),
    (
        "Spy Hunter",
        "/home/romain/Documents/zxSpectrum/games/spy_hunter/spy_hunter.wav"
    ),
    (
        "Tempest",
        "/home/romain/Documents/zxSpectrum/games/tempest/tempest.wav"
    )
)

class MainWin(Frame):
    """
    """
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master.title(app_name)
        #self.master.attribute)("-fullscreen", True)

        for x in range(0, len(games_library)):
            but = Button(master,
                         text = games_library[x][0],
                         width = 30,
                         command = lambda:self.playWave(games_library[x][1]))
            but.pack()

    def playGame(self, wav):
        playWave(wav)

    def playWave(self, wav):
        wave_obj = sa.WaveObject.from_wave_file(wav)
        play_obj = wave_obj.play()
        play_obj.wait_done()


if __name__ == '__main__':
    root = Tk()
    win = MainWin(root)
    win.mainloop()


# vim: ft=python ts=8 et sw=4 sts=4
