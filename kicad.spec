%define _disable_ld_no_undefined 1

%define name kicad
%define version 20080715
%define date 2008-07-15
%define release %mkrel 1

Summary:  An open source software for the creation of electronic schematic diagrams
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0:  disable_svn_header.patch
License: GPL
Group: Sciences/Computer science
Url: http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: wxGTK-devel >= 2.6
BuildRequires: mesa-common-devel
BuildRequires: ImageMagick
BuildRequires: boost-devel
BuildRequires: cmake
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

%build
export LC_ALL=C
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%make

# trem: this workaround is no longer needed
# work-around broken wxGTK2.6 package
# ln -s %{_bindir}/wxrc-2.6-ansi ./wxrc
# export PATH=`pwd`:$PATH

# trem: this new libs.linux is no longer needed
# recreate the libs.linux, the one provided is totaly broken
# cat << EOF > libs.linux
# SRCSUFF = .cpp
# OBJSUFF = .o
# FINAL = 1
# MESALIBSPATH = %{_libdir}
# WXPATH = `wx-config --prefix`/%{_lib}
# PREFIX_WX_LIBS = lib`wx-config --basename`
# SUFFIX_WX_LIBGL = \$(PREFIX_WX_LIBS)_gl-\$(LIBVERSION) 
# SUFFIX_WX_LIBSTD = \`wx-config --utility=\`
# LIBSTDC = -lstdc++
# LIBVERSION=`wx-config --release`
# WXSYSLIB= `wx-config --libs` `wx-config --libs gl` -lGL -lGLU ../common/common.a
# LIBS = -L%{_prefix}/X11R6/%{_lib} \$(EXTRALIBS) \$(WXSYSLIB) \$(LIBSTDC)
#LIBS3D =  `wx-config --libs gl` -lGL -lGLU
# EOF

# trem: this 'fix' is no longer needed
# find . -name makefile.gtk -exec perl -pi -e 's/cp .*//' {} \;

# trem: this is no longer needed
# export CFLAGS=$RPM_OPT_FLAGS
# export CXXFLAGS=$RPM_OPT_FLAGS
# export CPPFLAGS=$RPM_OPT_FLAGS

# %make -f makefile.gtk


%install
rm -rf %{buildroot}
make -C build DESTDIR=%buildroot install

# create desktop file
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

