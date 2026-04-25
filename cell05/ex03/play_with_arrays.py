original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
i = 0
while i < len(original):

    if original[i] > 5:
        value = original[i] + 2
        new.append(value)
    i += 1
newset= set(new)
print("original array", original)
print("new array", newset)