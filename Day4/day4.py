import re

blank_line_regex = r"(?:\r?\n){2,}"

class License:
    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])

def readData():
    with open('input.txt', "r") as file:
        data = file.read().splitlines()
        return data


def readData2():
    with open('input.txt', "r") as file:
        data2 = file.read()
        updatedData = re.split(blank_line_regex, data2.strip())

    return updatedData


def testNewDeconstruction():
    data = readData2()
    validLicense = 0
    newValidLicense = 0
    for lines in data:
        updatedLine1 = lines.splitlines()
        updateLines2 = []
        for newLine in updatedLine1:
            data2 = newLine.split(' ')
            for entry in data2:
                updateLines2.append(entry)
        licenseDict = {}
        for values in updateLines2:
            [key, value] = values.split(':')
            licenseDict[key] = value

        license = License(licenseDict)
        licenseCheck = validateLicense(license)
        if licenseCheck:
            validLicense = validLicense + 1
            updateCheck = validateLicense2(license)
            if updateCheck:
                newValidLicense = newValidLicense + 1


    print (validLicense)
    print (newValidLicense)
    

def validateLicense(license):
    #we are being handing a class license
    #byr (Birth Year)
    #iyr (Issue Year)
    #eyr (Expiration Year)
    #hgt (Height)
    #hcl (Hair Color)
    #ecl (Eye Color)
    #pid (Passport ID)
    #cid (Country ID)
    #fieldsNeeded = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    fieldsNeeded = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid = True

    for field in fieldsNeeded:
        if hasattr(license, field):
            continue
        else:
            valid = False    
    return valid


def validateLicense2(license):

    overallValid = True
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if 1920 <= int(license.byr) <= 2002:
        pass
    else:
        overallValid = False
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if 2010 <= int(license.iyr) <= 2020:
        pass
    else:
        overallValid = False
    
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if 2020 <= int(license.eyr) <= 2030:
        pass
    else:
        overallValid = False

    #hgt (Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.
    if ('cm' in license.hgt or 'in' in license.hgt):
        if ('cm' in license.hgt):
            height, null = license.hgt.split('cm')
            if 150 <= int(height) <= 193:
                pass
            else:
                overallValid = False
        if ('in' in license.hgt):
            height, null = license.hgt.split('in')
            if 59 <= int(height) <= 76:
                pass
            else:
                overallValid = False
    else:
        overallValid = False

    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if (license.hcl.startswith("#") and len(license.hcl) == 7):
        null, numbers = license.hcl.split('#')
        pattern = re.compile("[a-f0-9]+")
        if pattern.fullmatch(numbers) is not None:
            pass
        else:
            overallValid = False
    else:
        overallValid = False
  
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    allowedColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    colorFound = False
    for colors in allowedColors:
        if colors == license.ecl:
            colorFound = True
                
    if not colorFound:
        overallValid = False

    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    print (license.pid)
    print (len(license.pid))
    if len(license.pid) == 9 and license.pid.isdigit():
        pass
    else:
        overallValid = False

    #cid (Country ID) - ignored, missing or not.


    return overallValid        

def deconstructData():
    fullData = readData()

    counter = 0
    dbData = {}

    dbData[counter] = []
    temp = []
    print ('Start')
    for data in fullData:
        if data == '':
            tempDict = {counter: temp}
            dbData.update(tempDict)
            print (dbData)
            del temp[:]
            print (temp)
            counter = counter + 1
        else:
            temp.append(data)


    print('Done')

    # for key, value in dbData.items():
    #     print ('Key: %s' %key)
    #     print ('Value: %s' %value)

    # print (type(dbData))


#deconstructData()
testNewDeconstruction()