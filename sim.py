from board import Board
from board import IndustryType
from game import Game
from player import Player

board = Board(2)
game = Game(2)


name_to_index = {
    "Stoke On Trent": 0,
    "Stone": 1,
    "Leek": 2,
    "Uttoxeter":4,
    "Belper":3,
    "Derby":5,
    "Stafford":7,
    "Burton On Trent":6,
    "Cannock":8,
    "City0":9,
    "Coalbrookdale":12,
    "Wolverhampton":13,
    "Walsall":10,
    "Tamworth":11,
    "Nuneaton":15,
    "Birmingham":14,
    "Coventry":16,
    "Redditch":21,
    "Dudley":17,
    "Kidderminster":20,
    "City1":19,
    "Worcester":18 
}
#print(board.cities)
#for city in board.cities:
#    city.printLinks()

#print(board.trading_hubs)
board.coal_market.removeResource()
board.iron_market.removeResource()
board.iron_market.removeResource()
print(board.coal_market.getPrice())
print(board.iron_market.getPrice())

print(game.cards)
player = game.players[0]
#print(player.build(game.board.cities[1], player.getManufactory()))
print(game.board.cities)
print(player.coins)
#print(game.board.cities[1].squares[0].building_instance.building.industry_type) # bruh 
player.coins = 100

dudley = game.board.cities[name_to_index.get("Dudley")]
kidderminster = game.board.cities[name_to_index.get("Kidderminster")]
worcester = game.board.cities[name_to_index.get("Worcester")]
city1 = game.board.cities[name_to_index.get("City1")]

print(player.build(dudley, player.getCoalmine()))
print(dudley.squares[0].building_instance.building.resources)
print(dudley.isAvailable(0, IndustryType.IRONWORKS))
#print(game.board.cities[name_to_index.get("Dudley")].squares[0].building_instance.building.industry_type)
print(player.build(dudley, player.getIronworks()))
print(dudley.squares[1].getStats())
print(player.coins)
print(player.develop([IndustryType.IRONWORKS]))
print(player.coins)
print(dudley.squares[1].building_instance.building.resources)

