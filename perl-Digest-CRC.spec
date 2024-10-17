%define upstream_name    Digest-CRC
%define upstream_version 0.18
Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.18
Release:	3

Summary:	Generic CRC functions
License:	Public Domain
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Digest/Digest-CRC-0.18.tar.gz

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.160.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2
+ Revision: 681419
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 587624
- new version

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 555241
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 403127
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.14-4mdv2009.0
+ Revision: 256680
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.14-2mdv2008.1
+ Revision: 152063
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2008.1
+ Revision: 106539
- update to new version 0.14

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.1
+ Revision: 104523
- update to new version 0.11


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdv2007.1
+ Revision: 139557
- fix deps
- fix deps
- Import perl-Digest-CRC

* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-1mdv2007.1
- initial Mandriva package


