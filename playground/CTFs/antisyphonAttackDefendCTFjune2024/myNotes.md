

- my team: 
- number: 201
- token: 85JGxGEsmjCScBv3 

`ssh ubuntu@boxes.mctf.io -p 5201` 

- 5000 + Team Number



Our boxes:
"LambdaPyxel" service hosted at http://boxes.mctf.io:1201
"Brightside" service hosted at http://boxes.mctf.io:2201
"Eventdim" service hosted at http://boxes.mctf.io:3201


username: admin 
password: 85JGxGEsmjCScBv3

Connect to services
 `ssh ubuntu@boxes.mctf.io -p 5201`

edit file on server for patching, VM VScode (browser)
https://boxes.mctf.io:9201

tulip for monitoring (browser)
https://boxes.mctf.io:7201 

packet captures (browser)
https://boxes.mctf.io:8201 




## Connecting to enemy services
- find the live active services with: 

```
GET /endpoints HTTP/1.1
Host: scoreboard.mctf.io:8000
Cookie: team-token=85JGxGEsmjCScBv3
team-token: 85JGxGEsmjCScBv3
Content-Length: 618

Sec-Ch-Ua: "Not-A.Brand";v="99", "Chromium";v="124"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i
Connection: keep-alive

```


browser connect / burp:

 `http://boxes.mctf.io:2001/` 


 curl -X POST http://boxes.mctf.io:2001/new_patient -d "export_string=<ENCODED_PAYLOAD>"
