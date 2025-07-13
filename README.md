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

| Malayalam     | Manglish         | Meaning (C Equivalent) |
| ------------- | ---------------- | ---------------------- |
| `എഴുതി`       | `ezhuthi`        | `PRINT` (output)       |
| `വായിക്കുക`   | `vaayikkuka`     | `INPUT` (user input)   |
| `സത്യമെങ്കിൽ` | `sathyamenkil`   | `IF` (condition)       |
| `കലമെങ്കിൽ`   | `kalamenkil`     | `ELSE` (alternative)   |
| `എത്രകാലം`    | `ethrakaalam`    | `WHILE` (loop)         |
| `പൂർണ്ണസംഖ്യ` | `poornnasankhya` | `INT` (integer type)   |
| `ദശാംശം`      | `dashamsham`     | `FLOAT` (float type)   |
| `വാചകം`       | `vaachakam`      | `STR` (string type)    |
| `സത്യം`       | `sathyam`        | `BOOL` (boolean type)  |

🧾 Sample Program (Malayalam Syntax)

<img width="1110" height="862" alt="image" src="https://github.com/user-attachments/assets/63cc5343-67e3-46b2-b007-d62403a53053" />
<img width="880" height="862" alt="image" src="https://github.com/user-attachments/assets/5f4c0557-b638-4a8b-be96-4a1854f7ef97" />

🧪 Sample C Code 
<img width="986" height="1280" alt="image" src="https://github.com/user-attachments/assets/43de43c8-599f-4de8-962d-13626da7400a" />
