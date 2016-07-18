import requests
import PasswordDecrypt
import winsound
import threading

username = "ProeliatorOrdo"
password = input("Enter Password: ")

cblesspayload = {
     "thumbs" : "0",
     "PHPSESSID" : "l2ppe9c3p90n1afn2ds3ghnli1",
     }

hblesspayload = {
    "Host" : "a1k4.chatwitch.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-US,en;q=0.5",
    "Accept-Encoding" : "gzip, deflate",
    "Referer" : "http://a1k4.chatwitch.com/login/bless.php?a=&user=&url=http%3A%2F%2Fa1k4.chatwitch.com%2Fmysts%2Findex.php",
    "Connection" : "keep-alive",
    "Content-Type" : "application/x-www-form-urlencoded",
    "Content-Length" : "64",
    "DNT" : "1",
    "Origin" : "http://a1k4.chatwitch.com",
    }

dblesspayload = {

    "user" : username,
    "password" : password,
    "submitbtn" : "Submit",
    "a" : "",
    "head" : "",
    }

with requests.session() as current:
    print("POSTing login request")
    login = current.post("http://a1k4.chatwitch.com/login/bless.php", headers = hblesspayload, data = dblesspayload, cookies = cblesspayload)
    print("Retrieved response from http://a1k4.chatwitch.com/login/bless.php")
    print(login.headers)

cookiecutter=login.cookies.values()
blessing=cookiecutter[0]

print("Blessing requests with: "+str(blessing))

cmystspayload = {
	"thumbs" : "0",
	"PHPSESSID" : "l2ppe9c3p90n1afn2ds3ghnli1",
	"blessing" : blessing,
	}
	
hmystspayload = {
    "Host" : "a1k4.chatwitch.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-GB",
    "Accept-Encoding" : "gzip, deflate",
    "Referer" : "http://a1k4.chatwitch.com/login/bless.php?a=&user=&url=http%3A%2F%2Fa1k4.chatwitch.com%2Fmysts%2Findex.php",
    "Cookie" : "thumbs=0; PHPSESSID=l2ppe9c3p90n1afn2ds3ghnli1",
    "Connection" : "keep-alive",
    "Content-Type" : "application/x-www-form-urlencoded",
    "Content-Length" : "64",
    "DNT" : "1",
    "Origin" : "http://a1k4.chatwitch.com",
    }

def get_friends():
    with requests.session() as current:
        print("GETting mysts")
        scan = current.get("http://a1k4.chatwitch.com/mysts/index.php?user="+username+"&blessing="+str(blessing), headers = hmystspayload, cookies = cmystspayload)
        print("Retrieved response from "+"http://a1k4.chatwitch.com/mysts/index.php?user="+username+"&blessing="+str(blessing))
        print(scan.headers)

    with open('FriendList.txt',"r") as textlist:
        friendlist=(textlist.readlines())
        for friends in friendlist:
            if (friends.lower() in scan.text.lower() == True):
                print(friends + " online!")
                winsound.PlaySound("SystemExclamation",winsound.SND_ALIAS)
            else:
                print(friends + " offline")
    threading.Timer(300,get_friends).start()

get_friends()
