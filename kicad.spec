################################################################################
#	NOTE	Edit the above version tags if any of the Source tarballs update
#	NOTE	outside of KiCad major releases & bump for major version updates.
################################################################################
#	NOTE	Update the kicad-doc and kicad-packages3d packages when you update-
#	NOTE	this package.
#	NOTE	This package requires the kicad-packages3d package.
#	NOTE	The KiCad packages are split this way to accommodate the build farm.
################################################################################
%global tplver 9.0.0
%global symver 9.0.0
%global footver 9.0.0
%define cxxstd 20

Name:		kicad
Version:	9.0.0
Release:	4
Summary:	EDA software suite for creation of schematic diagrams and PCBs
URL:		https://www.kicad.org
License:	GPL-3.0-or-later
Group:		Sciences/Computer science
Source0:	https://gitlab.com/kicad/code/kicad/-/archive/%{version}/kicad-%{version}.tar.gz
Source1:	https://gitlab.com/kicad/libraries/kicad-templates/-/archive/%{tplver}/kicad-templates-%{tplver}.tar.gz
Source2:	https://gitlab.com/kicad/libraries/kicad-symbols/-/archive/%{symver}/kicad-symbols-%{symver}.tar.gz
Source3:	https://gitlab.com/kicad/libraries/kicad-footprints/-/archive/%{footver}/kicad-footprints-%{footver}.tar.gz

############################
# Upstream only support x86_64 (inc znver1) and aarch64 builds.
ExclusiveArch:  x86_64 znver1 aarch64

BuildRequires:	boost-devel >= 1.87.0
BuildRequires:	cmake
BuildRequires:	cmake(absl)
BuildRequires:	ninja
BuildRequires:	chrpath
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	nng-devel
BuildRequires:	cmake(harfbuzz)
BuildRequires:	cmake(openssl)
BuildRequires:	appstream-util
BuildRequires:	glibc
BuildRequires:	glibc-devel
BuildRequires:	lib64secret1_0
BuildRequires:	cmake(opencascade)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glm)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	lib64ngspice-devel
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	protobuf-compiler >= 28.3
BuildRequires:	python-devel >= 3.11
BuildRequires:	python-wxpython >= 4.0
BuildRequires:	shared-mime-info
BuildRequires:	pkgconfig(source-highlight)
BuildRequires:	swig
BuildRequires:	pkgconfig(odbc)
BuildRequires:	wxgtku3.2-devel
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(zlib-ng)

############################
Provides:	bundled(fmt) >= 9.0.0
Provides:	bundled(libdxflib) >= 3.26.4
Provides:	bundled(polyclipping) >= 6.4.2
Provides:	bundled(potrace) >= 1.15

############################
Requires:	pkgconfig(libgit2)
Requires:	pkgconfig(libsecret-1)
Requires:	pkgconfig(ngspice)
Requires:	pkgconfig(protobuf)
Requires:	python-wxpython >= 4.0
Requires:	pkgconfig(odbc)

Requires:	kicad-packages3d = %{version}-%{release}
Suggests:	kicad-doc = %{version}-%{release}

Obsoletes:	%{name}-library < %{EVRD}
Obsoletes:	%{name}-unstable < %{EVRD}


%description
KiCad is EDA software to design electronic schematic diagrams and printed
circuit board artwork of up to 32 layers.

############################
%prep
%setup -q -n %{name}-%{version} -a1 -a2 -a3
#autopatch -p1

############################
%build

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -v -Wl,--verbose --warn-backrefs"

# KiCad
# NOTE Keep KICAD_USE_CMAKE_FINDPROTOBUF set OFF, setting this ON will break-
# NOTE the build on modern platforms using CMake.
# NOTE Keep KICAD_WAYLAND set OFF, Wayland is unsuported by upstream at this time.
pushd .
%cmake \
	-DCMAKE_CXX_STANDARD=%{cxxstd} \
	-DCMAKE_C_COMPILER="/usr/bin/clang" \
	-DCMAKE_CXX_COMPILER="/usr/bin/clang++" \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_DATADIR=%{_datadir} \
	-DCMAKE_INSTALL_DOCDIR=%{_docdir} \
	-DPYTHON_SITE_PACKAGE_PATH=%{python_sitearch} \
	-DKICAD_SCRIPTING_WXPYTHON=ON \
	-DKICAD_BUILD_I18N=ON \
	-DKICAD_BUILD_QA_TESTS=OFF \
	-DKICAD_USE_EGL=ON \
	-DKICAD_WAYLAND=OFF \
	-DKICAD_USE_OCC=ON \
	-DKICAD_INSTALL_DEMOS=ON \
	-DKICAD_I18N_UNIX_STRICT_PATH=ON \
	-DKICAD_STDLIB_DEBUG=ON \
	-DKICAD_MAKE_LINK_MAPS=ON \
	-DKICAD_IPC_API=ON \
	-DKICAD_IDF_TOOLS=ON \
	-DKICAD_USE_CMAKE_FINDPROTOBUF=OFF \
	-DKICAD_VERSION_EXTRA=%{release} \
	-DKICAD_DATA=%{_datadir}/%{name} \
	-DKICAD_DOCS=%{_docdir}/%{name} \
	-G Ninja
%ninja_build
popd

# Template libraries
pushd %{name}-templates-%{tplver}/
%cmake \
	-G Ninja \
	-DCMAKE_CXX_STANDARD=%{cxxstd} \
	-DKICAD_DATA=%{_datadir}/%{name}
%ninja_build
popd

# Symbol libraries
pushd %{name}-symbols-%{symver}/
%cmake \
	-G Ninja \
	-DCMAKE_CXX_STANDARD=%{cxxstd} \
	-DKICAD_DATA=%{_datadir}/%{name}
%ninja_build
popd

# Footprint libraries
pushd %{name}-footprints-%{footver}/
%cmake \
	-G Ninja \
	-DCMAKE_CXX_STANDARD=%{cxxstd} \
	-DKICAD_DATA=%{_datadir}/%{name}
%ninja_build
popd

############################
%install

# KiCad application
%ninja_install -C build

# Binaries must be executable to be detected by find-debuginfo.sh
chmod +x %{buildroot}%{python3_sitearch}/_pcbnew.so

# Binaries are not allowed to contain rpaths
chrpath --delete %{buildroot}%{python3_sitearch}/_pcbnew.so

# Install desktop
for desktopfile in %{buildroot}%{_datadir}/applications/*.desktop ; do
	desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original                          \
	${desktopfile}
done

# Templates
pushd %{name}-templates-%{tplver}/
%ninja_install -C build
cp -p LICENSE.md ../LICENSE-templates.md
popd

# Symbol libraries
pushd %{name}-symbols-%{symver}/
%ninja_install -C build
cp -p LICENSE.md ../LICENSE-symbols.md
popd

# Footprint libraries
pushd %{name}-footprints-%{footver}/
%ninja_install -C build
cp -p LICENSE.md ../LICENSE-footprints.md
popd

%find_lang %{name}

############################
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

############################
%files -f %{name}.lang
%doc AUTHORS.txt
%attr(0755, root, root) %{_bindir}/*
%{_libdir}/%{name}/
%{_libdir}/libkiapi.so*
%{_libdir}/libkicad_3dsg.so*
%{_libdir}/libkigal.so*
%{_libdir}/libkicommon.so*
%{python3_sitearch}/_pcbnew.so
%{python3_sitearch}/pcbnew.py
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*.*
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.metainfo.xml
%license LICENSE*
