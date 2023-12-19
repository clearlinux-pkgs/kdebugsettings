#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdebugsettings
Version  : 23.08.4
Release  : 62
URL      : https://download.kde.org/stable/release-service/23.08.4/src/kdebugsettings-23.08.4.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.4/src/kdebugsettings-23.08.4.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.4/src/kdebugsettings-23.08.4.tar.xz.sig
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
%setup -q -n kdebugsettings-23.08.4
cd %{_builddir}/kdebugsettings-23.08.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702976557
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702976557
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdebugsettings
cp %{_builddir}/kdebugsettings-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/kdebugsettings-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdebugsettings-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdebugsettings/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/kdebugsettings-%{version}/src/data/org.kde.kdebugsettings.desktop.license %{buildroot}/usr/share/package-licenses/kdebugsettings/864bc0eb28c73bd997ac19ff91935ab771846615 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kdebugsettings
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kdebugsettings
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
/V3/usr/lib64/libkdebugsettings.so.23.08.4
/V3/usr/lib64/libkdebugsettingscore.so.23.08.4
/usr/lib64/libkdebugsettings.so.23.08.4
/usr/lib64/libkdebugsettings.so.5
/usr/lib64/libkdebugsettingscore.so.23.08.4
/usr/lib64/libkdebugsettingscore.so.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdebugsettings/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdebugsettings/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/kdebugsettings/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/kdebugsettings/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files locales -f kdebugsettings.lang
%defattr(-,root,root,-)

