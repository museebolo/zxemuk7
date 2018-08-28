#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
import simpleaudio as sa


app_name = "rpiZXloader"
logo_title_path = "/home/romain/Documents/rpiZXloader/logo/header.png"
logo_bg_path = "/home/romain/Documents/rpiZXloader/logo/logo-rainbow.png"
logo_bolo_path = "/home/romain/Documents/rpiZXloader/logo/logo-bolo.png"
information_path = "/home/romain/Documents/rpiZXloader/logo/information.png"

games_library = (
    (
        "SHORT",
        "/home/romain/Documents/zxSpectrum/short.wav"
    ),
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

ZX_RED    = "#fe0000"
ZX_YELLOW = "#ffff01"
ZX_GREEN  = "#00ff01"
ZX_BLUE   = "#01ffff"


class MainWin(Frame):
    """
    """
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.screen_width  = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.but_game = [0]*len(games_library)

        self.master.title(app_name)
        self.master.config(background = window_background)
        self.master.attributes("-fullscreen", True)

        #  LOGO
        ## TITLE
        logo_title_img = Image.open(logo_title_path)
        logo_title = ImageTk.PhotoImage(logo_title_img)
        title = Label(image = logo_title, bg = window_background)
        title.image = logo_title
        title.place(x = (self.screen_width-logo_title_img.size[0])/2,
                    y = 0)
        ## BACKGROUND
        logo_bg_img = Image.open(logo_bg_path)
        logo_bg = ImageTk.PhotoImage(logo_bg_img)
        bg = Label(image = logo_bg, bg = window_background)
        bg.image = logo_bg
        bg.place(x = self.screen_width - logo_bg_img.size[0],
                 y = self.screen_height - logo_bg_img.size[1])
        ## LOGO BOLO
        logo_bolo_img = Image.open(logo_bolo_path)
        logo_bolo = ImageTk.PhotoImage(logo_bolo_img)
        bolo = Label(image = logo_bolo, bg = window_background)
        bolo.image = logo_bolo
        bolo.place(x = 10,
                   y = self.screen_height - logo_bolo_img.size[1] - 10)

        #  MAIN ZONE
        main_zone = Frame(master,
                          bg = window_background,
                          height = logo_bg_img.size[1],
                          width = self.screen_width/2 - logo_title_img.size[0]/2)
        ## BUTTONS TO PLAY THE GAMES
        f_but_games = LabelFrame(main_zone,
                                 bg = window_background, fg = ZX_YELLOW,
                                 padx = 10, pady = 10,
                                 text = "JEUX")
        self.displayButtonsGames(f_but_games)
        f_but_games.pack()
        ## CONTROL BUTTONS
        control_zone = Frame(main_zone, bg = window_background,
                             padx = 10, pady = 10)
        but_info = Button(control_zone,
                          activebackground = ZX_GREEN,
                          bg = window_background,
                          fg = ZX_BLUE,
                          highlightbackground = ZX_GREEN,
                          relief = "flat",
                          text = "INFORMATION",
                          command = lambda:self.infoWin(master))
        but_info.pack(padx = 3, side = LEFT)
        but_help = Button(control_zone,
                          activebackground = ZX_GREEN,
                          bg = window_background,
                          fg = ZX_BLUE,
                          highlightbackground = ZX_GREEN,
                          relief = "flat",
                          text = "HELP",
                          command = lambda:self.helpWin(master))
        but_help.pack(padx = 3, side = LEFT)
        but_quit = Button(control_zone,
                          activebackground = ZX_GREEN,
                          bg = window_background,
                          fg = ZX_BLUE,
                          highlightbackground = ZX_GREEN,
                          relief = "flat",
                          text = "QUITTER",
                         command = self.master.destroy)
        but_quit.pack(padx = 3, side = RIGHT)
        control_zone.pack(pady = 15, side = BOTTOM)
        main_zone.place(x = self.screen_width/2 - main_zone.winfo_reqwidth()/2,
                        y = logo_title_img.size[1]
                            + self.screen_height/2
                            - main_zone.winfo_reqheight()/2)

    def displayButtonsGames(self, master):
        for x in range(len(games_library)):
            self.but_game[x] = Button(master,
                                      activebackground = ZX_YELLOW,
                                      bg = window_background,
                                      fg = ZX_RED,
                                      highlightbackground = ZX_YELLOW,
                                      relief = "flat",
                                      text = games_library[x][0],
                                      command = lambda val=x:self.playGame(val))
            self.but_game[x].pack(fill = X, side = TOP,
                                  pady = 3)

    def disableButtonsGames(self, exception):
        for x in range(len(games_library)):
            if x == exception:
                self.but_game[x].config(bg = ZX_YELLOW,
                                        fg = "black",
                                        state = "active",
                                        command = lambda:self.stopWave())
            else:
                self.but_game[x].config(bg = ZX_RED,
                                        fg = "black",
                                        highlightbackground = ZX_YELLOW,
                                        state = "disabled")

    def enableAllButtonsGames(self):
        for x in range(len(games_library)):
            self.but_game[x].config(state = "normal",
                                    bg = window_background,
                                    fg = ZX_RED,
                                    highlightbackground = ZX_YELLOW,
                                    command = lambda val=x:self.playGame(val))

    def playGame(self, game_nb):
        self.disableButtonsGames(game_nb)
        self.playWave(game_nb)

    def playWaveLoop(self):
        if not self.play_obj.is_playing():
            self.stopWave()
        self.after(1000, self.playWaveLoop)

    def playWave(self, game_nb):
        self.wave_obj = sa.WaveObject.from_wave_file(games_library[game_nb][1])
        self.play_obj = self.wave_obj.play()
        self.playWaveLoop()

    def stopWave(self):
        self.play_obj.stop()
        self.enableAllButtonsGames()

    def helpWin(self, master):
        pup = Toplevel(master)
        display = Label(pup, text = "LOAD \"\"")
        display.pack()
        button_quit = Button(pup, text = "Quit", command = pup.destroy)
        button_quit.pack()

    def infoWin(self, master):
        self.pup_info = Toplevel(master, bg = window_background)
        #self.pup_info.geometry("%dx%d+%d+%d" % (info_img.size[0]+20,
        #                              info_img.size[1]+20,
        #                              (self.screen_width/2)-(info_img.size[0]/2)-10,
        #                              0))
        self.pup_info.attributes("-fullscreen", True)
        info_img = Image.open(information_path)
        info = ImageTk.PhotoImage(info_img)
        info_l = Label(self.pup_info, image = info, bg = window_background)
        info_l.image = info
        info_l.pack(side = TOP)
        but_quit = Button(self.pup_info,
                          activebackground = ZX_GREEN,
                          bg = window_background,
                          fg = ZX_BLUE,
                          highlightbackground = ZX_GREEN,
                          relief = "flat",
                          text = "QUITTER",
                         command = self.unlock)
        but_quit.pack(pady = 5, side = BOTTOM)

    def unlock(self):
        self.passwdWin()
        self.pup.destroy()

    def passwdWin(self, master):
        self.pup_passwd = Toplevel(master, bg = window_background)
        self.passwd = StringVar()
        self.e_passwd = Entry(master, textvariable = self.passwd)
        but_ok = Button(master, text = "OK", command = )

    def checkPasswd(self)
        if self.asswd.get() == "1234":
            break


if __name__ == '__main__':
    root = Tk()
    win = MainWin(root)
    win.mainloop()


# vim: ft=python ts=8 et sw=4 sts=4
