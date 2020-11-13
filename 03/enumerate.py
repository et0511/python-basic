#enumerate

index = 1
for color in ['red', 'blue', 'yellow', 'grey']:
    print(f'{index}:{color}')
    index += 1

print("==")
for i, color in enumerate(['red', 'blue', 'yellow', 'grey']):
    print(f'{i+1}:{color}')
