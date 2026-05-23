# TibebLang

TibebLang is a beginner-friendly educational programming language built using Amharic keywords. The language is designed to help Ethiopian beginners learn programming concepts more naturally using familiar local-language expressions.

TibebLang translates `.yl` source files into executable Python code.

---

CSE ASTU Student Programming Team Project
Group Members	ID_No.
Yeabsira Goitom	UGR/31390/15


# Features

- Amharic-based programming keywords
- Unicode UTF-8 support
- Variables and assignments
- Arithmetic expressions
- Print statements
- if / else statements
- while loops
- Function definitions
- Return statements
- Parser-based architecture
- Python code generation

---

# Project Architecture

TibebLang uses a real parser-based translation architecture.

```text
Source Code (.yl)
        ↓
Lexer
        ↓
Tokens
        ↓
Parser
        ↓
AST
        ↓
Code Generator
        ↓
Python Output (.py)
