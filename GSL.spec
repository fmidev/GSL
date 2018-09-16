%define BINNAME GSL
Summary: C++ Guideline Support Library
Name: GSL
Version: 1.0.0
Release: 1
License: MIT
Group: Development/Tools
URL: https://github.com/Microsoft/GSL
Source0: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
Provides: GSL

%description
The Guideline Support Library (GSL) contains functions and types that
are suggested for use by the C++ Core Guidelines maintained by the
Standard C++ Foundation. This repo contains Microsoft's implementation
of GSL.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{BINNAME}
 
%build

%install
mkdir -m 0755 -p $RPM_BUILD_ROOT/%{_includedir}/gsl
install -m 644 include/gsl/* $RPM_BUILD_ROOT/%{_includedir}/gsl/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0664,root,root,-)
%{_includedir}/gsl/*

%changelog
* Tue Sep 11 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 1.0.0-1
- Initial RPM package


