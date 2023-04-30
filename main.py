import json


def z1():
    with open ("products.json",'r',encoding='utf-8') as file:
        data = json.load(file)

    p = {
        "name": input("Введите цену продукта"),
        "price": input("Введите название продукта"),
        "available": input("есть ли продукт в наличии(да или нет)") == "да",
        "weight": input("Введите вес продукта")
    }
    data["products"].append(p)

    with open ("products.json", "w",encoding='utf-8') as file:
        json.dump(data,file,indent=2)

    for product in data["products"]:
        print("название:", product["name"])
        print("цена:", product["price"])
        print("вес:", product["weight"])
        if product["available"]:
            print("есть в наличии")
        else:
            print("нет в наличии")
        print()
z1()

def z3():
    with open ("slovari.txt","r") as file:
        l = file.readlines()

    d = {}

    for line in l:
        eng = line.split(" - ")[0].strip()
        ru = line.split(" - ")[1].strip().split(', ')
        for word in ru:
            if word not in d:
                d[word] = [eng]
            else:
                d[word].append(eng)
    with open("ru-slovari.txt","w") as file:
        for ru,eng in sorted(d.items()):
            file.write(f"{ru} - {', '.join(eng)}\n")

z3()