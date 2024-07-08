import tkinter

def button_clicked():
    km = entered_km.get()
    km_to_miles = float(km) * 1.609
    text_4["text"] = round(km_to_miles, 2)



window = tkinter.Tk()

window.title("Tkinter Tutoriala Davitastvis")
window.minsize(100, 100)
window.config(padx=20, pady=20)

text_1 = tkinter.Label(text = "is equal to")
text_1.grid(row=1, column=0)

text_2 = tkinter.Label(text = "Miles")
text_2.grid(row= 0, column=2)

text_3 = tkinter.Label(text = "KM")
text_3.grid(row= 1, column=2)

text_4 = tkinter.Label(text = "")
text_4.grid(row=1, column=1)

entered_km = tkinter.Entry(width= 10)
entered_km.grid(row= 0, column= 1)

calculate_button = tkinter.Button(text= "Calculate", command= button_clicked)
calculate_button.grid(row=2, column= 1)


window.mainloop()