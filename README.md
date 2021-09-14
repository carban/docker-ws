# Docker Flask App and Google Spreadsheets

## Build

```
docker build -t appflask .
```

## Run

**IMMPORTANT** For run this container you need the key/toker file `key.json`. This work is inspire in this [link](https://gspread.readthedocs.io/en/latest/oauth2.html).
**Without this file the container will not run**.

```
docker run --rm -it -p 5001:5000 -v $(pwd):/workdir -d appflask
```

## Consuming the web service

```
curl http://localhost:5001/
```

```
curl -X POST -H "Content-type: application/json" -d '{"row": "3", "col": "2"}' http://localhost:5001/obtenervalor
```

```
curl -X POST -H "Content-type: application/json" -d '{"row": "3", "col": "2", "val": "message"}' http://localhost:5001/ponervalor
```

