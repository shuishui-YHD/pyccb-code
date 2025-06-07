import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog

def text_to_ccb(text):
    """将文本转换为鸡py语言的二进制形式（统一使用16位编码）"""
    ccb_code = []
    for char in text:
        code_point = ord(char)
        binary = bin(code_point)[2:].zfill(16)  # 统一使用16位表示
        ccb_char = binary.replace('0', '鸡').replace('1', '巴')
        ccb_code.append(ccb_char)
    return ''.join(ccb_code)

def ccb_to_text(ccb_code):
    """将鸡py语言的二进制形式转换回文本（统一使用16位解码）"""
    text = []
    i = 0
    while i < len(ccb_code):
        ccb_char = ccb_code[i:i+16]
        if len(ccb_char) != 16:
            break
        binary = ccb_char.replace('鸡', '0').replace('巴', '1')
        char = chr(int(binary, 2))
        text.append(char)
        i += 16
    return ''.join(text)

def compile_and_run_ccb(ccb_code):
    """编译并执行鸡py语言代码"""
    try:
        python_code = ccb_to_text(ccb_code)
        exec(python_code)
    except Exception as e:
        messagebox.showerror("错误", f"编译或运行cbpy代码时出错: {e}")

class CBCompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("鸡py语言编译器")
        
        # 设置主题颜色和字体
        self.bg_color = "#f5f5f5"
        self.accent_color = "#4a6bdf"
        self.text_color = "#333333"
        self.font = ("Segoe UI", 10)
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
    
    def create_widgets(self):
        # 创建标签和输入框
        tk.Label(
            self.root, 
            text="Python代码:", 
            font=self.font, 
            bg=self.bg_color, 
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        
        self.python_code_text = scrolledtext.ScrolledText(
            self.root, 
            width=70, 
            height=10, 
            font=self.font,
            bg="white",
            fg=self.text_color
        )
        self.python_code_text.grid(row=1, column=0, padx=10, pady=5)
        
        tk.Label(
            self.root, 
            text="鸡py代码:", 
            font=self.font, 
            bg=self.bg_color, 
            fg=self.text_color
        ).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        
        self.cb_code_text = scrolledtext.ScrolledText(
            self.root, 
            width=70, 
            height=10, 
            font=self.font,
            bg="white",
            fg=self.text_color
        )
        self.cb_code_text.grid(row=3, column=0, padx=10, pady=5)
        
        # 创建按钮
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
        
        tk.Button(
            button_frame, 
            text="转换为鸡py", 
            command=self.convert_to_cb, 
            width=15,
            font=self.font,
            bg=self.accent_color,
            fg="white",
            relief=tk.FLAT,
            padx=5,
            pady=5
        ).pack(side="left", padx=5)
        
        tk.Button(
            button_frame, 
            text="运行鸡py代码", 
            command=self.run_cb_code, 
            width=15,
            font=self.font,
            bg=self.accent_color,
            fg="white",
            relief=tk.FLAT,
            padx=5,
            pady=5
        ).pack(side="right", padx=5)
        
        file_frame = tk.Frame(self.root, bg=self.bg_color)
        file_frame.grid(row=5, column=0, sticky="ew", padx=10, pady=10)
        
        tk.Button(
            file_frame, 
            text="打开文件", 
            command=self.open_file, 
            width=15,
            font=self.font,
            bg=self.accent_color,
            fg="white",
            relief=tk.FLAT,
            padx=5,
            pady=5
        ).pack(side="left", padx=5)
        
        tk.Button(
            file_frame, 
            text="保存鸡py文件", 
            command=self.save_file, 
            width=15,
            font=self.font,
            bg=self.accent_color,
            fg="white",
            relief=tk.FLAT,
            padx=5,
            pady=5
        ).pack(side="right", padx=5)
    
    def convert_to_cb(self):
        python_code = self.python_code_text.get("1.0", tk.END)
        cb_code = text_to_ccb(python_code)
        self.cb_code_text.delete("1.0", tk.END)
        self.cb_code_text.insert(tk.END, cb_code)
    
    def run_cb_code(self):
        cb_code = self.cb_code_text.get("1.0", tk.END)
        compile_and_run_ccb(cb_code.strip())
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("鸡py文件", "*.jb"), ("所有文件", "*.*")]
        )
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                cb_code = file.read()
                self.cb_code_text.delete("1.0", tk.END)
                self.cb_code_text.insert(tk.END, cb_code)
    
    def save_file(self):
        cb_code = self.cb_code_text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(
            defaultextension=".jb",
            filetypes=[("鸡py文件", "*.cb"), ("所有文件", "*.*")]
        )
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cb_code)
            messagebox.showinfo("成功", f"文件已保存到 {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CBCompilerGUI(root)
    root.mainloop()

