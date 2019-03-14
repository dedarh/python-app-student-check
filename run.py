import json
import os.path
import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

if sys.argv[0] == '1':
    print('consul get task')
elif sys.argv[0] == 'main.py':
    path = 'config.json'
    with open(path, 'r') as f:
        data = json.loads(f.read())
    print("Задание №", data['item'], data['task'][data['item']]['name'])
    if data['task'][data['item']]['type'] == 'file':
      if os.path.exists(data['task'][data['item']]['answer']):
          data['item'] = data['item'] + 1
          with open('config.json', 'w') as outfile:
              json.dump(data, outfile)
          print("Задание выполнено")
          data['item'] = data['item'] - 1    
      else:
        print("Вы не верно выполнили задание")
    
    if data['task'][data['item']]['type'] == 'hash':
        if sys.argv[0] == data['task'][data['item']]['answer']:
            print("Задание выполнено")
            data['item'] = data['item'] + 1
            with open('config.json', 'w') as outfile:
                json.dump(data, outfile)
            data['item'] = data['item'] - 1
        else:
           print("Не верный ответ")
else:
    print('errornot found command')
