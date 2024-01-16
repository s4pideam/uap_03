
# Übersetzung und Analyse von Programmen

|                |                          |
|----------------|--------------------------|
| Name           | Pierre-Jordan de Amezaga |
| Matrikelnummer | 1133913                  |
| Email          | s4pideam@uni-trier.de    |

## Projekt 3

### Änderungen

```console
let m(x, y) {
    if (x == 0) then
        y * 2
    else
        let n(x, z) {
            x - y * z
        } in n(3 + x, y)
    }
    n(z, w) {
        while (z > 0) do {
            w = w * m(z, w);
            z = z - 1
        };
        w
    }
in m(2, 3); n(3, 2)
```

``` console
	GOTO L1
L2:	LOAD 0 0
	CONST 0
	EQ
	IFZERO L4
	LOAD 1 0
	CONST 2
	MUL
	GOTO L5
L4:	GOTO L6
L7:	LOAD 0 0
	LOAD 1 1
	LOAD 1 0
	MUL
	SUB
	RETURN
L6:	CONST 3
	LOAD 0 0
	ADD
	LOAD 1 0
	INVOKE 2 L7 0
L5:	NOP
	RETURN
L3:	LOAD 0 0
	CONST 0
	GT
	IFZERO L10
	GOTO L11
L8:	LOAD 0 0
	CONST 0
	GT
	IFZERO L9
	POP
L11:	LOAD 1 0
	LOAD 0 0
	LOAD 1 0
	INVOKE 2 L2 1
	MUL
	STORE 1 0
	LOAD 1 0
	POP
	LOAD 0 0
	CONST 1
	SUB
	STORE 0 0
	LOAD 0 0
	GOTO L8
L10:	CONST 0
L9:	NOP
	POP
	LOAD 1 0
	RETURN
L1:	CONST 2
	CONST 3
	INVOKE 2 L2 0
	POP
	CONST 3
	CONST 2
	INVOKE 2 L3 0
	HALT
```

![code_gen](screenshots/code_gen.png)

**Python Version:** 3.12.0

| Dependencies                                               | Version | Function                                                                                                                   |
|------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------|
| [PySide6](https://doc.qt.io/qtforpython-6/quickstart.html) | 6.6.0   | PySide6 ist das offizielle Python-Modul des Qt for Python-Projekts, das Zugang zum vollständigen Qt 6.0+ Framework bietet. |
| [graphviz](https://graphviz.org/)                          | 0.20.1  | Erstellung und Darstellung von Graphbeschreibungen in der DOT-Sprache der Graphviz-Software zur Graphenzeichnung           |
| [ply](https://www.dabeaz.com/ply/)                         | 3.11    | PLY ist eine Implementierung der Lex- und Yacc-Analysewerkzeuge für Python.                                                |


## Installation Graphviz

Graphviz benötigt die zusätzlichen binaries.

### Windows

```console
winget install graphviz
```

```console
setx PATH "%PATH%;C:\Program Files\Graphviz\bin"
```

### Debian/Ubuntu (apt):
```console
sudo apt-get install graphviz
```
### Red Hat/Fedora (dnf or yum):
```console
sudo dnf install graphviz
sudo yum install graphviz
```

### openSUSE (zypper):
```console
sudo zypper install graphviz
```

### Arch Linux (pacman):
```console
sudo pacman -S graphviz
```

### Alpine Linux (apk):
```console
sudo apk add graphviz
```

### macOS (Homebrew):
```console
brew install graphviz
```

## Installation Python Dependencies
### Unix/Windows/Mac:
```console
pip install -r requirements.txt
```

## Getting Starded
```console
python main.py
```





## Screenshots
![code_gen](screenshots/code_gen.png)
![01](screenshots/01.png)
![02](screenshots/02.png)
![03](screenshots/03.png)
![04](screenshots/04.png)
![05](screenshots/05.png)
