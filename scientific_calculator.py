import tkinter as tk
from tkinter import ttk
import math
import numpy as np

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("공학용 계산기")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # 계산식과 결과를 저장할 변수
        self.current = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.angle_mode = "DEG"  # 각도 모드 (DEG/RAD)
        
        self.create_widgets()
        
    def create_widgets(self):
        # 디스플레이
        display_frame = ttk.Frame(self.root)
        display_frame.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
        
        # 각도 모드 표시
        self.mode_label = ttk.Label(display_frame, text=self.angle_mode, font=("Arial", 10))
        self.mode_label.pack(side=tk.LEFT, padx=5)
        
        display = ttk.Entry(
            display_frame,
            textvariable=self.display_var,
            justify="right",
            font=("Arial", 20)
        )
        display.pack(fill=tk.BOTH, expand=True, padx=5)
        
        # 버튼 스타일 설정
        style = ttk.Style()
        style.configure("TButton", padding=5, font=("Arial", 12))
        
        # 버튼 텍스트와 위치
        buttons = [
            # 첫 번째 줄
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('DEG/RAD', 1, 3), ('C', 1, 4),
            # 두 번째 줄
            ('asin', 2, 0), ('acos', 2, 1), ('atan', 2, 2), ('(', 2, 3), (')', 2, 4),
            # 세 번째 줄
            ('x²', 3, 0), ('√', 3, 1), ('x^y', 3, 2), ('log', 3, 3), ('ln', 3, 4),
            # 네 번째 줄
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), ('←', 4, 4),
            # 다섯 번째 줄
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3), ('π', 5, 4),
            # 여섯 번째 줄
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3), ('e', 6, 4),
            # 일곱 번째 줄
            ('0', 7, 0), ('.', 7, 1), ('±', 7, 2), ('+', 7, 3), ('=', 7, 4)
        ]
        
        # 버튼 생성
        for text, row, col in buttons:
            btn = ttk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.button_click(t)
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        
        # 그리드 가중치 설정
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value == 'C':
            self.current = ""
            self.display_var.set("0")
        elif value == '←':
            self.current = self.current[:-1]
            self.display_var.set(self.current if self.current else "0")
        elif value == 'DEG/RAD':
            self.angle_mode = "RAD" if self.angle_mode == "DEG" else "DEG"
            self.mode_label.config(text=self.angle_mode)
        elif value == '=':
            try:
                # 특수 상수 처리
                expression = self.current.replace('π', str(math.pi)).replace('e', str(math.e))
                
                # 삼각함수 처리
                if self.angle_mode == "DEG":
                    expression = expression.replace('sin', 'math.sin(math.radians')
                    expression = expression.replace('cos', 'math.cos(math.radians')
                    expression = expression.replace('tan', 'math.tan(math.radians')
                    expression = expression.replace('asin', 'math.degrees(math.asin')
                    expression = expression.replace('acos', 'math.degrees(math.acos')
                    expression = expression.replace('atan', 'math.degrees(math.atan')
                else:
                    expression = expression.replace('sin', 'math.sin')
                    expression = expression.replace('cos', 'math.cos')
                    expression = expression.replace('tan', 'math.tan')
                    expression = expression.replace('asin', 'math.asin')
                    expression = expression.replace('acos', 'math.acos')
                    expression = expression.replace('atan', 'math.atan')
                
                # 기타 함수 처리
                expression = expression.replace('x²', '**2')
                expression = expression.replace('√', 'math.sqrt')
                expression = expression.replace('x^y', '**')
                expression = expression.replace('log', 'math.log10')
                expression = expression.replace('ln', 'math.log')
                
                # 괄호 닫기 추가
                if expression.count('(') > expression.count(')'):
                    expression += ')' * (expression.count('(') - expression.count(')'))
                
                result = eval(expression)
                
                # 결과가 정수면 정수로, 소수면 소수점 8자리까지 표시
                if isinstance(result, (int, float)):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 8)
                
                self.display_var.set(result)
                self.current = str(result)
            except Exception as e:
                self.display_var.set("Error")
                self.current = ""
        elif value == '±':
            try:
                if self.current and self.current[0] == '-':
                    self.current = self.current[1:]
                else:
                    self.current = '-' + self.current
                self.display_var.set(self.current)
            except:
                pass
        else:
            self.current += value
            self.display_var.set(self.current)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop() 