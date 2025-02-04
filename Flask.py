import os
import json
from flask import Flask, render_template_string

app = Flask(__name__)

# Folder z plikami JSON
FOLDER_DANYCH = "dane"

# Szablon HTML do wyświetlania plików
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista plików JSON</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }
        .file-container { background: white; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        h2 { color: #333; }
        pre { background: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>Lista plików JSON</h1>
    {% for file in files %}
        <div class="file-container">
            <h2>{{ file.name }}</h2>
            <pre>{{ file.content }}</pre>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    files_data = []

    # Przejrzyj wszystkie pliki w folderze 'dane'
    if os.path.exists(FOLDER_DANYCH):
        for filename in os.listdir(FOLDER_DANYCH):
            if filename.endswith(".json"):
                file_path = os.path.join(FOLDER_DANYCH, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = json.load(f)
                        formatted_content = json.dumps(content, indent=4, ensure_ascii=False)
                        files_data.append({"name": filename, "content": formatted_content})
                except Exception as e:
                    files_data.append({"name": filename, "content": f"Błąd wczytywania pliku: {e}"})

    return render_template_string(HTML_TEMPLATE, files=files_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
