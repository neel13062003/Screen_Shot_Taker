import tkinter as tk
import pyautogui
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class ScreenshotServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/capture':
            self.capture_screenshot()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Screenshot captured and saved.')

    def capture_screenshot(self):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot_{timestamp}.png")

def start_server():
    server = HTTPServer(('localhost', 8080), ScreenshotServer)
    server.serve_forever()

if __name__ == '__main__':
    threading.Thread(target=start_server).start()
    # Create the main application window
    app = tk.Tk()
    app.title("Screenshot Capture App")

    # Create a button with custom style
    capture_button = tk.Button(
        app,
        text="Capture Screenshot",
        command=lambda: capture_screenshot(),
        padx=10,
        pady=5,
        font=("Helvetica", 14),
        bg="lightblue",
        fg="black",
        relief=tk.RAISED,
    )
    capture_button.pack(pady=20)

    app.mainloop()
