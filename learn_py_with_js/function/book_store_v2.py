from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 内存数据库
books_db = []
book_id_counter = 0


# 图书模型（用于接收创建图书的请求数据）
class BookCreate(BaseModel):
    title: str
    author: str


# 图书模型（用于返回数据）
class Book(BookCreate):
    id: int


# 获取所有图书
@app.get("/books", response_model=list[Book])
def get_all_books():
    return books_db


# 获取单个图书
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:  # 注意这里改为字典访问
            return book
    return {"error": "Book not found"}


# 添加图书 - 修改为从请求体获取数据
@app.post("/books", response_model=Book)
def add_book(book: BookCreate):  # 参数是 Pydantic 模型类型
    global book_id_counter
    book_id_counter += 1
    # 将图书信息以字典形式存储（更灵活）
    new_book = {
        "id": book_id_counter,
        "title": book.title,
        "author": book.author
    }
    books_db.append(new_book)
    return new_book


# 更新图书
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    for index, b in enumerate(books_db):
        if b["id"] == book_id:
            books_db[index] = {
                "id": book_id,
                "title": book.title,
                "author": book.author
            }
            return books_db[index]
    return {"error": "Book not found"}


# 删除图书
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book["id"] == book_id:
            del books_db[index]
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}
