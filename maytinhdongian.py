import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation.get()
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn phép toán.")
            return
        
        label_result.config(text=f"Kết quả: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def reset():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Kết quả: ")
    operation.set(None)

root = tk.Tk()
root.title("Máy tính đơn giản")
root.geometry("350x280")
root.configure(bg="#f0f4f8")  # Màu nền sáng dịu

# Font chữ
font_label = ("Segoe UI", 11)
font_entry = ("Segoe UI", 12)
font_button = ("Segoe UI", 11, "bold")
font_result = ("Segoe UI", 14, "bold")

# Nhãn và Entry số thứ nhất
tk.Label(root, text="Số thứ nhất:", bg="#f0f4f8", font=font_label).place(x=20, y=20)
entry_num1 = tk.Entry(root, font=font_entry, bd=2, relief="groove")
entry_num1.place(x=130, y=18, width=180, height=28)

# Nhãn và Entry số thứ hai
tk.Label(root, text="Số thứ hai:", bg="#f0f4f8", font=font_label).place(x=20, y=65)
entry_num2 = tk.Entry(root, font=font_entry, bd=2, relief="groove")
entry_num2.place(x=130, y=63, width=180, height=28)

# Biến phép toán
operation = tk.StringVar(value=None)

# Khung chứa RadioButtons với nền sáng và bo góc
frame_ops = tk.Frame(root, bg="#dbe9f4", bd=1, relief="ridge")
frame_ops.place(x=20, y=110, width=290, height=50)

ops = {'+': 'Cộng (+)', '-': 'Trừ (-)', '*': 'Nhân (×)', '/': 'Chia (÷)'}
x_pos = 10
for val, text in ops.items():
    rb = tk.Radiobutton(frame_ops, text=text, variable=operation, value=val,
                        bg="#dbe9f4", font=font_label, activebackground="#a9c1f7", cursor="hand2")
    rb.place(x=x_pos, y=12)
    x_pos += 70

# Nút Tính với màu xanh, bo góc
btn_calculate = tk.Button(root, text="Tính", font=font_button, bg="#4a90e2", fg="white",
                          activebackground="#357abd", activeforeground="white", bd=0, cursor="hand2",
                          command=calculate)
btn_calculate.place(x=70, y=180, width=90, height=35)

# Nút Reset với màu đỏ nhạt, bo góc
btn_reset = tk.Button(root, text="Reset", font=font_button, bg="#e94e4e", fg="white",
                      activebackground="#ba3535", activeforeground="white", bd=0, cursor="hand2",
                      command=reset)
btn_reset.place(x=190, y=180, width=90, height=35)

# Label kết quả
label_result = tk.Label(root, text="Kết quả: ", bg="#f0f4f8", font=font_result, fg="#333333")
label_result.place(x=20, y=230)

root.mainloop()
