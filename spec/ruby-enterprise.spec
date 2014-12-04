# Package Maintainer: Increment phusion_release to match latest release available
%define phusion_release	2012.02
%define ree_prefix /opt/ruby

Summary: Ruby Enterprise Edition (Release %{phusion_release})
Name: ruby-enterprise
Vendor: Phusion.nl
Packager: Adam Vollrath <adam@endpoint.com>
Version: 1.8.7
Release: 2%{?dist}
License: GPL
Group: Development/Languages
URL: http://www.rubyenterpriseedition.com/

Source0: ruby-enterprise-%{version}-%{phusion_release}.tar.gz

Patch0: ssl_no_ec2m.patch
Patch1: CVE-2014-8080-REXML-billion-laughs-attack.patch
Patch2: CVE-2014-8090-REXML-incomplete-fix-for-CVE-2014-8080.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{phusion_release}-root-%(%{__id_u} -n)
BuildRequires: readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel autoconf gcc unzip openssl-devel db4-devel byacc
BuildRequires: ruby

%description
Ruby Enterprise Edition is a server-oriented friendly branch of Ruby which includes various enhancements:
* A copy-on-write friendly garbage collector. Phusion Passenger uses this, in combination with a technique called preforking, to reduce Ruby on Rails applications' memory usage by 33% on average.
* An improved memory allocator called tcmalloc, which improves performance quite a bit.
* The ability to tweak garbage collector settings for maximum server performance, and the ability to inspect the garbage collector's state. (RailsBench GC patch)
* The ability to dump stack traces for all running threads (caller_for_all_threads), making it easier for one to debug multithreaded Ruby web applications.

%prep
%setup -q -n ruby-enterprise-%{version}-%{phusion_release}
%patch -P 0 -F1

%package rubygems
Summary: The Ruby standard for packaging ruby libraries
Version: 1.3.5
License: Ruby or GPL+
Group: Development/Libraries
Requires: ruby-enterprise >= 1.8
Provides: ruby-enterprise(rubygems) = %{version}

%description rubygems
RubyGems is the Ruby standard for publishing and managing third party
libraries. This rubygems package is for ruby-enterprise.

%build
# no-op

%install
./installer --auto %{ree_prefix} --dont-install-useful-gems --destdir $RPM_BUILD_ROOT --no-dev-docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{ree_prefix}/
%doc source/ChangeLog
%doc source/COPYING
%doc source/LEGAL
%doc source/LGPL
%doc source/NEWS
%doc source/README
%doc source/README.EXT
%doc source/ToDo

# rubygems
%exclude %{ree_prefix}/bin/gem
%exclude %{ree_prefix}/lib/ruby/site_ruby/1.8/rubygems*
%exclude %{ree_prefix}/lib/ruby/site_ruby/1.8/ubygems.rb
%exclude %{ree_prefix}/lib/ruby/site_ruby/1.8/rbconfig

%files rubygems
%{ree_prefix}/bin/gem
%{ree_prefix}/lib/ruby/site_ruby/1.8/rubygems*
%{ree_prefix}/lib/ruby/site_ruby/1.8/ubygems.rb
%{ree_prefix}/lib/ruby/site_ruby/1.8/rbconfig
%doc rubygems/History.txt
%doc rubygems/LICENSE.txt
%doc rubygems/MIT.txt
%doc rubygems/Manifest.txt
%doc rubygems/README.rdoc
%doc rubygems/UPGRADING.rdoc

%post
# Symlink bins (without clobbering!)
if [ ! -f /usr/bin/ruby ]; then
  ln -s %{ree_prefix}/bin/ruby /usr/bin/ruby
fi
if [ ! -f /usr/bin/irb ]; then
  ln -s %{ree_prefix}/bin/irb /usr/bin/irb
fi
if [ ! -f /usr/bin/erb ]; then
  ln -s %{ree_prefix}/bin/erb /usr/bin/erb
fi
if [ ! -f /usr/bin/rdoc ]; then
  ln -s %{ree_prefix}/bin/rdoc /usr/bin/rdoc
fi
if [ ! -f /usr/bin/ree-version ]; then
  ln -s %{ree_prefix}/bin/ree-version /usr/bin/ree-version
fi
if [ ! -f /usr/bin/ri ]; then
  ln -s %{ree_prefix}/bin/ri /usr/bin/ri
fi
if [ ! -f /usr/bin/testrb ]; then
  ln -s %{ree_prefix}/bin/testrb /usr/bin/testrb
fi

%changelog
* Wed Jun 04 2014 David Radcliffe <radcliffe.david@gmail.com>
- Added ssl_no_ec2m patch
- Fixed build/install order
- Linked all bins

* Wed Jun 06 2012 Rafael Felix Correa <rafael dot felix at rf4solucoes dot com dot br>
- Updated for release 2012.02
- Updated doc and file list for rubygems

* Fri May 07 2010 Brad Fults <brad at causes dot com>
- Updated for release 2010.01
- Changed default destination to /opt/ruby via ree_prefix variable
- Fix release variable's use of %{?dist}

* Wed Dec 02 2009 Adam Vollrath <adam@endpoint.com>
- Updated for release 2009.10

* Wed Oct 07 2009 Adam Vollrath and Richard Templet <hosting@endpoint.com>
- Updated for release 20090928

* Wed Jun 10 2009 Adam Vollrath <adam@endpoint.com>
- Updated for release 20090610

* Tue Jun 02 2009 Adam Vollrath <adam@endpoint.com>
- Added check for existing /usr/local/bin/gem
- Added LICENSE and other important document files

* Mon Jun 01 2009 Adam Vollrath <adam@endpoint.com>
- Refactored to use Phusion's installer instead of building from source
- Changed prefix to just /usr/local
- Added check for existing /usr/local/bin/ruby
- Split rubygems into a subpackage

* Sat May 30 2009 Adam Vollrath <adam@endpoint.com>
- Changed Release number convention
- Added tcmalloc support and `make test`

* Tue May 26 2009 Adam Vollrath <adam@endpoint.com>
- Updated for 1.8.6-20090520
- Several small improvements to spec file

* Fri Dec 13 2008 Tim C. Harper <tim.harper@leadmediapartners.com>
- first build of REE package
