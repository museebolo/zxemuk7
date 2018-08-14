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

start_games_pages = 1
current_page = 1
nb_games_per_page = 5

class MainWin(Frame):
    """
    """
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master.title(app_name)
        self.master.geometry("150x200")
        #self.master.attribute)("-fullscreen", True)

        self.f_but_games = Frame(master)
        self.displayFrameButtonsGames(current_page)

        f_but_sel_page = Frame(master)
        but_next_page = Button(f_but_sel_page,
                               text = "->",
                               command = lambda:self.displayFrameButtonsGames(
                                                            current_page+1)
                              )
        but_next_page.pack(side = RIGHT)
        but_prev_page = Button(f_but_sel_page,
                               text = "<-",
                               command = lambda:self.displayFrameButtonsGames(
                                                            current_page-1)
                               )
        but_prev_page.pack(side = LEFT)

        but_help = Button(f_but_sel_page,
                          text = "HELP",
                          command = lambda:self.helpWin(master))
        but_help.pack()

        f_but_sel_page.pack(side = BOTTOM)

    def displayFrameButtonsGames(self, page):
        if page > int(len(games_library)/nb_games_per_page+1):
            page = int(len(games_library)/nb_games_per_page+1)
        if page < 1:
            page = 1
        if self.f_but_games.winfo_ismapped():
            self.f_but_games.destroy()
            self.f_but_games = Frame(self.master)
        self.displayButtonsGames(self.f_but_games,
                                 (page-1)*nb_games_per_page,
                                 (page*nb_games_per_page))
        self.f_but_games.pack()

    def displayButtonsGames(self, master, first_game, last_game):
        if last_game > len(games_library):
            last_game = len(games_library)
        for x in range(first_game, last_game):
            but = Button(master,
                         text = games_library[x][0],
                         #width = 30,
                         command = lambda:self.playWave(games_library[x][1]))
            but.pack()

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
