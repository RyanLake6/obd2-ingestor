$ nmap -p- 192.168.0.150
Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-11 16:44 Pacific Standard Time
Nmap scan report for 192.168.0.150
Host is up (0.00023s latency).
Not shown: 65519 closed ports
PORT      STATE    SERVICE
135/tcp   open     msrpc
137/tcp   filtered netbios-ns
139/tcp   open     netbios-ssn
445/tcp   open     microsoft-ds
3306/tcp  open     mysql
5040/tcp  open     unknown
6666/tcp  open     irc
8080/tcp  open     http-proxy
27036/tcp open     unknown
33060/tcp open     mysqlx
49664/tcp open     unknown
49665/tcp open     unknown
49666/tcp open     unknown
49667/tcp open     unknown
49668/tcp open     unknown
49684/tcp open     unknown

Nmap done: 1 IP address (1 host up) scanned in 26.34 seconds
