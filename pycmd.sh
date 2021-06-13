#!/usr/bin/env bash

case $1 in
reinstall)
  pip uninstall pytrx
  python setup.py install
;;
esac