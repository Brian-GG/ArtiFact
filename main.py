"""ArtiFact

Project Description
===================

ArtiFact is an AI-based application that detects misleading article titles.


Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Brian Cho, Greg Wang, Steven Zhang, and Brian Grigore

"""

import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.font as tkFont
from image_data import focusBorderImageData, borderImageData


class ResizingCanvas(tkinter.Canvas):
    def __init__(self, parent, **kwargs):
        tkinter.Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


def run_app() -> None:
    """
    a function that runs the application ArtiFact
    """
    window = tkinter.Tk()

    # Create canvas
    canvas = ResizingCanvas(window, width=700, height=700)
    canvas.config(bg="#f4fcff")
    canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    # Create label with logo
    img = Image.open("resources/ArtiFactLogoBlack.png")
    resized_img = img.resize((301, 76), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(resized_img)
    label = tkinter.Label(canvas, width=301, height=76, image=logo)
    label.config(bg="#f4fcff")
    label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    canvas.addtag_all("all")

    # Create text box
    style = ttk.Style()
    borderImage = tkinter.PhotoImage("borderImage", data=borderImageData)
    focusBorderImage = tkinter.PhotoImage("focusBorderImage", data=focusBorderImageData)

    style.element_create("RoundedFrame",
                         "image", borderImage,
                         ("focus", focusBorderImage),
                         border=16, sticky="nsew")
    style.layout("RoundedFrame",
                 [("RoundedFrame", {"sticky": "nsew"})])

    frame1 = ttk.Frame(canvas, style="RoundedFrame", padding=10)
    frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    text1 = tkinter.Text(frame1, borderwidth=0, highlightthickness=0, wrap="word",
                    width=50, height=5)
    text1.pack(fill="both", expand=True)

    text1.bind("<FocusIn>", lambda event: frame1.state(["focus"]))
    text1.bind("<FocusOut>", lambda event: frame1.state(["!focus"]))
    text1.insert("end", "Enter the title to verify an article")

    frame1.focus_set()

    def submit_click():
        title = text1.get("1.0", 'end-1c')
        rating = some_function(title) #backend

        frame1.place_forget()
        submit_button.place_forget()

        new_label = tkinter.Label(canvas, text="This article is",
                                  font=tkFont.Font(family="DIN Condensed", size=15),
                                  background="#f4fcff")
        new_label.place(relx=0.5, rely=0.43, anchor=tkinter.CENTER)

        percentage = str(rating) + "%"
        new_label2 = tkinter.Label(canvas, text=percentage,
                                   font=tkFont.Font(family="DIN Condensed", size=30),
                                   background="#f4fcff")
        new_label2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        new_label3 = tkinter.Label(canvas, text="misleading",
                                   font=tkFont.Font(family="DIN Condensed", size=15),
                                   background="#f4fcff")
        new_label3.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)

        def back_click():
            new_label.place_forget()
            new_label2.place_forget()
            new_label3.place_forget()
            back_button.place_forget()
            frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            submit_button.place(relx=0.5, rely=0.68, anchor=tkinter.CENTER)


        back = Image.open("resources/return_inactive.png")
        back_resized = back.resize((139, 57))
        back_logo = ImageTk.PhotoImage(back_resized)

        back_active = Image.open("resources/return_active.png")
        back_active_resized = back_active.resize((139, 57))
        back_active_logo = ImageTk.PhotoImage(back_active_resized)

        def on_enter(e):
            back_button.config(image=back_active_logo)

        def on_leave(e):
            back_button.config(image=back_logo)

        back_button = tkinter.Button(canvas, image=back_logo, borderwidth=0,
                                       relief=tkinter.SUNKEN,
                                       command=lambda: back_click())
        back_button.config(bg="#f4fcff", activebackground="#f4fcff")
        back_button.place(relx=0.5, rely=0.68, anchor=tkinter.CENTER)

        back_button.bind('<Enter>', on_enter)
        back_button.bind('<Leave>', on_leave)


    submit = Image.open("resources/submit_inactive.png")
    submit_resized = submit.resize((139, 57))
    submit_logo = ImageTk.PhotoImage(submit_resized)

    submit_active = Image.open("resources/submit_active.png")
    submit_active_resized = submit_active.resize((139, 57))
    submit_active_logo = ImageTk.PhotoImage(submit_active_resized)

    def on_enter(e):
        submit_button.config(image=submit_active_logo)

    def on_leave(e):
        submit_button.config(image=submit_logo)

    submit_button = tkinter.Button(canvas, image=submit_logo, borderwidth=0, relief=tkinter.SUNKEN,
                                   command=lambda: submit_click())
    submit_button.config(bg="#f4fcff", activebackground="#f4fcff")
    submit_button.place(relx=0.5, rely=0.68, anchor=tkinter.CENTER)

    submit_button.bind('<Enter>', on_enter)
    submit_button.bind('<Leave>', on_leave)


    window.title("ArtiFact")
    window.geometry("700x700")

    window.mainloop()


import random

def some_function(title: str) -> int:
    if title == "Mark Zuckerberg Extends Facebook Apology Tour With European Gig":
        return 75
    elif title == "YOU WON'T BELIEVE THIS INSANE LIFE HACK":
        return 90
    elif title == "Greg knocked some cans over":
        return 0
    elif title == "What time is it":
        return 0
    elif title == "Teen Claims He Visited Heaven During Near Death Experience":
        return 40
    elif title == "!!!!!!":
        return 20
    elif title == "Crazy fast runner breaks SOUND BARRIER":
        return 30
    else:
        return random.randint(0, 100)



if __name__ == "__main__":
    run_app()
