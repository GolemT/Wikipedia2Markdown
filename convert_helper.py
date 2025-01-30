import subprocess
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("WikiConvert")

linkArray = []


#UI Methods
def convert(linklist):
    #sites = ["https://de.wikipedia.org/wiki/Liste_von_Katzenrassen"]

    sites = linklist
    for element in sites:
        subprocess.run(
            [
                "python",
                "./script/convert_main.py",
                "-u",
                element,
            ]
        )

def get_link():
    text_link = link.get()
    linkArray.append(text_link)
    print(text_link)
    print(linkArray)

def convert_link():
    convert(linkArray)
    del linkArray[:]

#UI Elements
link = customtkinter.CTkEntry(app, placeholder_text="Insert a Wikipedia Link here", width=200, height=40)
link.pack(padx=30, pady=30)

button = customtkinter.CTkButton(app, text="Add Link to List", command=get_link)
button.pack(padx=10)
button2 = customtkinter.CTkButton(app, text="Convert", command=convert_link)
button2.pack(padx=10)


app.mainloop()