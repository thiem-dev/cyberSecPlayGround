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



## Ding-O-Tron
```
100
What came first? The ding...or the flag?

https://uscybercombine-s4-web-ding-o-tron.chals.io/

Author: tsuto
```



```
- `wasm2wat ding.wasm -o ding.wat`
- `wat2wasm ding.wat -o ding.ll`
```

`scheduleTimeoutEvent` seems like an important item



## Tubes Tubes

### Task
```
108
The internet is a series of tubes...

ssh -i id_uscg uscg@tubes.challs.uscybergames.com

https://ctfd.uscybergames.com/files/aa104b91f3aab653308fc7619f3294c8/id_uscg
```

### My Solve

- `ssh -i id_uscg uscg@tubes.challs.uscybergames.com` 
- key not secure enough. change permissions: `chmod 600 id_uscg`
- tcpdump seems like the only binary available for us. `ls /bin /sbin /usr/bin /usr/sbin` 
- once logged in, you'll find the readme that likely hints at focusing on the network. 

```
-bash-5.0$ tcpdump -D
1.ens4 [Up, Running]
2.lo [Up, Running, Loopback]
3.any (Pseudo-device that captures on all interfaces) [Up, Running]
4.bluetooth-monitor (Bluetooth Linux Monitor) [none]
5.nflog (Linux netfilter log (NFLOG) interface) [none]
6.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]

```

- `tcpdump -i ens4` there's just too much data coming in. so let's grep it for the flag
  - `tcpdump -i ens4 | grep "SIVUSCG"` - nope

  - ens4 interface: too much info. so let's capture it into our own wireshark: `ssh -i id_uscg uscg@tubes.challs.uscybergames.com 'tcpdump -i ens4 -w -' | wireshark -k -i -` 
  - any interface: : `ssh -i id_uscg uscg@tubes.challs.uscybergames.com 'tcpdump -i any -w -' | wireshark -k -i -` 
  - we notice something looks odd on the udp (plus it's sending 1337 that's gotta be the hint). So we listen in on it and then see where that takes us, because it's a bunch of pipes and lines. Maybe this has it. 


ssh -i id_uscg uscg@tubes.challs.uscybergames.com 'tcpdump -i any udp -w -' | wireshark -k -i -


- capture the udp and display as hexdump. it's a vertical message. 

`sivuscg{t0t4lly_tub4l4r}`



#### I believe the below is to mislead us. 



- found an json object that i could export with the rsa key 

`ssh -i rsa1.rsa coachelliott@35.229.42.74`

- strange pipes characters found between 56577 -> 1337

ssh -i id_uscg uscg@tubes.challs.uscybergames.com 'tcpdump -i any -w -' | wireshark -k -i -


`echo "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPiyaCvgEnLCL79gS6ak1QjdAlbJ92/t2/rUHh01JCMrILj/iOUxcxjPbg11erUjnrBeRJh24pgMm3aedJNM+yE= coachelliott@uscybergames.org" >> ~/.ssh/authorized_keys` 


wireshark filter to ind a private rsa key `tls.handshake.type == 1`

