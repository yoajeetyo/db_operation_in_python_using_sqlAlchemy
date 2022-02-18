from  main import User,session,engine

# allUsers=[{
#     "username" : "My111",
#     "password" : "Ash000",
#     "email" : "Ashis@000"
#     },
# {
#     "username" : "He121",
#     "password" : "sanj000",
#     "email" : "sanjit@000"
# },
# {
#     "username" : "She131",
#     "password" : "Akh000",
#     "email" : "aman@000"
# },
# ]
#
# def InsertData():
#     try:
#         local_session = session(bind=engine)
#         for user in allUsers:
#             new_user = User(username=user["username"],password=user["password"],email=user["email"])
#             local_session.add(new_user)
#             local_session.commit()
#     except Exception as  e:
#         print(e)
# InsertData()
class CreateUsers:

    def __init__(self,allUsers):
        self.allUsers = allUsers

    def InsertData(self):
        try:
            self.local_session = session(bind=engine)
            for user in allUsers:
                self.new_user = User(username=user["username"], password=user["password"], email=user["email"])
                self.local_session.add(self.new_user)
                self.local_session.commit()
        except Exception as e:
            print(e)


allUsers = [{
            "username": "Namita",
            "password": "Namita000",
            "email": "Namita@000"
        },
            {
                "username": "Ashneer",
                "password": "Ashneer000",
                "email": "Ashneer@000"
            },
            {
                "username": "Lol212",
                "password": "Loi000",
                "email": "L88@000"
            },
        ]
create= CreateUsers(allUsers)
create.InsertData()