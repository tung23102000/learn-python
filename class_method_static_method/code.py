# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
#     @staticmethod
#     def static_method():
#         print("Call static_method")
    
# #khởi tạo đối tượng
# test = ClassTest()
# # #c1:
# # test.instance_method()
# # #c2:
# # ClassTest.instance_method(test)


# #sd classmethod thì k cần khởi tạo 1 đối tượng như trên để truy cập 
# ClassTest.class_method()



class Book:
    TYPES=("hardcover","paperback") #class attributes
    def __init__(self,name,book_type,weight): 
        self.name= name #self.name,book_type,weight are instance attributes
        self.book_type= book_type
        self.weight= weight
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight={self.weight} g>"
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)
    
    @classmethod
    def tostring(cls):
        print('Book Class Type Attributes: type=',cls.TYPES[0])
# print(Book.TYPES)
# book = Book("HP","hardcover",1500) #khởi tạo đối tượng instant sử dụng __init__

book = Book.hardcover("HP", 1500)
typeofBook = Book.tostring()
print(book)