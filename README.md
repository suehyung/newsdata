# Logs Analysis Project
This is source code for a simple script that generates three reports from a SQL database.

## 1. INSTALLATION
It is assumed that Vagrant 2.0.1, newsdata.sql, and the database are already installed.

Clone the GitHub repository from Bash prompt:

`$ cd [Vagrant folder]`<br>
`$ git clone https://github.com/suehyung/newsdata.git`<br>
`$ cd newsdata`

Install Python 2.7, if not already installed:

`https://www.python.org/downloads/`

## 2. USAGE
Run the virtual machine from the terminal:

`$ vagrant up`<br>
`$ vagrant ssh`

Run the Python script:

`$ cd /vagrant/newsdata`<br>
`$ python news-report.py`

The script will generate text comprising the 3 reports from the SQL database.