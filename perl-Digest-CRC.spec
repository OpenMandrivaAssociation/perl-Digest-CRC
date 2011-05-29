%define upstream_name    Digest-CRC
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Generic CRC functions
License:	Public Domain
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Digest/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains wrapper
functions with the correct parameters for CRC-CCITT, CRC-16 and CRC-32.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
