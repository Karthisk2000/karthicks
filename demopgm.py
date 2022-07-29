books = ['c', 'c++', 'java', 'DSA', 'python', 'rdbms', 'mobile computing',]
#jp = Library(books)

msg = """
      ** 1.Display Book **
      ** 2.Borrow  Book **
      ** 3.Return  Book **
"""
while True:
    print(msg)
    ch = int(input("----- Enter your Choice -------: "))
    if ch == 1:
        jp.listofbooks()
    elif ch == 2:
        book = input("----- Enter Book Name To Borrow:")
        jp.borrowbooks(book)
    elif ch == 3:
        book = input("----- Enter Book Name To Return:")
        jp.receivebook(book)
    else:
        print(" ** Your choice is Incorrect ")
        print(" ** Thank you ** Please come again !!!! ")
