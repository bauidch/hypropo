## Ino
```
ino init
ino build -m mega2560
ino upload -m mega2560 -p /dev/ttyACM1
ino serial -p /dev/ttyACM1
```
```ctrl-a, then Ctrl-q
Ctrl-a,a,Ctrl-x
```

### 3prt libarys
https://github.com/amperka/ino/issues/164
```
lib
├── TinkerKit
│   ├── TinkerKit.cpp
│   └── TinkerKit.h
src
└──Blink.ino
```
