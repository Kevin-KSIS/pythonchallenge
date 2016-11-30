# pythonchallenge

# Table of contents

[1. Level 0](#1)

[2. Level 1](#2)

[3. Level 2](#3)

[4. Level 3](#4)

[5. Level 4](#5)

[6. Level 5](#6)

[7. Level 6](#7)

[8. Level 7](#8)

[9. Level 8](#9)

[10. Level 9](#10)

# Contents

<a name="1"></a>
[1. Level 0](http://www.pythonchallenge.com/pc/def/0.html)

 - `2^38` = 274877906944
 - `274877906944.html`

<a name="2"></a>
[2. Level 1](http://www.pythonchallenge.com/pc/def/map.html)
 
 ```
 	K --> M
	O --> Q
 	E --> G
 ```
  ====> Ceasar cipher, key = 2
 ```
 	g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

  	i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
 ```
 - [ceasar_cipher.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/ceasar_cipher.py)
 - `map.html ==> ocr.html`

<a name="3"></a>
[3. Level 2](http://www.pythonchallenge.com/pc/def/ocr.html)

 - Hint: `recognize the characters. maybe they are in the book, but MAYBE they are in the page source.`
 - View source: 
 ```
 	<!--
	find rare characters in the mess below:
	-->
	<!--
	%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
	...
	...-->
 ```
 - [level2.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/level_2.py)
 - `equality.html`

<a name='4'></a>
[4. Level 3](http://www.pythonchallenge.com/pc/def/equality.html)

 - Hint: `One small letter, surrounded by EXACTLY three big bodyguards on each of its sides`
 - exercises: AAAbCCC ==> b
 - [Level 3](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/level_3.py)
 - `linkedlist.html`

<a name="5"></a>
[5. Level 4](http://www.pythonchallenge.com/pc/def/linkedlist.php)

 - Hint: `<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.-->`
 - `http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345`
 - [url-request.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/url-request.py)
 - `peak.html`

<a name="6"></a>
[6. Level 5](http://www.pythonchallenge.com/pc/def/peak.html)

 - View source: (http://www.pythonchallenge.com/pc/def/banner.p)
 - Use pickle lib decode: (https://docs.python.org/3/library/pickle.html)
 - [pickle-load.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/pickle-load.py)
 - `channel.html`

<a name="7"></a>
[7. Level 6](http://www.pythonchallenge.com/pc/def/channel.html)

 - Hint: `<!-- <-- zip -->`
 - Download file from url: (http://www.pythonchallenge.com/pc/def/channel.zip)
 - Read file `readme.txt`: 
```	
	hint1: start from 90052
	hint2: answer is inside the zip
```
 - Unordered list: start from `90052.txt`
 - Then, read the info from the file `channel.zip`
 - [channel.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/channel.py)
 - `oxygen.html`

<a name="8"></a>
[8. Level 7](http://www.pythonchallenge.com/pc/def/oxygen.html)

 - Download picture (http://www.pythonchallenge.com/pc/def/oxygen.png)
 - Get pixel from picture with Image lib
 - [level 7.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/level_7)
 - `integrity.html`

<a name='9'></a>
[9. Level 8](http://www.pythonchallenge.com/pc/def/integrity.html)

 - View comment in source HTML
'''
	un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
'''
 - Use bz2 lib to decompress it and click to the bee
 - [bz2.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/bz2.py)
 - `huge:file`

<a name='10'></a>
[10. Level 9](http://www.pythonchallenge.com/pc/return/good.html)

 - Hint: `connect the dots`
 - View source: two string are first string and second string
 - use polygon of PIL.ImageDraw
 - [ImageDraw.py](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/ImageDraw.py)
 - 'bull.html'

<a name='11'></a>
[11. Level 10](http://www.pythonchallenge.com/pc/return/bull.html)

 - hint: `a = [1, 11, 21, 1211, 111221, `
 - Algorithm: look and say
 - use `group by` of `itertools`
 - [level 10](https://github.com/Kevin-KSIS/pythonchallenge/tree/master/Code/level_7.py)
 - `5808.html`