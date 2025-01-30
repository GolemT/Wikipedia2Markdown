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
    label.pack_forget()
    if len(linkArray) > 0:
        try:
            convert(linkArray)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            del linkArray[:]
            print("List cleared")
    else:
        label.pack()
        print("No links provided")

#UI Elements
link = customtkinter.CTkEntry(app, placeholder_text="Insert a Wikipedia Link here", width=200, height=40)


button = customtkinter.CTkButton(app, text="Add Link to List", command=get_link)

button2 = customtkinter.CTkButton(app, text="Convert", command=convert_link)

label = customtkinter.CTkLabel(app, text="No links provided", fg_color="transparent", text_color = "red")

#Layout
link.pack(padx=30, pady=30)
button.pack()
button2.pack(pady=5)



app.mainloop()