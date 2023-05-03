title = "This program will draw a rectangle for you."
underlined_title = "\x1B[4m" + title + "\x1B[0m"
print(underlined_title)
rows = int(input("\nHow many rows do you want to draw? "))
if rows < 1 or rows > 100:
    rows = int(input("Sorry rows need to be between 1 and 100 .\n Try again: "))
else:
    print(f'Your rectangle will have {rows} rows!')

columns = int(input("How many columns do you want to draw? "))

if columns < 1 or columns > 100:
    print(int(input("Sorry rows need to be between 1 and 100 .\n Try again: ")))
    columns = int(input("Sorry rows need to be between 1 and 100 "))
else:
    print(f'Your rectangle will have {columns} rows!')

symbol = str(input("What symbol do you want to use? "))
if len(symbol) == 1:
    print(f'The rectangle will be made from {symbol} ')
else:
    print(str(input("Sorry only one symbol is allowed? Try again!")))

index_rows = index_columns = 0

while index_rows != rows:
    print(symbol * columns)
    index_rows += 1


