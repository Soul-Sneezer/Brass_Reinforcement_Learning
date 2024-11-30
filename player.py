# classes related to storing player state
# such as victory points, money, income, hand (the cards you have), buildings available
# to reach a higher level building you first have to exhaust the lower level ones

# there are also actions you can take every round

from board import IndustryType
from game import Game

class Building:
    def __init__(self, industry_type, stats, price, beers=0, resources=0):
        self.industry_type = industry_type
        self.stats = stats
        self.price = price
        self.beers = beers # number of beers required for it to be sold
        self.resources = resources

buildings = [[[IndustryType.IRONWORKS,( 3, 3, 1), (5, 1, 0), 0, 4, 1],
              [IndustryType.IRONWORKS,( 5, 3, 1), (7, 1, 0), 0, 4, 1],
              [IndustryType.IRONWORKS,( 7, 2, 1), (9, 1, 0), 0, 5, 1],
              [IndustryType.IRONWORKS,( 9, 1, 1),(12, 1, 0), 0, 6, 1]],
             [[IndustryType.COALMINE,( 1, 4, 2), (5, 0, 0), 0, 2, 1],
              [IndustryType.COALMINE,( 2, 7, 1), (7, 0, 0), 0, 3, 2],
              [IndustryType.COALMINE,( 3, 6, 1), (8, 0, 1), 0, 4, 2],
              [IndustryType.COALMINE,( 4, 5, 1),(10, 0, 1), 0, 5, 2]],
             [[IndustryType.BREWERY,( 4, 4, 2), (5, 0, 1), 0, 1, 2],
              [IndustryType.BREWERY,( 5, 5, 2), (7, 0, 1), 0, 1, 2],
              [IndustryType.BREWERY,( 7, 5, 2), (9, 0, 1), 0, 1, 2],
              [IndustryType.BREWERY,(10, 5, 2), (9, 0, 1), 0, 1, 1]], # will have the modify the number of resources produced to 2 in second phase
             [[IndustryType.POTTERY,(10, 5, 1), (17, 0, 1), 1, 0, 1],
              [IndustryType.POTTERY,( 1, 1, 1), ( 0, 1, 0), 1, 0, 1],
              [IndustryType.POTTERY,(11, 5, 1), (22, 2, 0), 2, 0, 1],
              [IndustryType.POTTERY,( 1, 1, 1), ( 0, 1, 0), 1, 0, 1],
              [IndustryType.POTTERY,(20, 5, 1), (24, 2, 0), 2, 0, 1]],
             [[IndustryType.MANUFACTORY,( 5, 5, 1), (12, 0, 0), 1, 0, 3],
              [IndustryType.MANUFACTORY,( 5, 4, 2), (14, 1, 0), 1, 0, 2],
              [IndustryType.MANUFACTORY,( 9, 3, 1), (16, 1, 1), 1, 0, 3],
              [IndustryType.MANUFACTORY,(12, 2, 1), (18, 1, 1), 1, 0, 3]],
            [[IndustryType.COTTONMILL,( 3, 5, 2), ( 8, 1, 0), 1, 0, 1],
              [IndustryType.COTTONMILL,( 5, 1, 1), (10, 0, 1), 1, 0, 2],
              [IndustryType.COTTONMILL,( 4, 4, 0), (12, 2, 0), 0, 0, 1],
              [IndustryType.COTTONMILL,( 3, 6, 1), ( 8, 0, 1), 1, 0, 1],
              [IndustryType.COTTONMILL,( 8, 2, 2), (16, 1, 0), 2, 0, 2],
              [IndustryType.COTTONMILL,( 7, 6, 1), (20, 0, 0), 1, 0, 1],
              [IndustryType.COTTONMILL,( 9, 4, 0), (16, 1, 1), 0, 0, 1],
              [IndustryType.COTTONMILL,(11, 1, 0), (20, 0, 2), 1, 0, 2]]]

class Player:
    def createBuildingType(self, i):
        for building in buildings[i]:
            for i in range(building[5]):
                industry_type = building[0]
                stats = building[1]
                price = building[2]
                beers = building[3]
                resources = building[4]
                new_building = Building(industry_type, stats, price, beers, resources)
                
                if i == 0:
                    self.iron_works.append(new_building)
                elif i == 1:
                    self.coal_mines.append(new_building)
                elif i == 2:
                    self.breweries.append(new_building)
                elif i == 3:
                    self.potteries.append(new_building)
                elif i == 4:
                    self.manufactories.append(new_building)
                else:
                    self.cotton_mills.append(new_building)
    
    def createIronWorks(self):
        self.createBuildingType(0)
    def createCoalMines(self):
        self.createBuildingType(1) 
    def createBreweries(self):
        self.createBuildingType(2)
    def createManufactories(self):
        self.createBuildingType(3)
    def createPotteries(self):
        self.createBuildingType(4)
    def createCottonMills(self):
        self.createBuildingType(5)
   
    def createBuildings(self):
        self.createIronWorks()
        self.createCoalMines()
        self.createBreweries()
        self.createManufactories()
        self.createPotteries()
        self.createCottonMills()

    def __init__(self):
        self.iron_works = []
        self.coal_mines = []
        self.breweries = []
        self.potteries = []
        self.manufactories = []
        self.cotton_mills = []

        self.createBuildings()
        self.victory_points = 0
        self.income = 0
        self.coins = 17

        self.cards = []
        self.discard_pile = [] 

    def build(self, build_card):
        pass

    def network(self, targets):         # expects 3 cards to discard
        self.discardCard(targets[0])
        self.discardCard(targets[1])
        self.discardCard(targets[2])
        pass

    def develop(self):
        pass

    def sell(self, target):
        pass

    def loan(self):
        self.coins += 30
        self.adjustIncome(-3)
        pass

    def scout(self):
        pass

    def drawCard(self, card):
        self.cards.append(card)

    def discardCard(self, target): # discard a card from hand
        self.discard_pile.append(target)
        self.cards.remove(target) # find a way to choose which card to discard

    def adjustIncome(self, levels, steps = 0):
        # up to income level 0, there is one step between levels VP 0 - 10
        # up to income level 10, there are 2 steps between levels VP 11 -30
        # up to income level 20, there are 3 steps between levels VP 31 - 60
        # up to income level 29, there are 4 steps between levels VP 61 - 96
        # for income level 30, there are 3 steps, and I guess you can't have more than 30 income VP 97 - 99
        self.income += steps

