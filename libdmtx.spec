%define major 0
%define libname %mklibname dmtx %{major}
%define develname %mklibname -d dmtx

Name:		libdmtx
Version:	0.7.4
Release:	2
Summary:	A library for reading and writing Data Matrix 2D barcodes
Group:		Development/C++
License: 	GPLv2
URL:		http://www.libdmtx.org
Source0:	http://downloads.sourceforge.net/project/libdmtx/libdmtx/0.7.4/%{name}-%{version}.tar.bz2

%description
libdmtx is open source software for reading and writing Data Matrix 2D barcodes
on Linux and Unix. At its core libdmtx is a shared library, allowing C/C++
programs to use its capabilities without restrictions or overhead.

%package -n %{libname}
Group:		Development/C++
Summary:	%{name} library package

%description -n %{libname}
A library for reading and writing Data Matrix 2D barcodes.

%package -n %{develname}
Group:		Development/C++
Summary:	%{name} developement files
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{name} < 0.7.4

%description -n %{develname}
This package contains header files needed when building applications based on
%{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog README NEWS KNOWNBUG
%{_includedir}/dmtx.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}*

