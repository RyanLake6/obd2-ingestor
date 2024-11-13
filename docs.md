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













 PS C:\Users\Ryan Lake\Documents\Tech Projects\obd2-ingestor> python .\main.py
testing port: 135
Connected to OBD-II sensor at 192.168.0.150:135
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 137
Failed to connect to 192.168.0.150:137 - [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions
testing port: 139
Connected to OBD-II sensor at 192.168.0.150:139
exception on port 139
testing port: 445
Connected to OBD-II sensor at 192.168.0.150:445
Failed to send command: [WinError 10054] An existing connection was forcibly closed by the remote host
Failed to send command: [WinError 10054] An existing connection was forcibly closed by the remote host
Failed to send command: [WinError 10054] An existing connection was forcibly closed by the remote host
The response is:  None
testing port: 3306
Connected to OBD-II sensor at 192.168.0.150:3306
exception on port 3306
testing port: 5040
Connected to OBD-II sensor at 192.168.0.150:5040
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 6666
Connected to OBD-II sensor at 192.168.0.150:6666
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 8080
Connected to OBD-II sensor at 192.168.0.150:8080
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 27036
Connected to OBD-II sensor at 192.168.0.150:27036
Failed to send command: timed out
Failed to send command: [WinError 10054] An existing connection was forcibly closed by the remote host
Failed to send command: [WinError 10054] An existing connection was forcibly closed by the remote host
The response is:  None
testing port: 33060
Connected to OBD-II sensor at 192.168.0.150:33060
Response: ♣
♣→
Response: 
Failed to send command: [WinError 10053] An established connection was aborted by the software in your host machine
The response is:  None
testing port: 49664
Connected to OBD-II sensor at 192.168.0.150:49664
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 49665
Connected to OBD-II sensor at 192.168.0.150:49665
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 49666
Connected to OBD-II sensor at 192.168.0.150:49666
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 49667
Connected to OBD-II sensor at 192.168.0.150:49667
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 49668
Connected to OBD-II sensor at 192.168.0.150:49668
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None
testing port: 49684
Connected to OBD-II sensor at 192.168.0.150:49684
Failed to send command: timed out
Failed to send command: timed out
Failed to send command: timed out
The response is:  None