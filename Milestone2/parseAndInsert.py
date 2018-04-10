import json
import psycopg2
from datetime import datetime

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'

def insert2BusinessTable():
    #reading the JSON file
    with open('.//yelp_dataset//yelp_business.JSON','r') as f:    
        outfile =  open('.//yelp_dataset//yelp_business.SQL', 'w')  
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='projectTest' user='postgres' host='localhost' password='Abigail1'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            #Generate the INSERT statement for the current business hours
            # include values for all hoursTable attributes

            sql_str = "INSERT INTO business (business_id, name, address,city, state_code, postal_code, latitude, longitude, stars, reviewcount, is_open, numcheckins, reviewrating) " \
                      "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["address"]) + "','" + \
                      cleanStr4SQL(data["city"]) + "','" + cleanStr4SQL(data["state"]) + "','" + cleanStr4SQL(data["postal_code"]) + "'," + str(data["latitude"]) + "," + \
                      str(data["longitude"]) + "," + str(data["stars"]) + "," + str(data["review_count"]) + "," + str(data["is_open"])  + ",0 ,0"+ ");"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to businessTABLE failed!" + " " + data['business_id'] + " " + data['name'] +" ")
            conn.commit()
            # write the INSERT statement to a file.
            outfile.write(sql_str + '\n')

            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    outfile.close()  
    f.close()

# Helper parses hours array
def parseHours(hours, business_id):

    sql_str = []
    
    for day in hours.items():
        time = day[1].split("-", 1)
        sql_hours = ""

        day = day[0] + "'"
        sql_hours = "INSERT INTO hours (dayOfWeek, open, close, business_id) " \
                    "VALUES ('" + str(day) + ", '" + time[0] + "', '" + time[1] + "', '"  + business_id + "');"
        sql_str.append(sql_hours)
        
    return sql_str

def insert2HoursTable():
    with open('.//yelp_dataset//yelp_business.JSON','r') as f:    
        outfile =  open('.//yelp_dataset//yelp_hours.SQL', 'w')
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='projectTest' user='postgres' host='localhost' password='Abigail1'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            hours = parseHours(data['hours'], cleanStr4SQL(data['business_id']))

            #Generate the INSERT statement for the current business
            # include values for all hoursTable attributes
            for val in hours:
                sql_str = val
                
                try:
                    cur.execute(sql_str)
                except:
                    print("Insert to hoursTABLE failed!" + " " + data['business_id'] + " " + data['name'] +" ")
                conn.commit()
                # write the INSERT statement to a file.
                outfile.write(sql_str + '\n')

            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    outfile.close()  
    f.close()

def insert2CategoryTable():
    with open('.//yelp_dataset//yelp_business.JSON','r') as f:    
        outfile =  open('.//yelp_dataset//yelp_categories.SQL', 'w')
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='projectTest' user='postgres' host='localhost' password='Abigail1'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)

            #Generate the INSERT statement for the current business/category
            # include values for all categoriesTable attributes
            for val in data['categories']:
                sql_str = "INSERT INTO Categories (category_name, business_id) " \
                          "VALUES ('" + cleanStr4SQL(val) + "', '"  + data['business_id'] + "');"
                
                try:
                    cur.execute(sql_str)
                except:
                    print("Insert to categoryTABLE failed!" + " " + data['business_id'] + " " + val)
                conn.commit()
                # write the INSERT statement to a file.
                outfile.write(sql_str + '\n')

            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    outfile.close()  
    f.close()

def insert2UsersTable():
    #reading the JSON file
    with open('.//yelp_dataset//yelp_user.JSON','r') as f:    
        outfile =  open('.//yelp_dataset//yelp_user.SQL', 'w')  
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='projectTest' user='postgres' host='localhost' password='Abigail1'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            #Generate the INSERT statement for the current user
            # include values for all userTable attributes

            sql_str = "INSERT INTO users (user_id, yelping_since, name, review_count, useful, funny, fans, cool, average_stars) " \
                      "VALUES ('" + cleanStr4SQL(data['user_id']) + "','" + cleanStr4SQL(data["yelping_since"]) + "','" + cleanStr4SQL(data["name"]) + "'," + \
                      str(data["review_count"]) + "," + str(data["useful"]) + "," + str(data["funny"]) + "," + str(data["fans"]) + "," + \
                      str(data["cool"]) + "," + str(data["average_stars"]) + ");"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to userTABLE failed!" + " " + data['user_id'] + " " + data['name'] +" ")
            conn.commit()
            # write the INSERT statement to a file.
            outfile.write(sql_str + '\n')

            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    outfile.close()
    f.close()

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

        Weekly.append((day, "morning", AM))
        Weekly.append((day, "afternoon", AN))
        Weekly.append((day, "evening", EV))
        Weekly.append((day, "night", NI))        
        
    return Weekly

def insert2CheckinsTable():
    with open('.//yelp_dataset//yelp_checkin.JSON','r') as f:    
        outfile =  open('.//yelp_dataset//yelp_checkins.SQL', 'w')
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='projectTest' user='postgres' host='localhost' password='Abigail1'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)

            checkins = parseCheckins(data['time'])

            #Generate the INSERT statement for the current checkin data/business
            # include values for all checkinsTable attributes
            for val in checkins:
                sql_str = "INSERT INTO Checkins (day, start_time, num_checkins, business_id) " \
                          "VALUES ('" + str(val[0]) + "', '" + str(val[1]) + "', '" + str(val[2]) + "', '"  + data['business_id'] + "');"
                
                try:
                    cur.execute(sql_str)
                except:
                    print("Insert to checkinTABLE failed!" + " " + data['business_id'] + " " + str(val))
                conn.commit()
                # write the INSERT statement to a file.
                outfile.write(sql_str + '\n')

            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    outfile.close()  
    f.close()

def insert2ReviewTable():
    #reading the JSON file
    with open('.//yelp_dataset//yelp_review.JSON','r') as f:    
        outfile =  open('.//yelp_dataset//yelp_review.SQL', 'w')  
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='projectTest' user='postgres' host='localhost' password='Abigail1'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            #Generate the INSERT statement for current review
            # include values for all reviewTable attributes

            sql_str = "INSERT INTO review (review_id, user_id, business_id, date, text, stars, funny, cool, useful) " \
                      "VALUES ('" + cleanStr4SQL(data['review_id']) + "','" + cleanStr4SQL(data["user_id"]) + "','" + cleanStr4SQL(data["business_id"]) + "','" + \
                      cleanStr4SQL(data["date"]) + "','" + cleanStr4SQL(data["text"]) + "'," + str(data["stars"]) + "," + str(data["funny"]) + "," + \
                      str(data["cool"]) + "," + str(data["useful"]) + ");"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to businessTABLE failed!" + " " + data['review_id'])
            conn.commit()
            # write the INSERT statement to a file.
            outfile.write(sql_str + '\n')

            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    outfile.close() 
    f.close()

def insert2FriendTable():
    #reading the JSON file
    with open('.//yelp_dataset//yelp_user.JSON','r') as f:    
        outfile =  open('.//yelp_dataset//yelp_friends.SQL', 'w')  
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='projectTest' user='postgres' host='localhost' password='Abigail1'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            #Generate the INSERT statement for current review
            # include values for all reviewTable attributes

            for val in data['friends']:
                sql_str = "INSERT INTO Friends (user_id, friend_id) " \
                          "VALUES ('" + cleanStr4SQL(data['user_id']) + "', '"  + str(val) + "');"
                
                try:
                    cur.execute(sql_str)
                except:
                    print("Insert to friendsTABLE failed!" + " " + data['user_id'] + " " + val)
                conn.commit()
                # write the INSERT statement to a file.
                outfile.write(sql_str + '\n')

            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    outfile.close() 
    f.close()

insert2BusinessTable()
insert2HoursTable()
insert2CategoryTable()
insert2UsersTable()
insert2CheckinsTable()
insert2ReviewTable()
insert2FriendTable()
