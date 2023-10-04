# import tkinter as tk
# import pyautogui
# from datetime import datetime

# def capture_screenshot():
#     now = datetime.now()
#     timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
#     screenshot = pyautogui.screenshot()
#     screenshot.save(f"screenshot_{timestamp}.png")
#     status_label.config(text=f"Screenshot saved as screenshot_{timestamp}.png")

# # Create the main application window
# app = tk.Tk()
# app.title("Screenshot Capture App")

# # Create a button to capture the screenshot
# capture_button = tk.Button(app, text="Capture Screenshot", command=capture_screenshot)
# capture_button.pack(pady=20)

# # Create a label to display status
# status_label = tk.Label(app, text="")
# status_label.pack()

# # Start the GUI application
# app.mainloop()


import tkinter as tk
import pyautogui
from datetime import datetime

def capture_screenshot():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshot_{timestamp}.png")
    status_label.config(text=f"Screenshot saved as screenshot_{timestamp}.png")

# Create the main application window
app = tk.Tk()
app.title("Screenshot Capture App")

# Create a button with custom style
capture_button = tk.Button(
    app,
    text="Capture Screenshot",
    command=capture_screenshot,
    padx=10,  # Horizontal padding
    pady=5,   # Vertical padding
    font=("Helvetica", 14),  # Font and font size
    bg="lightblue",  # Background color
    fg="black",  # Text color
    relief=tk.RAISED,  # Button border style
)
capture_button.pack(pady=20)

# Create a label to display status
status_label = tk.Label(app, text="")
status_label.pack()

# Start the GUI application
app.mainloop()
