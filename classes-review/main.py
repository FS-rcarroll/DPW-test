#this is an import statement
import webapp2

#this is my applications main class
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        yoda = Character()
        yoda.name = "Yoda"
        yoda.age = -7
        yoda.gender = "Male"
        yoda.occupation = "Jedi Master"
        yoda.print_info()
        #instance.attributes
        #instance.method()
        #instance.property

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.gender = "Male"
        luke.age = 23
        luke.occupation = "Jedi Knight"
        luke.print_info()

        leia = Character()
        leia.name = "Leia Organa"
        leia.gender = "Female"
        leia.occupation = "Princess"
        leia.age = luke.age

        leia.squad_no = "Purple 10"
        #print leia.squad_no

#this is my data object class
class Character(object):
    def __init__(self): #constructor function
        self.name = ""
        self.__age = 0
        self.occupation = ""
        self.gender = ""
        self.__rogue_squadron_no = "DEFAULT"

    def print_info(self):
        print self.name + " is a(n) " + self.occupation

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        #validation
        if new_age < 0 or new_age > 1000:
            print "Error with age input!!!!!!"
        else:
            self.__age = new_age


    #PROVIDES READ ACCESS
    @property
    def squad_no(self):
        return self.__rogue_squadron_no

    #PROVIDES WRITE ACCESS
    @squad_no.setter
    def squad_no(self, new_no):
        #validation
        if new_no == "Pink 5":
            new_no = "Red 5"
        #showing info - more code at once!
        print new_no
        self.__rogue_squadron_no = new_no



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
