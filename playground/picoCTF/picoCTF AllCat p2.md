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

## Web Exploit Cookies
Change cookie Name value to 18 on the /check endpoint

Use Burpsuite. Proxy-Intercept it for /check endpoint. Peer through site, Rclick send to Intruder parameterize the name variable (sniper, numbers, set 0 - 20 attack)

picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}

## Wireshark doo dooo do doo...
open it in wireshark, right click follow stream, look through the streams for 

Stream 5
Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}