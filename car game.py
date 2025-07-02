started=False
while True:
  command=input('Enter the command:').lower()
  if command =='start':
    if started:
      print('Car is already started..\n')
    else:
      print('car started')
      started==True
  elif command =='stop':
    if not started:
      print('car is already stopped')
    else:
      print('car stopped')
      started=False

  elif command =='help':
    print('''start- to start the car,
stop- to stop the car
quit- to quit the game\n''')
  elif command =='quit':
    print('Thanks for playing this game')
    break
else:
  print(' I dont understand the command')