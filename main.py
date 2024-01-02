import tkinter as tk
import subprocess

# Create the main application window
root = tk.Tk()
root.title("GESTURE CONTROL")

# Function to be called when Button 1 is clicked
def button1_click():
    script_path = "C:/Users/andre/Downloads/Mini Project/python/virtual_mouse_AI-main/virtual_mouse_AI-main/AiVirtualMouseProject.py"  # Replace with the actual path to your volume control script
    subprocess.Popen(["python", script_path])
    
def button2_click():
    script_path = "C:/Users/andre/Downloads/Mini Project/python/Volume-Control-With-Hand-Detection-OpenCV-Python-Source-Code (2)/Volume-Control-With-Hand-Detection-OpenCV-Python-Source-Code/Volume Control With Hand Detection OpenCV Python Source Code/main.py"  # Replace with the actual path to your volume control script
    subprocess.Popen(["python", script_path])

# Create a header label
header_label = tk.Label(root, text="GESTURE CONTROL", font=("Helvetica", 24))
header_label.pack(pady=20)

# Create buttons with larger width and height
button1 = tk.Button(root, text="Virtual Mouse", command=button1_click, width=20, height=3)
button2 = tk.Button(root, text="Volume Control", command=button2_click, width=20, height=3)

# Place the buttons in the window
button1.pack(pady=10)
button2.pack(pady=10)

# Set the size of the main window
root.geometry("800x500")  # Width x Height

# Start the main event loop 
root.mainloop()