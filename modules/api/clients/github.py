import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    
    def search_repo(self, name):
        r = requests.get(
                        "https://api.github.com/search/repositories",
                        params={"q": name}
        )
        body = r.json()

        return body


 #This part of the code was for independent study 
    #and was not part of the lecture material   
    def get_emojis_list(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body


    def get_commit_list(self):
        r = requests.get("https://api.github.com/repos/Kleunod/QAcourse/commits")
        body = r.json()

        return body