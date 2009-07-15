%define _disable_ld_no_undefined 1

%define name kicad
%define version 20090216
%define date 2009-02-16
%define release %mkrel 1

Summary:  An open source software for the creation of electronic schematic diagrams
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-sources-%{date}.tar.gz
Patch0: disable_svn_header.patch
Patch1: fix_desktop.patch
Patch2: fix_printf_format.patch
Patch3: fix_printf_format2.patch
Patch4: fix_printf_format3.patch
Patch5: fix_printf_format4.patch
Patch6: fix_printf_format5.patch
Patch7: fix_printf_format6.patch
Patch8: fix_printf_format7.patch
Patch9: fix_printf_format8.patch
Patch10: fix_printf_format9.patch
Patch11: fix_printf_format10.patch
Patch12: fix_printf_format11.patch

License: GPLv2+
Group: Sciences/Computer science
Url: http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: wxGTK-devel >= 2.6
BuildRequires: mesa-common-devel
BuildRequires: imagemagick
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
%setup -q -n %{name}-%{date}
#patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

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
%{_datadir}/pixmaps/%{name}_cvpcb.png
%{_datadir}/pixmaps/%{name}_eeschema.png
%{_datadir}/pixmaps/%{name}_gerbview.png
%{_datadir}/pixmaps/%{name}_pcbnew.png
%doc %{_datadir}/doc/%{name}
