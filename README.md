# Hantverk Syntax Checker

 A final project for the subject Programming Language, that checks the syntax of
 the Hantverk Language developed back during midterms

---

## Table of Contents

- [Hantverk Programming Language](#hantverk-programming-language)
- [Syntax Checker](#syntax-checker)
- [Sample Code](#sample-code)
  - [Window](#window)
  - [Player](#player)
  - [Other Sample Code](#other-sample-codes)
- [How to Run](#how-to-run)
  - [Using Anaconda or Conda (Environment)](#using-anaconda-or-conda-environment)
  - [Using Python (Standalone)](#using-python-standalone)
- [Running the Program](#running-the-program)
- [Resources for Development](#resources-for-development)

---

## Hantverk Programming Language

Hantverk is a (supposedly) new programming language that will help in game
development by simplifying the process of development in a way that it provides
a framework that handles the setup of the main window, title, and layout. This
will allow the developers to focus on adding engaging features to the game and
not worry about the setup of the game window.

## Syntax Checker

The syntax checker is a program that checks the syntax of the Hantverk Language.
As of now, this program only acts as a parser or a syntax checker. It checks the
syntax of the Hantverk Language and outputs the errors found in the code like how
a compiler would do.

## Sample Code

### Window

A sample code that creates a window with a title "Game Title" and maximizes the
window.

```hantverk
use hantverk.hantverkui.Window;
use hantverk.hantverkui.lsiteners.KeyListener;
use hantverk.hantverkui.lsiteners.Event;

template Main ext Window modded KeyListener {
    fn main() {
        my->title = "Game Title";
        my->dimension = Window->Dimension->MAXIMIZED;
        my->state = Window->State->MAXIMIZED;
        
        my->setUI();
        
        my->show();
    }
    
    fn setUI() {
        my->setLayout();
    }
    
    ::Overwrite
    fn keyUp(Event e) {}
    
    ::Overwrite
    fn keyDown(Event e) {}
    
    ::Overwrite
    fn keyPressed(Event e) {}
}
```

### Player

A sample code for a Player template that extends the Entity template.

```hantverk
use hantverk.hantverkui.GameObject;

template Player ext Entity {
    fn Player() {
        parent();
    }
    
    ::Overwrite
    fn clientRun() {
        my->paint(
            my->position,
            my->drawSprite()
        )
    }
}
```

### Other Sample Codes

This sample code provides the other basic functionalities of the Hantverk
Language, along with how declarations, assignments, and function calls are
done in the language. A basic logging function is also provided in the code
in the form of `log()` function.

```hantverk
use util.Math;

template SampleCodes {
    fn main() {
        str txt = "Sample string";
        str literal = `{txt} literal`;
        
        log("Strings:");
        log(txt);
        log(literal);
        log(`Lengths: [txt: {txt.len}, literal: {literal.len}]`);
        
        arr<int> ary = [1, 2, 3, 4, 5];
        
        log("\nArrays:");
        log(ary);
        log(arr->size);
        
        map<str, flt> mp = [
            "pi" => Math->PI,
            "e" => Math->E,
            "tau" => Math->TAU
        ];
        
        log("\nMap:");
        log(mp);
        log(map->size);
        
        log("\nLogs:");
        log("Debugging log", Log->DEBUG);
        log("Information log", Log->INFO);
        log("Warning log", Log->WARNING);
        log("Error log", Log->ERROR);
    }
}
```

## How to Run

### Dependencies Installation

The project has several dependencies that are needed. To install these dependencies, just follow one of the items below.

#### Using Anaconda or Conda (Environment)

When using Conda, you can open to the directory using a terminal. If Python is able to run
in your terminal, then you could use the following command:

```bat
conda install --f "requirements.txt"
```

#### Using Python (Standalone)

Using a standalone python without environments such as Miniconda or Anaconda, you could simply use the `pip` command in your terminal.

```bat
pip install -r "requirements.txt"
```

### Running the Program

There's already a bat file created to run the program. Though, you could still manually run the program by just simply typing the command below in the terminal while pointed inside the project directory:

```bat
python main.py
```

The alternative is of course, run the batch file by simply typing the command below:

```bat
hvsyntax
```

The batch file also allows you to create a shortcut for the program so you can just access the program via that batch file.

### Resources for Development

- [Writing your own programming language and compiler with Python - Marcelo Andrade (Medium)](https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)
- [I wrote a programming language. Here’s how you can, too. - William W Wold (Free Code Camp)](https://www.freecodecamp.org/news/the-programming-language-pipeline-91d3f449c919/)
- [Generating Lexers (rply Documentation)](https://rply.readthedocs.io/en/latest/users-guide/lexers.html)
- [Generating Parsers (rply Documentation)](https://rply.readthedocs.io/en/latest/users-guide/parsers.html)
- [Writing a Tokenizer - ndesmic (Dev.to)](https://dev.to/ndesmic/writing-a-tokenizer-1j85)
