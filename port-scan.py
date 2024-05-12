import socket
import tkinter as tk
from tkinter import messagebox, filedialog

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def pscan(ip, port, output_file):
    try:
        conn = s.connect((ip, port))
        output_file.write(f"Port {port} is open on {ip}\n")
        conn.close()
    except:
        output_file.write(f"Port {port} is not open on {ip}\n")

def scan_ip_range(start_ip, end_ip, port, output_file):
    start_ip_parts = start_ip.split(".")
    end_ip_parts = end_ip.split(".")

    for i in range(int(start_ip_parts[3]), int(end_ip_parts[3]) + 1):
        ip = ".".join(start_ip_parts[:3]) + "." + str(i)
        pscan(ip, port, output_file)

def start_scan():
    start_ip = start_ip_entry.get().strip()
    end_ip = end_ip_entry.get().strip()
    port = int(port_entry.get().strip())
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if not start_ip or not end_ip or not port or not output_file_path:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    with open(output_file_path, "w") as output_file:
        scan_ip_range(start_ip, end_ip, port, output_file)
        messagebox.showinfo("Scan Complete", "Port scan completed successfully. Results saved to file.")

# Create Tkinter window
root = tk.Tk()
root.title("IP Range Port Scanner")

# IP range entry
start_ip_label = tk.Label(root, text="Start IP:")
start_ip_label.grid(row=0, column=0, padx=5, pady=5)
start_ip_entry = tk.Entry(root)
start_ip_entry.grid(row=0, column=1, padx=5, pady=5)

end_ip_label = tk.Label(root, text="End IP:")
end_ip_label.grid(row=1, column=0, padx=5, pady=5)
end_ip_entry = tk.Entry(root)
end_ip_entry.grid(row=1, column=1, padx=5, pady=5)

# Port entry
port_label = tk.Label(root, text="Port:")
port_label.grid(row=2, column=0, padx=5, pady=5)
port_entry = tk.Entry(root)
port_entry.grid(row=2, column=1, padx=5, pady=5)

# Scan button
scan_button = tk.Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
