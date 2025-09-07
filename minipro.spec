Summary:	Program for controlling the MiniPRO TL866xx series of chip programmers
Name:		minipro
Version:	0.7.4
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://gitlab.com/DavidGriffith/minipro/-/archive/%{version}/minipro-%{version}.tar.gz
# Source0-md5:	8a40654c974f3c1673585ed9ce56a055
URL:		https://gitlab.com/DavidGriffith/minipro/
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software for Minipro TL866XX series of programmers from
autoelectric.cn Used to program flash, EEPROM, etc.

%prep
%setup -q
%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+(bash|sh)(\s|$),#!/bin/bash\2,' dump-alg-minipro.bash

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	SHARE_INSTDIR="%{_datadir}/minipro"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

#install -D -p udev/centos7/80-minipro.rules $RPM_BUILD_ROOT/lib/udev/rules.d/80-minipro.rules
install -D -p bash_completion.d/minipro $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/minipro

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
# /etc/bash_completion.d/minipro
/lib/udev/rules.d/60-minipro.rules
/lib/udev/rules.d/61-minipro-plugdev.rules
/lib/udev/rules.d/61-minipro-uaccess.rules
%attr(755,root,root) %{_bindir}/minipro
%attr(755,root,root) %{_bindir}/dump-alg-minipro.bash
%dir %{_datadir}/minipro
%{_datadir}/minipro/logicic.xml
%{_datadir}/minipro/infoic.xml
%{_mandir}/man1/minipro.1*
