%bcond_without	doc

Summary:	EDA software suite for creation of schematic diagrams and PCBs
Name:		kicad
License:	GPLv3+
Group:		Sciences/Computer science
Version:	7.0.5
Release:	1
URL:		https://www.kicad.org
Source0:	https://gitlab.com/kicad/code/kicad/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:	https://gitlab.com/kicad/services/%{name}-doc/-/archive/%{version}/%{name}-doc-%{version}.tar.bz2
Source2:	https://gitlab.com/kicad/libraries/%{name}-templates/-/archive/%{version}/%{name}-templates-%{version}.tar.bz2
Source3:	https://gitlab.com/kicad/libraries/%{name}-symbols/-/archive/%{version}/%{name}-symbols-%{version}.tar.bz2
Source4:	https://gitlab.com/kicad/libraries/%{name}-footprints/-/archive/%{version}/%{name}-footprints-%{version}.tar.bz2
Source5:	https://gitlab.com/kicad/libraries/%{name}-packages3D/-/archive/%{version}/%{name}-packages3D-%{version}.tar.bz2
# (mageia)
Patch0:		kicad-wxBitmapBundle.patch
#Patch1:	0001-include-algorithm-so-std-sort-is-found.patch
Source100:	kicad.rpmlintrc

BuildRequires:	cmake ninja
BuildRequires:	chrpath
BuildRequires:	boost-devel
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
#BuildRequires:	git
BuildRequires:	fontconfig
#BuildRequires:	gomp-devel
#BuildRequires:	imagemagick
BuildRequires:	po4a
BuildRequires:	source-highlight
BuildRequires:	opencascade-devel
BuildRequires:	perl(Unicode::GCString)
BuildRequires:	python3dist(wxpython)
BuildRequires:	cmake(opencascade)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glm)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ngspice)
BuildRequires:	pkgconfig(odbc)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	swig
BuildRequires:	wxgtku3.2-devel
BuildRequires:	po4a
#BuildRequires:	rubygem-asciidoctor
%if %{with doc}
BuildRequires:	a2x
BuildRequires:	asciidoc
BuildRequires:	asciidoctor
#BuildRequires:	dblatex
%endif

Requires:	%{name}-doc
Requires:	python3dist(wxpython)

Obsoletes:	%{name}-library < %{EVRD}

%description
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad is a set of four programs and a project manager:

* Eeschema:	Schematic entry.
* Pcbnew:	Board editor.
* Gerbview:	GERBER viewer (photoplotter documents).
* Cvpcb:	footprint selector for components used in the circuit design.
* Kicad:	project manager.

%files -f %{name}.lang
%license LICENSE*
%doc AUTHORS.txt README-*.md
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/*.so*
%{py3_platsitedir}/*
%{_datadir}/%{name}
%{_datadir}/applications
%{_datadir}/mime/packages/kicad*.xml
%{_iconsdir}/*/*/*
%{_metainfodir}/*metainfo.xml

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for kicad (creation of electronic schematic diagrams)
License:	GPLv3+ or CC-BY
BuildArch:	noarch

%description doc
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

%{name}-doc is the documentation for kicad.

%files doc
%doc %{_datadir}/doc/%{name}

#----------------------------------------------------------------------------

%prep
# (mandian) this is a workaround suggested by berolinux
# in order to handle multiple sources because autosetup
# fails
%setup -a1 -a2 -a3 -a4 -a5
%autopatch -p1

%build
export LDFLAGS="%{ldflags} `pkg-config --libs libcurl`"

# kicad
pushd .
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DKICAD_BUILD_I18N:BOOL=ON \
	-DKICAD_BUILD_QA_TESTS:BOOL=OFF \
	-DKICAD_I18N_UNIX_STRICT_PATH:BOOL=ON \
	-DKICAD_INSTALL_DEMOS:BOOL=ON \
	-DKICAD_PCM:BOOL=ON \
	-DKICAD_SCRIPTING:BOOL=ON \
	-DKICAD_SCRIPTING_ACTION_MENU:BOOL=ON \
	-DKICAD_SCRIPTING_MODULES:BOOL=ON \
	-DKICAD_SCRIPTING_PYTHON3:BOOL=ON \
	-DKICAD_SCRIPTING_WXPYTHON:BOOL=ON \
	-DKICAD_SPICE:BOOL=ON \
	-DKICAD_USE_EGL:BOOL=ON \
	-DKICAD_USE_OCC:BOOL=ON \
	-DKICAD_VERSION_EXTRA=%{release} \
	-DPYTHON_SITE_PACKAGE_PATH=%{python3_sitearch} \
	-G Ninja
%ninja_build
popd

# docs (HTML only)
%if %{with doc}
pwd
pushd %{name}-doc-%{version}
%cmake \
	-DBUILD_FORMATS=html \
	-DPDF_GENERATOR=none \
	-G Ninja
%ninja_build
popd
%endif

# footprints
pushd %{name}-footprints-%{version}
%cmake -G Ninja
%ninja_build
popd

# packages3D
pushd %{name}-packages3D-%{version}
%cmake -G Ninja
%ninja_build
popd

# symbols
pushd %{name}-symbols-%{version}
%cmake -G Ninja
%ninja_build
popd

# templates
pushd %{name}-templates-%{version}
%cmake -G Ninja
%ninja_build
popd

%install
# kicad
%ninja_install -C build

# Binaries must be executable to be detected by find-debuginfo.sh
#chmod +x %{buildroot}%{python3_sitearch}/_pcbnew.so

# Binaries are not allowed to contain rpaths
#chrpath --delete %{buildroot}%{python3_sitearch}/_pcbnew.so

# footprints
pushd %{name}-footprints-%{version}
%ninja_install -C build
cp -p LICENSE.md ../LICENSE-footprints.md
cp -p README.md ../README-footprints.md
popd

# packages3D
pushd %{name}-packages3D-%{version}
%ninja_install -C build
cp -p LICENSE.md ../LICENSE-packages3D.md
cp -p README.md ../README-packages3D.md
popd

# symbols
pushd %{name}-symbols-%{version}
%ninja_install -C build
cp -p LICENSE.md ../LICENSE-symbols.md
cp -p README.md ../README-symbols.md
popd

# templates
pushd %{name}-templates-%{version}
%ninja_install -C build
cp -p LICENSE.md ../LICENSE-templates.md
cp -p README.md ../README-templates.md
popd

# docs (HTML only)
%if %{with doc}
pushd %{name}-doc-%{version}
%ninja_install -C build
popd
%endif

# .desktop
for desktopfile in %{buildroot}%{_datadir}/applications/*.desktop ; do
	desktop-file-install \
		--remove-category='Scientific' \
		--add-category='Science;Electronics;Education' \
		--dir=%buildroot%{_datadir}/applications \
		${desktopfile}
done

# locales
%find_lang %{name}

