%define		_class		XML
%define		_subclass	NITF
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	4
Summary:	Parse NITF documents
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_NITF/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package provides a NITF XML parser. The parser was designed with
NITF version 3.1, but should be forward-compatible when new versions
of the NITF DTD are produced. Various methods for accessing the major
elements of the document, such as the hedline(s), byline, and lede are
provided. This class was originally tested against the Associated
Press's (AP) XML data feed.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

# nuke useless(?) files
rm -rf %{buildroot}%{_datadir}/pear/data/XML_NITF/.buildpath
rm -rf %{buildroot}%{_datadir}/pear/data/XML_NITF/.project
rm -rf %{buildroot}%{_datadir}/pear/data/XML_NITF/.settings/org.eclipse.php.core.prefs

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdv2012.0
+ Revision: 742305
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 679609
- mass rebuild

* Wed Dec 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdv2011.0
+ Revision: 625909
- fix build
- 1.1.1

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-6mdv2011.0
+ Revision: 613795
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-5mdv2010.1
+ Revision: 464957
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-4mdv2010.0
+ Revision: 441757
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2009.1
+ Revision: 322830
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2009.0
+ Revision: 237165
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdv2007.0
+ Revision: 82879
- Import php-pear-XML_NITF

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdk
- 1.1.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdk
- initial Mandriva package (PLD import)

