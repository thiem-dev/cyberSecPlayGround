
- Instructions for CTF: In an Attack & Defense style CTF, each team starts out with an identical set of vulnerable services. Their goal is to find flaws in these services, patch their own instances of them, and exploit the vulnerabilities they find in other teams's instances to steal flags.


interacting with API

All endpoints are rate limited to 4 requests per minute per team with the exception of the "/submit" endpoint, which is limited to 1000 submissions per minute.

You must send your private team-token in the header.

`https://scoreboard.mctf.io:8000/endpoints (GET)`

Send a request to this endpoint to get a JSON list of all of the available team machines. This list will get updated as more teams join.

`https://scoreboard.mctf.io:8000/live_flags (GET)`

Access this endpoint to see the list of flag identifiers for all available and unexpired flags for all teams except yours.

`https://scoreboard.mctf.io:8000/submit (POST)`

Send your flag (as flag_in in the body) to the scoring engine to be graded. You must send your private team-token in the header.


```js
GET request

const options = {method: 'GET', headers: {'team-token': 'abcd'}};

fetch('https://scoreboard.mctf.io:8000/live_flags', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
POST request

const options = {
  method: 'POST',
  headers: {
    'team-token': 'abcd',
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: new URLSearchParams({flag_in: 'META{XYZ123}'})
};

fetch('https://scoreboard.mctf.io:8000/submit', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```


```
Box services / open ports:

- SSH, for box administration. Each team will receive unique SSH credentials through the MetaCTF platform. Not intended as an attack vector. (OUT OF SCOPE)
  - SSH to boxes.mctf.io on port 5000 + TeamNumber.
- VSCode, to view the code stored on the machine, search for exploits, or work on patches. (You will need to use ssh to actually push the patch in most cases). Use your credentials to access this. Not intended as an attack vector. (OUT OF SCOPE)
  - HTTP to boxes.mctf.io on port 6000 + TeamNumber.
- Tulip, an Attack/Defense traffic visualization tool. Use your credentials to access this. Not intended as an attack vector. (OUT OF SCOPE)
  - HTTP to boxes.mctf.io on port 7000 + TeamNumber.
- TCPDump pcap listings, for forensics. Use your credentials to access this. Not intended as an attack vector. (OUT OF SCOPE)
  - HTTP to boxes.mctf.io on port 8000 + TeamNumber.
The scored services. Intended for attacks. (IN SCOPE)
HTTP to boxes.mctf.io on port 1000/2000/3000 + TeamNumber.
For example, if your team number was Team 1, then a scored service for your team would be hosted on 1000 + 1 = 1001, and you would run curl boxes.mctf.io 1001 to reach it. If you wanted to attack Team 67's instance, 1000 + 67 = 1067, you would send your traffic to boxes.mctf.io:1067.
```


