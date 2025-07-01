#Extract car names from this text: txt = 'LMaasleitbtui'
txt = 'LMaasleitbtui'

if txt:
    car1 = txt[::2]
    car2 = txt[1::2]
    print("First car name:", car1)
    print("Second car name:", car2)
else:
    print("No car name found.")