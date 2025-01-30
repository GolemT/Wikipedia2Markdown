import subprocess
import customtkinter
import markdown
from tkinterweb import HtmlFrame
import os


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("WikiConvert")

folder_path1 = "./landing"
folder_path = os.path.abspath(folder_path1)
linkList = []
markdown_files = []


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

def display_markdown(filepath, tab_name):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            markdown_content = f.read()
            html_content = markdown.markdown(markdown_content)

            if tab_name not in app.tabview.tab_names():
                app.tabview.add(tab_name)  # Add the tab if it doesn't exist
                frame = HtmlFrame(app.tabview.tab(tab_name))
                frame.pack(fill="both", expand=True)
            else:
                frame = app.tabview.tab(tab_name).winfo_children()[0] #get the HtmlFrame

            frame.set_content(html_content)

    except FileNotFoundError:
        print(f"Markdown file not found: {filepath}")

    except Exception as e:
        print(f"An error occurred: {e}")


def get_link():
    text_link = link.get()
    linkList.append(text_link)
    print(text_link)
    print(linkList)

def convert_link():
    label.pack_forget()
    if len(linkList) > 0:
        try:
            convert(linkList)

            app.tabview = customtkinter.CTkTabview(app)
            app.tabview.pack(fill="both", expand=True)

            if os.path.isdir(folder_path):
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)  # Get the full file path
                    if os.path.isfile(file_path):
                        markdown_files.append(file_path)
            else:
                print(f"The folder '{folder_path}' does not exist.")

            for tab_name, filepath in markdown_files.items():
                display_markdown(filepath, tab_name)

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            del linkList[:]
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