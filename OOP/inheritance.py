# single inheritance


# class synnfeo:
#     def __init__(s):
#         print("register")
#     def python(s):
#         print("python")
#     def mern():
#         print("mern")

# class novavi(synnfeo):
#     def dm(self):
#         print("dm")
#     def web_dev(self)    :
#         print("web_dev")


# manu=novavi()
# manu.python()
# manu.web_dev()

# multiple inheritance

# class synnfeo:
#     def __init__(s):
#         print("register")
#     def python(s):
#         print("python")
#     def mern():
#         print("mern")

# class novavi():
#     def dm(self):
#         print("dm")
#     def web_dev(self):
#         print("web_dev")

# class std(synnfeo,novavi):
    # def reg(self):
    #     print("std reg")



# manu=std()
# manu.python()
# manu.web_dev()
# manu.reg()

# multi level inheritance

# class college:
    # def __init__(s):
    #     print("register")
    # def python(s):
    #     print("python")
    # def mern():
    #     print("mern")


# class department():
#     def bca(self):
#         print("bca")
#     def bcom(self):
#         print("b.com")


# class std(college,department):
    # def reg(self):
    #     print("std reg")



# manu=std()
# manu.python()
# manu.bca()
# manu.reg()

# heiarchial inheritance

# class synnfeo:
    # def __init__(s):
        # print("register")
    # def python(s):
        # print("python")
    # def mern():
        # print("mern")
# 
# class novavi(synnfeo):
    # def dm(self):
        # print("dm")
    # def web_dev(self):
        # print("web_dev")

# class std(synnfeo):
    # def reg(self):
        # print("std reg")



# manu=std()
# sanu=novavi()
# sanu.python()
# manu.python()
# manu.reg()
# 

# hybrid inheritance

# class A:
    # def a1(self):
        # print("a1")
# class B:
    # def b1(self):
        # print("b1")
# class F:
    # def f1(self):
        # print("f1")        
# class C(A,B):
    # def c1(self):
        # print("c1")        
# class D(B,F):
    # def d1(self):
        # print("d1")    
# class E(C,D):
    # def e1(self):
        # print("e1")
# 
# e_obj=E()        
# e_obj.b1()
# 
# d_obj=D()
# d_obj.b1()
# 
# b_obj=B()
# b_obj.b1()

# Q1single inheritance

# Parent class
class BakeryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price:.2f}")

# Child class inheriting from BakeryItem
class Pastry(BakeryItem):
    def __init__(self, name, price, filling):
        super().__init__(name, price)
        self.filling = filling

    def display_info(self):
        super().display_info()
        print(f"Filling: {self.filling}")

# Creating an instance of Pastry
croissant = Pastry("Croissant", 2.50, "Butter")
croissant.display_info()

# Q2.mutiple inheritance

# Parent class 1
class Dessert:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price:.2f}")

# Parent class 2
class BakeryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price:.2f}")

# Child class inheriting from both Dessert and BakeryItem
class Cake(Dessert, BakeryItem):
    def __init__(self, name, price, layers):
        Dessert.__init__(self, name, price)
        BakeryItem.__init__(self, name, price)
        self.layers = layers

    def display_info(self):
        super().display_info()
        print(f"Layers: {self.layers}")

# Creating an instance of Cake
birthday_cake = Cake("Chocolate Cake", 35.00, 3)
birthday_cake.display_info()

# 3.multi level inheritance

# Grandparent class
class BakeryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price:.2f}")

# Parent class inheriting from BakeryItem
class Bread(BakeryItem):
    def __init__(self, name, price, loaf_size):
        super().__init__(name, price)
        self.loaf_size = loaf_size

    def display_info(self):
        super().display_info()
        print(f"Loaf Size: {self.loaf_size}")

# Child class inheriting from Bread
class Baguette(Bread):
    def __init__(self, name, price, loaf_size, crust_type):
        super().__init__(name, price, loaf_size)
        self.crust_type = crust_type

    def display_info(self):
        super().display_info()
        print(f"Crust Type: {self.crust_type}")

# Creating an instance of Baguette
baguette = Baguette("French Baguette", 3.50, "Large", "Crispy")
baguette.display_info()


# 4.heiarchial

# Parent class
class BakeryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price:.2f}")

# Child class 1 inheriting from BakeryItem
class Bread(BakeryItem):
    def __init__(self, name, price, loaf_size):
        super().__init__(name, price)
        self.loaf_size = loaf_size

    def display_info(self):
        super().display_info()
        print(f"Loaf Size: {self.loaf_size}")

# Child class 2 inheriting from BakeryItem
class Pastry(BakeryItem):
    def __init__(self, name, price, filling):
        super().__init__(name, price)
        self.filling = filling

    def display_info(self):
        super().display_info()
        print(f"Filling: {self.filling}")

# Creating instances of Bread and Pastry
baguette = Bread("French Baguette", 3.50, "Large")
croissant = Pastry("Croissant", 2.50, "Butter")

# Displaying information
print("--- Baguette Info ---")
baguette.display_info()

print("\n--- Croissant Info ---")
croissant.display_info()

#  5.hybrid in heritance       

# Parent class 1
class BakeryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price:.2f}")

# Parent class 2
class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def display_recipe(self):
        print("Ingredients:", ', '.join(self.ingredients))

# Child class inheriting from BakeryItem and Recipe
class Cake(BakeryItem, Recipe):
    def __init__(self, name, price, ingredients, layers):
        BakeryItem.__init__(self, name, price)
        Recipe.__init__(self, ingredients)
        self.layers = layers

    def display_info(self):
        super(BakeryItem, self).display_info()
        self.display_recipe()
        print(f"Layers: {self.layers}")

# Creating an instance of Cake
birthday_cake = Cake("Chocolate Cake", 35.00, ["Chocolate", "Flour", "Sugar"], 3)

# Displaying information
print("--- Birthday Cake Info ---")
birthday_cake.display_info()
