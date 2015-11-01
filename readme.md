# hungryStack V0.1.0
A reverse Polish Notation stack-orientated language written in Python.

# Instalation - Windows
To install hungryStack download the exe [here](https://www.github.com/ScratchOs/hungryStack/dist/stack.exe).

Then you will need to add the location that you downloaded the file into to your `path` variable.  You can do this by opening the command prompt and then typing `rundll32 sysdm.cpl,EditEnvironmentVariables` to get up the dialouge to edit environment variables. Then paste the location of `stack.exe` into the `path` variable.  makesure that there is a `;` between the rest of `path` and the location you have pasted.  You should now be able to run `stack` from command prompt.  You mayy have to restart it for the changes to take effect.
# Building - Windows
1. Install python 3.5
2. In command prompt type `pip install pyinstaller`
3. Download this repositry
4. In command prompt go to the main folder of this repositry on you computer. that you have downloaded.
5. In command prompt type `pyinstaller.exe --onefile src\stack.py`
6. The exe will be created in the dist folder.
