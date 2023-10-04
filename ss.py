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

# Global variables to store the coordinates of the selection rectangle
start_x = None
start_y = None
end_x = None
end_y = None

def on_mouse_press(event):
    global start_x, start_y
    start_x = app.winfo_pointerx() - app.winfo_rootx()
    start_y = app.winfo_pointery() - app.winfo_rooty()

def on_mouse_release(event):
    global end_x, end_y
    end_x = app.winfo_pointerx() - app.winfo_rootx()
    end_y = app.winfo_pointery() - app.winfo_rooty()

def capture_screenshot():
    if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
        
        # Determine the coordinates for the screenshot region
        x1, x2 = min(start_x, end_x), max(start_x, end_x)
        y1, y2 = min(start_y, end_y), max(start_y, end_y)
        
        # Capture the screen region
        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        screenshot.save(f"screenshot_{timestamp}.png")
        status_label.config(text=f"Screenshot saved as screenshot_{timestamp}.png")
    else:
        status_label.config(text="Select a region first")

# Create the main application window
app = tk.Tk()
app.title("Custom Screenshot Capture App")

# Create a canvas for drawing the selection rectangle
canvas = tk.Canvas(app, bg="gray", cursor="cross")
canvas.pack(fill="both", expand=True)
canvas.bind("<ButtonPress-1>", on_mouse_press)
canvas.bind("<ButtonRelease-1>", on_mouse_release)

# Create a button to capture the custom screenshot
capture_button = tk.Button(
    app,
    text="Capture Custom Screenshot",
    command=capture_screenshot,
    padx=10,
    pady=5,
    font=("Helvetica", 14),
    bg="lightblue",
    fg="black",
    relief=tk.RAISED,
)
capture_button.pack(pady=20)

# Create a label to display status
status_label = tk.Label(app, text="")
status_label.pack()

# Start the GUI application
app.mainloop()
