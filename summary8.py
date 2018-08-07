# Third party packages
# Package Management
# PyPI = Repository of software for the Python programming language
# pip: the Python package manager

# Install/Uninstall a package
$ pip install package_name
$ pip uninstall package_name
# Upgrade an existing package to the newest version
$ pip install --upgrade package_name
# Install from requirements file
$ pip freeze > requirements.txt
$ pip install -r requirements.txt

# File: requirements.txt
ipython==4.2.0
matplotlib==1.5.1
numpy==1.11.0
pandas==0.18.0
pep8==1.7.0
Pillow==3.2.0
requests==2.9.1
scipy==0.17.0

# common pip commands
# Install to Python user-specific install directory
$ pip install --user package_name
# Require specific versions to be installed
$ pip install "package_name==4.1.0"
$ pip install "package_name >= 1.0, != 1.4.0, < 2.0"
# Show information about a particular package
$ pip show package_name
# Search PyPI for matching packages
$ pip search query

# The very best Third party packages
# 1) requests: HTTP for Humans
# ref : http://docs.python-requests.org/en/master/user/quickstart/

# eg)
#  A simple GET request
response = requests.get('https://api.example.com/users')
if response.ok:
    raw_data = response.content
    json_data = response.json() # If server response is in
# client(chrome/python) -> server(google.com)

# eg)
# GET with params
payload = {'name': 'sredmond', 'field': ['email', 'org']}
response = requests.get('https://api.example.com/users', params=payload)
print(response.url)
# => https://api.example.com/users?name=sredmond&field=email&field=org

# POST with params
payload = {'username': 'sredmond', 'password': 'pyth0n'}
response = requests.post('https://api.example.com/login', data=payload)

# Intro to Scientific Python
# CME 193

# 1) NumPy (Numerical Python)
# N-dimensional array object
# Sophisticated functions
# Capabilities
# Linear algebra
# Fourier transform
# Random sampling
# Read the docs

# Using numpy
a = np.arange(15).reshape(3, 5)
print(a)
# array([[ 0, 1, 2, 3, 4],
# [ 5, 6, 7, 8, 9],
# [10, 11, 12, 13, 14]])
print(a.shape) # => (3, 5)
print(a.ndim) # => 2
print(a.dtype.name) # => 'int64'
print(type(a)) # => numpy.ndarray
print(a[:, 1]) # => array([ 1, 6, 11])

a = np.array([3, 4, 5])
a + 4 # => array([7, 8, 9])
a * 1.5 # => array([ 4.5, 6. , 7.5])
b = np.array([4, -1, 0])
np.dot(a, b) # => 8 (= 3 * 4 + 4 * -1 + 5 * 0)
a.sum() # => 12
space = np.linspace(0, 2 * np.pi, 100)
sinusoid = np.sin(b)

# 2) SciPy (Scientific Python)
# Everything you need for mathematics, science, and engineering.
# https://docs.scipy.org/doc/scipy/reference/index.html

# eg)
from scipy import spatial, linalg
# Build a KD Tree
points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
tree = spatial.KDTree(points)
tree.query([0.1, 0.1]) # => (0.14142135623730953, 0)
# Invert a matrix
A = np.array([[1, 2], [3, 4]])
print(linalg.inv(A))
# array([[-2. , 1. ],
# [ 1.5, -0.5]])

# 3) Matplotlib
# eg)
import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# 4) tensorflow (MI)
# 5) keras (Deep Learning)
# 6) scikit-learn (ML)
# 7) nltk (Natural Language)

# Development Tools
# 1) PEP8 and AutoPEP8
# Style Enforcers for PEP8 – Python's Style Guide
# PEP8 identifies errors
# AutoPEP8 fixes errors
# http://pep8.readthedocs.io/en/latest/intro.html
# https://github.com/hhatto/autopep8

# Using PEP8 and AutoPEP8
# Print PEP8 errors
$ pep8 mystery.py
mystery.py:18:1: E302 expected 2 blank lines, found 1
mystery.py:22:19: E231 missing whitespace after ':'

# Overwrites file.py for PEP8 compliance
$ autopep8 --in-place --aggressive --aggressive file.py

# Web Frameworks
# 1) Flask
# eg) file: hello.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)

# Run a local server
$ python hello.py
# * Running on http://localhost:5000/

# 2) Django Hello World : SKIPPED
# 3) Twisted : Asynchronous, event-driven. Networking engine. Fast, but complicated
# 4) Bottle

# Other neat packages
# Selenium – Automated web client
# Dateutil – Better date/time handling
# SQLAlchemy – Build objects on top of database schemas
# bcrypt / cryptography – Cryptographic tools
# scrapy – Web scraping
# pandas – Vectorized data manipulation
# boto – Python interface to Amazon Web Services
# PyEphem – Track planets and satellites.
# Basemap – Plot 2D data on maps.
# PRAW – Play with reddit's API, write a reddit bot.
# robobrowser / mechanize – Automate web tasks.
# networkx – Visualize small graphs.
# BeautifulSoup – Rapidly prototype HTML parsers.
# pygame – Basic game-playing tools.
# GOvals and GRects?

# MOST IMP
# https://docs.python.org/3.4/library/index.html#library-index
# https://docs.python.org/3.4/reference/index.html