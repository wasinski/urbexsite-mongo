Urbex Site
======
[![Build Status](https://travis-ci.org/wasinski/urbexsite.svg?branch=develop)](https://travis-ci.org/wasinski/urbexsite)

this project is in an hatching state, and for now more of a playground than a real deal, but who knows what will come out of it?

A lot of the **code is scattered on many branches**, so pls. do not just checkout master and develop.

About
------
Urbex Site aims to be a site where urban explorers can safely exchange
abandoned (or not) locations to explore.
With most of the sites up on the net there is one problem: they are more or less
open to vandals, taggers, scrappers etc., because of that locations get ruined, and explorers don't want to share most interesting locations. This project is hopefully going to deal with that issue.

###### Tech. stack:
This project is using **Django** and **Django REST Framework** on the backend.
Frontend part is **currently** setup for React stack, but it won't be developed by me [@wasinski](https://github.com/wasinski/) (I thought about it but dropped the idea), so if some frontend dev. wishes to take part in this project feel free to contact me, whichever is the tech. of your choosing.

Install
------
**Vagrant** and **Ansible** v2 are required. After clone run `vagrant up` -> `vagrant ssh`
and `run` on the guest machine. This should bring up a **tmux** session with 4 terminals,
including **Django** on the backend and **Webpack** on the front.

Authors
------
[@wasinski](https://github.com/wasinski/)
