# NEWS-APP
## Author
#### Denis Kisavi
## Description
#### This is a web application built using Python framework (Flask) and consumes the NEWS API. The app displays different News Sources and articles from different news sources.
## Requirements
#### A user can perform the following functions
* See various top articles from different news sources on the homepage of the application.
* See various news sources and select on any to see the articles they have.
* See the image, author, title, description and the time a news article was created.
* Click on an article and read the full article from the source website.
## Installation / Setup instruction
### These installations are required in order to run the application:
* python3.6
* pip
* gunicorn
* flask
## Cloning
* On your terminal, run the following commands:
* $ git clone https://github.com/Kisavi/News-app.git
* $ cd News-app
* Create a virtual environment $ pv -m venv --without-pip virtual
* Activate the virtual environment $ source virtual/bin/activate
* Install Dependancies $ pip install -r requirements.txt
* Run the application $ ./start.sh
## Development
#### Want to make a contribution to enhance an existing module or fix a bug? Great!
* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request
## Technology Used
* python3.8
* unittest (Python test framework)
* flask
## Known Bugs
#### 
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Contact Information
* For any inqueries feel free to write to me deniskisavi@gmail.com
## Licence
* MIT License
* Copyright (c) 2022 Denis Kisavi


