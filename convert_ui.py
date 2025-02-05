import subprocess
import customtkinter
from tkinter import scrolledtext
import os
from script.modules.logger import global_logger as logger

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def set_log_level(level):
    logger.set_level(level)

app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Wikipedia2Markdown")

log_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
log_dropdown = customtkinter.CTkComboBox(app, values=log_levels, command=set_log_level)
log_dropdown.pack()

folder_path = os.path.abspath("./landing")
convert_script_path = os.path.abspath("./script/convert_main.py")

linkList = []
html_frames = {} # used to display a preview of the markdown files

def get_link():
    text_link = link.get()
    if text_link:
        linkList.append(text_link)
        textbox.configure(state="normal")
        textbox.insert("end",text_link + "\n")
        textbox.configure(state="disabled")
        print(linkList)
    else:
        label.configure(text=f"Please enter a valid link.")
        label.pack()
    link.delete(0, customtkinter.END)

def convert(linklist):
    for element in linklist:
        try:
            subprocess.run(
                ["python", convert_script_path, "-u", element],
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as e:
            label.configure(text=f"{e}")
            label.pack()
            return False
        except FileNotFoundError:
            label.configure(text=f"convert_main.py not found at {convert_script_path}")
            label.pack()
            return False
    return True

def display_markdown(filepath, tab_name):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        if tab_name not in html_frames:  # Use html_frames for consistency
            app.tabview.add(tab_name)
            text_widget = scrolledtext.ScrolledText(app.tabview.tab(tab_name), wrap=customtkinter.WORD)
            text_widget.pack(fill="both", expand=True)
            html_frames[tab_name] = text_widget
        else:
            text_widget = html_frames[tab_name]

        text_widget.delete("1.0", customtkinter.END)
        text_widget.insert(customtkinter.END, markdown_content)  # Insert raw Markdown
        text_widget.config(state=customtkinter.DISABLED)  # Make it read-only

    except FileNotFoundError:
        label.configure(text=f"Markdown file not found: {filepath}")
        label.pack()
    except Exception as e:
        label.configure(text=f"An error occurred: {e}")
        label.pack()


def find_markdown_files(root_dir):
    markdown_files = []
    for directory, directoryname, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(directory, filename)
                markdown_files.append(filepath)
    return markdown_files

def convert_link():
    label.pack_forget()

    if not linkList:
        label.configure(text="No links found.")
        label.pack()
        return

    else:
        try:
            if not convert(linkList):
                return

            if hasattr(app, "tabview"):
                app.tabview.destroy()
                html_frames.clear()

            app.tabview = customtkinter.CTkTabview(app)
            app.tabview.pack(fill="both", expand=True)

            markdown_files = find_markdown_files(folder_path)

            if markdown_files:
                for filepath in markdown_files:
                    tab_name = os.path.basename(filepath)[:-3]
                    display_markdown(filepath, tab_name)
            else:
                label.configure(text=f"No markdown files found in '{folder_path}' or its subdirectories.")
                label.pack()

        except Exception as e:
            label.configure(text=f"An error occurred: {e}")
            label.pack()

    linkList.clear()
    textbox.configure(state="normal")
    textbox.delete(0.0, "end")
    textbox.configure(state="disabled")


link = customtkinter.CTkEntry(app, placeholder_text="Insert a Wikipedia Link here", width=200, height=40)
button = customtkinter.CTkButton(app, text="Add Link to List", command=get_link, fg_color="#623CEA")
button2 = customtkinter.CTkButton(app, text="Convert", command=convert_link, fg_color="#623CEA")
label = customtkinter.CTkLabel(app, fg_color="transparent", text_color="red")
listLabel = customtkinter.CTkLabel(app, fg_color="transparent", text="List of all Links to Convert")
textbox = customtkinter.CTkTextbox(app, width=400, height=200)
textbox.configure(state="disabled")

link.pack(padx=30, pady=30)
button.pack()
button2.pack(pady=5)
listLabel.pack(pady=5)
textbox.pack()

def on_closing():
    logger.shutdown()  # <-- Logger beenden, bevor die GUI schließt
    app.quit()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()