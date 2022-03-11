from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)
otch = []
otchestvo = re.findall(r"(\w+)(вич|вна)", str(contacts_list))
for el in otchestvo:
  sur = ''
  for word in el:
    sur += word
  otch.append(sur)


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
list2.pop(0)
list2.pop(0)


i = 0
surname_list = []
name_list = []
while i < len(list2):
  if i % 2 == 1:
    name_list.append(list2[i])
  else:
    surname_list.append(list2[i])
  i += 1
list = []
tuple_name = tuple(name_list)
tuple_surname = tuple(surname_list)
tuple_otch = tuple(otch)
list.append(tuple_surname)
list.append(tuple_name)
list.append(tuple_otch)


with open("phonebook.csv", "w") as file:
  datawriter = csv.writer(file, delimiter=",")
  print(list)
  datawriter.writerows(list)
