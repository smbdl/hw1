data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations, codes = [i for i in data if i[0] != "0"], [i for i in data if i[0] == "0"]
operators = {}
i = 0
while i < len(codes):
    operators[designations[i]] = [codes[i]]
    i += 1
del operators['Katel']
del operators['Fonex']
operators["O!"].extend(["0700", "0500"])
operators["Megacom"].extend(["0999", "0555"])
operators["Beeline"].extend(["0222", "0777"])
operators["O!"] = set(operators["O!"])
operators["Megacom"] = set(operators["Megacom"])
operators["Beeline"] = set(operators["Beeline"])
for i in operators:
    print(f'{i} - {operators[i]}')


# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
# designations, codes = [], []
