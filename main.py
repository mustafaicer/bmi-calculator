from tkinter import *

window = Tk()
window.title("BMI calculator")
window.minsize(width=400, height=300)

log = Label(window)
def calc_bmi():
    log.config(text="")
    try:
        height_of_user = float(height_value.get())
        weight_of_user = float(weight_value.get())

        bmi = weight_of_user / (height_of_user ** 2)

        if bmi < 18.5:
            log.config(text=f"BMI result : {bmi:.1f}\nUnderweight")
            log.pack()

        elif (bmi > 18.5) and (bmi < 24.9):
            log.config(text=f"BMI result : {bmi:.1f}\nNormal")
            log.pack()

        elif (bmi > 25) and (bmi < 29.9):
            log.config(text=f"BMI result : {bmi:.1f}\nOverweight")
            log.pack()

        elif (bmi > 30) and (bmi < 34.9):
            log.config(text=f"BMI result : {bmi:.1f}\nObese")
            log.pack()
        elif bmi > 35:
            log.config(text=f"BMI result : {bmi:.1f}\nExtremely obese")
            log.pack()
    except:
        log.config(text="Enter a int..")
        log.pack()
        weight_entry.delete(0,END)
        height_entry.delete(0,END)

text_label = Label(text="Welcome to BMI calculator",padx=10,pady=10)
text_label.pack()

height_value = StringVar()
height_text = Label(text="Enter Your Height (m)")
height_text.pack()
height_entry = Entry(textvariable=height_value,borderwidth=5)
height_entry.pack()

weight_value = StringVar()
weight_text = Label(text="Enter Your Weight (kg)")
weight_text.pack()
weight_entry = Entry(textvariable=weight_value,borderwidth=5)
weight_entry.pack()

calc_button = Button(text="Calc",command=calc_bmi,padx=10,pady=10)
calc_button.pack()

window.mainloop()