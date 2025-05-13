# CustomCopyPaste

This is a **custom copy-paster tool** that gives you the ability to:

- Copy as many items as you want (using `Command+C` or `Ctrl+C`)
- Automatically collect them into a list
- Paste all items at once, each optionally wrapped with a **start** and **end** character, and separated by a **custom delimiter**

---

## Requirements

Before running the script, make sure you have Python installed and run:

```bash
pip install pynput pyperclip
```

---

##  How to Run

You can run the script using:

```bash
python CustomCopyPaste.py [-d DELIMITER] [--start START_TOKEN] [--end END_TOKEN]
```

All parameters are optional:

- `-d` or `--delimiter`: The string used to separate items when pasting (default: space)
- `--start`: Token to insert **before** each copied item (default: empty)
- `--end`: Token to insert **after** each copied item (default: empty)

---

## Example

Suppose you run the script like this:

```bash
python CustomCopyPaste.py -d "," --start '"' --end '"'
```

Then:

1. You copy `First` using `Command+C`
2. Then copy `Second`
3. Then copy `Third`

Now when you press `Command+V` to paste, you'll get:

```
"First","Second","Third"
```

---

## Reset Clipboard

To reset the clipboard history at any time, press:

- `Command+Shift+R` (on macOS)
- `Ctrl+Shift+R` (on Windows/Linux)

You’ll see this confirmation:

```
[Reset] Clipboard history cleared.
```

---

## Enjoy!

Use this tool to enhance your copy-paste workflow — especially when collecting data, code snippets, words, or sentences for structured pasting.

Happy copying!
