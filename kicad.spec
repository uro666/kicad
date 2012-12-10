%define Werror_cflags            %nil

# Generated debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

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
%define date 20120119
%define revision 3256
%define version %{date}.bzr%{revision}

%define docname kicad-doc
%define docdate 20111221
%define docrevision 303
%define docversion %{docdate}.bzr%{docrevision}

%define libname kicad-library
%define libdate 20120119
%define librevision 114
%define libversion %{libdate}.bzr%{librevision}

Name:		%{name}
Summary:	An open source software for the creation of electronic schematic diagrams
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://www.lis.inpg.fr/realise_au_lis/kicad/
Source0:	%{name}-sources-bzr%{revision}.tar.bz2
Source1:	%{docname}-bzr%{docrevision}.tar.bz2
Source2:	%{libname}-bzr%{librevision}.tar.bz2

# Fedora & upstream patches
Patch11:	%{name}-2011.07.12-fix-linking.patch
Patch12:	%{name}-2011.07.12-boost-polygon-declare-gtlsort-earlier.patch
Patch13:	%{name}-2012.01.19-fix-linking.patch
Patch14:	%{name}-2012.01.19-fix-bom-in-python.patch
Patch20:	%{name}-2012.01.19-fix-plotting-scale.patch
Patch21:	%{name}-2012.01.19-move-up-junction-button.rev3371.patch
Patch22:	%{name}-2012.01.19-thermal-relief.rev3281.patch
Patch23:	%{name}-2012.01.19-undo-redo-auto.rev3297.patch
Patch24:	%{name}-2012.01.19-cvpcb-preview.rev3303.patch
Patch25:	%{name}-2012.01.19-pcb-calculation.rev3328.patch
Patch26:	%{name}-2012.01.19-ps-plotting-width-correction.rev3342.patch

BuildRequires:	wxgtku-devel
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
Summary:	Documentation for kicad (creation of electronic schematic diagrams)
Version:	%{docversion}
License:	GPL
Requires:	%{name}
BuildArch:	noarch

%description doc
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-doc is the documentation for kicad.

%package locales-ca
Summary:	Catalan Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ca
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Catalan locales for kicad.

%package locales-cs
Summary:	Czech Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-cs
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Czech locales for kicad.

%package locales-de
Summary:	German Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-de
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides German locales for kicad.

%package locales-es
Summary:	Spanish Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-es
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Spanish locales for kicad.

%package locales-fi
Summary:	Finnish Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-fi
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Finnish locales for kicad.

%package locales-fr
Summary:	French Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-fr
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides French locales for kicad.

%package locales-hu
Summary:	Hungarian Kicad locales
Version:	%{docversion}
Release:	%{release}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-hu
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Hungarian locales for kicad.

%package locales-it
Summary:	Italian Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-it
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Italian locales for kicad.

%package locales-ja
Summary:	Japanese Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ja
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Japanese locales for kicad.

%package locales-ko
Summary:	Korean Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ko
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Korean locales for kicad.

%package locales-nl
Summary:	Dutch Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-nl
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Dutch locales for kicad.

%package locales-pl
Summary:	Polish Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-pl
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Polish locales for kicad.

%package locales-pt
Summary:	Portuguese Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-pt
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Portuguese locales for kicad.

%package locales-ru
Summary:	Russian Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-ru
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Russian locales for kicad.

%package locales-sl
Summary:	Slovenian Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-sl
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Slovenian locales for kicad.

%package locales-sv
Summary:	Salvadoran Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-sv
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Salvadoran locales for kicad.

%package locales-zh-cn
Summary:	Chinese Kicad locales
Version:	%{docversion}
License:	GPL
Requires:	%{name}
Provides:	%{name}-locale
BuildArch:	noarch

%description locales-zh-cn
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-locales provides Chinese locales for kicad.

%package library
Summary:	Library for kicad (creation of electronic schematic diagrams)
Version:	%{libversion}
License:	GPL
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
pushd ../%{name}
%patch11 -p0 -b .fix-linking1
%patch12 -p0 -b .gcc-4.7
%patch13 -p0 -b .fix-linking2
%patch14 -p1 -b .fix-bom-in-python
%patch20 -p0 -b .fix-plotting-scale
%patch21 -p0 -b .junction-button
%patch22 -p0 -b .thermal-relief
%patch23 -p1 -b .undo-redo
%patch24 -p1 -b .cvpcb-preview
%patch25 -p0 -b .pcb-calculation
%patch26 -p1 -b .width-correction
popd

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
cd ../

# Installing kicad-doc
pushd %{docname}
	%makeinstall_std -C build
popd

# Installing kicad-library
pushd %{libname}
	%makeinstall_std -C build
popd

# Installing kicad
pushd %{name}
	%makeinstall_std -C build

	# create desktop file
	desktop-file-install --vendor='' \
		--remove-category='Scientific' \
		--add-category='Science;Electronics;Education' \
		--dir=%{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/applications/*.desktop

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


%changelog
* Mon Jan 16 2012 Andrey Bondrov <abondrov@mandriva.org> 20111228.bzr3254-1mdv2011.0
+ Revision: 761801
- New revisions: kicad 3254, library 112, doc 303. Build against utf8 wxGTK2.8

* Sun Jun 05 2011 Alexandre Lissy <alissy@mandriva.com> 20110525.bzr3009-6
+ Revision: 682787
- Only one %%mkrel
- Split kicad-locales into several package, each providing kicad-locales-X and kicad-locale
- Adding Suggests from kicad to kicad-locale

* Sun Jun 05 2011 Alexandre Lissy <alissy@mandriva.com> 20110525.bzr3009-5
+ Revision: 682786
- Unifying versions number
- Changing requires
- Adding missing License
- Release bump, package eaten by build system :(
- Updating release ...
- Fix bad version number for kicad-locales

* Fri Jun 03 2011 Alexandre Lissy <alissy@mandriva.com> 20110525.bzr3009-1
+ Revision: 682668
- Fixing typo in versions definitions
- Unification of all kicad sources packages
- Updating kicad, kicad-doc and kicad-library to latest (stable) bazaar revsion
- Adding new kicad-locales package
- Setting noarch for kicad-doc, kicad-library and kicad-locales
- Updating Kicad to latest release

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 20100314-2mdv2011.0
+ Revision: 612604
- the mass rebuild of 2010.1 packages

* Wed Apr 14 2010 Funda Wang <fwang@mandriva.org> 20100314-1mdv2010.1
+ Revision: 534645
- clean old switches

  + trem <trem@mandriva.org>
    - remove use of iconscaldir
    - update to 20100314

* Wed Jul 15 2009 trem <trem@mandriva.org> 20090216-1mdv2010.0
+ Revision: 396494
- update to 2009-02-16
- add lot of patches to fix printf format

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Aug 26 2008 trem <trem@mandriva.org> 20080715-4mdv2009.0
+ Revision: 276407
- new mdvrelease
- replace kicad-20080715-fix-desktop.patch by fix_desktop.patch

* Tue Aug 26 2008 Funda Wang <fwang@mandriva.org> 20080715-3mdv2009.0
+ Revision: 276396
- drop our own desktop file

* Tue Aug 26 2008 Funda Wang <fwang@mandriva.org> 20080715-2mdv2009.0
+ Revision: 276135
- fix license
- fix desktop file

* Thu Aug 21 2008 trem <trem@mandriva.org> 20080715-1mdv2009.0
+ Revision: 274944
- update to 20080715

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - import kicad

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Aug  1 2006 Couriousous <couriousous@mandriva.org> 20060626-1mdv2007.0
- XDG
- 20060626

* Tue Apr 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 20060321-2mdk
- Fix BuildRequires
- use mkrel

* Mon Apr 17 2006 Couriousous <couriousous@mandriva.org> 20060321-1mdk
- 20060321

* Fri Sep  9 2005 Couriousous <couriousous@mandriva.org> 20050906-1mdk
- 20050906

* Tue Jul 26 2005 Couriousous <couriousous@mandriva.org> 20050725-1mdk
- 20050725
- Kicad is now FHS complient

* Sun Jul 17 2005 Couriousous <couriousous@mandriva.org> 20050704-1mdk
- First Mandriva release
- Patch for gcc4
- Patch for amd64

