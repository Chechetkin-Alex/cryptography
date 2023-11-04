#!/bin/bash

coverage run -m unittest discover && coverage html && open -a "Google Chrome" htmlcov/index.html
