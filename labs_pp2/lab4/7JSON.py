import json
import os
file_path = os.path.join(os.path.dirname(__file__), "sample-data.json")
with open(file_path) as file:
    data = json.load(file)

# Заголовок таблицы
header = "Interface Status"
separator = "=" * 80
columns = f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}"
divider = "-" * 80

# Вывод заголовков
print(header)
print(separator)
print(columns)
print(divider)

# Вывод данных
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else " " * 20
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
