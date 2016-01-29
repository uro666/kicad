%define	Werror_cflags	%nil
%define	debug_package	%nil

# Use ./update.sh to generate latest tarballs and the corresponding
# specfile fragment

%define	name kicad
%define	version 4.0.1

%define	docname kicad-doc
%define	docversion 4.0.1

%define	libname kicad-library
%define	libversion 4.0.1

%define release 3

Name:		%{name}
Summary:	An open source program for the creation of electronic schematic diagrams
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.xz
Source1:	%{docname}-%{docversion}.tar.gz
Source2:	%{libname}-%{libversion}.tar.gz
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRequires:	wxgtku3.0-devel
BuildRequires:	mesa-common-devel
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	po4a
BuildRequires:	asciidoc
BuildRequires:	dblatex
Requires:	%{libname}
Requires:	%{docname}
Suggests:	%{name}-locale

%description
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad is a set of four programs and a project manager:

* Eeschema:	Schematic entry.
* Pcbnew:	Board editor.
* Gerbview:	GERBER viewer (photoplotter documents).
* Cvpcb:	footprint selector for components used in the circuit design.
* Kicad:	project manager.

%package doc
Summary:	Documentation for kicad (creation of electronic schematic diagrams)
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
BuildArch:	noarch

%description doc
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-doc is the documentation for kicad.

%package locales-ca
Summary:	Catalan Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-ca
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ca
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Catalan locales for kicad.

%package locales-cs
Summary:	Czech Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-cs
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-cs
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Czech locales for kicad.

%package locales-de
Summary:	German Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-de
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-de
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides German locales for kicad.

%package locales-en
Summary:	English Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-en
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-en
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides English locales for kicad.

%package locales-es
Summary:	Spanish Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-es
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-es
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Spanish locales for kicad.

%package locales-fi
Summary:	Finnish Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-fi
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-fi
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Finnish locales for kicad.

%package locales-fr
Summary:	French Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-fr
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-fr
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides French locales for kicad.

%package locales-hu
Summary:	Hungarian Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-hu
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-hu
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Hungarian locales for kicad.

%package locales-it
Summary:	Italian Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-it
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-it
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Italian locales for kicad.

%package locales-ja
Summary:	Japanese Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-ja
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ja
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Japanese locales for kicad.

%package locales-ko
Summary:	Korean Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-ko
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ko
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Korean locales for kicad.

%package locales-nl
Summary:	Dutch Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-nl
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-nl
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Dutch locales for kicad.

%package locales-pl
Summary:	Polish Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-pl
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-pl
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Polish locales for kicad.

%package locales-pt
Summary:	Portuguese Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-pt
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-pt
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Portuguese locales for kicad.

%package locales-ru
Summary:	Russian Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-ru
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ru
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Russian locales for kicad.

%package locales-sl
Summary:	Slovenian Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-sl
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-sl
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Slovenian locales for kicad.

%package locales-sv
Summary:	Salvadoran Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-sv
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-sv
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Salvadoran locales for kicad.

%package locales-zh-cn
Summary:	Chinese Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Requires:	locales-zh
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-zh-cn
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-locales provides Chinese locales for kicad.

%package library
Summary:	Library for kicad (creation of electronic schematic diagrams)
Version:	%{libversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
BuildArch:	noarch

%description library
Kicad is an open source (GPL) program for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-library is a set of library needed by kicad.

%prep
%setup -q -T -b 0 
%setup -q -T -b 1 -n %{docname}-%{docversion}
%setup -q -T -b 2 -n %{libname}-%{docversion}
cd ..

%build
%setup_compile_flags
export LC_ALL=C
cd ../

# Building kicad-doc
pushd %{docname}-%{docversion}
	%cmake \
		-DKICAD_STABLE_VERSION:BOOL=ON \
		-DKICAD_wxUSE_UNICODE=ON \
		-DCMAKE_BUILD_TYPE=Release \
		-DBUILD_FORMATS=html
	%make
popd

# Building kicad-library
pushd %{libname}-%{libversion}
	%cmake \
		-DKICAD_STABLE_VERSION:BOOL=ON \
		-DCMAKE_BUILD_TYPE=Release
	%make
popd

# Building kicad
pushd %{name}-%{version}
	%cmake \
		-DBUILD_SHARED_LIBS:BOOL=OFF \
		-DKICAD_STABLE_VERSION:BOOL=ON \
		-DKICAD_wxUSE_UNICODE=ON \
		-DCMAKE_BUILD_TYPE=Release

	#ugly workaround to fix build
	#dunno what causes the extra ; in CXX_FLAGS which causes the failure
	find . -name flags.make -exec sed -i -e 's,-pthread;-fpermissive,-pthread -fpermissive,g' {} \;
	find . -name link.txt -exec sed -i -e 's,-pthread;-fpermissive,-pthread -fpermissive,g' {} \;

	%make
popd

%install
cd ../

# Installing kicad-doc
pushd %{docname}-%{docversion}
	make -C build DESTDIR=%buildroot install
popd

# Installing kicad-library
pushd %{libname}-%{docversion}
	make -C build DESTDIR=%buildroot install
popd

# Installing kicad-%{version}
pushd %{name}
	make -C build DESTDIR=%buildroot install

	# create desktop file
	desktop-file-install --vendor='' \
		--remove-category='Scientific' \
		--add-category='Science;Electronics;Education' \
		--dir=%buildroot%{_datadir}/applications \
		%buildroot%{_datadir}/applications/*.desktop

	# create icons
	mkdir -p %{buildroot}%{_miconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_liconsdir}
	convert -resize 16x16 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg %{buildroot}%{_miconsdir}/%{name}.png
	convert -resize 32x32 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg %{buildroot}%{_iconsdir}/%{name}.png
	convert -resize 48x48 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg %{buildroot}%{_liconsdir}/%{name}.png
popd

%files
%{_bindir}/*
%{_prefix}/lib/%{name}/plugins/netlist_form_pads-pcb.xsl
%{_iconsdir}/*/*/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/%{name}/demos/
%{_datadir}/%{name}/template/
%{_datadir}/applications
%{_datadir}/mime/packages/kicad.xml
%{_datadir}/mimelnk/application/x-kicad-project.desktop
%{_datadir}/mimelnk/application/x-kicad-schematic.desktop

%files doc
%doc %{_datadir}/doc/%{name}

%files locales-ca
%{_datadir}/%{name}/internat/ca/

%files locales-cs
%{_datadir}/%{name}/internat/cs/

%files locales-de
%{_datadir}/%{name}/internat/de/

%files locales-en
# No files in this package

%files locales-es
%{_datadir}/%{name}/internat/es/

%files locales-fi
%{_datadir}/%{name}/internat/fi/

%files locales-fr
%{_datadir}/%{name}/internat/fr/

%files locales-hu
%{_datadir}/%{name}/internat/hu/

%files locales-it
%{_datadir}/%{name}/internat/it/

%files locales-ja
%{_datadir}/%{name}/internat/ja/

%files locales-ko
%{_datadir}/%{name}/internat/ko/

%files locales-nl
%{_datadir}/%{name}/internat/nl/

%files locales-pl
%{_datadir}/%{name}/internat/pl/

%files locales-pt
%{_datadir}/%{name}/internat/pt/

%files locales-ru
%{_datadir}/%{name}/internat/ru/

%files locales-sl
%{_datadir}/%{name}/internat/sl

%files locales-sv
%{_datadir}/%{name}/internat/sv/

%files locales-zh-cn
%{_datadir}/%{name}/internat/zh_CN/

%files library
%{_datadir}/%{name}/library
%{_datadir}/%{name}/modules
