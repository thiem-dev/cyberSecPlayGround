## Commitment Issues
- Download the files, unzip

- cd into main folder, `git log` `git checkout [commit id]`
- cat message.txt

$ cat message.txt
picoCTF{s@n1t1z3_30e86d36}


## Scavenger Hunt
check the source code, js, css
- robots.txt
- .htaccess (apache default file)
- .DS_Store (MAC default files)

picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_fa04427c}

## Shop
- Buy a negative amount of items to get more gold to buy the flag item. Then buy the flag item, and decode the ASCII

![image](https://github.com/thiem-dev/ePortfolio-cyberSecPlayGround/assets/16260510/c8080390-fc86-402e-8b4b-6bc8ba8113aa)


picoCTF{b4d_brogrammer_3da34a8f}

## Speedand Feeds
Put the Gcode into a CNC viewer

![speedandfeed](https://github.com/thiem-dev/ePortfolio-cyberSecPlayGround/assets/16260510/4bcbc09a-b96f-4fd1-9ebf-77fbdc846524)


## Wireshark doo dooo do doo...
open it in wireshark, right click follow stream, look through the streams for 

Stream 5
Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}


## Web Exploit Cookies
Change cookie Name value to 18 on the /check endpoint

Use Burpsuite. Proxy-Intercept it for /check endpoint. Peer through site, Rclick send to Intruder parameterize the name variable (sniper, numbers, set 0 - 20 attack)

picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}


## ARMssembly 0
https://surya-dev.medium.com/armssembly-0-picoctf-8000fa11e2b0 

sudo apt install qemu-user-static && gcc-aarch64-linux-gnu
aarch64-linux-gnu-as -o chall.o chall.S
aarch64-linux-gnu-gcc -static -o chall chall.o

./chall 266134863 1592237099

python -c "print(hex(1592237099))"
0x5ee79c2b


## tunn3l v1s10n
it's a bm


## Matryoshka doll
`binwalk --extract -M dolls.jpg --run-as=root`

```
┌──(kali㉿kali)-[~/_dolls.jpg.extracted]
└─$ cat /home/kali/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt
picoCTF{4f11048e83ffc7d342a15bd2309b47de}  
```


