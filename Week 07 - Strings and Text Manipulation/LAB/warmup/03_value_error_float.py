# Fixed: the input must contain a numeric value before float() conversion.
raw_line = "srv-01,used=87,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=", 1)
    print(key.strip(), float(value.strip()))
