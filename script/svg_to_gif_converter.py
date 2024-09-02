import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import base64
from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def svg_to_gif(svg_file, gif_file, width, height, duration=3000, frames=60):
    # Set up a headless Chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Create a simple HTML file to display the SVG
    html_content = f"""
    <html>
    <body style="margin:0;padding:0;overflow:hidden;">
        <img src="file:///{os.path.abspath(svg_file)}" style="width:100%;height:100%;object-fit:contain;">
    </body>
    </html>
    """
    with open('temp.html', 'w') as f:
        f.write(html_content)

    # Open the HTML file in the browser
    driver.get(f"file:///{os.path.abspath('temp.html')}")
    driver.set_window_size(width, height)

    # Capture frames
    frame_duration = duration / frames
    frame_images = []
    for _ in range(frames):
        # Capture the current state of the page
        screenshot = driver.get_screenshot_as_base64()
        img = Image.open(BytesIO(base64.b64decode(screenshot)))
        frame_images.append(img.resize((width, height), Image.LANCZOS))
        time.sleep(frame_duration / 1000)  # Wait for next frame

    # Save as GIF
    frame_images[0].save(
        gif_file,
        save_all=True,
        append_images=frame_images[1:],
        duration=frame_duration,
        loop=0
    )

    # Clean up
    driver.quit()
    os.remove('temp.html')

def select_svg_file():
    file_path = filedialog.askopenfilename(filetypes=[("SVG files", "*.svg")])
    svg_entry.delete(0, tk.END)
    svg_entry.insert(0, file_path)

def select_gif_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    gif_entry.delete(0, tk.END)
    gif_entry.insert(0, file_path)

def convert():
    svg_file = svg_entry.get()
    gif_file = gif_entry.get()
    resolution = resolution_var.get()
    duration = int(duration_entry.get())
    frames = int(frames_entry.get())
    
    if not svg_file or not gif_file:
        messagebox.showerror("Error", "Please select both input SVG and output GIF files.")
        return
    
    if resolution == "Custom":
        width = int(width_entry.get())
        height = int(height_entry.get())
    elif resolution == "720x405":
        width, height = 720, 405
    elif resolution == "720p":
        width, height = 1280, 720
    elif resolution == "1080p":
        width, height = 1920, 1080
    
    try:
        svg_to_gif(svg_file, gif_file, width, height, duration, frames)
        messagebox.showinfo("Success", "Conversion completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def on_resolution_change(*args):
    if resolution_var.get() == "Custom":
        width_entry.config(state="normal")
        height_entry.config(state="normal")
    else:
        width_entry.config(state="disabled")
        height_entry.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("SVG to GIF Converter")

# Create and pack widgets
tk.Label(root, text="Select SVG file:").pack()
svg_entry = tk.Entry(root, width=50)
svg_entry.pack()
tk.Button(root, text="Browse", command=select_svg_file).pack()

tk.Label(root, text="Select output GIF file:").pack()
gif_entry = tk.Entry(root, width=50)
gif_entry.pack()
tk.Button(root, text="Browse", command=select_gif_file).pack()

tk.Label(root, text="Resolution:").pack()
resolution_var = tk.StringVar(root)
resolution_var.set("720x405")  # default value
resolution_options = ["720x405", "720p", "1080p", "Custom"]
resolution_menu = ttk.Combobox(root, textvariable=resolution_var, values=resolution_options)
resolution_menu.pack()
resolution_var.trace("w", on_resolution_change)

tk.Label(root, text="Custom Width:").pack()
width_entry = tk.Entry(root, state="disabled")
width_entry.pack()

tk.Label(root, text="Custom Height:").pack()
height_entry = tk.Entry(root, state="disabled")
height_entry.pack()

tk.Label(root, text="Duration (ms):").pack()
duration_entry = tk.Entry(root)
duration_entry.insert(0, "3000")
duration_entry.pack()

tk.Label(root, text="Frames:").pack()
frames_entry = tk.Entry(root)
frames_entry.insert(0, "60")
frames_entry.pack()

tk.Button(root, text="Convert", command=convert).pack()

# Start the GUI event loop
root.mainloop()
