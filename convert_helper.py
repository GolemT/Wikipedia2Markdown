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
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error converting {element}: {e}")
            print(e.stderr)
            return False
        except FileNotFoundError:
            print(f"convert_main.py not found at {convert_script_path}")
            return False
    return True

def display_markdown(filepath, tab_name):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            markdown_content = f.read()
            html_content = markdown.markdown(markdown_content)

            if tab_name not in html_frames:  # Correct check
                app.tabview.add(tab_name)
                frame = HtmlFrame(app.tabview.tab(tab_name))
                frame.pack(fill="both", expand=True)
                html_frames[tab_name] = frame # Store the frame with the tab name as the key.
            else:
                frame = html_frames[tab_name] #Retrieve the frame using the tab name as the key

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
    else:
        label.pack()
        print("No links provided")

link = customtkinter.CTkEntry(app, placeholder_text="Insert a Wikipedia Link here", width=200, height=40)
button = customtkinter.CTkButton(app, text="Add Link to List", command=get_link)
button2 = customtkinter.CTkButton(app, text="Convert", command=convert_link)
label = customtkinter.CTkLabel(app, text="No links provided", fg_color="transparent", text_color="red")

link.pack(padx=30, pady=30)
button.pack()
button2.pack(pady=5)

app.mainloop()