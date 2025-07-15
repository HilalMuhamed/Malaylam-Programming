# 🧾 Malayalam-Inspired Compiler – Python to C Translator

**Malayalam-Inspired Compiler** is a custom compiler developed in Python that translates code written in a Malayalam-like syntax into executable C code. It is designed to support basic programming constructs and demonstrate how compilers function under the hood.

---

## 🔍 Overview

This compiler is capable of:

- Parsing a custom language with **Malayalam-style keywords** and identifiers  
- Translating the syntax into valid **C code**  
- Performing **lexical analysis**, **syntax parsing**, and **code generation**
- Compiling and executing **1000+ lines of source code** in **under 100ms**

The goal is to make programming feel more accessible and native by allowing developers to code using familiar regional-language syntax, while still benefiting from the power of C underneath.

---

## 🚀 Features

- 🌐 **Malayalam Syntax Support**: Write code using Malayalam terms for constructs like `PRINT`, `INPUT`, `WHILE`, etc.
- 🛠️ **Lexical Analyzer**: Tokenizes source input and identifies keywords, identifiers, literals, and operators
- 🧠 **Parser & Code Generator**: Implements grammar rules and emits C code
- ⚠️ **Error Handling**: Detects and reports common syntax errors
- ⏱️ **High Performance**: Can compile large source files quickly (~1000 lines in under 100ms)
- 📄 **Unicode Support**: Handles UTF-8 Malayalam input and output

---

## 🛠️ Tech Stack

### ⚙️ Compiler Components

- **Lexer** – Identifies tokens in source code
- **Parser** – Validates grammar and syntax structure
- **Code Generator** – Translates parsed structure into equivalent C code

### 🧰 Language & Tools

- **Python 3.11+** – Core compiler logic
- **Regular Expressions** – Token parsing and identifier matching
- **indic-transliteration** – Converts Malayalam identifiers to Manglish for valid C naming
- **GCC** – Used to compile the final generated `.c` file
### 📘 Language Syntax Reference

| Malayalam     | Manglish         | English Version  or C Equivalent | Syntax Example                      |
| ------------- | ---------------- | ---------------------- | ----------------------------------- |
| `എഴുതി`       | `ezhuthi`        | `PRINT` (output)       | `എഴുതി "ഹലോ ലോകം"`             |
| `വായിക്കുക`   | `vaayikkuka`     | `INPUT` (user input)   | `വായിക്കുക x`                         |
| `സത്യമെങ്കിൽ` | `sathyamenkil`   | `IF` (condition)       | `സത്യമെങ്കിൽ x > 0 { ... }`        |
| `കലമെങ്കിൽ`   | `kalamenkil`     | `ELSE` (alternative)   |`കലമെങ്കിൽ { ... }`                |
| `എത്രകാലം`    | `ethrakaalam`    | `WHILE` (loop)         | `എത്രകാലം i < 10 { ... }`        |
| `പൂർണ്ണസംഖ്യ` | `poornnasankhya` | `INT` (integer type)   | `പൂർണ്ണസംഖ്യ i = 5`              |
| `ദശാംശം`      | `dashamsham`     | `FLOAT` (float type)   | `ദശാംശം pi = 3.14`              |
| `വാചകം`       | `vaachakam`      | `STR` (string type)    |`വാചകം msg = "ഹലോ"`           |
| `സത്യം`       | `sathyam`        | `BOOL` (boolean type)  |`സത്യം valid = 1`                 |
| `ജോലി`        | `joli`           | `FUNCTION` (function ) |`ജോലി greet(age) { ezhuthi age }` |



### 🧾 Sample Program (Malayalam Syntax)

```
എഴുതി "എത്ര ഫിബോണാച്ചി സംഖ്യകൾ വേണം?"
വായിക്കുക എണ്ണം
എഴുതി ""

പൂർണ്ണസംഖ്യ ക = 0
പൂർണ്ണസംഖ്യ ഖ = 1

എത്രകാലം എണ്ണം > 0 {
    എഴുതി ക
    പൂർണ്ണസംഖ്യ ഗ = ക + ഖ
    പൂർണ്ണസംഖ്യ ക = ഖ
    പൂർണ്ണസംഖ്യ ഖ = ഗ
    പൂർണ്ണസംഖ്യ എണ്ണം = എണ്ണം - 1
}

```

### 📝 Sample Program (Manglish Syntax)

```
ezhuthi "How many Fibonacci numbers?"
vaayikkuka n
ezhuthi ""

poornnasankhya a = 0
poornnasankhya b = 1

ethrakaalam n > 0 {
    ezhuthi a
    poornnasankhya c = a + b
    poornnasankhya a = b
    poornnasankhya b = c
    poornnasankhya n = n - 1
}

```

### 🧪 Sample C Code 

```
#include <stdio.h>
int main() {
    float n;
    int a, b, c;

    printf("How many Fibonacci numbers?\n");
    scanf("%f",&n);
    printf("\n");

    a = 0;
    b = 1;

    while (n > 0) {
        printf("%.2f\n", (float)a);
        c = a + b;
        a = b;
        b = c;
        n = n - 1;
    }
    return 0;
}
```

