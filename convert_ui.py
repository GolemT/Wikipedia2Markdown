import subprocess
import customtkinter
from tkinter import scrolledtext
import os
from script.modules.logger import global_logger as logger

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Wikipedia2Markdown")

folder_path = os.path.abspath("./landing")
convert_script_path = os.path.abspath("./script/convert_main.py")

linkList = []
html_frames = {}  # used to display a preview of the markdown files


def get_link():
    text_link = link.get()
    if text_link:
        linkList.append(text_link)
        textbox.configure(state="normal")
        textbox.insert("end", text_link + "\n")
        textbox.configure(state="disabled")
    else:
        logger.error("Kein gültiger Link eingegeben")
        label.configure(text="Bitte geben Sie einen gültigen Link ein.")
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
            logger.error(f"Ein Fehler ist während der Konvertierung aufgetreten: {e}")
            label.configure(text="Fehler während der Konvertierung")
            label.pack()
            return False
        except FileNotFoundError as e:
            logger.debug(f"FileNotFoundError: {e}")
            label.configure(text="convert_main.py nicht gefunden")
            label.pack()
            return False
    return True

def display_markdown(filepath, tab_name):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            markdown_inhalt = f.read()

        if tab_name not in html_frames:  # html_frames für Konsistenz verwenden
            app.tabview.add(tab_name)
            text_widget = scrolledtext.ScrolledText(app.tabview.tab(tab_name), wrap=customtkinter.WORD)
            text_widget.pack(fill="both", expand=True)
            html_frames[tab_name] = text_widget
        else:
            text_widget = html_frames[tab_name]

        text_widget.delete("1.0", customtkinter.END)
        text_widget.insert(customtkinter.END, markdown_inhalt)  # Rohes Markdown einfügen
        text_widget.config(state=customtkinter.DISABLED)  # Schreibgeschützt machen


    except FileNotFoundError as e:
        logger.debug(f"FileNotFoundError: {e}")
        label.configure(text="Markdown-Datei nicht gefunden")
        label.pack()
    except Exception as e:
        logger.error(e)
        label.configure(text="Ein Fehler ist beim Anzeigen der Markdown-Vorschau aufgetreten")
        label.pack()


def find_markdown_files(root_dir):
    markdown_dateien = []
    for verzeichnis, verzeichnisname, dateinamen in os.walk(root_dir):
        for dateiname in dateinamen:
            if dateiname.endswith(".md"):
                dateipfad = os.path.join(verzeichnis, dateiname)
                markdown_dateien.append(dateipfad)
    return markdown_dateien


def convert_link():
    label.pack_forget()

    if not linkList:
        logger.error("Keine gültigen Links eingegeben")
        label.configure(text="Keine Links gefunden.")
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

            markdown_dateien = find_markdown_files(folder_path)

            if markdown_dateien:
                for dateipfad in markdown_dateien:
                    tab_name = os.path.basename(dateipfad)[:-3]
                    display_markdown(dateipfad, tab_name)
            else:
                logger.error(f"Keine Markdown-Dateien in '{folder_path}' oder seinen Unterverzeichnissen gefunden.")
                label.configure(text="Keine Markdown-Dateien gefunden")
                label.pack()

        except Exception as e:
            logger.error(e)
            label.configure(text="Ein Fehler ist während der Konvertierung aufgetreten")
            label.pack()

    linkList.clear()
    textbox.configure(state="normal")
    textbox.delete(0.0, "end")
    textbox.configure(state="disabled")


link = customtkinter.CTkEntry(app, placeholder_text="Fügen Sie hier einen Wikipedia-Link ein", width=400, height=40)
button = customtkinter.CTkButton(app, text="Link zur Liste hinzufügen", command=get_link, fg_color="#623CEA", width=400)
button2 = customtkinter.CTkButton(app, text="Konvertieren", command=convert_link, fg_color="#623CEA", width=400)
label = customtkinter.CTkLabel(app, fg_color="transparent", text_color="red")
listLabel = customtkinter.CTkLabel(app, fg_color="transparent", text="Liste aller zu konvertierenden Links")
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
