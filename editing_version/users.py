"""
Ta file hendla vse z json in databajsom userjov



userbase json file 1

nove userje se adda nakonc data
nove atribute se adda nakonc data[user]

ko user pošlje reminder se shran v njegov json file tko k preference 
bereš vn z readlines da najds kar iscs

----------
with open(jsonfile, 'r') as file:
    data = json.load(file)
    data[id] = value

with open(jsonfile, 'w') as file:
    json.dump(data, file)
----------
kr sexi solution


nacin 
"""