import json


def main():
    with open('chips.csv', 'r') as f:
        data = f.read()

    raw_types = [
        t.split('\n') for t in data.split('$$TYPE$$') if t != '\n'
    ]

    items = []
    for t in raw_types:
        type_name = t[0].strip()

        print(type_name)
        raw_items = [item.split('\t') for item in t[1:] if item != '\n']

        for item in raw_items:
            if len(item) != 4:
                continue

            (name, oz, upc, case) = item
            items.append({'type': type_name, 'name': name,
                          'oz': oz, 'upc': upc, 'case': case})

    with open('chips.json', 'w') as f:
        json.dump(items, f, indent=2)


if __name__ == "__main__":
    main()
