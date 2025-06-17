import json, operator

dataDef = {
    "Enemy health": [0, 0],
    "Player health": [20, 20],
    "Health potions": [6, 6],
    "MP potions": [6, 6],
    "MP": [15, 15],
    "Loadout": [1, 1, 1],
    "Triggers": [0, 0, 0, 0, 0],
    "XP": [0, 20, 1]
}
enemiesDef = {
    "Bob": ["Bob", 40, 1, 6, 40, 40],
    "Linda": ["Linda", 16, 2, 7, 50, 50]
}
movesDef = {
    "Sword": [8, 60],
    "Dagger": [4, 80],
    "Great Axe": [12, 30],
    "Shield": [5, 1],
    "Agility": [10, 1],
    "Rage": [0],
    "Fireball": [4, 0, 80]   
}
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "**": operator.pow
}

#Data file functions

def resetData():
    with open("data.json", "w") as f:
        json.dump(dataDef, f, indent = 4)
        f.close()

def setData(classS: str, object: int, value):
    with open("data.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("data.json", "w") as f:
        temp = data[classS]
        temp[object] = value
        data[classS] = temp
        f.seek(0)
        json.dump(data, f, indent = 4)

def manipData(classS: str, object: int, value: int, operator: str):
    with open("data.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("data.json", "w") as f:
        temp = data[classS]
        temp[object] = operators[operator](temp[object], value)
        data[classS] = temp
        f.seek(0)
        json.dump(data, f, indent = 4)

def readData(classS: str, object: int):
    with open("data.json", "r") as f:
        data = json.load(f)
        data = data[classS]
        return data[object]

#Enemy file functions

def resetEnemy():
    with open("enemies.json", "w") as f:
        json.dump(enemiesDef, f, indent=4)
        f.close()

def setEnemy(classS: str, object: int, value):
    with open("enemies.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("enemies.json", "w") as f:
        temp = data[classS]
        temp[object] = value
        data[classS] = temp
        f.seek(0)
        json.dump(data, f, indent = 4)

def manipEnemy(classS: str, object: int, value: int, operator: str):
    with open("enemies.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("enemies.json", "w") as f:
        temp = data[classS]
        temp[object] = operators[operator](temp[object], value)
        data[classS] = temp
        f.seek(0)
        json.dump(data, f, indent = 4)

def readEnemy(classS: str, object: int):
    with open("enemies.json", "r") as f:
        data = json.load(f)
        data = data[classS]
        return data[object]
    
#Move file functions

def resetMove():
    with open("moves.json", "w") as f:
        json.dump(movesDef, f, indent=4)
        f.close()

def setMove(classS: str, object: int, value):
    with open("moves.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("moves.json", "w") as f:
        temp = data[classS]
        temp[object] = value
        data[classS] = temp
        f.seek(0)
        json.dump(data, f, indent = 4)

def manipMove(classS: str, object: int, value: int, operator: str):
    with open("moves.json", "r") as f:
        data = json.load(f)
        f.close()
    with open("moves.json", "w") as f:
        temp = data[classS]
        temp[object] = operators[operator](temp[object], value)
        data[classS] = temp
        f.seek(0)
        json.dump(data, f, indent = 4)

def readMove(classS: str, object: int):
    with open("moves.json", "r") as f:
        data = json.load(f)
        data = data[classS]
        return data[object]