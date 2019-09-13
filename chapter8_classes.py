#chapter 8 - classes
#class
class Hotel(object):
    ""виртуальный отель""
    #Звёздность отеля - статический параметр, задающий условия игры
    hotels_conditions = {
        1 : {'room_fee' : 2, 'room_wage' : 1, 'additional_room_cost': 7},
        2 : {'room_fee' : 5, 'room_wage' : 2, 'init_upgrade' : 70, 'upgrade_per_room': 15, 'additional_room_cost': 16},
        3 : {'room_fee' : 10, 'room_wage' : 4, 'init_upgrade' : 170, 'upgrade_per_room': 20, 'additional_room_cost': 30},
        4 : {'room_fee' : 17, 'room_wage' : 8, 'init_upgrade' : 200, 'upgrade_per_room': 30, 'additional_room_cost': 50},
        5 : {'room_fee' : 25, 'room_wage' : 12, 'init_upgrade' : 500, 'upgrade_per_room': 80, 'additional_room_cost': 120}        
        }
    #статически параметр, зависит от коньюнктуры
    max_tourists = 150
    money_amount = 10
    def __init__(self, name, stars = 1, rooms = 10):
        self.__stars = stars #private property
        self.rooms = rooms #public property
        self.__room_fee = __calculate_room_fee()
        self.name = name
    #private method
    def __calculate_room_fee(self):
        return Hotel.hotels_conditions[self.stars]['room_fee']
    #getter for property stars
    @property
    def stars(self):
        return self.__stars
    @stars.setter
    def stars(self, new_stars):
        if new_stars < self.__stars:
            print("")
        else if new_stars > self.__stars:
            needed_money = __calculate_star_money(new_stars)
            if needed_money <= money_amount:
                print("")
            else:
                
            
    def __calculate_star_money(self, new_stars):
        
    def 
    def __str__(self):
        print("Отель '" + name + "'")
        print(" :" + rooms)
        print(" :" + room_fee)
        print(" :" + stars)
