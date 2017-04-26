from InvoiceFactory import InvoiceFactory

i = InvoiceFactory()

def test_file_write():
    dict_to_test = {'test1': 'test1', 'test2': 'test2'}
    i.write_to_file(dict_to_test)

#test_file_write()

def test_read_students():
    i.get_users()

test_read_students()
