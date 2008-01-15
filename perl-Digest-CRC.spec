%define module Digest-CRC

Summary:	Generic CRC functions
Name: 		perl-%{module}
Version: 	0.14
Release:	%mkrel 2
License:	Public Domain
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains wrapper
functions with the correct parameters for CRC-CCITT, CRC-16 and CRC-32.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorarch}/auto/Digest/CRC
%{perl_vendorarch}/auto/Digest/CRC/*.so
%{perl_vendorarch}/Digest/CRC.pm
%{_mandir}/*/*


