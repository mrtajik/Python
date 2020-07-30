"""
Fun project
not finished just an example
"""
 
import requests

def star():
    api_url="https://api.github.com/search/repositories"
    
    parameters={"q":"stars>5000"}
    res=requests.get(api_url,params=parameters)
    
    response_json=res.json()["items"]
    return response_json

if __name__== "__main__":
    results=star()
    for result in results:
        lang=result["language"]
        stars=result["stargazers_count"]
        name=result["name"]
        print(lang)
        print(stars)
        print(name)


 



 
 