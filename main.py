#! /usr/bin/env python3

class FirstAcc:
    def __init__(self, name='Unknown'):
        self.__money = 0.00
        self.name = name

    def top_up_balance(self, amount):
        self.total = self.__money + amount
        return amount

    def top_down_balance(self, amount):
        if self.__money - amount < 0:
            print('Not enough funds!')
            raise ValueError ('Not enough funds!')
        else:
            self.total = self.__money - amount
        return amount

    def balance(self):
        print(self.name)
        print(self.total)

class SecondAcc:
    def __init__(self, name='Unknown'):
        self.__money = 0.00
        self.name = name

    def top_up_balance(self, amount):
        self.total = self.__money + amount

    def top_down_balance(self, amount):
        if self.__money - amount < 0:
            print('Not enough funds!')
            raise ValueError ('Not enough funds!')
        else:
            self.total = self.__money - amount

    def balance(self):
        print(self.name)
        print(self.total)

ch_account = input("Choice account: ")
    
if ch_account == '1':
    name = input("Write your name: ")
    x = FirstAcc(name)
    print("Welcome ", name)

if ch_account == '2':
    name = input("Write your name: ")
    x = SecondAcc(name)
    print("Welcome ", name)

c = input("What you wanna: ")

if c in('1', '2'):
    i = int(input("Write how much u want: "))

    if c == '1':
        x.top_up_balance(i)
        print(x.balance())
        
    if c == '2':
        x.top_down_balance(i)
        print(x.balance())
