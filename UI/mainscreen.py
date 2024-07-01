
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1024x600")
window.configure(bg = "#000000")
window.attributes("-fullscreen", True)
common_canvas = Canvas(window, bg = "#000000", height = 600, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")
common_canvas.create_rectangle(0.0, 0.0, 1024.0, 59.0, fill = "#B27A27", outline = "")
common_canvas.create_rectangle(965.0, 0.0, 1024.0, 600.0, fill = "#B27A27", outline = "")
common_canvas.create_text(66.0, -12.0, anchor = "nw", text = "BatteryBeam", fill = "#FFFFFF", font = ("Homenaje Regular", 40))
common_canvas.create_text(525.0, 10.0, anchor = "nw", text = "Battery Profiler & Emulator", fill = "#FFFFFF", font = ("Gruppo", 30))
image_image_1 = PhotoImage(file = relative_to_assets("logo.png"))
image_1 = common_canvas.create_image(36.0, 29.0, image = image_image_1)
common_canvas.place(x = 0, y = 0)

def get_reading():
    # This function should return the new reading value

    a = 1.3
    c = 3.7
    b = 0.1  # Adjust this value to change the rate of decay
    return a * np.exp(-b * len(samples)) + c

def back():
    global backpressed
    Canvas
    backpressed = True

def constant_voltage():
    global backpressed, samples, readings, backbutton, canvas, label_3, label_4
    backpressed = False
    samples = []
    readings = []
    
    button_1.destroy()
    button_2.destroy()
    button_3.destroy()
    label_1.destroy()

    backbutton_image = PhotoImage(file=relative_to_assets("back.png")) # Change this to back button image
    backbutton = Button(
        image=backbutton_image,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    backbutton.image = backbutton_image
    backbutton.place(x=22, y=520, width=200*0.9, height=80*0.9)

    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.set_xlabel("Time")
    plot.set_ylabel("Voltage")
    plot.set_title("Voltage vs Time")
    plot.grid()
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().place(x=50, y=50, width=750, height=400)
    label_3 = Label(main_frame, text="Current level", bg="#000000", fg="#ffffff", font=("Gruppo", 18))
    label_3.place(x=810, y=40)
    label_4 = Label(main_frame, text="15A", bg="#000000", fg="#ffffff", font=("Gruppo", 25))
    label_4.place(x=810, y=90)
    def update_plot():
        if backpressed:
            reset_main_screen()
            return
        plot.clear()
        samples.append(len(readings))
        readings.append(get_reading())
        plot.plot(samples, readings)
        plot.set_xlabel("Time")
        plot.set_ylabel("Voltage")
        plot.set_title("Voltage vs Time")
        plot.set_xlim(0, ((len(samples) // 100) + 1) * 100)
        plot.set_ylim(0, 7)   # Adjust as necessary based on expected reading values
        plot.grid()
        canvas.draw()
        window.after(1000, update_plot)

    update_plot()

def reset_main_screen():
    backbutton.destroy()
    label_3.destroy()
    label_4.destroy()
    global label_1, button_1, button_2, button_3, canvas
    canvas.get_tk_widget().destroy()
    label_1 = Label(main_frame, text="Select Mode", bg="#000000", fg="#ffffff", font=("Gruppo", 45))
    label_1.place(x=320, y=10)
    
    button_image_1 = PhotoImage(file=relative_to_assets("constantvoltage.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
    button_1.image = button_image_1
    button_1.place(x=76.0, y=200.0, width=250, height=110)

    button_image_2 = PhotoImage(file=relative_to_assets("constantcurrent.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
    button_2.image = button_image_2
    button_2.place(x=644.0, y=200.0, width=250, height=110)

    button_image_3 = PhotoImage(file=relative_to_assets("constantpower.png"))
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
    button_3.image = button_image_3
    button_3.place(x=360.0, y=385.0, width=250, height=110)

main_frame = Frame(window, bg="#000000", height=541, width=965, bd=0, highlightthickness=0, relief="ridge")
label_1 = Label(main_frame, text="Select Mode", bg="#000000", fg="#ffffff", font=("Gruppo", 45))
label_1.place(x=320, y=10)

button_image_1 = PhotoImage(file=relative_to_assets("constantvoltage.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
button_1.image = button_image_1
button_1.place(x=76.0, y=200.0, width=250, height=110)

button_image_2 = PhotoImage(file=relative_to_assets("constantcurrent.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
button_2.image = button_image_2
button_2.place(x=644.0, y=200.0, width=250, height=110)

button_image_3 = PhotoImage(file=relative_to_assets("constantpower.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=constant_voltage, relief="flat")
button_3.image = button_image_3
button_3.place(x=360, y=385.0, width=250, height=110)

main_frame.place(x=0, y=59)

window.mainloop()
