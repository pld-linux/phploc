%define		pearname	phploc
%include	/usr/lib/rpm/macros.php
Summary:	A tool for quickly measuring the size of a PHP project
Name:		php-phpunit-phploc
Version:	2.0.4
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	2d8cf318bc1c2c9f631dc6aede63bcf6
URL:		http://pear.phpunit.de/package/phploc/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(tokenizer)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-phpunit-FinderFacade >= 1.1.0
Requires:	php-phpunit-Git >= 1.0.0
Requires:	php-phpunit-Version >= 1.0.0
Requires:	php-symfony2-Console >= 2.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phploc is a tool for quickly measuring the size of a PHP project.

The goal of phploc is not not to replace more sophisticated tools such
as phpcs, pdepend, or phpmd, but rather to provide an alternative to
them when you just need to get a quick understanding of a project's
size.

%prep
%pear_package_setup
mv docs/phploc/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/phploc
%{php_pear_dir}/SebastianBergmann/PHPLOC
