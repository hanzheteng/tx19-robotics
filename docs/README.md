## Make a backup file
```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```

## Create a new file and Copy & Paste the following content into the file

First

```
sudo vim /etc/apt/sources_cn.list

or

sudo nano /etc/apt/sources_cn.list

choose whatever editor you want
```


Then copy

```
deb http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse 
deb http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse 
deb http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse 
deb http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse 
deb http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse 
deb-src http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse 
deb-src http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse 
deb-src http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse 
deb-src http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse 
deb-src http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
```



## Change the source file /etc/apt/sources.list into the modified file

``` 
sudo cp /etc/apt/sources_cn.list /etc/apt_sources.list
```
