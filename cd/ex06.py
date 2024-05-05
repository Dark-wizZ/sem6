print("Recursive Desent Parsing For following grammar\n")
print("E->TE'\nE'->+TE'/@\nT->FT'\nT'->*FT'/@\nF->(E)/i\n")
print("Enter the string want to be checked\n")

def match(a):
  global s, i
  if i<len(s) and s[i]==a:
    i+=1
    return True
  return False

def E():
  return T() and Ex()

def Ex():
  return(
    (match('+') and T() and Ex())
    or True
  )
  
def T():
  return F() and Tx()

def Tx():
  return(
    (match('*') and F() and Tx())
    or True
  )
  
def F():
  return(
    (match('(') and E() and match(')'))
    or match('i')
  )
  
s=''
i=0
while(s!='exit'):
  s=input()
  i=0
  if E() and i==len(s):
    print('Accepted')
  else: print("Not accepted")