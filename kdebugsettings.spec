#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kdebugsettings
Version  : 21.12.0
Release  : 35
URL      : https://download.kde.org/stable/release-service/21.12.0/src/kdebugsettings-21.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.0/src/kdebugsettings-21.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 MIT
Requires: kdebugsettings-bin = %{version}-%{release}
Requires: kdebugsettings-data = %{version}-%{release}
Requires: kdebugsettings-lib = %{version}-%{release}
Requires: kdebugsettings-license = %{version}-%{release}
Requires: kdebugsettings-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
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
%setup -q -n kdebugsettings-21.12.0
cd %{_builddir}/kdebugsettings-21.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639633633
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1639633633
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdebugsettings
cp %{_builddir}/kdebugsettings-21.12.0/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kdebugsettings/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kdebugsettings-21.12.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe
cp %{_builddir}/kdebugsettings-21.12.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kdebugsettings-21.12.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/kdebugsettings-21.12.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/adadb67a9875aeeac285309f1eab6e47d9ee08a7
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
"/usr/share/kdebugsettings/groups/Full Debug Ruqola"
/usr/share/metainfo/org.kde.kdebugsettings.appdata.xml
/usr/share/qlogging-categories5/kde.renamecategories
/usr/share/qlogging-categories5/kdebugsettings.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdebugsettings.so.21.12.0
/usr/lib64/libkdebugsettings.so.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdebugsettings/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kdebugsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdebugsettings/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/kdebugsettings/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/kdebugsettings/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files locales -f kdebugsettings.lang
%defattr(-,root,root,-)

