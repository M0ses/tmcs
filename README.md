# tmcs - The tmate configuration switcher

## Installation
```
sudo make install
```

or

```
PREFIX=$HOME make install
```


## Usage

```
tmcs <profile>
```

## Configuration

Place the following content in $HOME/.tmcs.yml and modify to your needs

```
work:
  host: tmate.example.com
  conf_url: https://www.example.com/tmate.conf

io:
  host: ssh.tmate.io
  port: 22
  rsa-fingerprint: af:2d:81:c1:fe:49:70:2d:7f:09:a9:d7:4b:32:e3:be
  ecdsa-fingerprint: c7:a1:51:36:d2:bb:35:4b:0a:1a:c0:43:97:74:ea:42

home:
  host: tmate.home.com
  port: 23
  ecdsa-fingerprint: 12:34:56:78:90:ab:cd:ef:fe:dc:ba:09:87:65:43:21
  rsa-fingerprint: fe:dc:ba:09:87:65:43:21:12:34:56:78:90:ab:cd:ef

```
