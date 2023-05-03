book_search = input()
book_num = 0
book_checked = input()

while book_checked != book_search and book_checked != "No More Books":
    book_num += 1
    book_checked = input()

if book_checked == "No More Books":
    print('The book you search is not here!')
    print(f'You checked {book_num} books.')
    quit()
if book_checked == book_search:
    print(f'You checked {book_num} books and found it.')
    quit()

