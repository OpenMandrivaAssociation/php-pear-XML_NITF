%define		_class		XML
%define		_subclass	NITF
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	%mkrel 1
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

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
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
