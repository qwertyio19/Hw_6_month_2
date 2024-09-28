""" Домашнее задание """

" 1 "
import sqlite3

connect = sqlite3.connect("Wizards.db")
cursor = connect.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS wizards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20),
        age INTEGER,
        house VARCHAR (20),
        magic_level INTEGER, 
        special_ability VARCHAR (50)
    )
""")

connect.commit()





" 2 "
def add_wizards():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    house = input("Укажите дом: ")
    magic_level = int(input("Укажите уровень мага: "))
    special_ability = input("Уникальная способность мага: ")
    
    cursor.execute("""INSERT INTO wizards
                   (name, age, house, magic_level, special_ability)
                   VALUES (?, ?, ?, ?, ?)""", (name, age, house, magic_level, special_ability))
    connect.commit()

# add_wizards()    
    
   
   
    
" 3 "
def find_wizard_by_ability(special_ability):
    cursor.execute("""SELECT * FROM wizards WHERE special_ability = ? """, (special_ability,))
    abilitys = cursor.fetchall()
    
    print(abilitys)
    
find_wizard_by_ability(special_ability = "Физическая сила")
 
 
 
 
    
" 4 "
def lift_wizards_by_house(house):
    cursor.execute("""SELECT * FROM wizards WHERE house = ?""", (house,))
    house = cursor.fetchall()
    
    print(house)
    
# lift_wizards_by_house(house = "")





" 5 "
def update_magic_level(wizard_id, new_level):
    cursor.execute("""UPDATE wizards
                   SET magic_level = ?
                   WHERE id = ?
                   """, (new_level, wizard_id))
    
    connect.commit()
    print(f"Маг по ID {wizard_id} обновлён на {new_level}.")
    
# update_magic_level(3,1)






" 6 "
def delete_wizard(wizard_id):
    cursor.execute("""DELETE FROM wizards
                   WHERE id = ?
                   """, (wizard_id,))
    
    connect.commit()
    print(f"Маг с ID {wizard_id} был удален.")
    
# delete_wizard(4)