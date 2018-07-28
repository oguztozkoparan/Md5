**[UNDER DEVELOPMENT] MD5-DECODE-ENCODE.V1**

This tool provides decoding-encoding with MD5.

**WARNING:** You need to download word lists for decrypt method!

```
  usage: md5.py [-h] [-hs HASHOBJECT] [-p FILEPATH] [-e | -d]
     -h, --help            show this help message and exit
     -hs HASHOBJECT, --hashobject HASHOBJECT use as : -hs [string] or --hashobject [string]
     -p FILEPATH, --filepath FILEPATH use as : -p [filepath] or --filepath [filepath]
     -e, --encode          use as:-hs [object] -e
     -d, --decode          use as: -hs [object] -p [path] -d

    Example:
      CommandLine ~$ python3 md5.py -hs [hash object here] -e

      CommandLine ~$ python3 md5.py -hs [hashed object here] -d

      CommandLine ~$ python3 md5.py -hs hashing -e

      ENCODED: 72a40ac74b7a2472826f306f02e508fc

      CommandLine ~$ python3 md5.py -hs 72a40ac74b7a2472826f306f02e508fc -p home/user1/Desktop/wordlist -d

      DECODED OBJECT: 72a40ac74b7a2472826f306f02e508fc RESULT: hashing

      TOTAL TIME: 0.0638728141784668 SECONDS
```
Attention:Only Educational Purposes.
