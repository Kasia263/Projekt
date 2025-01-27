import os
import json
from flask import Flask, render_template_string

app = Flask(__name__)

def load_json_files(directory):
    data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = json.load(f)
                        data.append(content)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    return data

@app.route('/')
def index():
    json_data = load_json_files(os.path.dirname(os.path.abspath(__file__)))
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wyświetlanie danych JSON</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Dane z plików JSON</h1>
        <div id="data-container"></div>

        <script>
            const jsonData = {{ json_data|tojson }};
            const container = document.getElementById('data-container');

            jsonData.forEach(item => {
                const table = document.createElement('table');
                const headerRow = document.createElement('tr');
                const headers = ['Parameter', 'Value'];
                headers.forEach(header => {
                    const th = document.createElement('th');
                    th.textContent = header;
                    headerRow.appendChild(th);
                });
                table.appendChild(headerRow);

                Object.keys(item).forEach(key => {
                    if (key !== 'values') {
                        const row = document.createElement('tr');
                        const cell = document.createElement('td');
                        cell.textContent = key;
                        row.appendChild(cell);
                        const valueCell = document.createElement('td');
                        valueCell.textContent = item[key];
                        row.appendChild(valueCell);
                        table.appendChild(row);
                    }
                });

                item.values.forEach(value => {
                    const row = document.createElement('tr');
                    Object.keys(value).forEach(key => {
                        const cell = document.createElement('td');
                        cell.textContent = key;
                        row.appendChild(cell);
                        const valueCell = document.createElement('td');
                        valueCell.textContent = value[key];
                        row.appendChild(valueCell);
                    });
                    table.appendChild(row);
                });

                container.appendChild(table);
            });
        </script>
    </body>
    </html>
    ''', json_data=json_data)

if __name__ == '__main__':
    app.run(debug=True)
