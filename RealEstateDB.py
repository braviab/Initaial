import sqlite3

con=sqlite3.connect("RealEstateManagement.db")
c=con.cursor()

def create(table,credential):
    id,username,password=credential
    try:
        c.execute("""insert into {} values("{}","{}","{}")""".format(table,id,username,password))
        con.commit()
        print("\n{} created successfully".format(table))
    except:
        print("\nSomething went wrong")
        return False


def delete(table,id):
    try:
        c.execute("""delete from {} where id="{}";""".format(table,id))
        con.commit()
        print("\n{} Deleted successfully".format(table))
    except:
        print("\nSomething went wrong")
        return False

def view(table):
    try:
        data=c.execute("""select * from {}""".format(table))
        return data
    except:
        print("\nSomething went wrong")
        return False



try:
    c.execute("""create table page(id,aboutUs,contactUs)""")
    c.execute("""create table woner(id primary key,name, mobile)""")
    c.execute("""create table agent(id primary key,name,mobile)""")
    c.execute("""create table review(id primary key,pid,rev,approve)""")
    c.execute("""create table property(id primary key,ptype,country,state,city,wid,aid)""")
    c.execute("""create table admin(id primary key, username, password)""")
    c.execute("""create table user(id primary key, username, password)""")
except:
    pass



def adminPage(username):
    print("\n\n\t\t  Welcome "+username)
    while True:
        print("\n\n\n====================MENU======================")
        print("\n1. Add Property\n2. Update Property")
        print("3. Users\n4. Woners")
        print("5. Agents\n6. Pages")
        print("7. Search Property\n8. Count the  Fields")
        print("9. Create Agents\n10. Create Woners")
        print("11. List the Property")
        print("12. Reviews")
        print("==============================================\n\n")

        try:
            
            inp = int(input("Enter Your Choice : "))
        except:
            exit(1)
        if inp==1:
            id_list = c.execute("""select id from property""")
            print("\n\t\t Add Property")
            try:
                id = int(id_list.fetchall()[-1][0]) + 1
            except:
                id = 1
            ptype=input("Property Type : ")
            country=input("Country : ")
            state = input("State : ")
            city = input("City : ")
            wid = input("Woner ID : ")
            aid = input("Agent ID : ")
            won_list=c.execute("""select id from woner""").fetchall()
            ids = []
            for tid in won_list:
                ids.append(tid[0])
            if not wid in ids:
                print("\nInvalid Woner")

            agt_list = c.execute("""select id from agent""").fetchall()
            ids = []
            for tid in agt_list:
                ids.append(tid[0])
            if not aid in ids:
                print("\nInvalid Agent")

            else:
                c.execute("""insert into property values("{}","{}","{}","{}","{}","{}","{}")""".format(id,ptype,country,state,city,wid,aid))
                con.commit()
                print("\nProperty Added")


        if inp==2:
            print("\n\t\tUpdata Property")
            id=input("\nEnter the ID of Property which is to be Updated : ")
            id_list = c.execute("""select id from property""").fetchall()
            ids=[]
            for tid in id_list:
                ids.append(tid[0])
            if not id in ids:
                print("\ninvalid Property ID ")
                return False
            ptype = input("Property Type : ")
            country = input("Country : ")
            state = input("State : ")
            city = input("City : ")
            wid = input("Woner ID : ")
            aid = input("Agent ID : ")
            won_list = c.execute("""select id from woner""").fetchall()
            ids = []
            for tid in won_list:
                ids.append(tid[0])
            if not wid in ids:
                print("\nInvalid Woner")

            agt_list = c.execute("""select id from agent""").fetchall()
            ids = []
            for tid in agt_list:
                ids.append(tid[0])
            if not aid in ids:
                print("\nInvalid Agent")

            else:
                c.execute("""update  property set ptype="{}",country="{}",state="{}",city="{}",wid="{}",aid="{}" where id="{}";""".format(ptype, country,state, city, wid, aid,id))
                con.commit()
                print("\nProperty Updated")
        if inp==3:
            users= c.execute("""select * from user""").fetchall()
            for user in users:
                print("{} . {} Password  {}".format(user[0],user[1],user[2]))

        if inp==4:
            woners= c.execute("""select * from woner""").fetchall()
            for woner in woners:
                print("{} . {} contact number  {}".format(woner[0],woner[1],woner[2]))

        if inp==5:
            agents= c.execute("""select * from agent""").fetchall()
            for agent in agents:
                print("{} . {} contact number  {}".format(agent[0],agent[1],agent[2]))

        if inp == 6:
            while True:
                print("\n\n\n====================MENU======================")
                print("\n1. Add About Us and Contact Us")
                print("2. Update About Us\n3. Update Contact Us \n4. Exit")
                print("\n==============================================\n\n")

                inp = int(input("Enter Your Choice : "))
                if inp==1:
                    id_list = c.execute("""select id from page""")
                    print("\n\t\t Add About Us Agent")
                    try:
                        id = int(id_list.fetchall()[-1][0]) + 1
                    except:
                        id = 1
                    about = input("About us : ")
                    contact=input("Contact us : ")
                    credential=(id,about,contact)
                    create("page", credential)
                if inp==2:
                    print("\n\t\tUpdata About Us")
                    id = input("Enter the ID of About us which is to be Updated : ")
                    id_list = c.execute("""select id from page""").fetchall()
                    ids = []
                    for tid in id_list:
                        ids.append(tid[0])
                    if not id in ids:
                        print("\ninvalid About us ID ")
                        return False
                    aboutus = input("About us : ")
                    c.execute("""update  page set aboutUs="{}" where id="{}";""".format(aboutus, id))
                    con.commit()
                    print("\nAbout us Updated")

                if inp == 3:
                    print("\n\t\tUpdata Contact us")
                    id = input("Enter the ID of Contact us which is to be Updated : ")
                    id_list = c.execute("""select id from page""").fetchall()
                    ids = []
                    for tid in id_list:
                        ids.append(tid[0])
                    if not id in ids:
                        print("\ninvalid Contact us ID ")
                        return False
                    contactus = input("Contact us : ")
                    c.execute("""update  page set aboutUs="{}" where id="{}";""".format(contactus, id))
                    con.commit()
                    print("\nContact us Updated")
                if inp==4:
                    return False

        if inp==7:
            print("\n\n\t\tSearch Property")
            search=input("Search By Id or Name/type or Mobile Number : ")
            properties = c.execute("""select * from property where id="{}" or ptype="{}";""".format(search,search)).fetchall()
            for property in properties:  # id primary key,ptype,country,state,city,wid,aid)
                print("============================================")
                print("Property : {}".format(property[0]))
                print("Name : {}".format(property[1]))
                print("Country : {}".format(property[2]))
                print("State : {}".format(property[3]))
                print("City : {}".format(property[4]))
                woner = c.execute("""select * from woner where id="{}";""".format(property[5])).fetchall()
                print("Woner : {}".format(woner[0][1]))
                print("Contact number : {}".format(woner[0][2]))
                agent = c.execute("""select * from agent where id="{}";""".format(property[6])).fetchall()
                print("Agnent : {}".format(agent[0][1]))
                print("Contact number : {}".format(agent[0][2]))

            wids = c.execute("""select id from woner where mobile="{}";""".format(search)).fetchall()
            try:
                properties = c.execute("""select * from property where wid="{}";""".format(wids[0][0])).fetchall()
            except:
                pass
            aids = c.execute("""select id from agent where mobile="{}";""".format(search)).fetchall()

            try:
                properties+=c.execute("""select * from property where aid="{}";""".format(aids[0][0])).fetchall()
            except:
                pass
            for property in properties:  # id primary key,ptype,country,state,city,wid,aid)
                print("============================================")
                print("Property : {}".format(property[0]))
                print("Name : {}".format(property[1]))
                print("Country : {}".format(property[2]))
                print("State : {}".format(property[3]))
                print("City : {}".format(property[4]))
                woner = c.execute("""select * from woner where id="{}";""".format(property[5])).fetchall()
                print("Woner : {}".format(woner[0][1]))
                print("Contact number : {}".format(woner[0][2]))
                agent = c.execute("""select * from agent where id="{}";""".format(property[6])).fetchall()
                print("Agnent : {}".format(agent[0][1]))
                print("Contact number : {}".format(agent[0][2]))


        def count(table):
            return c.execute("""select count(*) from {};""".format(table)).fetchall()[0][0]

        if inp==8:
            print("Total Users : ", count("user"))
            print("Total Admins : ", count("admin"))
            print("Total Agents : ", count("agent"))
            print("Total Woners : ", count("woner"))
            print("Total Properties : ", count("property"))
            print("Total Countries : ",len(set(c.execute("""select country from property;""").fetchall())))
            print("Total States : ",len(set(c.execute("""select state from property;""").fetchall())))






        if inp==9:
            id_list = c.execute("""select id from agent""")
            print("\n\t\t Create Agent")
            try:
                id = int(id_list.fetchall()[-1][0]) + 1
            except:
                id = 1
            name = input("Agent name : ")
            mobile = input("Mobile number : ")
            credential=(id,name,mobile)
            create("agent",credential)

        if inp==10:
            id_list = c.execute("""select id from woner""")
            print("\n\t\t Create Woner")
            try:
                id = int(id_list.fetchall()[-1][0]) + 1
            except:
                id = 1
            name = input("Woner name : ")
            mobile = input("Mobile number : ")
            credential=(id,name,mobile)
            create("woner",credential)

        if inp==11:
            properties=c.execute("""select * from property""").fetchall()
            for property in properties: #id primary key,ptype,country,state,city,wid,aid)
                print("============================================")
                print("Property : {}".format(property[0]))
                print("Name : {}".format(property[1]))
                print("Country : {}".format(property[2]))
                print("State : {}".format(property[3]))
                print("City : {}".format(property[4]))
                woner = c.execute("""select * from woner where id="{}";""".format(property[5])).fetchall()
                print("Woner : {}".format(woner[0][1]))
                print("Contact number : {}".format(woner[0][2]))
                agent = c.execute("""select * from agent where id="{}";""".format(property[6])).fetchall()
                print("Agnent : {}".format(agent[0][1]))
                print("Contact number : {}".format(agent[0][2]))

        if inp==12:
            reviews = c.execute("""select * from review""").fetchall()
            for review in reviews:
                print("{}. Review for Property ID {} is {} : Aproved -{}".format(review[0],review[1],review[2],review[3]))
                print("Press {} to Manage.".format(review[0]))
            if len(reviews)>0:
                manage=input(" : ")
                id_list = c.execute("""select id from review""").fetchall()
                ids = []
                for tid in id_list:
                    ids.append(tid[0])
                if not manage in ids:
                    print("\ninvalid Review ID")
                    return False
                action=int(input("\n\n1 .Approve\n2. Delete\nEnter Your Choice : "))
                if action==1:
                    c.execute("""update review set approve="True" where id="{}";""".format(manage))
                    print("Review Approved")
                if action==2:
                    c.execute("""delete from review where id="{}";""".format(manage))
                    print("Review Deleted")






def userPage(username):
    print("\n\n\t\tHi ",username," Welcome")
    properties = c.execute("""select * from property""").fetchall()
    for property in properties:  # id primary key,ptype,country,state,city,wid,aid)
        print("============================================")
        print("Property : {}".format(property[0]))
        print("Name : {}".format(property[1]))
        print("Country : {}".format(property[2]))
        print("State : {}".format(property[3]))
        print("City : {}".format(property[4]))
        woner = c.execute("""select * from woner where id="{}";""".format(property[5])).fetchall()
        print("Woner : {}".format(woner[0][1]))
        print("Contact number : {}".format(woner[0][2]))
        agent = c.execute("""select * from agent where id="{}";""".format(property[6])).fetchall()
        print("Agnent : {}".format(agent[0][1]))
        print("Contact number : {}".format(agent[0][2]))
        print("PRESS {} to write Review about the Property".format(format(property[0])))
    pid=input("Enter ID to write Review : ")
    review=input("Write Review : ")
    id_list = c.execute("""select id from review""")
    try:
        id = int(id_list.fetchall()[-1][0]) + 1
    except:
        id = 1
    id_list = c.execute("""select id from property""").fetchall()
    ids = []
    for tid in id_list:
        ids.append(tid[0])
    if not pid in ids:
        print("\ninvalid Property ID ")
        return False #id primary key,pid,rev,approve
    c.execute("""insert into review values("{}","{}","{}","{}");""".format(id,pid,review,"false"))
    con.commit()
    print("Thank You for the Review")



if __name__ == '__main__':
    while True:
        print("\n\n\n====================MENU======================")
        print("\n1. User Registration\t\t2. User Login")
        print("3. Admin Registration\t\t4. Admin Login")
        print("==============================================\n\n")

        try:
            inp=int(input("Enter Your Choice : "))
        except:
            exit(1)
        if inp==1:
            id_list=c.execute("""select id from user""")
            print("\n\t\t User Registration")
            try:
                id = int(id_list.fetchall()[-1][0]) + 1
            except:
                id = 1
            username=input("Username : ")
            password= input("Password :")
            username_list=c.execute("""select username from user""")
            confpass=input("Confirm Password :")
            if not password==confpass:
                print("\nPassword Missmatch, Retry")
            try:
                if  username in username_list.fetchall()[0]:
                    print("\nUsername already Exists")
            except:
                credential=(id,username,password)
                create("user",credential)
            else:
                credential=(id,username,password)
                create("user",credential)
           
            


        elif inp==2:
            print("\n\t\tUser Login")
            username=input("Enter the Username : ")
            password=input("Enter the Password : ")
            user=c.execute("""select * from user where username="{}";""".format(username)).fetchall()
            if not user:
                print("\nInvalid Username")
            else:

                if password == user[0][2]:
                    userPage(username)
                else:
                    print("\ninvalid Password")
        elif inp==3:
            id_list=c.execute("""select id from admin""")
            print("\n\t\t Admin Registration")
            try:
                 id=int(id_list.fetchall()[-1][0])+1
            except:
                 id=1
            username=input("Username : ")
            password= input("Password :")
            username_list=c.execute("""select username from admin""")
            confpass=input("Confirm Password :")
            if not password==confpass:
                print("\nPassword Missmatch, Retry")
            try:
                if  username in username_list.fetchall()[0]:
                    print("\nUsername already Exists")
            except:
                credential = (id, username, password)
                create("admin", credential)
            else:
                credential=(id,username,password)
                create("admin",credential)


        elif inp==4:
            print("\n\t\tAdmin Login")
            username=input("Enter the Username : ")
            password=input("Enter the Password : ")
            user=c.execute("""select * from admin where username="{}";""".format(username)).fetchall()
            if not user:
                print("\nInvalid Username")
            else:

                if password == user[0][2]:
                    adminPage(username)
                else:
                    print("\ninvalid Password")
