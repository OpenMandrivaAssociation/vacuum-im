%define sname vacuum

%define major 1.17
%define libname %mklibname vacuumutils %{major}
%define devname %mklibname vacuumutils -d

Summary:	Crossplatform Jabber client written in Qt
Name:		%{sname}-im
Version:	1.2.1
Release:	1
License:	GPLv3+
Group:		Networking/Instant messaging
Url:		http://www.vacuum-im.org/
Source:		http://vacuum-im.googlecode.com/files/%{sname}-%{version}.tar.xz
Patch0:		vacuum-1.2.1-linkage.patch
BuildRequires:	cmake >= 2.8
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(zlib)

%description
The core program is just a plugin loader - all functionality is made
available via plugins. This enforces modularity and ensures well defined
component interaction via interfaces.

%package -n %{libname}
Summary:	Shared library for Vacuum-IM
Group:		System/Libraries

%description -n %{libname}
This package includes shared libraris needed to work Vacuum-IM program.

%package -n %{devname}
Summary:	Development files for Vacuum-IM
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	vacuumutils-devel = %{version}-%{release}

%description -n %{devname}
This package includes files needed to develop Vacuum-IM modules.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DINSTALL_SDK=1 \
	-DINSTALL_LIB_DIR=%{_lib}

%make

%install
%makeinstall_std -C build

install -D -m644 resources/menuicons/shared/mainwindowlogo128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo96.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -D -m644 resources/menuicons/shared/mainwindowlogo16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

sed -i "s/Exec=%{sname}/Exec=%{name}/;s/Icon=%{sname}/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{sname}.desktop

mv %{buildroot}%{_datadir}/applications/%{sname}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_datadir}/pixmaps/%{sname}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mv %{buildroot}%{_bindir}/%{sname} %{buildroot}%{_bindir}/%{name}

%files
%doc %{_docdir}/%{sname}
%{_bindir}/%{name}
%{_libdir}/%{sname}
%{_datadir}/%{sname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png

%files -n %{libname}
%{_libdir}/libvacuumutils.so.%{major}*

%files -n %{devname}
%{_libdir}/libvacuumutils.so
%{_includedir}/%{sname}

