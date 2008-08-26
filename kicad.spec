%define _disable_ld_no_undefined 1

%define name kicad
%define version 20080715
%define date 2008-07-15
%define release %mkrel 4

Summary:  An open source software for the creation of electronic schematic diagrams
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: disable_svn_header.patch
Patch1: fix_desktop.patch
License: GPLv2+
Group: Sciences/Computer science
Url: http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: wxGTK-devel >= 2.6
BuildRequires: mesa-common-devel
BuildRequires: ImageMagick
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
Requires: %{name}-library %{name}-doc

%description
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad is a set of four softwares and a project manager: 
 
	Eeschema :  Schematic entry. 
	Pcbnew :    Board editor. 
	Gerbview :  GERBER viewer (photoplotter documents). 
	Cvpcb :     footprint selector for components used in the circuit design. 
	Kicad:      project manager.

%prep
%setup -q -n %{name} 
%patch0 -p1
%patch1 -p1

%build
export LC_ALL=C
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%make

%install
rm -rf %{buildroot}
make -C build DESTDIR=%buildroot install

# create desktop file
desktop-file-install --vendor='' \
	--remove-category='Scientific' \
	--add-category='Science;Electronics' \
	--dir=%buildroot%{_datadir}/applications \
	%buildroot%{_datadir}/applications/*.desktop

# create icons
mkdir -p %{buildroot}%{_miconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_liconsdir}
convert -resize 16x16 %{buildroot}%{_datadir}/pixmaps/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 %{buildroot}%{_datadir}/pixmaps/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 %{buildroot}%{_datadir}/pixmaps/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png


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
%{_prefix}/lib/%{name}/plugins/netlist_form_pads-pcb
%{_datadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png
%doc %{_datadir}/doc/%{name}
