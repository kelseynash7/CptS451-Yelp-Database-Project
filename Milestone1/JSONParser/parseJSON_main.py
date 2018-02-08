import json
import unicodedata
from datetime import datetime

# converts unicode values (read in from JSON) to ascii so they can be properly handled
def convertUnicode(data):
    return unicodedata.normalize('NFKD', data).encode('ascii','ignore')

# Given in skeleton code - cleans strings for SQL
def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

# prints an array
def printArray(array, outfile):
    for item in array:
        outfile.write(str(item))

# Helper parses hours array
def parseHours(hours):
    hourArray = []

    for day in hours.items():
        time = day[1].split("-", 1)
        hourArray.append((convertUnicode(day[0]), convertUnicode(time[0]), convertUnicode(time[1])))
            
    return hourArray

# Helper parses nested attribute structure
def parseAttributes(attrData):
    attributeData = []
    for key in attrData.keys():
        if isinstance(attrData.get(key), dict):
            parseAttributes(attrData.get(key))
        else:
            attributeData.append((convertUnicode(key), convertUnicode(unicode(attrData.get(key)))))

    return attributeData

# Helper parses nested checkin (time) structure and aggregates
def parseCheckins(checkIns):
    Weekly = []
    six = datetime.strptime("06:00", "%M:%S")
    twelve = datetime.strptime("12:00", "%M:%S")
    five = datetime.strptime("17:00", "%M:%S")
    eleven = datetime.strptime("23:00", "%M:%S")
    
    for day in checkIns.keys():
        AM = 0
        AN = 0
        EV = 0
        NI = 0
        
        for time in checkIns.get(day):            
            realtime = datetime.strptime(time, "%M:%S")

            if (realtime >= six and realtime < twelve):
                AM += int(checkIns.get(day).get(time))
            elif (realtime >= twelve and realtime < five):
                AN += int(checkIns.get(day).get(time))
            elif (realtime >= five and realtime > eleven):
                EV += int(checkIns.get(day).get(time))
            elif (realtime >= eleven or  realtime < six):
                NI += int(checkIns.get(day).get(time))

        Weekly.append((convertUnicode(day), "morning", AM))
        Weekly.append((convertUnicode(day), "afternoon", AN))
        Weekly.append((convertUnicode(day), "evening", EV))
        Weekly.append((convertUnicode(day), "night", NI))        
        
    return Weekly

# Parse Business Data File
def parseBusinessData():
    #read the JSON file
    with open('.\yelp_business.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('business.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['business_id'])+', ') #business id
            outfile.write(cleanStr4SQL(convertUnicode(data['name']))+', ') #name
            outfile.write(cleanStr4SQL(data['address'])+', ') #full_address
            outfile.write(cleanStr4SQL(data['state'])+', ') #state
            outfile.write(cleanStr4SQL(data['city'])+', ') #city
            outfile.write(cleanStr4SQL(data['postal_code']) + ', ')  #zipcode
            outfile.write(str(data['latitude'])+', ') #latitude
            outfile.write(str(data['longitude'])+', ') #longitude
            outfile.write(str(data['stars'])+', ') #stars
            outfile.write(str(data['review_count'])+', ') #reviewcount
            outfile.write(str(data['is_open'])+', ') #openstatus
            outfile.write(str('Categories: '))
            outfile.write(str([convertUnicode(item) for item in data['categories']])+'  ') #category list
            outfile.write(str('Attributes: '))
            outfile.write(str('['))
            printArray(parseAttributes(data['attributes']), outfile) #attributes
            outfile.write(str('] '))
            outfile.write(str('Hours: '))
            outfile.write(str('['))
            printArray(parseHours(data['hours']), outfile) #hours
            outfile.write(str(']'))
            outfile.write('\n');

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

# Parse the User Data File
def parseUserData():
    #read the JSON file
    with open('.\yelp_user.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('userData.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['user_id'])+', ') #user_id
            outfile.write(cleanStr4SQL(convertUnicode(data['name']))+', ') #name
            outfile.write(cleanStr4SQL(data['yelping_since']) + ', ') #yelping_since
            outfile.write(str(data['useful']) + ', ') #useful
            outfile.write(str(data['review_count']) +', ') #review_count
            outfile.write(str(data['funny']) +', ') #funny
            outfile.write(str('Friends: '))
            outfile.write(str([convertUnicode(item) for item in data['friends']])+', ')#friends - array
            outfile.write(str(data['fans']) +', ') #fans
            outfile.write(str(data['cool']) +', ') #cool
            outfile.write(str(data['average_stars']))#average_stars
            outfile.write('\n');

            line = f.readline()
            count_line +=1
            
    print(count_line)
    outfile.close()
    f.close()

# Parse the Check In Data File
def parseCheckinData():
    #read the JSON file
    with open('.\yelp_checkin.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('checkins.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['business_id']) + ', ') #business_id
            printArray(parseCheckins(data['time']), outfile) #time array
            outfile.write('\n');

            line = f.readline()
            count_line +=1
            
    print(count_line)
    outfile.close()
    f.close()
    
# Parse the Review Data File
def parseReviewData():
    #read the JSON file
    with open('.\yelp_review.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('reviews.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['review_id']) + ', ') #review_id
            outfile.write(cleanStr4SQL(data['user_id']) + ', ') #user_id
            outfile.write(cleanStr4SQL(data['business_id']) + ', ') #business_id
            outfile.write(str(data['stars']) + ', ') #stars
            outfile.write(cleanStr4SQL(data['date']) + ', ') #date
            outfile.write(cleanStr4SQL(convertUnicode(data['text'])) + ', ') #text
            outfile.write(str(data['useful']) + ', ') #useful
            outfile.write(str(data['funny']) + ', ') #funny
            outfile.write(str(data['cool'])) #cool
            outfile.write('\n');
            
            line = f.readline()
            count_line +=1
            
    print(count_line)
    outfile.close()
    f.close()
    
## MAIN - Parse CALLS
print('Parsing Business Data: ')
parseBusinessData()
print('Parsing User Data: ')
parseUserData()
print('Parsing Check in Data: ')
parseCheckinData()
print('Parsing Review Data: ')
parseReviewData()
