%define major 0
%define libname %mklibname dmtx %major
%define develname %mklibname -d dmtx

Name:		libdmtx
Version:	0.7.2
Release:	%mkrel 2
Summary:	a library for reading and writing Data Matrix 2D barcodes
Source0:	http://downloads.sourceforge.net/project/libdmtx/libdmtx/0.7.2/%{name}-%{version}.tar.bz2
Group:		Development/C++
License: 	GPLv2
URL:		http://www.libdmtx.org
BuildRequires:	png-devel 
BuildRequires:  tiff-devel
BuildRequires:	imagemagick-devel

%description
libdmtx is open source software for reading and writing Data Matrix 2D barcodes
on Linux and Unix. At its core libdmtx is a shared library, allowing C/C++
programs to use its capabilities without restrictions or overhead.

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS KNOWNBUG

#-------------------------------------------------------------------------------

%package -n %libname
Group: Development/C++
Summary: %{name} library package

%description -n %libname
%summary.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*
%{_mandir}/man3/%{name}*

#-------------------------------------------------------------------------------

%package -n %develname
Group: Development/C++
Summary: %{name} developement files
Provides: %{name}-devel = %version-%release
Requires: %libname = %version

%description -n %develname
This package contains header files needed when building applications based on
%{name}.

%files -n %develname
%defattr(-,root,root)
%{_includedir}/dmtx.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#-------------------------------------------------------------------------------

%package utils
Group: Development/C++
Summary: command line tools for %{name}
Requires: %libname = %version

%description utils
This package contains command line tools (dmtxread, dmtxwrite and dmtxquery)
to test %{name} and to learn its behavior.

%files utils
%defattr(-,root,root)
%{_bindir}/dmtxquery
%{_bindir}/dmtxread
%{_bindir}/dmtxwrite
%{_mandir}/man1/dmtxquery*
%{_mandir}/man1/dmtxread*
%{_mandir}/man1/dmtxwrite*

#-------------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall

# don't ship .la
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}
