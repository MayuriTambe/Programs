from http.client import HTTPConnection

try:
    connection=HTTPConnection("google.com")
    connection.request("GET", "/")
    result=connection.getresponse()
    print(result)

    UrlContent=result.read()
    print(UrlContent)
except:
    print("Invalid URL")
