import json

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def parseBusinessData():
    #read the JSON file
    with open('.\yelp_business.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('business.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['business_id'])+'\t') #business id
            outfile.write(cleanStr4SQL(data['name'])+'\t') #name
            outfile.write(cleanStr4SQL(data['address'])+'\t') #full_address
            outfile.write(cleanStr4SQL(data['state'])+'\t') #state
            outfile.write(cleanStr4SQL(data['city'])+'\t') #city
            outfile.write(cleanStr4SQL(data['postal_code']) + '\t')  #zipcode
            outfile.write(str(data['latitude'])+'\t') #latitude
            outfile.write(str(data['longitude'])+'\t') #longitude
            outfile.write(str(data['stars'])+'\t') #stars
            outfile.write(str(data['review_count'])+'\t') #reviewcount
            outfile.write(str(data['is_open'])+'\t') #openstatus
            outfile.write(str([item for item in  data['categories']])+'\t') #category list
            outfile.write(str([])) # write your own code to process attributes
            outfile.write(str([])) # write your own code to process hours
            outfile.write('\n');

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()
    # In yelp_business.json : Parse all keys except neighborhoods. 

def parseUserData():
    #write code to parse yelp_user.JSON
    # In yelp_user.json : Parse all keys except compliment fields and elite. 
    pass

def parseCheckinData():
    #write code to parse yelp_checkin.JSON
    #In yelp_checkin.json : Parse all keys. (You need to aggregate the check-in information for
    #the hours of the day. See below.) 
    #Parsing Check-in Data: The check-in objects include information about the number of check-ins for a
    #particular business . The “time” check-in JSON objects are in the form of:
    #”day”: {“hour”: number of checkins ,….}
    #For example “Friday”:{“20:00”: 5,“21:00”: 10} shows that there are 5 check-ins between
    #20:00pm and 20:59pm and 10 check-ins between 21:00pm and 21:59pm on Friday. (time values are
    #based on 24hour clock (i.e., military time))
    #For simplicity, in your project you will aggregate the check-in information further and sum up the checkin
    #values for morning hours (6am-12noon), afternoon hours (12noon-5pm), evening hours (5pm-11pm),
    #and night hours (11pm-6am) (Assume start time of each interval is inclusive and end time is exclusive.)
    #Therefore, for each day of the week, you will have 4 check-in values: morning, afternoon, evening and
    #night. 
    pass


def parseReviewData():
    #write code to parse yelp_review.JSON
    #In yelp_review.json: Parse all keys. 
    pass

parseBusinessData()
parseUserData()
parseCheckinData()
parseReviewData()
