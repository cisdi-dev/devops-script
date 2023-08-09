#!/bin/bash

sed -i "s#type: file#type: string#g" $1

python3 main.py -i $1 -e $2