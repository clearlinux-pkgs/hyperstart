#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hyperstart
Version  : 9e31bd560357c358ae4bbd94e86066847996620a
Release  : 33
URL      : https://github.com/clearcontainers/hyperstart/archive/0.7.0-clearcontainers/9e31bd560357c358ae4bbd94e86066847996620a.tar.gz
Source0  : https://github.com/clearcontainers/hyperstart/archive/0.7.0-clearcontainers/9e31bd560357c358ae4bbd94e86066847996620a.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: hyperstart-bin = %{version}-%{release}
Requires: hyperstart-license = %{version}-%{release}
Requires: hyperstart-services = %{version}-%{release}
BuildRequires : glibc-bin
BuildRequires : pkgconfig(systemd)
Patch1: CVE-2018-10205.patch

%description
The init Task for HyperContainer. You can get the binary installer of
HyperContainer and HyperStart through https://github.com/hyperhq/hyperd.

%package bin
Summary: bin components for the hyperstart package.
Group: Binaries
Requires: hyperstart-license = %{version}-%{release}
Requires: hyperstart-services = %{version}-%{release}

%description bin
bin components for the hyperstart package.


%package license
Summary: license components for the hyperstart package.
Group: Default

%description license
license components for the hyperstart package.


%package services
Summary: services components for the hyperstart package.
Group: Systemd services

%description services
services components for the hyperstart package.


%prep
%setup -q -n hyperstart-0.7.0-clearcontainers
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568946827
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%autogen --disable-static --enable-daemon
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1568946827
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hyperstart
cp LICENSE %{buildroot}/usr/share/package-licenses/hyperstart/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/hyperstart/NOTICE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hyperstart

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hyperstart/LICENSE
/usr/share/package-licenses/hyperstart/NOTICE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/hyperstart.service
