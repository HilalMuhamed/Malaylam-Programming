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
