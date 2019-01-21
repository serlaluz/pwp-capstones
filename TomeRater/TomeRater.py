class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = dict()

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email address has been updated")

    def __repr__(self):
        print("User"  + str(self.name) + ", email: " + str(self.email) + ", books read \n: " + str(len(self.books.keys())))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, books, rating=None):
        if rating is not None:
            self.books[books] = rating 

    def get_average_ratings(self):
        if len(self.books.values()) == 0:
            return 0
        else:
            sum = 0.0
            element = 0
            for value in self.books.values():
                if value is not None:
                    sum += value
                    element += 1
            return sum / element
            

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = list()

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn 

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISNB has been updated")

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
        
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    
    def get_average_rating(self):
        if len(self.ratings) == 0:
                return 0
        else:
                sum = 0.0
                element = 0
                for value in self.ratings:
                    if value is not None:
                        sum += value
                        element += 1
                return sum / element
    
    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return '{title} by {author}'.format(title = self.title, author = self.author)

class Non_fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
    
    def __repr__(self):
        return ' {title}, a {level} manual on {subject}'.format(title = self.title, level = self.level, subject = self.subject)

class TomeRater():
    def __init__(self):
        self.users = dict()
        self.books = dict()
    
    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_fiction(title, subject, level, isbn)
        return non_fiction
    
    def add_book_to_user(self, book, email, rating=None):
        if not email in self.users:
            return "No users with email {email}".format(email = email)
        else:
            user = self.users[email]
            user.read_book(book, rating)
            if not book in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
    
    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book.get_title())
    
    def print_users(self):
        for user in self.users:
           user.__repr__()

    def most_read_book(self):
        book_most = " "
        view_most = 0
        for (book, view) in self.books.items():
            if view >= view_most:
                view_most = view
                book_most = book.get_title()
        print(book_most + ", " + view_most)

    def highest_rated_book(self): 
        highest_book = " "
        highest_book_average = 0
        for book in self.books.keys():
            if book.get_average_rating() >= highest_book_average:
                highest_book_average = book.get_average_rating()
                highest_book = book.get_title()
        print(highest_book)
    
    def most_positive_user(self):
        most_positive_user = " "
        highest_average_rating = 0
        for user in self.users.values():
            if user.get_average_rating() >= highest_average_rating:
                highest_average_rating = user.get_average_rating()
                most_positive_user = user.__repr__
        print(most_positive_user)
                 

