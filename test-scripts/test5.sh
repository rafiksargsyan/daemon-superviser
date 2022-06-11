#!/bin/bash

if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1