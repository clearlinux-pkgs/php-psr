#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-psr
Version  : 1.1.0
Release  : 12
URL      : https://pecl.php.net/get/psr-1.1.0.tgz
Source0  : https://pecl.php.net/get/psr-1.1.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause-FreeBSD
Requires: php-psr-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
# php-psr
[![GitHub Linux Build Status](https://github.com/jbboehr/php-psr/workflows/linux/badge.svg)](https://github.com/jbboehr/php-psr/actions?query=workflow%3Alinux)
[![GitHub OSX Build Status](https://github.com/jbboehr/php-psr/workflows/osx/badge.svg)](https://github.com/jbboehr/php-psr/actions?query=workflow%3Aosx)
[![GitHub Windows Build Status](https://github.com/jbboehr/php-psr/workflows/windows/badge.svg)](https://github.com/jbboehr/php-psr/actions?query=workflow%3Awindows)
[![GitHub Docker Build Status](https://github.com/jbboehr/php-psr/workflows/docker/badge.svg)](https://github.com/jbboehr/php-psr/actions?query=workflow%3Adocker)
[![Appveyor Build Status][:badge-appveyor:]][:build-appveyor:]
[![Coverage Status][:badge-coveralls:]][:build-coveralls:]
[![License][:badge-license:]][:ext-license:]

%package dev
Summary: dev components for the php-psr package.
Group: Development
Requires: php-psr-lib = %{version}-%{release}
Provides: php-psr-devel = %{version}-%{release}
Requires: php-psr = %{version}-%{release}

%description dev
dev components for the php-psr package.


%package lib
Summary: lib components for the php-psr package.
Group: Libraries

%description lib
lib components for the php-psr package.


%prep
%setup -q -n psr-1.1.0
cd %{_builddir}/psr-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
autoupdate
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/psr/php_psr.h
/usr/include/php/ext/psr/psr_cache.h
/usr/include/php/ext/psr/psr_container.h
/usr/include/php/ext/psr/psr_event_dispatcher.h
/usr/include/php/ext/psr/psr_http_client.h
/usr/include/php/ext/psr/psr_http_factory.h
/usr/include/php/ext/psr/psr_http_message.h
/usr/include/php/ext/psr/psr_http_server_handler.h
/usr/include/php/ext/psr/psr_http_server_middleware.h
/usr/include/php/ext/psr/psr_link.h
/usr/include/php/ext/psr/psr_log.h
/usr/include/php/ext/psr/psr_simple_cache.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20200930/psr.so
