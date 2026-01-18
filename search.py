import re
from models import Author, Quote

def search_by_name(name):
    regex = re.compile(f"^{re.escape(name)}", re.IGNORECASE)
    authors = Author.objects(fullname=regex)
    results = []
    for author in authors:
        quotes = Quote.objects(author=author)
        for q in quotes:
            results.append(f"{author.fullname}: {q.quote}")
    return results

def search_by_tag(tag):
    regex = re.compile(f"^{re.escape(tag)}", re.IGNORECASE)
    quotes = Quote.objects(tags=regex)
    results = [f"{q.author.fullname}: {q.quote}" for q in quotes]
    return results

def search_by_tags(tags_list):
    quotes = Quote.objects(tags__in=tags_list)
    results = [f"{q.author.fullname}: {q.quote}" for q in quotes]
    return results

def main():
    print("Пошук цитат. Формати команд:\n"
          "name:ім'я_автора\n"
          "tag:тег\n"
          "tags:тег1,тег2\n"
          "exit - выход\n")

    while True:
        command = input("Введіть команду: ").strip()
        if command.lower() == "exit":
            break

        if command.startswith("name:"):
            name = command[5:].strip() 
            results = search_by_name(name)
        elif command.startswith("tag:"):
            tag = command[4:].strip()
            results = search_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command[5:].split(",")
            results = search_by_tags(tags)
        else:
            print("Невірна команда")
            continue

        if results:
            print("\n".join(results))
        else:
            print("Нічого не знайдено")

if __name__ == "__main__":
    main()
