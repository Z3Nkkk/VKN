import random as r

class Bookshelf:

    book_name = ""
    book_list = []
    mixed_book_list = []
    def init(self, b_n):
        self.book_name = str(b_n)
        self.book_list.append(b_n)
    def del_book (self, b_n):
        self.book_list.remove(b_n)
        return(self.book_list)
    def get_book_list(self):
        return(self.book_list)
    def mix(self):
        lmbl = len(self.mixed_book_list)
        lbl = len(self.book_list)
        while lbl != lmbl:
            ind = r.randint(0,lbl-1)
            el = self.book_list[ind]
            if el not in self.mixed_book_list:
                self.mixed_book_list.append(el)
                lmbl = len(self.mixed_book_list)
    def get_mix(self):
        return(self.mixed_book_list)
    


bs = Bookshelf()
bs.init( "Віталій")
bs.init( "Олег")
bs.init( "Євгеній")
bs.init( "Олександр")
bs.init( "Андрій")
bs.init( "Вадим")
bs.init( "Олексій")
bs.init( "Анатолій")
print(bs.get_book_list())
bs.del_book("Євгеній")
bs.mix()
print(bs.get_mix())
