import requests

BASE_URL = "https://cutt.ly/api/api.php"

def get_api():
    with open("key.txt", "r") as key:
        return key.read()
    
    
def shorten(original_link, link_name):
    payload = {"key": get_api(), "short": original_link, "name": link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()
    
    
    try:
        title = data["url"]["title"]
        new_link = data["url"]["shortLink"]
    
        print("\nTitle: ", title)
        print("Shorten Link: ", new_link)
    except:
        status = data["url"]["status"]
        match status:
            case 1:
                print("Error code 1: the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened")
            case 2:
                print("Error code 2: the entered link is not a link")
            case 3:
                print("Error code 3: the preferred link name is already taken")
            case 4:
                print("Error code 4: Invalid API key")
            case 5:
                print("Error code 5: the link has not passed the validation. Includes invalid characters")
            case 6:
                print("Error code 6: The link provided is from a blocked domain")
            case 7:
                print("Error code 7: OK - the link has been shortened")
            case 8:
                print("Error code 8: You have reached your monthly link limit. You can upgrade your subscription plan to add more links.")
        
        
        
        
link = input("Enter a link to shortener: ")
title = input("Enter a title for link: ")
shorten(link, title)