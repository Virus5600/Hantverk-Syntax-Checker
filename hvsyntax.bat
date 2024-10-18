echo off
cls
@REM %n defines an argument that's been defined on startup.
@REM %* defines all the argument that's been defined on startup.

@REM LOOP == loopChecker
set LOOP="1"

@REM PREFIX == includePrefix
set PREFIX="0"

@REM DEBUG == debugMode
set DEBUG="0"

set isHelp="0"
for %%a in (%*) do (
	@REM LOOP
	if [%%a] == [--loop] set LOOP="1"
	if [%%a] == [-l] set LOOP="1"
	if [%%a] == [--no-loop] set LOOP="0"
	if [%%a] == [-nl] set LOOP="0"

	@REM PREFIX
	if [%%a] == [--include-prefix] set PREFIX="1"
	if [%%a] == [-ip] set PREFIX="1"
	if [%%a] == [--no-prefix] set PREFIX="0"
	if [%%a] == [-np] set PREFIX="0"

	@REM DEBUG
	if [%%a] == [--debug] set DEBUG="1"
	if [%%a] == [-d] set DEBUG="1"
	if [%%a] == [--no-debug] set DEBUG="0"
	if [%%a] == [-nd] set DEBUG="0"

	@REM HELP
	if [%%a] == [--help] set isHelp="1"
	if [%%a] == [-h] set isHelp="1"

	if %isHelp% == "1" goto help
)

if %isHelp% == "0" goto runProgram

@REM Show help
:help
echo Runs the Hantverk Syntax Checker program with a pre-defined options.
echo [0m
echo Usage: hvsyntax [--]
echo [0m
echo [32m-l, --loop[0m			Allows the program to loop continuously [33m[Default loop option][0m
echo [32m-nl, --no-loop[0m			Turns off the continuous loop
echo [0m
echo [32m-ip, --include-prefix[0m		Includes the prefix (if there's any) of the token keys
echo [32m-np, --no-prefix[0m		Discards the prefix (if there's any) of the token keys [33m[Default prefix option][0m
echo [0m
echo [32m-d, --debug[0m			Enables the debug mode for the program, allowing logging
echo [32m-nd, --no-debug[0m			Disables the debug mode for the program, preventing the program from logging [33m[Default debug option][0m
echo [0m
echo [32m-h, --help[0m			Shows this message

goto end

@REM Run the syntax checker program
:runProgram
python com/teamang/hvsyntax/main.py %LOOP% %PREFIX% %DEBUG%

goto end

@REM End the program
:end
echo on
