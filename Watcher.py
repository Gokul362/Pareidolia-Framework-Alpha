import yaml
import os
import time


class Item:
    def __init__(self, name):
        self.name = name

def create():
    try:
        with open('items.yaml') as f:
            stats = yaml.safe_load(f)

        for k, d in stats['Items'].items():
            new = Item(d['name'])
            print(new.name)
    except:
        print('Error: Retrying in a second')
        time.sleep(1)
        return create()
    
path = os.path.getmtime('C:\\Gokul\\Coding\\items.yaml')

# C_origin stands for Creation original 
C_origin = os.path.getmtime('C:\\Gokul\\Coding\\items.yaml')
C_new = os.path.getmtime('C:\\Gokul\\Coding\\items.yaml')

create()

while True:
    C_origin = C_new

    # C_new stands for Creation new
    C_new = os.path.getmtime('C:\\Gokul\\Coding\\items.yaml')
    time.sleep(0.5)

    if C_origin != C_new:
        create()