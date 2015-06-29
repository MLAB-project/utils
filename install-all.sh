#! /bin/sh

sudo cp utils.py /usr/local/lib/python$(python3 -c 'from sys import version_info; print("{}.{}".format(version_info.major, version_info.minor))')/dist-packages/utils.py

sudo chmod +x gerbdim
sudo cp gerbdim /usr/bin/gerbdim
sudo chmod +x mils2mm
sudo cp mils2mm /usr/bin/mils2mm
sudo chmod +x mm2mils
sudo cp mm2mils /usr/bin/mils2mm
sudo chmod +x pst
sudo cp pst /usr/bin/pst
