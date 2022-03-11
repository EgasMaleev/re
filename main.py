from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)
contacts_list.pop(0)
otch = []
otchestvo = re.findall(r"(\w+)(вич|вна)", str(contacts_list))
for el in otchestvo:
  sur = ''
  for word in el:
    sur += word
  otch.append(sur)
# otch.append(' ')

FIO = re.findall(r"(\['\w+)('|\s)(')?(,)?(\s)?(\s)?(\s)?(')?(\w+)", str(contacts_list))
list2 = []
for el in FIO:
  for word in el:
    str = ''
    if word != '' and word != ' ' and word != "'" and word != ",":
      for letter in word:
        if letter != '[' and letter != "'":
          str += letter
      list2.append(str)
i = 0
surname_list = []
name_list = []
while i < len(list2):
  if i % 2 == 1:
    name_list.append(list2[i])
  else:
    surname_list.append(list2[i])
  i += 1
count = 0

for person in contacts_list:
  person[0] = surname_list[count]
  person[1] = name_list[count]
  if count != len(otch):
    person[2] = otch[count]
  # print(person)
  count += 1
  # if count == len(otch):
  #   break
list = []
for person in contacts_list:
  if person[0] in list:
    for pers in contacts_list:
      if pers[0] == person[0] and pers[1] == person[1]:
        if pers[3] == '':
          pers[3] = person[3]
        if pers[4] == '':
          pers[4] = person[4]
        if pers[5] == '':
          pers[5] = person[5]
        if pers[6] == '':
          pers[6] = person[6]
          # print(pers)
        # contacts_list.append(pers)
        contacts_list.remove(person)
    print(person[0])
    # contacts_list.remove(pers)
  list.append(person[0])
pprint(contacts_list)
with open("phonebook.csv", "w") as file:
  datawriter = csv.writer(file, delimiter=",")
  datawriter.writerows(contacts_list)
