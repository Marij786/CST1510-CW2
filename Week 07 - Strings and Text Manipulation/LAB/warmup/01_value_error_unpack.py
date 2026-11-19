# Fixed: maxsplit=1 ensures exactly two pieces even if the value contains "=".
piece = "note=server=east"
key, value = piece.split("=", 1)
print(key, value)
