======= tkinter 기반 GUI Nmap 결과 출력 예제 =========
아래 코드는 네트워크 스캔 결과를 표 형태(GUI)로 표시한다.

import nmap
import tkinter as tk
from tkinter import ttk

# 스캔 함수 정의
def scan():
    target = entry.get()
    nm = nmap.PortScanner()
    output_text.delete(*output_text.get_children())  # 기존 결과 초기화

    result_label.config(text=f"스캔 중: {target}")
    root.update()  # GUI 업데이트

    nm.scan(target, arguments='-T4 -F')

    for host in nm.all_hosts():
        status = nm[host].state()
        ports = []

        if 'tcp' in nm[host]:
            for port, details in nm[host]['tcp'].items():
                ports.append(f"{port} ({details['name']}) - {details['state']}")

        ports_str = ', '.join(ports) if ports else 'No TCP ports found.'
        output_text.insert('', 'end', values=(host, status, ports_str))

# GUI 구성
root = tk.Tk()
root.title("Nmap 스캔 결과")
root.geometry("800x400")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="스캔할 IP 범위 또는 네트워크 주소:").pack(side='left')
entry = tk.Entry(frame, width=40)
entry.pack(side='left', padx=5)
entry.insert(0, "30.1.1.0/24")
tk.Button(frame, text="스캔 시작", command=scan).pack(side='left')

result_label = tk.Label(root, text="스캔 결과 없음")
result_label.pack(pady=5)

# 결과 출력 테이블
columns = ('IP 주소', '상태', '열린 TCP 포트')
output_text = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    output_text.heading(col, text=col)
    output_text.column(col, width=200 if col != '열린 TCP 포트' else 400)
output_text.pack(fill='both', expand=True)

root.mainloop()
