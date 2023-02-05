# Domain Availability Checker by ChatGPT

This is a simple python script to check the availability and expiration date of a domain from the command line.  

It was written entirely by ChatGPT.  
The only direct change I made to the script was adding the shebang, which ChatGPT suggested I do to make the script easier to run.  

I treated the experiment as if I had no knowledge of the Python language, and merely copied the code it
generated verbatim with each iteration.  
I would then make suggestions or report a problem and the AI would alter the code as needed. 

For the entire transcript of the conversation that generated this code see the file transcript.md.  
Granted this is a simple script, but it took only a few iterations to complete.  
My idea was to have a job I wanted done and see if ChatGPT would write the code needed to perform the task 
without me requiring any coding skills at all.

### UPDATE

I went back and had ChatGPT write a GUI version of the script using TKinter.
It took only a few iterations to generate the final script, although the first run resulted in a properly working GUI app.

To run the GUI version, TKinter will have to be installed on your system.

#### Installing TKinter
Debian/Ubuntu:
```
sudo apt install python3-pip
pip install tkinter
```
Fedora:
```
sudo dnf install python3-pip
pip install tkinter
```
Arch:
```
sudo pacman -S python-pip
pip install tkinter
```
