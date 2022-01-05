#!/bin/sh

export FLASH_APP=$(pwd)/app.py

flask run -h 0.0.0.0
