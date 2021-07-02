#!/bin/bash
#First we check if the script is run as root (or sudo) if not exit with error
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root" 
	exit 1
fi
#check os id: cat /etc/os-release prints file contents, grep -w gets the line that has the word ID only, cut searchs the line for the '=' symbol and
#it finds only one so it divides it by 2 field one (-f 1) that contains the string 'ID' and field 2 (-f 2) that contains the os ID in my case fedora
os=$(cat /etc/os-release |grep -w ID |cut -d '=' -f 2);
packageManager='';
packages='';
srcDir='files'
dstDir='/usr/share/nginx/html/piazo';
#We use switch case in order to select the package manager and package names  based on the OS id
case $os in
  'centos')
	echo 'centos';
	packageManager='yum';
	packages='python3 nodejs npm pip nginx';
    ;;

  'fedora')
	echo 'fedora';
	packageManager='dnf';
	packages='python3 nodejs npm pip nginx';
    ;;

  'debian')
	echo 'debian';
	packageManager='apt-get';
	packages='python3 nodejs npm build-essential pip nginx';
    ;;

  'ubuntu')
	echo 'ubuntu';
	packageManager='apt-get';
	packages='python3 nodejs npm build-essential pip nginx';
    ;;

  *)
	echo 'UNKNOWN OS';
	exit 1;
    ;;
esac
$packageManager install -y $packages; #installs the packages required
pip install flask --user; #installs flask
npm install -g @vue/cli; #install vue
#If destination dir does not exists we create it with mkdir
if [ -d $dstDir ]; then
	echo 'Dst dir exists';
else
        mkdir -p $dstDir;
fi
#Now we copy the contents of the folder files to the dstDir and change to it.
cp -Rf $srcDir/* $dstDir;
cd $dstDir;
cp $srcDir/site.conf /etc/nginx/conf.d/;
systemctl enable nginx && systemctl start nginx
