documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(number):
    for doc in documents:
        if number == doc['number']:
            return doc['name']


def list():
    for doc in documents:
        print(doc['type'], doc['number'], doc['name'])
    return doc


def shelf(s):
    for dir in directories.items():
        if s in dir[1]:
            return dir[0]


def add():
    a = input("Тип, номер, имя, полку(Через запятую) ").split(", ")
    if a[3] in directories.keys():
        documents.append({"type": a[0], "number": a[1], "name": a[2]})
        directories[a[3]].append(a[1])
        print(documents)
        print(directories)
    elif a[3] not in directories.keys():
        directories[a[3]] = []
        documents.append({"type": a[0], "number": a[1], "name": a[2]})
        directories[a[3]].append(a[1])
        print(documents)
        print(directories)

