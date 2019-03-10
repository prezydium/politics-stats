import requests
import analyzer


print("Welcome to the word of polish politics")


list_of_webpages = ["http://www.gazeta.pl", "http://www.niezalezna.pl", "http://www.onet.pl", "http://www.tvp.info"]
list_of_names = ["kaczyńsk", "tusk", "morawiecki", "schetyna", "biedroń", "dulkiewicz"]
result = {}

for web in list_of_webpages:
    req = requests.get(web)
    result[web] = analyzer.analyze(req.text, list_of_names)

for k, v in result.items():
    print(k, v)
