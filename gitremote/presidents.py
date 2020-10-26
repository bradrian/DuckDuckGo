import requests


url_ddg = "https://api.duckduckgo.com"

def get_presidents():
    q = "presidents of the united states"
    resp = requests.get(url_ddg + "/?q=" + q + "&format=json")

    rsp_data = resp.json()

    return rsp_data["RelatedTopics"]


def main():
    print(get_presidents())

main()
