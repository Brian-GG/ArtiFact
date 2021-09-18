"""ArtiFact

Project Description
===================

ArtiFact is an AI-based application that detects misleading article titles.


Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Brian Cho, Greg Wang, Steven Zhang, and Brian Grigore

"""

import tkinter


def run_app() -> None:
    """
    a function that runs the application ArtiFact
    """
    window = tkinter.Tk()

    canvas = tkinter.Canvas(window, width=301, height=76)
    canvas.pack()
    logo = tkinter.PhotoImage(file="")

    window.title("ArtiFact")
    window.geometry("700x700")

    # if light mode chosen
    window.config(bg="#f4fcff")

    window.mainloop()


if __name__ == "__main__":
    run_app()
