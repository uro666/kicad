%define Werror_cflags            %nil

# To create source package: 
# bzr branch lp:kicad/stable
# 
# You can get the date by querying:
# $ bzr log -r-1 --line stable/
# 3009: jean-pierre charras 2011-05-25 Libedit: actual line thickness  taken in account by collector. Thick lines are now more easy t...
#
# $ bzr export --format=tbz2 --root=kicad kicad-sources-bzr$(bzr revno stable/).tar.bz2 stable/

# For library,
# See http://iut-tice.ujf-grenoble.fr/cao/how_to_download_sources.txt
# bzr branch lp:~kicad-lib-committers/kicad/library
#
# You can get the date by querying:
# $ bzr log -r-1 --line library/
# 109: xtony 2010-12-08 Add various modules.
#
# $ bzr export --format=tbz2 --root=kicad-library kicad-library-bzr$(bzr revno library/).tar.bz2 library/

# For doc,
# See http://iut-tice.ujf-grenoble.fr/cao/how_to_download_sources.txt
# bzr branch lp:~kicad-developers/kicad/doc
# 
# You can get the date by querying:
# $ bzr log -r-1 --line doc/
# 216: Andrey Fedorushkov 2011-06-02 update russian GUI

%define name kicad
%define date 20110525
%define revision 3009
%define version %{date}.bzr%{revision}

%define docname kicad-doc
%define docdate 20110602
%define docrevision 216
%define docversion %{docdate}.bzr%{docrevision}

%define libname kicad-library
%define libdate 20101208
%define librevision 109
%define libversion %{libdate}.bzr%{librevision}

%define release %mkrel 6

Name:		%{name}
Summary:	An open source software for the creation of electronic schematic diagrams
Version:	%{version}
Release:	%{release}
Source0:	%{name}-sources-bzr%{revision}.tar.bz2
Source1:	%{docname}-bzr%{docrevision}.tar.bz2
Source2:	%{libname}-bzr%{librevision}.tar.bz2
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	wxGTK-devel >= 2.6
BuildRequires:	mesa-common-devel
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
Requires:	%{libname} = %{libversion}-%{release}
Requires:	%{docname} = %{docversion}-%{release}
Suggests:	%{name}-locale

%description
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad is a set of four softwares and a project manager: 
 
	Eeschema :  Schematic entry. 
	Pcbnew :    Board editor. 
	Gerbview :  GERBER viewer (photoplotter documents). 
	Cvpcb :     footprint selector for components used in the circuit design. 
	Kicad:      project manager.

%package doc
Summary:  	Documentation for kicad (creation of electronic schematic diagrams)
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
BuildArch:	noarch

%description doc
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-doc is the documentation for kicad.

%package locales-ca
Summary:	Catalan Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ca
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Catalan locales for kicad.

%package locales-cs
Summary:	Czech Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-cs
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Czech locales for kicad.

%package locales-de
Summary:	German Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-de
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides German locales for kicad.

%package locales-es
Summary:	Spanish Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-es
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Spanish locales for kicad.

%package locales-fi
Summary:	Finnish Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-fi
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Finnish locales for kicad.

%package locales-fr
Summary:	French Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-fr
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides French locales for kicad.

%package locales-hu
Summary:	Hungarian Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-hu
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Hungarian locales for kicad.

%package locales-it
Summary:	Italian Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-it
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Italian locales for kicad.

%package locales-ja
Summary:	Japanese Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ja
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Japanese locales for kicad.

%package locales-ko
Summary:	Korean Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ko
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Korean locales for kicad.

%package locales-nl
Summary:	Dutch Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-nl
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Dutch locales for kicad.

%package locales-pl
Summary:	Polish Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-pl
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Polish locales for kicad.

%package locales-pt
Summary:	Portuguese Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-pt
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Portuguese locales for kicad.

%package locales-ru
Summary:	Russian Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ru
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Russian locales for kicad.

%package locales-sl
Summary:	Slovenian Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-sl
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Slovenian locales for kicad.

%package locales-sv
Summary:	Salvadoran Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-sv
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Salvadoran locales for kicad.

%package locales-zh-cn
Summary:	Chinese Kicad locales
Version:  	%{docversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-zh-cn
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Chinese locales for kicad.

%package library
Summary:  	Library for kicad (creation of electronic schematic diagrams)
Version:  	%{libversion}
Release:  	%{release}
License:  	GPL
Requires:	%{name}
BuildArch:	noarch

%description library
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-library is a set of library needed by kicad.

%prep
%setup -q -T -b 0 -n %{name}
%setup -q -T -b 1 -n %{docname}
%setup -q -T -b 2 -n %{libname}

%build
export LC_ALL=C
cd ../

# Building kicad-doc
pushd %{docname}
	%cmake \
		-DKICAD_STABLE_VERSION:BOOL=ON \
		-DCMAKE_BUILD_TYPE=Release
	%make
popd

# Building kicad-library
pushd %{libname}
	%cmake \
		-DKICAD_STABLE_VERSION:BOOL=ON \
		-DCMAKE_BUILD_TYPE=Release
	%make
popd

# Building kicad
pushd %{name}
	%cmake \
		-DBUILD_SHARED_LIBS:BOOL=OFF \
		-DKICAD_STABLE_VERSION:BOOL=ON \
		-DCMAKE_BUILD_TYPE=Release
	%make
popd

%install
rm -rf %{buildroot}

cd ../

# Installing kicad-doc
pushd %{docname}
	make -C build DESTDIR=%buildroot install
popd

# Installing kicad-library
pushd %{libname}
	make -C build DESTDIR=%buildroot install
popd

# Installing kicad
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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr(-,root,root)
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
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}

%files locales-ca
%defattr(-,root,root)
%{_datadir}/%{name}/internat/ca/

%files locales-cs
%defattr(-,root,root)
%{_datadir}/%{name}/internat/cs/

%files locales-de
%defattr(-,root,root)
%{_datadir}/%{name}/internat/de/

%files locales-es
%defattr(-,root,root)
%{_datadir}/%{name}/internat/es/

%files locales-fi
%defattr(-,root,root)
%{_datadir}/%{name}/internat/fi/

%files locales-fr
%defattr(-,root,root)
%{_datadir}/%{name}/internat/fr/

%files locales-hu
%defattr(-,root,root)
%{_datadir}/%{name}/internat/hu/

%files locales-it
%defattr(-,root,root)
%{_datadir}/%{name}/internat/it/

%files locales-ja
%defattr(-,root,root)
%{_datadir}/%{name}/internat/ja/

%files locales-ko
%defattr(-,root,root)
%{_datadir}/%{name}/internat/ko/

%files locales-nl
%defattr(-,root,root)
%{_datadir}/%{name}/internat/nl/

%files locales-pl
%defattr(-,root,root)
%{_datadir}/%{name}/internat/pl/

%files locales-pt
%defattr(-,root,root)
%{_datadir}/%{name}/internat/pt/

%files locales-ru
%defattr(-,root,root)
%{_datadir}/%{name}/internat/ru/

%files locales-sl
%defattr(-,root,root)
%{_datadir}/%{name}/internat/sl

%files locales-sv
%defattr(-,root,root)
%{_datadir}/%{name}/internat/sv/

%files locales-zh-cn
%defattr(-,root,root)
%{_datadir}/%{name}/internat/zh_CN/

%files library
%defattr(-,root,root)
%{_datadir}/%{name}/library
%{_datadir}/%{name}/modules
