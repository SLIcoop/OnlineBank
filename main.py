#! /usr/bin/env python3

class Money:
    def __init__(self, name='Unknown'):
        self.money = 0.00
        self.name = name

    def balance(self):
        print(self.money)
        print(self.name)

x = Money('Kirill')
x.balance()
