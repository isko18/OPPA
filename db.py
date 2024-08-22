import json
phones_dict = {}
id = 0
with open('phones.txt', 'rb') as file:
    for i in file.readlines():
        b = str(i).replace("b'", '')
        b = b.replace(' ','')
        b = b.replace("\\n'", '')
    
        phone = '+996' + b[1::]  if b[0] =='0' else '+996'+b
        phones_dict[id] = {
            'phone': phone
        }
        id+=1
        with open('phones.json', 'w', encoding="utf-8") as ph:
            json.dump(phones_dict, ph, indent=4, ensure_ascii=False)
    # for i in file.readlines():
    #     print(i)