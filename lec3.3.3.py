# Paste your code into this box
gennum=50
minnum=0
maxnum=100
number=raw_input('Please think of a number between 0 and 100!')
try:
  number=int(number)
except ValueError:
  number = -1
while True:
  if number>maxnum or number<minnum:
    number=raw_input('Please think of a number between 0 and 100!')
    try:
      number=int(number)
    except ValueError:
      number = -1
  else:
    break
    

while True:
  print 'Is your secret number ' + str(gennum)
  while True:
    znak=raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\'...')
    if znak == 'h' or znak == 'l' or znak == 'c':
	break
    else: 
	print('Sorry, I did not understand your input.')
  if znak=='c':
      print('Game over. Your secret number was: ' + str(gennum) )
      break
  elif znak=='h':
	minnum=gennum
	gennum = minnum+(maxnum-minnum)/2
  else:
	maxnum=gennum
	gennum = minnum+(maxnum-minnum)/2
	