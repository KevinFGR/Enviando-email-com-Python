# Enviando-email-com-Python
Using python to send automatic emails

## About the project:

<p>This program was made in python using the library Pywin32 used to give the Python the power of work with some Windows tools like the Windows Mail.
The meaning of this project is to send my curriculum automatically to the companie's emails. The script is made in python and does the following actions:</p>
<ul>
<li>Open all the files of folder "arquivos" one by one to get the mail address and the subject;</li>
<li>Get the content of the file "curruculum.html" wich has my HTML curriculum version;</li>
<li>Format and sand the email heaving my curriculum as the body for the address indicated in the file.</li> 
</ul>


## Topics: 

:small_blue_diamond: [Tecnologies used](#technologies-used)

:small_blue_diamond: [Files](#files)

:small_blue_diamond: [How to run the code](#how-to-run-the-code)

## Technologies used:

<ul>
<li>Python</li>
<li>Pywin32</li>
<li>HTML</li>
<li>CSS</li>
</ul>
<div style='display:flex'>
    <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height="60px" width="60px"/>
    <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" alt="HTML logo" height="60px"/>
    <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" alt="CSS logo" height="60px"/>
</div>

## Files:
<ul>
  <li><b>app.py: </b>The main file of the project. this is the file which has the Python script to send the mail;</li>
  <li><b>curriculum.html: </b> this file has the informatio that will be insearted in the body of the E-mail.</li>
</ul>

## Folder "arquivos:"
  <p>This is the folder which you will create the files containing the mails and subjects. inside the folder you can find an exemple file to see how is the sintax. The program will take as an email address the content after the sequence of characters "Email :" and the subject will be what comes after "Assunto a ser colocado no email :". If there's no subject the program will take "Envio de curriculum" as subject.</p>

  <p>The sintax is like this because of the apinfo.com (job site). so you just have to copy the e-mail address and the subject by there and paste in the file.</p>

  <img src='https://user-images.githubusercontent.com/109561598/230694943-069de9a1-6fc6-4238-9c60-e0884cca3e1c.png'  height='450px'/>

## How to run the code:

### Requirements:

<ul>
<li>Python</li>
<li>Pywin32</li>
<li>Windows mail</li>
</ul>
<div style='display:flex'>
    <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height="60px" width="60px"/>
    <img src="https://techcommunity.microsoft.com/t5/image/serverpage/image-id/172206i70472167E79B9D0F?v=v2" height='60px' width='60px'/>
</div>

### Hands-on:
<ol>
  <li>If you don't have Python installed in your computer, you can intall following this link:</li>
  
```
https://www.python.org/downloads/
```
  <li>To install the pywin32 open the your comand propt and set this code:</li>
  
```
pip install pywin32
```
  
  <li>Open the Git Bash in the folder you want to run the project and paste the following code:</li>
 
```
git clone https://github.com/KevinFGR/Enviando-email-com-Python.git
```
  
  <li>Open the folder "Enviando-email-com-Python" and execute the file "app.py".</li>
  <span>OBS: At the first time you run the code your computer suppose to open a window to configurate the sender options.</span>
  
</ol>
 
:small_blue_diamond: [Go to the top](#enviando-email-com-python)