gram = { 'S':['S+S','S-S','S*S','(S)','id']}
start='S'
stack=''
input='(id+id-id)$'

print(f'{"Stack":<15}|{"Input Buffer":<15}|Parsing Action')
print('-'*50)

while True:
  flag=1
  for i in gram[start]:
    if i in stack:
      flag=0
      stack = stack.replace(i, start)
      print(f'{stack:<15}|{input:<15}|Reduce {start} -> {i}')
  if len(input)>1:
    flag=0
    stack += input[0]
    input = input[1:]
    print(f'{stack:<15}|{input:<15}|{"Shift"}')
  if input=='$' and stack==start:
    print("Accepted")
    break
  if flag:
    print("Not Accepted")
    break