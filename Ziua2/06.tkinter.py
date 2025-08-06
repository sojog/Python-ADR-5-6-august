import tkinter as tk
import requests

fereastra =  tk.Tk()
fereastra.title("Programul meu")

width = 400
height = 600
x = 300
y  = 100

fereastra.geometry(f"{width}x{height}+{x}+{y}")

def cauta_gluma():
    # print("Aici va fi implementata logica aplicatiei")
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept" : "application/json"} )
    response_dict = response.json()
    new_joke = response_dict["joke"]
    label.config(text=new_joke)

label = tk.Label(fereastra, text="Aici va fi rezultatul")
label.pack()


buton_cauta = tk.Button(fereastra, text="Cauta", command=cauta_gluma)
buton_cauta.pack()


fereastra.mainloop()

