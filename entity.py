from typing import List, Dict

class Item:
    def __init__(self, itemName: str, itemPrice: float, isAlcohol:bool, peopleList:List):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.peopleList = peopleList
        self.isAlcohol = isAlcohol
    
class Person:
    def __init__(self, personName: str, itemList: List[Item]):
        self.personName = personName
        self.itemList = itemList

class Bill:
    def __init__(self, itemList: List[Item] = [], vat = 0.18, gst = 0.05, serviceCharge = 0.1):
        self.itemList = itemList
        self.personDict: Dict[str, Item] = {}
        self.preItemPrice: Dict[str, float] = {}
        self.postItemPrice: Dict[str, float] = {}
        self.vat = vat
        self.gst = gst
        self.serviceCharge = serviceCharge

    def addItem(self, item: Item):
        for person in item.peopleList:
            if person in self.personDict:
                self.personDict[person].append(item)
            else:
                self.personDict[person] = [item]
        self.preItemPrice[item.itemName] = item.itemPrice

        self.itemList.append(item)

    def calculateFoodPrices(self):
        preTaxFoodBill = sum(item.itemPrice for item in self.itemList if not item.isAlcohol)
        preTaxAlcoholBill = sum(item.itemPrice for item in self.itemList if item.isAlcohol)

        postTaxFoodBill = preTaxFoodBill*(1 + self.gst)*(1 + self.serviceCharge)
        postTaxAlcoholBill = preTaxAlcoholBill*(1 + self.vat)*(1 + self.serviceCharge)

        for item in self.itemList:
            if item.isAlcohol:
                self.postItemPrice[item.itemName] = self.preItemPrice[item.itemName]*(postTaxAlcoholBill/preTaxAlcoholBill)
            else:
                self.postItemPrice[item.itemName] = self.preItemPrice[item.itemName]*(postTaxFoodBill/preTaxFoodBill)
        finalBill: Dict[str, float] = {}
        for person in self.personDict.keys():
            totalPrice = 0
            for item in self.personDict[person]:
                if item.isAlcohol:
                    totalPrice += self.postItemPrice[item.itemName]/len(item.peopleList)
                else:
                    totalPrice += self.postItemPrice[item.itemName]/len(item.peopleList)
            finalBill[person] = totalPrice
        return finalBill
            

    