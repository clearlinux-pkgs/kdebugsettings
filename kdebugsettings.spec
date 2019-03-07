#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdebugsettings
Version  : 18.12.3
Release  : 5
URL      : https://download.kde.org/stable/applications/18.12.3/src/kdebugsettings-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kdebugsettings-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kdebugsettings-18.12.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: kdebugsettings-bin = %{version}-%{release}
Requires: kdebugsettings-data = %{version}-%{release}
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
%setup -q -n kdebugsettings-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551995183
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1551995183
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdebugsettings
cp COPYING %{buildroot}/usr/share/package-licenses/kdebugsettings/COPYING
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
/usr/share/xdg/kde.categories
/usr/share/xdg/kde.renamecategories

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdebugsettings/COPYING

%files locales -f kdebugsettings.lang
%defattr(-,root,root,-)

