"""
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
"""

film = {
    'title' : 'Edge of Tomorrow',
    'director' : 'Unknown',
    'year' : 2013,
    'budget' : 100500,
    'main actor' : 'Tom Cruz',
    'slogan' : 'not aplicable'
}

print(film)
print(film.keys())
print(film.values())
print(film.items())