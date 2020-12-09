#Vending Machine
products = [
  { 'number': 1, 'price': 100, 'name': 'Orange juice' },
  { 'number': 2, 'price': 200, 'name': 'Soda' },
  { 'number': 3, 'price': 150, 'name': 'Chocolate snack' },
  { 'number': 4, 'price': 250, 'name': 'Cookies' },
  { 'number': 5, 'price': 180, 'name': 'Gummy bears' },
  { 'number': 6, 'price': 500, 'name': 'Condoms' },
  { 'number': 7, 'price': 120, 'name': 'Crackers' },
  { 'number': 8, 'price': 220, 'name': 'Potato chips' },
  { 'number': 9, 'price': 80,  'name': 'Small snack' }
]

changes =  [500, 200, 100, 50, 20, 10]

def vending_machine(products, money, product_number):
    output = {}
    for snack in products:
        if product_number == snack['number']:
            if money >= snack["price"]:
                output["product"] = snack["name"]
                change = money - snack["price"]
                changelst = []
                pointer = 0
                while pointer < len(changes)-1:
                    while change > 0:
                        while change >= changes[pointer]:
                            changelst.append(changes[pointer])
                            change -= changes[pointer]
                        pointer += 1
                    break
                output["change"] = changelst
                return output
            else:
                return "Not enough money for this product"
    return "Enter a valid product number"


