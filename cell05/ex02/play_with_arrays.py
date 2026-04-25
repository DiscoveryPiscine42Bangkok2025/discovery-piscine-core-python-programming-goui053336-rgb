original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

i = 0
while i < len(original):
    if original[i] > 5:
        new.append(original[i] + 2)
    i += 1

print("Original array:", original)
print("New array:", new)