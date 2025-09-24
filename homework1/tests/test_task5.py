import src.task5 as task5
#basic test, asserts the  books title
def test_books_list():
    assert isinstance(task5.books, list)
    assert task5.books[0]["title"] == "Book A"
    assert len(task5.books[:3]) == 3

def test_students_dict():
    assert isinstance(task5.students, dict)
    assert task5.students["Alice"] == 1001

