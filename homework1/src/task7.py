import requests

def get_status_code(url):
    #returns a status code for a given url
    response = requests.get(url)
    return response.status_code

if __name__ == "__main__":
    print(get_status_code("https://www.example.com"))

