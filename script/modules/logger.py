import os
import datetime
import threading
import queue
import sys

class Logger:
    LEVELS = {"DEBUG": 1, "INFO": 2, "WARNING": 3, "ERROR": 4}

    def __init__(self, level="INFO", log_to_file=True, log_dir=".logs", show_cli=True):
        self.level = level
        self.log_to_file = log_to_file
        self.log_dir = log_dir
        self.show_cli = show_cli
        self.queue = queue.Queue()
        self.lock = threading.Lock()
        self._stop_event = threading.Event()  # <-- NEU: Beenden des Threads ermöglichen

        if self.log_to_file:
            os.makedirs(self.log_dir, exist_ok=True)
            self._update_log_filename()

        self.worker_thread = threading.Thread(target=self._process_logs, daemon=False)  # <-- KEIN Daemon mehr
        self.worker_thread.start()

    def _update_log_filename(self):
        """Generiert den aktuellen Log-Dateinamen mit Datum und Uhrzeit."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file = os.path.join(self.log_dir, f"log_{timestamp}.log")

    def _write_to_file(self, log_entry):
        """Schreibt den Log-Eintrag mit UTF-8-Encoding in die Datei."""
        with self.lock:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")

    def _process_logs(self):
        """Verarbeitet die Logs asynchron aus der Warteschlange."""
        while not self._stop_event.is_set() or not self.queue.empty():
            try:
                level, message, timestamp = self.queue.get(timeout=0.1)  # Warte auf neue Logs
                log_entry = f"[{timestamp}] [{level}] {message}"

                if self.show_cli:
                    print(log_entry, file=sys.stdout)

                if self.log_to_file:
                    self._write_to_file(log_entry)
            except queue.Empty:
                continue  # Wenn keine neuen Logs da sind, weiterlaufen

    def shutdown(self):
        """Stoppt den Logger und verarbeitet verbleibende Logs."""
        self._stop_event.set()
        self.worker_thread.join()  # Warte, bis alle Logs verarbeitet sind
        print("[Logger] Alle Logs gespeichert. Logger beendet.")

    def log(self, level, message):
        if self.LEVELS[level] >= self.LEVELS[self.level]:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.queue.put((level, message, timestamp))

    def debug(self, message):
        self.log("DEBUG", message)

    def info(self, message):
        self.log("INFO", message)

    def warning(self, message):
        self.log("WARNING", message)

    def error(self, message):
        self.log("ERROR", message)

    def set_level(self, new_level):
        """Ändert das Log-Level zur Laufzeit."""
        if new_level in self.LEVELS:
            self.level = new_level
            self.info(f"Log-Level geändert auf: {new_level}")
        else:
            self.warning(f"Ungültiges Log-Level: {new_level}")

# Globale Logger-Instanz für alle Scripts
global_logger = Logger(level="ERROR", show_cli=True)
