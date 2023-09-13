import tkinter


def miles_to_km():
    miles=float(input.get())
    km = round(miles * 1.609)
    label3.config(text=f"{km}")


window = tkinter.Tk()
window.title('Mile to km converter')
window.minsize(width=200,height=150)
window.config(padx=50, pady=35)

input = tkinter.Entry()
input.grid(column=1, row=0)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = tkinter.Label(text='0')
label3.grid(column=1, row=1)

label4 = tkinter.Label(text='Km')
label4.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=miles_to_km)
button.grid(column=1, row=2)







window.mainloop()
