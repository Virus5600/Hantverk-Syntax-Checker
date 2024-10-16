# Hantverk Syntax Checker
 A final project for the subject Programming Language, that checks the syntax of
 the Hantverk Language developed back during midterms

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