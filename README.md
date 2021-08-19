# mookit-scrapper
*Ready to use Scrapper for Mookit Lectures*
\
\
This automated scrapper has been made using Selenium and BeatifulSoup libraries in Python. 
It scraps latest lectures for any course the user has access to view. The scrapped lecture meta-data is given in form of csv file whose name consists of course name
and number of lectures scrapped. The file shows you week of lecture, lecture name, its duration, and the link to it.
\
\
**How It Works**
\
Once the script is run using python3 (required libraries need to be installed on system), user is asked to enter some details on terminal - mookit username, password, course for which lectures are to be scrapped and finally number of lectures to be scrapped. Once these details have been entered, new chrome window opens 
at the Mookit login page and you are automatially logged in(if details are correct ofcourse) and you are redirected towards that course home page where the scrapping is done and chrome window closes. Now the output csv file (coursename_n.csv) is created in same directory where script file in present. And you have your lectures now :)
\
\
I have included esc201a_10.csv in this repo for demostrating how the output file looks like.

