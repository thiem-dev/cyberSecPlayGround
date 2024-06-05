# Cyber Games Main

Flag type:
`SIVUSCG{xxxxx}`

## Certified

### Task 
```
Certified
100
One of our machines was recently hit with malware and appears to have opened a backdoor. We were able to get this PCAP from around the time when it was accessed but aren't sure what was exfiltrated from the network. Take a look and see if you can make sense of it!

Author: tsuto

https://ctfd.uscybergames.com/files/6f9d8cad46a69ec3408cc68560d9cf64/certified.pcapng?token=eyJ1c2VyX2lkIjoxOTYyLCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoyODR9.Zl8ZzQ.CeNN3KtBazLgH3kKEPxxpYsItzM

```

### My Solve

- Given a pcap file we can see there are exports available. We export the backdoor.php files
- take a look into them and see the cert and the RSA keys. 
  - separate the key to into a cert and key.pem (RSA) file 
  - then in wireshark, edit preferences, add the TLS RSA key in. 
  - then follow the TLS stream again and you'll see the message. 

`SIVUSCG{c3rtif1abl3_h4ck3rs}`

![alt text](certified.png)


## Touch Grass [Web]

### Task 

### My solve


## Unravel 

### Task
```
Unravel
331pts
This challenge has several parts. You are given a PCAP which shows how to attack the service provided below. Reverse the attack to gather and decrypt an unravel{} flag, then provide that to the API (/api/submit_flag) to gain the SIVUSCG{} flag to submit here.

Additional details are provided on the index page of the challenge.

https://ctfd.uscybergames.com/files/302e6b0827e0efc5a05ba792c62a4e42/unravel_exploit.pcap

https://uscybercombine-s4-unravel.chals.io/
```

### My Solve 


- burp : https://uscybercombine-s4-unravel.chals.io/ 



## Emoticonsole
### Task 
```
462
Finally, a programming language that is Gen Z approved!

Author: tsuto

https://ctfd.uscybergames.com/files/2a0330a42fa526e85a0e5333b10a8873/program.emo
https://ctfd.uscybergames.com/files/08f708f633199eb11e5113999d3d3d5b/runtime.pyc

```

### My Solve

- used a python decompiler on the .pyc file 

