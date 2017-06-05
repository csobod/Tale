"""
The Olde Shoppe in the town.

'Tale' mud driver, mudlib and interactive fiction framework
Copyright by Irmen de Jong (irmen@razorvine.net)
"""

from tale.base import Item, Location, Exit
from tale.items.basic import gameclock, diamond, gem, newspaper, woodenYstick, elastic_band
from tale.shop import ShopBehavior
from npcs.town_creatures import ShoppeShopkeeper, CustomerJames


# create the Olde Shoppe and its owner
shopinfo = ShopBehavior()
toothpick = Item("toothpick", "pointy wooden toothpick")
toothpick.value = 0.12
shopinfo.forsale.add(toothpick)   # never run out of toothpicks
shopinfo.banks_money = True
shopkeeper = ShoppeShopkeeper("Lucy", "f", short_descr="Lucy, the shop owner, is looking happily at her newly arrived customer.")
shopkeeper.money = 14000
shop = Location("Curiosity Shoppe", "A weird little shop. It sells odd stuff.")
shop.insert(shopkeeper, None)
shop.get_wiretap().subscribe(shopkeeper)
shop.add_exits([Exit(["door", "out"], "town.lane", "A fancy door provides access back to the lane outside.")])


# provide some items in the shop
clock = gameclock.clone()
clock.value = 500
paper = newspaper.clone()
gem2 = diamond.clone()
gem2.value = 80000
gem3 = gem.clone()
gem3.value = 9055
stick = woodenYstick.clone()
elastic = elastic_band.clone()
shopkeeper.init_inventory([gem2, gem3, toothpick, stick, elastic])
shopkeeper.set_shop(shopinfo)


# some stuff and people that are present in the shoppe
shop.insert(clock, None)
shop.insert(paper, None)
lamp = Item("lamp", "rather small lamp")
lamp.value = 600
customer = CustomerJames("James", "m", title="Sir James", descr="Sir James is trying to sell something, it looks like a lamp.")
lamp.add_extradesc({"lamp"}, "The lamp looks quite old, but otherwise is rather unremarkable."
                             " There is something weird going on with the cord though!")
lamp.add_extradesc({"cord"}, "Even when the lamp doesn't move, the power cord keeps snaking around as if it were alive. How odd.")
customer.insert(lamp, customer)
shop.insert(customer, None)
shop.get_wiretap().subscribe(customer)
