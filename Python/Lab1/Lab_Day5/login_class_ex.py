#Login class

from http import server


class Login:
    username = "user1"
    password = "pawssord"
    server = "server.com"

    def login(self):
        print("you have logged in to : " + self.server + "as: " + self.username)

    def emailcheck(self):
        print("You got main in: ", self.server)

gmail = Login()
gmail.username = "ABC"

hotmail = Login()
hotmail.username = "user123"
yahoo = Login()

print(yahoo.emailcheck())
print(gmail.emailcheck())

# idea of self
