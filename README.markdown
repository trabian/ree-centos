# A Recipe for a Ruby Enterprise Edition RPM on CentOS

## Create an RPM Build Environment: The Vagrant way

If you're familiar with Vagrant (http://vagrantup.com), just do the following:

    vagrant up
    vagrant ssh

## Create an RPM Build Environment: The Manual way

You'll need to perform these tasks:

### Prepare the RPM Build Environment

    yum install rpmdevtools
    rpmdev-setuptree

### Install Prerequisites for RPM Creation

    yum groupinstall 'Development Tools'
    yum install readline-devel ncurses-devel gdbm-devel db4-devel

### Download REE

    cd /tmp
    wget http://rubyenterpriseedition.googlecode.com/files/ruby-enterprise-1.8.7-2012.02.tar.gz
    cp ruby-enterprise-1.8.7-2012.02.tar.gz ~/rpmbuild/SOURCES/

### Get Necessary System-specific Configs

    git clone git://github.com/dwradcliffe/ree-centos.git
    cp ree-centos/spec/ruby-enterprise.spec ~/rpmbuild/SPECS/
    cp ree-centos/patches/ssl_no_ec2m.patch ~/rpmbuild/SOURCES/

## Build the RPM

    cd ~/rpmbuild/
    # the QA_RPATHS var tells the builder to ignore file path errors
    QA_RPATHS=$[ 0x0002 ] rpmbuild -ba SPECS/ruby-enterprise.spec

The resulting RPMs (one for REE, one for REE's Rubygems) will be:

    ~/rpmbuild/RPMS/x86_64/ruby-enterprise-1.8.7-2.x86_64.rpm
    ~/rpmbuild/RPMS/x86_64/ruby-enterprise-rubygems-1.3.5-2.x86_64.rpm

Remember to build the RPM using an unprivileged user! More information on http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch-creating-rpms.html

## Credits

Based on the `ruby-enterprise.spec` file from Adam Vollrath, found
on [GitHub as a Gist][gs].

 [gs]: http://gist.github.com/108940