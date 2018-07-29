Summary:	Program for controlling the MiniPRO TL866xx series of chip programmers
Name:		minipro
Version:	0.1
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://github.com/vdudouyt/minipro/archive/%{version}.tar.gz
# Source0-md5:	d3498236888b24fcba14736cf34dac70
URL:		https://github.com/vdudouyt/minipro
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software for Minipro TL866XX series of programmers from
autoelectric.cn Used to program flash, EEPROM, etc.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D -p udev/rules.d/80-minipro.rules $RPM_BUILD_ROOT/lib/udev/rules.d/80-minipro.rules
install -D -p bash_completion.d/minipro $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/minipro

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
# /etc/bash_completion.d/minipro
/lib/udev/rules.d/80-minipro.rules
%attr(755,root,root) %{_bindir}/minipro
%attr(755,root,root) %{_bindir}/minipro-query-db
%attr(755,root,root) %{_bindir}/miniprohex
%{_prefix}/lib/udev/rules.d/80-minipro.rules
%{_mandir}/man1/minipro.1*
