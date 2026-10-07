def angram():
    words=['eat','tea','tan','ate','nat','bat']

    groups={}

    for word in words:
        key=tuple(sorted(word))

        if key in groups:
            groups[key].append(word)

        else:
            groups[key]=[word]
         

    return list(groups.values())

print(angram())
