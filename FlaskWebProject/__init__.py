"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import FlaskWebProject.views
import FlaskWebProject.helper
import FlaskWebProject.tokens
