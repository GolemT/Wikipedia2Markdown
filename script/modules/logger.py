import os
import datetime
import threading
import queue


class Logger:
    LEVELS = {"DEBUG": 1, "INFO": 2, "WARNING": 3, "ERROR": 4}

    def __init__(self, level="INFO", log_to_file=True, log_dir=".logs", show_cli=True):
        self.level = level
        self.log_to_file = log_to_file
        self.log_dir = log_dir
        self.show_cli = show_cli
        self.queue = queue.Queue()
        self.lock = threading.Lock()

        if self.log_to_file:
            os.makedirs(self.log_dir, exist_ok=True)
            self.log_file = os.path.join(self.log_dir, f"log_{datetime.date.today()}.log")

        self.worker_thread = threading.Thread(target=self._process_logs, daemon=True)
        self.worker_thread.start()

    def _process_logs(self):
        """Verarbeitet die Logs asynchron aus der Warteschlange."""
        while True:
            level, message, timestamp = self.queue.get()
            log_entry = f"[{timestamp}] [{level}] {message}"

            if self.show_cli:
                print(log_entry)

            if self.log_to_file:
                with self.lock:
                    with open(self.log_file, "a") as f:
                        f.write(log_entry + "\n")

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


logger = Logger(level="DEBUG", show_cli=True)
