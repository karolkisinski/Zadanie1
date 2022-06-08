
# Zadanie 1

Repozytorium dotyczące zadania numer 1 z przedmiotu Programowanie 
Aplikacji w Chmurze Obliczeniowej.






## Build

Aby zbudować obraz należy użyć poniższego polecenia:

```
  docker build --no-cache -t karolkisinski/zadanie1:latest .
```

## Uruchomienie


```
  docker run --name karolkisinski-flask -p 5000:5000 -d karolkisinski/zadanie1:latest
```

## Uzyskanie informacji (logów)

Aby uzyskać dostęp do logów, należy przejść na podstronę /logs.

[Logi](http://localhost:5000/logs "Logi")

## Uzyskanie informacji o warstwach

Należy użyć polecenia:

```
  docker history karolkisinski/zadanie1:latest
```

## Dowód działania
![dowod_dzialania](https://raw.githubusercontent.com/karolkisinski/Zadanie1/main/screen/working_screen.png "Logo Title Text 1")


## Docker hub

[Docker hub](https://hub.docker.com/repository/docker/karolkisinski/zadanie1 "DHub")