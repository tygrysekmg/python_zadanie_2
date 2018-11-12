data=[1, 2, 3, 1, 2, 5, 6, 7, 8]
uni_data=[]
for dat in data:
    if dat not in uni_data:
        uni_data.append(dat)

print(uni_data) 