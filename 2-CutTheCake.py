cake = '''
................
.....o..........
................
...............o
................
................
................
.....o..o.....o.
................
................
...o............
................
................
...............o
................
.o..............
'''.strip()
result = [
"""
................
.....o..........

""".strip(),
"""
................
...............o
""".strip(),
"""
........
........
........
.....o..
""".strip(),
"""
....
....
....
o...
....
....
....
....
""".strip(),
"""
....
....
....
..o.
....
....
....
.... 
""".strip(),
"""
........
........
...o....
........
""".strip(),
"""
................
...............o 
""".strip(),
"""
................
.o..............
""".strip()
]

def cut_piece(cake):
    raisins = cake.count("o")
    return raisins

def cut(cake):
    # coding and coding...
    print(cut_piece(cake))
    return []