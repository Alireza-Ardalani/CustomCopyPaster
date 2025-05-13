from pynput import keyboard
from collections import deque
import pyperclip
import platform
import time
import argparse

def run_clipboard_tool(delimiter, start_token, end_token):
    clipboard_history = deque()
    pressed_keys = set()

    IS_MAC = platform.system() == "Darwin"
    CMD_KEY = keyboard.Key.cmd if IS_MAC else keyboard.Key.ctrl
    SHIFT_KEY = keyboard.Key.shift

    def on_press(key):
        try:
            if key == CMD_KEY:
                pressed_keys.add('cmd')
            elif key == SHIFT_KEY:
                pressed_keys.add('shift')
            elif hasattr(key, 'char') and key.char in ('c', 'v', 'r'):
                if 'cmd' in pressed_keys:
                    if key.char == 'c':
                        time.sleep(0.1)
                        data = pyperclip.paste()
                        if data and (not clipboard_history or data != clipboard_history[-1]):
                            clipboard_history.append(data)
                            print(f"[Copied] {data}")
                    elif key.char == 'v':
                        formatted = delimiter.join(
                            f"{start_token}{item}{end_token}" for item in clipboard_history
                        )
                        pyperclip.copy(formatted)
                        print(f"[Pasted] {formatted}")
                    elif key.char == 'r' and 'shift' in pressed_keys:
                        clipboard_history.clear()
                        print("[Reset] Clipboard history cleared.")
        except Exception as e:
            print(f"[Error] {e}")

    def on_release(key):
        if key == CMD_KEY:
            pressed_keys.discard('cmd')
        elif key == SHIFT_KEY:
            pressed_keys.discard('shift')

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clipboard stack tool with delimiter and token formatting.")
    parser.add_argument("-d", "--delimiter", type=str, default=" ", help="Delimiter for joining (default: space)")
    parser.add_argument("--start", type=str, default="", help="Start token for each item (default: '')")
    parser.add_argument("--end", type=str, default="", help="End token for each item (default: '')")
    args = parser.parse_args()

    run_clipboard_tool(args.delimiter, args.start, args.end)
