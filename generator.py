import json
from jinja2 import Template

# Wczytanie definicji
with open('interface.json', 'r') as f:
    data = json.load(f)

# Wczytanie szablonu
with open('template.j2', 'r') as f:
    template = Template(f.read())

# Generowanie kodu
output = template.render(data)

with open('generated_code.py', 'w') as f:
    f.write(output)

print("Kod został wygenerowany w pliku generated_code.py")