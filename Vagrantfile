# -*- mode: ruby -*-
# vi: set ft=ruby :

$packages = <<PACKAGES

yum install -y rpmdevtools readline-devel ncurses-devel gdbm-devel db4-devel ruby
yum groupinstall -y 'Development Tools'

PACKAGES

$script = <<SCRIPT

rpmdev-setuptree

ln -s /vagrant/spec/ruby-enterprise.spec ~/rpmbuild/SPECS/ruby-enterprise.spec
ln -s /vagrant/patches/ssl_no_ec2m.patch ~/rpmbuild/SOURCES/ssl_no_ec2m.patch

cd /tmp
wget http://rubyenterpriseedition.googlecode.com/files/ruby-enterprise-1.8.7-2012.02.tar.gz
cp ruby-enterprise-1.8.7-2012.02.tar.gz ~/rpmbuild/SOURCES/

SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "opscode-centos-6.4"
  config.vm.provision "shell", inline: $packages
  config.vm.provision "shell", inline: $script, privileged: false
end
