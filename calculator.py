import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # 계산식과 결과를 저장할 변수
        self.current = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.create_widgets()
        
    def create_widgets(self):
        # 디스플레이
        display = ttk.Entry(
            self.root,
            textvariable=self.display_var,
            justify="right",
            font=("Arial", 20)
        )
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # 버튼 스타일 설정
        style = ttk.Style()
        style.configure("TButton", padding=5, font=("Arial", 12))
        
        # 버튼 텍스트와 위치
        buttons = [
            ('C', 1, 0), ('←', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2, 2)  # 마지막 2는 columnspan
        ]
        
        # 버튼 생성
        for button in buttons:
            if len(button) == 4:  # '=' 버튼의 경우
                text, row, col, colspan = button
                btn = ttk.Button(
                    self.root,
                    text=text,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")
            else:
                text, row, col = button
                btn = ttk.Button(
                    self.root,
                    text=text,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        
        # 그리드 가중치 설정
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value == 'C':
            self.current = ""
            self.display_var.set("0")
        elif value == '←':
            self.current = self.current[:-1]
            self.display_var.set(self.current if self.current else "0")
        elif value == '=':
            try:
                # % 기호를 /100으로 변환
                expression = self.current.replace('%', '/100')
                result = eval(expression)
                # 결과가 정수면 정수로, 소수면 소수점 8자리까지 표시
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)
                self.display_var.set(result)
                self.current = str(result)
            except:
                self.display_var.set("Error")
                self.current = ""
        else:
            self.current += value
            self.display_var.set(self.current)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop() 