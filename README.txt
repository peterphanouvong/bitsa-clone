## DOWNLOADS ##
download django : https://docs.djangoproject.com/en/2.2/intro/install/
download python : https://www.python.org/downloads/

## WORKING WITH TERMINAL / POWERSHELL ##
go to bitsa-website/mysite directory in terminal
  - clone the files onto your computer
  - open up powershell (windows) or terminal (mac)
  - into the terminal type 'ls' (list stuff) then enter to see all the stuff in that directory
  - into the terminal type 'cd' (change directory) to change directory into one of the stuff you saw when you did the 'ls'         command. You should be able to get to your Desktop or Documents or Downloads or wherever you cloned the website files         onto your computer.
  
  (You'll be doing that a lot so a quick tip with terminal is pressing up and down keys to use previous commands)
  
  - continue to cd and ls until you cd into the folder called 'mysite'. (the one after 'bitsa-website')
  - if you 'ls' now you should see a file called 'manage.py'
  
## RUNNING THE SERVER ##
type "python manage.py runserver" and hit enter in terminal
You'll see a url which you can copy and paste into any web browser and itll load a local version of the website!!
to stop the server typ ctrl+c into terminal

## MAKING CHANGES ##
most of the relevant files are in mysite/blog/templates/blog
if you want to make changes to the website you should be able to just type it into the files and save and then refresh the page to see it update.
if that doesn't work try stopping the server and then running it again.
