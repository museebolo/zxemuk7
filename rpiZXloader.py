#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
import simpleaudio as sa


app_name = "rpiZXloader"
logo_title_path = "/home/romain/Documents/rpiZXloader/logo/header.png"
logo_bg_path = "/home/romain/Documents/rpiZXloader/logo/logo-rainbow.png"

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
nb_games_per_page = 4

window_background =  "black"


class MainWin(Frame):
    """
    """
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title(app_name)
        screen_width  = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (screen_width, screen_height))
        self.master.config(background = window_background)
        self.master.attributes("-fullscreen", True)

        self.master.bind("<Escape>", self.prog_quit)

        #  LOGO
        ## TITLE
        logo_title_img = Image.open(logo_title_path)
        logo_title = ImageTk.PhotoImage(logo_title_img)
        title = Label(image = logo_title, bg = window_background)
        title.image = logo_title
        #title.pack(side = TOP)
        #title.grid(row = 0, column = 1, sticky = N)
        title.place(x = (screen_width-logo_title_img.size[0])/2,
                    y = 0)
        ## BACKGROUND
        logo_bg_img = Image.open(logo_bg_path)
        logo_bg = ImageTk.PhotoImage(logo_bg_img)
        bg = Label(image = logo_bg, bg = window_background)
        bg.image = logo_bg
        #bg.pack(side = RIGHT)
        #bg.grid(row = 1, column = 2, sticky = SE)
        bg.place(x = screen_width - logo_bg_img.size[0],
                 y = screen_height - logo_bg_img.size[1])

        # MAIN ZONE
        main_zone = Frame(master, bg = window_background)
        buttons_zone = Frame(main_zone, bg = window_background)
        self.f_but_games = Frame(buttons_zone, background = window_background)
        self.displayFrameButtonsGames(current_page)

        f_but_sel_page = Frame(buttons_zone)
        but_next_page = Button(f_but_sel_page,
                               bg = window_background,
                               fg = "white",
                               text = "\u21FE",
                               command = lambda:self.displayFrameButtonsGames(
                                                            current_page+1)
                              )
        but_next_page.pack(side = RIGHT)
        but_prev_page = Button(f_but_sel_page,
                               background = window_background,
                               fg = "white",
                               text = "\u21FD",
                               command = lambda:self.displayFrameButtonsGames(
                                                            current_page-1)
                               )
        but_prev_page.pack(side = LEFT)

        but_help = Button(f_but_sel_page,
                          background = window_background,
                          fg = "white",
                          text = "HELP",
                          command = lambda:self.helpWin(master))
        but_help.pack()

        f_but_sel_page.pack(side = BOTTOM)
        buttons_zone.pack()
        #main_zone.pack()
        #main_zone.grid(row = 1, column = 1)
        main_zone.place(x = 0,
                        y = logo_title_img.size[1])

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
                         activebackground = "gray",
                         bg = window_background,
                         fg = "white",
                         relief = "sunken",
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

    def prog_quit(self):
        self.master.quit()


if __name__ == '__main__':
    root = Tk()
    win = MainWin(root)
    win.mainloop()


# vim: ft=python ts=8 et sw=4 sts=4
