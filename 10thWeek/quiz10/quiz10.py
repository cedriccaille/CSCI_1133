#Problem A -- Double Values
def double_values(dct):
    out = []
    for key in dct.keys():
        dct[key] = dct[key]*2
    return dct

#Problem B -- Lookup Composition
def get_phones(name_office, office_phone):
    dict1 = {}

    for prof in name_office.keys():
        if name_office[prof] in office_phone.keys():
            dict1[prof] = office_phone[name_office[prof]]
    return dict1

#Problem C -- Total Hours
def log_hours(fname):
    dict1 = {}
    fp_in = open(fname, 'r')
    line = fp_in.read()
    linelist = line.split('\n')
    for ele in linelist:
        list = ele.split()
        print(ele)
        print(dict1.keys())
        if list[0] not in dict1.keys():
            dict1[list[0]] = int(list[1])
        else:
            dict1[list[0]] += int(list[1])
    return dict1
