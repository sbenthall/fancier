
# fancier

A [fancier](https://en.wikipedia.org/wiki/Pigeon_keeping) is somebody who keeps pigeons.

This repository contains scripts for managing a Twitter account.

## Congiguration

The file `config.ini.example` must be completed with
accurate information and renamed `config.ini` for the
script to work.

## Removing inactive friendships

To unfollow Twitter users that have been inactive within
some number of days (90, by default) who also do not
follow you back, run:

'''
python3 remove-inactive-followers.py
'''

## Python Package Requirements

* twitter