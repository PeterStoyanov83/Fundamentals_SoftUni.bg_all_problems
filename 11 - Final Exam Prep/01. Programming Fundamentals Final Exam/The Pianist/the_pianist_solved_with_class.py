class Piece:
    def __init__(self, name, composer, key):
        self.name = name
        self.composer = composer
        self.key = key


pieces = []

n = int(input())

for _ in range(n):
    name, composer, key = input().split("|")
    piece = Piece(name, composer, key)
    pieces.append(piece)

data = input()

while data != "Stop":
    split_data = data.split("|")

    if split_data[0] == "Add":
        piece, composer, key, = split_data[1:]

        all_names = [p.name for p in pieces]
        """list comprehension to find the names of all objects in the list """

        if piece in all_names:
            print(f"{piece} is already in the collection!")
        else:
            new_piece = Piece(piece, composer, key)
            """adding the new piece in the list of objects."""
            pieces.append(new_piece)
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif split_data[0] == "Remove":
        piece = split_data[1]
        all_names = [p.name for p in pieces]
        """again getting all the names from the list of objects"""
        if piece not in all_names:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            piece_to_remove = [p for p in pieces if p.name == piece][0]
            """list comprehension to remove the object in the list if it exist in the list
            the list is made of the unique names so the list will contain only one element 
            therefore we remove it from the position [0]"""
            pieces.remove(piece_to_remove)
            print(f'Successfully removed {piece}!')

    elif split_data[0] == "ChangeKey":
        piece, new_key = split_data[1:]
        all_names = [p.name for p in pieces]
        if piece in all_names:
            piece_to_change_key = [p for p in pieces if p.name == piece][0]
            """same procedure as in previous elif"""
            piece_to_change_key.key = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()

for piece in pieces:
    print(f"{piece.name} -> Composer: {piece.composer}, Key: {piece.key}")
