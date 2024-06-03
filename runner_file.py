from entity import Bill, Item, Person

def createBillForTesting():
    people = ["A", "B", "C", "D", "E"]
    paneer = Item("Paneer", 250, False,["A", "B", "C", "D"])
    roti = Item("Roti", 120, False,["A", "B", "C"])
    naan = Item("Naan", 80, False, ["C", "D"])
    starter = Item("Starter", 250, False,["A", "B", "C", "D", "E"])
    bill = Bill()
    bill.addItem(paneer)
    bill.addItem(roti)
    bill.addItem(naan)
    bill.addItem(starter)
    return bill



if __name__ == "__main__":
    #execute program here
    print("starting program")
    bill = createBillForTesting()
    finalSplit = bill.calculateFoodPrices()
    print(finalSplit)
    
    