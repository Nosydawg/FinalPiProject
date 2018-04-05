class cat:
    kind = "Feline"
    

    def __init__(self, a, b):
        self.name = a
        self.breed = b
        self.tricks = []
        self.friends = []

    def addTrick(self, a):
        self.tricks.append(a)

    def addFriend(self, a):
        self.friends.append(a)

    def meow(self):
        print " {}: Meow".format(self.name)


    
##############################################################
cat1 = cat("Leroy", "Tabby")
cat2 = cat("Isabella","Black")
cat3 = cat("Mimi","Calico")
cat4 = cat("Ally", "Tabby")
cat5 = cat("Thomas", "Tabby")

cat1.addTrick("Pounce")
cat2.addTrick("Scratch")
cat3.addTrick("Sunbathe")
cat4.addTrick("Eat")
cat5.addTrick("Sleep")

cat1.addFriend("Chris")
cat2.addFriend("Melissa")
cat3.addFriend("Donald")
cat4.addFriend("Daniel")
cat5.addFriend("Todd")

print "My cat is named {}, it is a {}, it can {}, and their best friend is {}".format(cat1.name, cat1.breed, cat1.tricks, cat1.friends)
print "My cat is named {}, it is a {}, it can {}, and their best friend is {}".format(cat2.name, cat2.breed, cat2.tricks, cat2.friends)
print "My cat is named {}, it is a {}, it can {}, and their best friend is {}".format(cat3.name, cat3.breed, cat3.tricks, cat3.friends)
print "My cat is named {}, it is a {}, it can {}, and their best friend is {}".format(cat4.name, cat4.breed, cat4.tricks, cat4.friends)
print "My cat is named {}, it is a {}, it can {}, and their best friend is {}".format(cat5.name, cat5.breed, cat5.tricks, cat5.friends)

cat1.meow()
cat2.meow()
cat3.meow()
cat4.meow()
cat5.meow()
