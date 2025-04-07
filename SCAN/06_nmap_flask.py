아래는 Flask 기반 Nmap 스캔 대시보드 예제야.
웹브라우저로 접속해서 IP 입력하고, 스캔 결과를 테이블 형태로 확인할 수 있어.

## ✅ 1. 폴더 구조

```bash
NMAP/
├── app.py                  # Flask 실행 파일
└── templates/
    └── result.html         # 결과 출력용 HTML 템플릿
```

## ✅ 2. `app.py`

```python
from flask import Flask, render_template, request
import nmap

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []

    if request.method == 'POST':
        target = request.form['target']
        nm = nmap.PortScanner()
        try:
            nm.scan(hosts=target, arguments='-T4 -F')

            for host in nm.all_hosts():
                host_info = {
                    'ip': host,
                    'status': nm[host].state(),
                    'ports': []
                }

                if 'tcp' in nm[host]:
                    for port, details in nm[host]['tcp'].items():
                        host_info['ports'].append({
                            'port': port,
                            'state': details['state'],
                            'name': details['name']
                        })

                results.append(host_info)
        except Exception as e:
            results.append({'error': str(e)})

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
```

## ✅ 3. `templates/result.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Nmap 스캔 대시보드</title>
    <style>
        body { font-family: sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .host-block { margin-bottom: 40px; }
    </style>
</head>
<body>
    <h1>Nmap 스캔 대시보드</h1>
    <form method="POST">
        <label>스캔할 IP 또는 네트워크 범위:</label>
        <input type="text" name="target" placeholder="예: 30.1.1.0/24" size="30" required>
        <button type="submit">스캔 시작</button>
    </form>

    {% if results %}
        <h2>스캔 결과</h2>
        {% for host in results %}
            {% if host.error %}
                <p style="color:red;">오류: {{ host.error }}</p>
            {% else %}
                <div class="host-block">
                    <h3>Host: {{ host.ip }} ({{ host.status }})</h3>
                    {% if host.ports %}
                        <table>
                            <tr>
                                <th>Port</th>
                                <th>State</th>
                                <th>Service</th>
                            </tr>
                            {% for port in host.ports %}
                                <tr>
                                    <td>{{ port.port }}</td>
                                    <td>{{ port.state }}</td>
                                    <td>{{ port.name }}</td>
                                </tr>
                            {% endfor %}
                        </table>
                    {% else %}
                        <p>열린 TCP 포트 없음.</p>
                    {% endif %}
                </div>
            {% endif %}
        {% endfor %}
    {% endif %}
</body>
</html>
```

## ✅ 4. 실행 방법

```bash
cd ~/PYTHONHOME/NMAP
python3 app.py
```

브라우저에서 접속:  
👉 `http://localhost:5000`


## ✅ 예상 결과 (예시)

| Host         | 상태 | 열린 포트                         |
|--------------|------|----------------------------------|
| 30.1.1.254   | up   | 22 (ssh), 80 (http), 443 (https) |
| 30.1.1.6     | up   | 21 (ftp), 514 (shell)            |


## ✅ 참고사항

- `-F`는 빠른 포트 스캔이므로 모든 포트를 보고 싶다면 `-p-` 또는 `-sV`로 변경 가능
- UDP 스캔은 `-sU` 추가 (속도 느림)
- 보안상 sudo 권한이 필요한 옵션 사용 시 `os.geteuid()` 체크 추가 가능

---

원하면 **부트스트랩 디자인 추가**, **CSV 다운로드 버튼**, **포트별 통계 시각화**도 가능해.  
필요하면 계속 확장해줄게!
