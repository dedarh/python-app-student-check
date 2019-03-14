import json
import os.path
import sys

if sys.argv[1] == 'init':
    print('consul get task')
elif sys.argv[1] == 'check':
        path = '/tmp/config.json'
        with open(path, 'r') as f:
            data = json.loads(f.read())
        if data['item'] >= len(data['task']):
            print("Вы высе прошли")
        else:
            print("Ваше задание:")
            print (data['task'][data['item']]['name'])
            print "Прогресс: ", data['item'],"/", len(data['task'])
            if data['task'][data['item']]['type'] == 'file':
                if os.path.exists(data['task'][data['item']]['answer']):
                    data['item'] = data['item'] + 1
                    with open('/tmp/config.json', 'w') as outfile:
                        json.dump(data, outfile)
                    print("Задание выполнено")
                    data['item'] = data['item'] - 1
                else:
                    print("Вы не верно выполнили задание")

            if data['task'][data['item']]['type'] == 'hash' and len(sys.argv) == 3:
                if sys.argv[2] == data['task'][data['item']]['answer']:
                    print("Задание выполнено")
                    data['item'] = data['item'] + 1
                    with open('/tmp/config.json', 'w') as outfile:
                        json.dump(data, outfile)
                    data['item'] = data['item'] - 1
                else:
                    print("Не верный ответ")
else:
    print('errornot found command')
