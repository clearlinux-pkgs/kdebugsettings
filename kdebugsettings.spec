#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdebugsettings
Version  : 19.12.3
Release  : 19
URL      : https://download.kde.org/stable/release-service/19.12.3/src/kdebugsettings-19.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.3/src/kdebugsettings-19.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.3/src/kdebugsettings-19.12.3.tar.xz.sig
Summary  : An application to enable/disable qCDebug
Group    : Development/Tools
License  : LGPL-2.0
Requires: kdebugsettings-bin = %{version}-%{release}
Requires: kdebugsettings-data = %{version}-%{release}
Requires: kdebugsettings-lib = %{version}-%{release}
Requires: kdebugsettings-license = %{version}-%{release}
Requires: kdebugsettings-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kdebugsettings package.
Group: Binaries
Requires: kdebugsettings-data = %{version}-%{release}
Requires: kdebugsettings-license = %{version}-%{release}

%description bin
bin components for the kdebugsettings package.


%package data
Summary: data components for the kdebugsettings package.
Group: Data

%description data
data components for the kdebugsettings package.


%package lib
Summary: lib components for the kdebugsettings package.
Group: Libraries
Requires: kdebugsettings-data = %{version}-%{release}
Requires: kdebugsettings-license = %{version}-%{release}

%description lib
lib components for the kdebugsettings package.


%package license
Summary: license components for the kdebugsettings package.
Group: Default

%description license
license components for the kdebugsettings package.


%package locales
Summary: locales components for the kdebugsettings package.
Group: Default

%description locales
locales components for the kdebugsettings package.


%prep
%setup -q -n kdebugsettings-19.12.3
cd %{_builddir}/kdebugsettings-19.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583441527
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1583441527
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdebugsettings
cp %{_builddir}/kdebugsettings-19.12.3/COPYING %{buildroot}/usr/share/package-licenses/kdebugsettings/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang kdebugsettings

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kdebugsettings

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kdebugsettings.desktop
/usr/share/metainfo/org.kde.kdebugsettings.appdata.xml
/usr/share/qlogging-categories5/kde.categories
/usr/share/qlogging-categories5/kde.renamecategories
/usr/share/qlogging-categories5/kdebugsettings.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdebugsettings.so.19.12.3
/usr/lib64/libkdebugsettings.so.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdebugsettings/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f kdebugsettings.lang
%defattr(-,root,root,-)

