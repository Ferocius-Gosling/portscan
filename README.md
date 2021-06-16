# Portscan

## Requirements
* Необходимы права администратора.

## Start
```python -m scan <host> [-t] [-u] [-p PORT PORT] [-m]```

## Сканирование tcp-портов
```python -m scan localhost -t```

**Вывод**
 
```
TCP 23 TELNET
TCP 53 DOMAIN
TCP 80 HTTP
TCP 135
TCP 445
TCP 853
```
## Сканирование udp-портов
``` python -m scan 8.8.8.8 -u -p 50 60 -m 3```

**Вывод**
 
```
UDP 53 DOMAIN
```