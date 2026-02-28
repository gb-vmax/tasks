#!/bin/bash
pidof -d , -o $(pgrep -u user sleep | sort -n | head -n1) sleep
