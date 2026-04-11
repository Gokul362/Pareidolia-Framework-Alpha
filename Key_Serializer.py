import yaml
import struct


class Keys:
    def __init__(self, value):
        self.value = value


with open('Keys.yaml') as f:
    keys = yaml.safe_load(f)

keys_list = []

for key, value in keys['Keys'].items():
    print(f'{key}: {value}')
    new_key = Keys(value)
    keys_list.append(new_key)

binary = struct.pack('iiii', keys_list[0].value, keys_list[1].value, keys_list[2].value, keys_list[3].value)

with open('Cos0.bin', 'wb') as secant:
    secant.write(binary)
    print('Binary file has been created. Check your folder.')