import tkinter as tk
from tkinter import messagebox
import threading
import time
import winsound

PASSWORD = "vanh"

# Hàm kiểm tra mật khẩu
def check_password():
    if password_entry.get() == PASSWORD:
        winsound.Beep(800, 200)
        root.destroy()
    else:
        messagebox.showerror("Sai mật khẩu", "Mật khẩu không đúng! Dữ liệu đang bị xóa...")

# Loading giả và tiếng beep đếm ngược
def fake_loading():
    for i in range(10, 0, -1):
        loading_text.set(f"Xóa ổ C: trong {i} giây...")
        winsound.Beep(1000, 300)
        time.sleep(1)
    loading_text.set("ĐANG XÓA DỮ LIỆU...!!!")
    for _ in range(100):
        winsound.Beep(1500, 100)
        time.sleep(0.1)

# Chặn sự kiện đóng cửa sổ
def disable_event():
    pass

# Giao diện chính
root = tk.Tk()
root.title("Hệ thống bị xâm nhập")
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", disable_event)

# Chặn tổ hợp phím
root.bind("<Alt-F4>", lambda e: "break")
root.bind("<Control-w>", lambda e: "break")
root.bind("<Escape>", lambda e: "break")

# Cảnh báo chính
warning = tk.Label(root, text="💀 MÁY TÍNH ĐÃ BỊ KIỂM SOÁT 💀", font=("Consolas", 30, "bold"), fg="lime", bg="black")
warning.pack(pady=80)

# Thanh loading giả
loading_text = tk.StringVar()
loading_label = tk.Label(root, textvariable=loading_text, font=("Consolas", 18), fg="red", bg="black")
loading_label.pack(pady=10)

# Nhập mật khẩu
password_label = tk.Label(root, text="Nhập mật khẩu để dừng lại:", font=("Consolas", 16), fg="white", bg="black")
password_label.pack(pady=10)
password_entry = tk.Entry(root, font=("Consolas", 16), show="*", width=20)
password_entry.pack()
password_entry.focus()

# Nút xác nhận
submit_btn = tk.Button(root, text="Xác nhận", command=check_password, font=("Consolas", 14), bg="lime", fg="black")
submit_btn.pack(pady=20)

# Bắt đầu thread loading + beep + countdown
t1 = threading.Thread(target=fake_loading, daemon=True)
t1.start()

# Chạy GUI
root.mainloop()