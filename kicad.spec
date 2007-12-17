%define name kicad
%define version 20060626
%define release %mkrel 1

Summary:  An open source software for the creation of electronic schematic diagrams
Name: %{name}
Version: %{version}
Release: %{release}
Source0: kicad-sources-2006-06-26.tar.bz2
Source1: kicad-data.tar.bz2
Patch0: kicad-makefile.patch.bz2
Patch1: kicad-gcc41.patch.bz2
License: GPL
Group: Sciences/Computer science
Url: http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRequires: wxGTK-devel >= 2.6
BuildRequires: mesa-common-devel
BuildRequires: ImageMagick

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
%setup -q -n %{name}-dev
%patch0 -p1
%patch1 -p0
%build

# work-around broken wxGTK2.6 package
ln -s %{_bindir}/wxrc-2.6-ansi ./wxrc
export PATH=`pwd`:$PATH

# recreate the libs.linux, the one provided is totaly broken
cat << EOF > libs.linux
SRCSUFF = .cpp
OBJSUFF = .o
FINAL = 1
MESALIBSPATH = %{_libdir}
WXPATH = `wx-config --prefix`/%{_lib}
PREFIX_WX_LIBS = lib`wx-config --basename`
SUFFIX_WX_LIBGL = \$(PREFIX_WX_LIBS)_gl-\$(LIBVERSION) 
SUFFIX_WX_LIBSTD = \`wx-config --utility=\`
LIBSTDC = -lstdc++
LIBVERSION=`wx-config --release`
WXSYSLIB= `wx-config --libs` `wx-config --libs gl` -lGL -lGLU ../common/common.a
LIBS = -L%{_prefix}/X11R6/%{_lib} \$(EXTRALIBS) \$(WXSYSLIB) \$(LIBSTDC)
LIBS3D =  `wx-config --libs gl` -lGL -lGLU
EOF

find . -name makefile.gtk -exec perl -pi -e 's/cp .*//' {} \;

export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
export CPPFLAGS=$RPM_OPT_FLAGS

%make -f makefile.gtk
%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}

install -m755 kicad/kicad cvpcb/cvpcb eeschema/eeschema pcbnew/pcbnew gerbview/gerbview eeschema/plugins/netlist_form_pads-pcb -D  %{buildroot}/%{_bindir}

pushd %{buildroot}
tar xfj %SOURCE1

pushd ./usr/share/doc/%{name}
find . -type f -exec perl -pi -e 'BEGIN {exit unless -T $ARGV[0];} tr/\r//d;' "{}" \; 
popd

pushd ./usr/share/
find . -type f -exec chmod 644 "{}" \;
popd

popd

mkdir -p %{buildroot}{%{_menudir},%{_miconsdir},%{_iconsdir},%{_liconsdir}}
cat << EOF > %{buildroot}%{_menudir}/%{name}
?package(%name):command="%{_bindir}/%{name}" \
icon="%name.png" needs="X11" \
section="More Applications/Sciences/Electricity" startup_notify="false" \
title="Kicad" longtitle="An open source software for the creation of electronic schematic diagrams" \
mimetypes="" accept_url="false" \
multiple_files="false" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Kicad
Comment=An open source software for the creation of electronic schematic diagrams
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Sciences-Electricity;Science;Electronics;
EOF


convert -resize 16x16 %{buildroot}%{_datadir}/%{name}/kicad_icon.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 %{buildroot}%{_datadir}/%{name}/kicad_icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 %{buildroot}%{_datadir}/%{name}/kicad_icon.png %{buildroot}%{_liconsdir}/%{name}.png


%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}


%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/*
%doc %{_datadir}/doc/%{name}

