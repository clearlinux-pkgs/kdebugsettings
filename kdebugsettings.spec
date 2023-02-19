#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdebugsettings
Version  : 22.12.2
Release  : 50
URL      : https://download.kde.org/stable/release-service/22.12.2/src/kdebugsettings-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/kdebugsettings-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/kdebugsettings-22.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kdebugsettings-bin = %{version}-%{release}
Requires: kdebugsettings-data = %{version}-%{release}
Requires: kdebugsettings-lib = %{version}-%{release}
Requires: kdebugsettings-license = %{version}-%{release}
Requires: kdebugsettings-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kdebugsettings-22.12.2
cd %{_builddir}/kdebugsettings-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676837865
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676837865
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdebugsettings
cp %{_builddir}/kdebugsettings-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/kdebugsettings/c011fda7746c087a127999da1c4044854ee42238 || :
cp %{_builddir}/kdebugsettings-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kdebugsettings/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kdebugsettings-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/kdebugsettings-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdebugsettings-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/kdebugsettings-%{version}/src/org.kde.kdebugsettings.desktop.license %{buildroot}/usr/share/package-licenses/kdebugsettings/864bc0eb28c73bd997ac19ff91935ab771846615 || :
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
/usr/lib64/libkdebugsettings.so.22.12.2
/usr/lib64/libkdebugsettings.so.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdebugsettings/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kdebugsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdebugsettings/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/kdebugsettings/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/kdebugsettings/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/kdebugsettings/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files locales -f kdebugsettings.lang
%defattr(-,root,root,-)

