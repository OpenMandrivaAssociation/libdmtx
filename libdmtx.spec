%define major 0
%define libname %mklibname dmtx %{major}
%define devname %mklibname -d dmtx

Name:		libdmtx
Version:	0.7.4
Release:	13
Summary:	A library for reading and writing Data Matrix 2D barcodes
Group:		Development/C++
License: 	GPLv2
Url:		http://libdmtx.wikidot.com/
# Git repository without tags at https://github.com/dmtx/libdmtx
Source0:	https://downloads.sourceforge.net/project/libdmtx/libdmtx/%{version}/libdmtx-%{version}.tar.bz2

%description
libdmtx is open source software for reading and writing Data Matrix 2D barcodes
on Linux and Unix. At its core libdmtx is a shared library, allowing C/C++
programs to use its capabilities without restrictions or overhead.

%package -n %{libname}
Group:		Development/C++
Summary:	%{name} library package

%description -n %{libname}
A library for reading and writing Data Matrix 2D barcodes.

%package -n %{devname}
Group:		Development/C++
Summary:	%{name} developement files
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{name} < 0.7.4

%description -n %{devname}
This package contains header files needed when building applications based on
%{name}.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README NEWS KNOWNBUG
%{_includedir}/dmtx.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}*

