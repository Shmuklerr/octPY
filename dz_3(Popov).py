class Kitchen:
    content = []

    def __init__(self, init_content):
        self.content = init_content

    def room_content(self):
        print('KITCHEN contains:')
        for item in self.content:
            print(f'\t{item.use_for()}')


class Furniture:
    name = None
    usage = None

    def __init__(self, init_name, init_usage):
        self.name = init_name
        self.usage = init_usage

    def __str__(self):
        return self.name.upper()

    def use_for(self):
        return f'{self.name.upper()} ({self.usage})'


class KitchenAppliances:
    name = None
    usage = None
    powered = None

    def __init__(self, init_name, init_usage, init_powered):
        self.name = init_name
        self.usage = init_usage
        self.powered = init_powered

    def __str__(self):
        return self.name.upper()

    def use_for(self):
        return f'{self.name.upper()} ({self.usage}, {self.powered})'


class StorageEquipment(KitchenAppliances):
    storage = []  # storage space - list
    temp = None

    def __init__(self, init_name, init_usage, init_powered, init_storage, init_temp):
        self.name = init_name
        self.usage = init_usage
        self.powered = init_powered
        self.storage = init_storage
        self.temp = init_temp

    def temperature(self):
        print(f'{self.name.upper()} keeps temperature about {self.temp}°C.')

    def content(self):
        print(f'{self.name.upper()} contains:')
        for prod in self.storage:
            print('\t', prod)

    def food_lifetime_calc(self):
        if 0 < self.temp <= 5:
            for food in self.storage:
                food.lifetime *= 2.5
                print(f'Lifetime of {food} in {self.name.upper()} is {food.lifetime} days')
        elif -10 < self.temp < 0:
            for food in self.storage:
                food.lifetime *= 5
                print(f'Lifetime of {food} in {self.name.upper()} is {food.lifetime} days')


class CookingEquipment(KitchenAppliances):

    def __init__(self, init_name, init_usage, init_powered):
        self.name = init_name
        self.usage = init_usage
        self.powered = init_powered


class Tool(KitchenAppliances):

    def __init__(self, init_name, init_usage, init_powered):
        self.name = init_name
        self.usage = init_usage
        self.powered = init_powered


class Food:
    name = None
    lifetime = 1

    def __init__(self, init_name):
        self.name = init_name

        if self.name == 'meat' or self.name == 'borsh' or self.name == 'eggs':
            self.lifetime = 2
        elif self.name == 'banana':
            self.lifetime = 3
        elif self.name == 'apples' or self.name == 'potatoes' or self.name == 'carrots':
            self.lifetime = 5

    def __str__(self):
        return self.name.upper()


meat = Food(init_name='meat')
apples = Food(init_name='apples')
banana = Food(init_name='banana')
potatoes = Food(init_name='potatoes')
carrots = Food(init_name='carrots')
milk = Food(init_name='milk')
borsh = Food(init_name='borsh')
eggs = Food(init_name='eggs')
ice_cream = Food(init_name='ice cream')

my_food = [apples, banana, potatoes, carrots, milk, borsh, eggs]
my_food2 = [meat, ice_cream]

dinner_table = Furniture(init_name='dinner table',
                         init_usage='is for a convenient meal')

cupboard = Furniture(init_name='cupboard',
                     init_usage='is for products/dishes storage')

chair = Furniture(init_name='chair',
                  init_usage='is for sitting')

refrigerator = StorageEquipment(init_name='refrigerator',
                                init_usage='is for food storage',
                                init_powered='powered by electricity',
                                init_storage=my_food,
                                init_temp=4)

freezer = StorageEquipment(init_name='freezer',
                           init_usage='is for food storage',
                           init_powered='powered by electricity',
                           init_storage=my_food2,
                           init_temp=-5)

oven = CookingEquipment(init_name='oven',
                        init_usage='is for heat treatment and cooking ',
                        init_powered='powered by electricity')

stove = CookingEquipment(init_name='stove',
                         init_usage='is for heat treatment and cooking',
                         init_powered='powered by electricity')

microwave = CookingEquipment(init_name='microwave',
                             init_usage='is for heating food',
                             init_powered='powered by electricity')

grinder = Tool(init_name='grinder',
               init_usage='is for grinding food',
               init_powered='powered by mechanical power')

mixer = Tool(init_name='mixer',
             init_usage='is for mixing food',
             init_powered='powered by electricity')

chair2 = chair
items = [dinner_table, chair, chair2, cupboard, refrigerator, freezer, oven, stove, microwave, grinder, mixer]

kitchen = Kitchen(init_content=items)

print('-' * 50)
kitchen.room_content()
print('-' * 50)
refrigerator.content()
freezer.content()
print('-' * 50)
for product in my_food:
    print(f'Lifetime of {product.name.upper()} on air is {product.lifetime} days.')
print('-' * 50)
refrigerator.temperature()
refrigerator.food_lifetime_calc()
print('-' * 50)
freezer.temperature()
freezer.food_lifetime_calc()
print('-' * 50)
