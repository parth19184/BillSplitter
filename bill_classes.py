'''
    PROBLEM STATEMENT:
        an item has multiple people who took that item.
        1. get post tax cost of each item
        2. divide by number of people and add to the divided cost to the weight of the person
'''
from typing import List


class People:
    def __init__(self, name):
        self.name = name

class Item:
    def __init__(self, itemName, peopleList, itemPrice):
        self.itemName = itemName
        self.peopleList = peopleList
        self.itemPrice = itemPrice
        self.postTaxPrice = 0

class Bill:
    def __init__(self, peopleList = [], itemList = [],alcoholList = [], gst = 5, vat = 18, serviceCharge = 10):
        self.peopleList: List[People] = peopleList
        self.itemList: List[Item] = itemList
        self.alcoholList: List[Item] = alcoholList
        self.vat: float = vat
        self.gst: float = gst
        self.serviceCharge: float = serviceCharge
        self.personDict = {}


    #do we need to have a method where we add items to the bill and then change the values of the class object(most probably yes)


    def addItem(self, item: Item, isItem: bool):
        if isItem:
            for person in item.peopleList:
                if person.name in self.personDict:
                    self.personDict[person.name].append(item.itemName)
                else:
                    self.personDict[person.name] = [item.itemName]
            self.itemList.append(item)
        else:
            for person in item.peopleList:
                if person.name in self.personDict:
                    self.personDict[person.name].append(item.itemName)
                else:
                    self.personDict[person.name] = [item.itemName]
            self.itemList.append(item)
    

    def splitBill(self):
        pass

    def getTotalFoodBill(self):
        return sum(foodItem.itemPrice for foodItem in self.itemList)

    def getTotalAlcoholBill(self):
        return sum(alcohol.itemPrice for alcohol in self.alcoholList)

    def getItemisedCostForAlcohol(self):
        preTaxPrice = self.getTotalAlcoholBill()
        postTaxPrice = preTaxPrice*(1 + self.vat)*(1 + self.serviceCharge)
        for alcohol in self.alcoholList:
            alcohol.postTaxPrice = alcohol.itemPrice*(postTaxPrice/preTaxPrice)
        return {alcohol.itemName: alcohol.itemPrice for alcohol in self.alcoholList}
    
    def getItemisedCostForItems(self):
        preTaxPrice = self.getTotalFoodBill()
        postTaxPrice = preTaxPrice*(1 + self.gst)*(1 + self.serviceCharge)
        for item in self.itemList:
            item.postTaxPrice = item.itemPrice*(postTaxPrice/preTaxPrice)
        return {item.itemName: item.postTaxPrice for item in self.itemList}
        

        

    