bandit.labs.overthewire.org

lvl1
bandit1 : NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

lvl2
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

ssh -p 2220 bandit3@bandit.labs.overthewire.org


bandit2@bandit:~$ cat "spaces in this filename" 
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG


bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden 
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

-good 4->5


bandit4@bandit:~/inhere$ find -type f | xargs file | grep text
./-file07: ASCII text

lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

bandit5: ----
bandit5@bandit:~/inhere$ du -ab | grep 1033
1033    ./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

bandit6
find / -user 'bandit7' -group 'bandit6'
/var/lib/dpkg/info/bandit7.password

z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

ssh -p 2220 bandit7@bandit.labs.overthewire.org

bandit7@bandit:~$ cat data.txt | grep millionth
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP

bandit8@bandit:~$ cat data.txt | sort | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t

---------------------------------------------------------------
bandit10@bandit:~$ strings data.txt | grep -E '=+'
=2""L(
x]T========== theG)"
========== passwordk^
Y=xW
t%=q
========== is
4=}D3
{1\=
FC&=z
=Y!m
        $/2`)=Y
4_Q=\
MO=(
?=|J
WX=DA
{TbJ;=l
[=lI
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
>8=6
=r=_
=uea
zl=4

------------------------------------------

bandit11@bandit:~$ base64 -d data.txt 
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

Amount = 13: The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


----------------------------------------------
bandit12@bandit:~$ mktemp -d 
/tmp/tmp.yGWH50t4DK

cat /tmp/tmp.xI7wwEjmMI/text.txt
xxd -r data.txt > data.gz
gzip -d data.gz
bzip2 -d data2.bz2
mv data5.bin data6.tar
tar -xf dat.tar.gz

The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

---------------------------------------------------
ssh -p 2220 bandit13@bandit.labs.overthewire.org

scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .

ssh -p 2220 bandit14@bandit.labs.overthewire.org -i sshkey.private

ssh -p 2220 bandit14@localhost -i sshkey.private



ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGSQ4TzdbZw5PshaEVz1o9ppCZAN2DO5cK/6mlkdr75u5KQ36CDS1yvsXDw0sZrn5TN5zasSDRaZ568HXcAihinQxnIROrjq36OT2m43BnAi31eAFm58a1kTBZsVbD+9Us3A5cF7hRZK0ZFbOA+kR5K/lNvVWMtkgF0amFMgrbYCbPpltOEyyIyfIlp8TAn9Pw9A7ebJL3W9QcS6g4wDOhQgPiQ3QwRnf5dqHIrQclWrrwqxU5t59cbW+8DcYAnb2TElqq9F+BiepmvJY3vDcIeM1Thz/YmSn6fwvRKfFo0D5ZgDuOI/JMXSKzy7MyVhDiXUvOH/z8ym+EJAXyvbZ3 rudy@localhost

-------------------------------------
bandit14 pass: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq


bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!

jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

----------------------------
ssh -p 2220 bandit15@bandit.labs.overthewire.org

openssl s_client -connect localhost:30001 -ign_eof
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

-------------------------------------------------
ssh -p 2220 bandit16@bandit.labs.overthewire.org

JQttfApK4SeyHwDlI9SXGR50qclOAil1

nmap -sV localhost -p 31000-32000 
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo

openssl s_client --connect localhost:31790 

read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1  
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----


^put the RSA key into a file locally into your kali

chmod 700 bandit1617.private

ssh -p 2220 bandit17@bandit.labs.overthewire.org -i bandit1617.private
------------------------------------------

LEVEL 17 -> 18
ssh -p 2220 bandit17@bandit.labs.overthewire.org -i bandit1617.private

bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< p6ggwdNHncnmCNxuAt0KtKVq185ZU7AW
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

---------------------------------------------

ssh -p 2220 bandit18@bandit.labs.overthewire.org cat readme.txt
bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC

ssh -p 2220 bandit18@bandit.labs.overthewire.org -t /bin/sh

------------------------------------------

ssh -p 2220 bandit19@bandit.labs.overthewire.org 

cat bandit20-do
./bandit20-20 id

bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT


----------------------------------------------------
ssh -p 2220 bandit20@bandit.labs.overthewire.org 

strings ./suconnect
(run two terminals as bandit20, nc will listen as the server and give the password if request goes to given port, and suconnect is listening for that pw, and will complete its execution for new pw if it matches)

bandit20@bandit:~$ ./suconnect 2525
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT

bandit20@bandit:~$ echo -n 'VxCazJaVykI6W36BkBU0mJTCM8rR95XT' | nc -l -n 2525
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

-------------------------------
ssh -p 2220 bandit21@bandit.labs.overthewire.org 

cd/etc/cron.d
cat cronjob_bandit22

cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff

-------------------------------------------------
ssh -p 2220 bandit22@bandit.labs.overthewire.org 

bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh

bandit22@bandit:/etc/cron.d$ echo I am user bandit23 | md5sum  
8ca319486bfbbc3663ea0fbe81326349  -
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349 
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G


cat /tmp/8ca319486bfbbc3663ea0fbe81326349 
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

---------------------------------------
ssh -p 2220 bandit23@bandit.labs.overthewire.org 

(because the cronjob runs all files inside /var/spool/bandit24/foo every minute, you need to cp a script from a tmp directory that prints out the pw from bandit24 into your tmp directory, set all permissoins before the cp, because it will run and delete whatever is in there every minute)

cd /etc/cron.d 
cat /usr/bin/cronjob_bandit24.sh

mktemp -d
cd (into the new temp directory)
touch bandit24_pass.sh 
nano bandit24_pass.sh 
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/tmp.GF4kvY3VJ1/password.txt

chmod 777 password.txt
chmod 777 bandit24_pass.sh

cp bandit24_pass.sh /var/spool/bandit24/foo

bandit23@bandit:/tmp/tmp.GF4kvY3VJ1$ ls -l
total 12
-rwxrwxrwx 1 bandit23 bandit23 77 May 15 19:42 bandit24_pass.sh
-rwxrwxrwx 1 bandit23 bandit23 33 May 15 19:45 password.txt
bandit23@bandit:/tmp/tmp.GF4kvY3VJ1$ cat password.txt 
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar


