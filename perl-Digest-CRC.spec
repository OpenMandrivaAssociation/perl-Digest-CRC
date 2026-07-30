%define upstream_name    Digest-CRC
%define upstream_version 0.24
Name:       perl-%{upstream_name}
Version:	0.24
Release:	2

Summary:	Generic CRC functions
License:	Public Domain
Group:		Development/Perl
Url:		https://metacpan.org/dist/Digest-CRC
Source0:	https://cpan.metacpan.org/authors/id/O/OL/OLIMAUL/Digest-CRC-0.24.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel

%description
The Digest::CRC module calculates CRC sums of all sorts. It contains wrapper
functions with the correct parameters for CRC-CCITT, CRC-16 and CRC-32.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test || :

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


