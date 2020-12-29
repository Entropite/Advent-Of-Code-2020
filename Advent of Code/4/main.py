REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hcl', 'ecl', 'pid', 'hgt']
EYE_COLOURS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
REQUIRED_FIELD_TESTS = [lambda year: int(year) <= 2002 and int(year) >= 1920, # byr test
                        lambda year: int(year) <= 2020 and int(year) >= 2010,
                        lambda year: int(year) <= 2030 and int(year) >= 2020,
                        lambda hcl: hcl[0] == '#' and len(hcl) == 7 and all([i in base16Chars for i in list(hcl[1:])]),
                        lambda ecl: ecl in EYE_COLOURS,
                        lambda pid: len(pid) == 9,
                        lambda height, unit: (height <= 193 and height >= 150) if unit == 'cm' else (height >= 59 and height <= 76)]


base16Chars = []

#initiate base16Chars
for i in range(10):
    base16Chars.append(chr(i+48))

for i in range(6):
    base16Chars.append(chr(i+97))

file = open('data.txt', 'r')
data = file.read().split('\n\n')

simpleValid = 0
valid = 0

# part one
def isSimpleValid(passport):
    for i in REQUIRED_FIELDS:
        if(passport.count(i) == 0):
            return False
    return True

# part two
def isValid(passport):
    for i in REQUIRED_FIELDS:
        if(passport.count(i) == 0):
            return False

    tempPassport = passport.replace(' ', ':')
    tempPassport = tempPassport.split(':')

    #build dictionary
    passportDict = {}
    for i in range(len(tempPassport) // 2):
        passportDict[tempPassport[i*2]] = tempPassport[i*2+1]

    for i in range(6):
        # pass simple tests
        if(not REQUIRED_FIELD_TESTS[i](passportDict[REQUIRED_FIELDS[i]])):
            return False

    # pass height tests
    if(len(passportDict['hgt']) < 3):
        return False
    else:
        if(not REQUIRED_FIELD_TESTS[-1](int(passportDict['hgt'][:-2]), passportDict['hgt'][-2:])):
            return False

    return True



for i in range(len(data)):
    data[i] = data[i].replace('\n', ' ')
    if(isSimpleValid(data[i])):
        simpleValid += 1
    if isValid(data[i]):
        valid += 1

print("Simple Valid: {}; Valid: {}".format(simpleValid, valid))