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
app.geometry("720x480")
app.title("Wikipedia2Markdown")

log_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
log_dropdown = customtkinter.CTkComboBox(app, values=log_levels, command=set_log_level)
log_dropdown.pack()

folder_path = os.path.abspath("./landing")
convert_script_path = os.path.abspath("./script/convert_main.py")

linkList = []
html_frames = {}

def convert(linklist):
    for element in linklist:
        try:
            result = subprocess.run(
                ["python", convert_script_path, "-u", element],
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Error converting {element}: {e}")
            return False
        except FileNotFoundError:
            print(f"convert_main.py not found at {convert_script_path}")
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
        print(f"Markdown file not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_link():
    text_link = link.get()
    linkList.append(text_link)
    print(linkList)
    link.delete(0, customtkinter.END)

def convert_link():
    label.pack_forget()
    if linkList:
        try:
            if convert(linkList):
                if hasattr(app, "tabview"):
                    app.tabview.destroy()
                    html_frames.clear() # Clear the stored frames as well
                app.tabview = customtkinter.CTkTabview(app)
                app.tabview.pack(fill="both", expand=True)

                def find_markdown_files(root_dir):
                    markdown_files = []
                    for dirpath, dirnames, filenames in os.walk(root_dir):
                        for filename in filenames:
                            if filename.endswith(".md"):
                                filepath = os.path.join(dirpath, filename)
                                markdown_files.append(filepath)
                    return markdown_files

                markdown_files = find_markdown_files(folder_path)

                if markdown_files:
                    for filepath in markdown_files:
                        tab_name = os.path.basename(filepath)[:-3]
                        display_markdown(filepath, tab_name)
                else:
                    print(f"No markdown files found in '{folder_path}' or its subdirectories.")

                linkList.clear()
            else:
                label.pack()
                print("Conversion failed. Check logs for errors.")
        except Exception as e:
            print(f"An error occurred: {e}")

        del linkList[:]

    else:
        label.pack()

link = customtkinter.CTkEntry(app, placeholder_text="Insert a Wikipedia Link here", width=200, height=40)
button = customtkinter.CTkButton(app, text="Add Link to List", command=get_link, fg_color="#623CEA")
button2 = customtkinter.CTkButton(app, text="Convert", command=convert_link, fg_color="#623CEA")
label = customtkinter.CTkLabel(app, text="No links provided", fg_color="transparent", text_color="red")

link.pack(padx=30, pady=30)
button.pack()
button2.pack(pady=5)

def on_closing():
    logger.shutdown()  # <-- Logger beenden, bevor die GUI schließt
    app.quit()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()