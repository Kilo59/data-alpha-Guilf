# Plate-reader Automated Data Wrangler
####Input data: Bioscreen derived .CSV file 
####Output: [Spreadsheet](https://docs.google.com/spreadsheets/d/1fJhE1hOMqVvf5T8YHxRATOQ8QHKfujZRym2wk-tYq4I/pubhtml "Output Sheet") | [Plotly: ggplot](https://dashboards.ly/ua-3iqBAQDFa93xVVHraRB3Tm "Plotly Dashboard")
#####[Create Plotly Account](https://plot.ly/)
##Platform Description/Scope:
Create a data processing/analytics platform to process/compute data stored locally and in Google Cloud Applications and output to Web-based interactive front end.  
##Methods and Materials to be Used:
Python/R for data processing/analysis and HTML, CSS, JavaScript/Jquery for Web Front End. Plate reader(Bioscreen C) derived datasets. 
##Form of Completed Work:
“Full Stack” system that allows for users with minimal to no knowledge of programming to: import/convert large raw datasets, perform complex computations and useful analysis, share and visualize the data, easily implement their own specialized computational functions. Well documented code and GitHub repository explaining the implementation of methods. Accompanying documentation exploring/explaining “real world” approaches to similar computational biology problems.     
##Progress Report Schedule:
Weekly(bi-weekly) meeting with Faculty advisors to demonstrate progress, refine function. Well documented GitHub repository. Screen captured videos demonstrating/explaining platform functions to supplement face to face meetings.

###Plate-reader Wells
####[Well Label-Replacement Sheet](https://docs.google.com/spreadsheets/d/1fJhE1hOMqVvf5T8YHxRATOQ8QHKfujZRym2wk-tYq4I/pubhtml)
![Well Guide](https://github.com/SpaceTuna8/data-alpha-Guilf/blob/master/Microplate_simple.PNG?raw=true)
  
##Installation 
* [Obtain OAuth2 credentials from Google Developers Console](http://gspread.readthedocs.io/en/latest/oauth2.html) (Steps 1-4)
* Setup Google Spreadsheet
* Download Zipfile
  * Place JSON authorization file in the same directory as main.py
  * Check config.ini preferences
    * Set google spreadsheet name
    * Set [plotly credentials (username and api key)](https://plot.ly/)
    * Set desired preferences, tolerances 
* [Install & Add to PATH R](https://cran.r-project.org/mirrors.html)
* [Install & Add to PATH Python35](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe)
  * Install python modules gspread & oauth2client

####To Install python modules on Windows:
1. Run commandprompt
2. python -m pip install gspread
3. python -m pip install oauth2client
