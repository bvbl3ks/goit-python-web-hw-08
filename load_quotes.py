import json
from models import Author, Quote

# Открываем JSON с цитатами
with open("quotes.json", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    # ищем автора в базе
    author = Author.objects(fullname=item["author"]).first()
    if not author:
        continue  # если автора нет — пропускаем

    # сохраняем цитату с ReferenceField на автора
    Quote(
        tags=item["tags"],
        author=author,
        quote=item["quote"]
    ).save()

print("Quotes loaded")
