from cProfile import label
import imp
from msilib.schema import Icon
from tkinter import ttk
from json import load
from operator import index
from tkinter import *
from turtle import circle, dot, left
from PIL import Image, ImageTk
from pygame import mixer
import os

color1 = "#ffffff"  # white
# color2 = "#357EC7"  # blue
color2 = "#FF8C00"  # orange

color3 = "#000000"  # black
color4 = "#FF0808"  # red

window = Tk()
window.title("Music Player")
# window.geometry('550x350')
window.geometry('800x500')
window.config(background=color2)
window.resizable(width=FALSE, height=FALSE)


# playing the music


def play_music():
    running = listbox.get(ACTIVE)
    current_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

# pause of music


def pause_music():
    mixer.music.pause()

# resume the music


def resume_music():
    mixer.music.unpause()

# stopping the music


def stop_music():
    mixer.music.stop()


def mute():
    mixer.music.fadeout

# next music


def next_music():
    playing = current_song['text']
    index = songs.index(playing)
    new_index = index+1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0, END)
    show()

    listbox.select_set(new_index)
    current_song['text'] = playing


# previous music


def previous_music():
    playing = current_song['text']
    index = songs.index(playing)
    new_index = index-1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(new_index)
    current_song['text'] = playing


def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)

# !!!!!


# frames

# left_frame = Frame(window, width=208, height=278, background=color3)
# left_frame.grid(row=0, column=0, padx=0, pady=3)

bottom_frame = Frame(window, width=800, height=500, background=color2)
bottom_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=0)

right_frame = Frame(window, width=400, height=200, background=color3)
right_frame.grid(row=0, column=1, padx=0, pady=0)


# Image


songcover = Image.open('icons/bg1.png')
songcover = songcover.resize((802, 502))
songcover = ImageTk.PhotoImage(songcover)
songcoverimg = Label(bottom_frame, height=500, image=songcover,
                     padx=0, pady=0, bg=color3,  relief=SOLID)
songcoverimg.grid(row=0, column=0)


# elif index == 1:
#     songcover = Image.open('icons/1.png')
#     songcover = songcover.resize((204, 204))
#     songcover = ImageTk.PhotoImage(songcover)
#     songcoverimg = Label(left_frame, height=204, image=songcover,
#                          padx=1, pady=1, bg=color3,  relief=SOLID)
#     songcoverimg.grid(row=0, column=0)
# elif index == 1:
#     songcover = Image.open('icons/de1.png')
#     songcover = songcover.resize((204, 204))
#     songcover = ImageTk.PhotoImage(songcover)
#     songcoverimg = Label(left_frame, height=204, image=songcover,
#                          padx=1, pady=1, bg=color3,  relief=SOLID)
#     songcoverimg.grid(row=0, column=0)


# listbox
listbox = Listbox(right_frame, selectmode=SINGLE, font=(
    "Arial 13 bold"), width=46, height=9, bg=color3, fg=color2, selectbackground=color2, selectforeground=color3)
listbox.grid(row=0, column=0, padx=0)

# scroll bar
scroll = Scrollbar(right_frame, bg=color1)
scroll.grid(row=0, column=1)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)


# Volume

scale = Scale(bottom_frame, from_=0, to=100,
              relief=SOLID, bg=color3, fg=color1, orient=HORIZONTAL, command=set_vol, sliderlength=30, troughcolor=color4, highlightbackground=color4)
scale.set(30)
scale.place(x=673, y=416)

# Labels

volume_label = Label(bottom_frame, text="VOLUME", font=(
    "David 12 bold"), width=10, height=1, padx=0, bg=color4, fg=color3)
volume_label.place(x=674, y=393)

credits_label = Label(bottom_frame, text="BY:\nIU2041220019\nIU2041220009\nIU2041220001", font=(
    "David 10 bold"), width=12, height=4, padx=0, bg=color4, fg=color3)
credits_label.place(x=28, y=388)


# Select song label

current_song = Label(bottom_frame, text="SELECT THE SONG", font=(
    "Ivy 12 bold"), width=78, height=1, padx=10, bg=color4, fg=color3)
current_song.place(x=0, y=475)


# All Buttons

back = Image.open('icons/4.png')
back = back.resize((60, 60))
back = ImageTk.PhotoImage(back)
backimg = Button(bottom_frame, height=60, image=back,
                 padx=10, bg=color3, command=previous_music)
backimg.place(x=152, y=392)

play = Image.open('icons/1.png')
play = play.resize((60, 60))
play = ImageTk.PhotoImage(play)
playimg = Button(bottom_frame, height=60, image=play,
                 padx=10, bg=color3, command=play_music)
playimg.place(x=240, y=392)

paused = Image.open('icons/2.png')
paused = paused.resize((60, 60))
paused = ImageTk.PhotoImage(paused)
pausedimg = Button(bottom_frame, height=60, image=paused,
                   padx=10, bg=color3, command=pause_music)
pausedimg.place(x=327, y=392)

resume = Image.open('icons/5.png')
resume = resume.resize((60, 60))
resume = ImageTk.PhotoImage(resume)
resumeimg = Button(bottom_frame, height=60, image=resume,
                   padx=10, bg=color3, command=resume_music)
resumeimg.place(x=414, y=392)

stop = Image.open('icons/6.png')
stop = stop.resize((60, 60))
stop = ImageTk.PhotoImage(stop)
stopimg = Button(bottom_frame, height=60, image=stop,
                 padx=10, bg=color3, command=stop_music)
stopimg.place(x=501, y=392)

next = Image.open('icons/3.png')
next = next.resize((60, 60))
next = ImageTk.PhotoImage(next)
nextimg = Button(bottom_frame, height=60, image=next,
                 padx=10, bg=color3, command=next_music)
nextimg.place(x=587, y=392)


# load the songs


os.chdir(r'C:\Users\RYZEN\Downloads\Songs')
songs = os.listdir()


def show():

    for i in songs:
        listbox.insert(END, i)


show()


mixer.init()
music_state = StringVar()
music_state.set("Choose Song!")


window.mainloop()
