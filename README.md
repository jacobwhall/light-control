# Jacob's Light Server

This is a simple webapp I run on a Raspberry Pi to control [my LIFX lights](https://www.lifx.com/products/lifx-color-a19) in my room.

It's tailored to my specific use-case (or, it will be), but it should be easy enough to modify for your own needs. And if you'd like to expand on it and submit a PR, I'd be open to collab :)

## Installation

These are the steps for installing on a Raspberry Pi, although they should translate fairly well to any other Python-running platform

Install python3
```
sudo apt install python3 python3-pip
```
Install Flask
```
sudo pip3 install flask
```
Install [lifxlan](https://github.com/mclarkk/lifxlan)
```
git clone https://github.com/mclarkk/lifxlan.git
cd lifxlan
sudo python3 setup.py install
```
Clone and run this repository
```
git clone https://github.com/jacobwhall/light-control.git
cd light-control
sudo ./web.py
```
I'll add instructions for daemonizing this soon!

## Thanks

A huge thanks to @mclarkk and the other contributors to [lifxlan](https://github.com/mclarkk/lifxlan). Their library has been so easy to work with.

Thanks to @[Elijah1111](https://github.com/Elijah1111) for introducing me to the wonders of Flask. This project was created through the modification of his work.

Thanks to the people who made Flask, whoever they are!
