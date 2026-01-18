import json
from models import Author

# Открываем JSON с авторами
with open("authors.json", encoding="utf-8") as f:
    data = json.load(f)

# Сохраняем авторов в базу
for item in data:
    Author(
        fullname=item["fullname"],
        born_date=item["born_date"],
        born_location=item["born_location"],
        description=item["description"]
    ).save()

print("Authors loaded")
