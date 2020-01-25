%define		pearname	%{name}
Summary:	A tool for quickly measuring the size of a PHP project
Name:		phploc
Version:	2.0.6
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/sebastianbergmann/phploc/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9ff44f461e6f8fe54b335acf97c42fb4
Patch0:		autoload.patch
URL:		https://github.com/sebastianbergmann/phploc
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(tokenizer)
Requires:	php-pear
Requires:	php-phpunit-FinderFacade >= 1.1.0
Requires:	php-phpunit-Git >= 1.0.0
Requires:	php-phpunit-Version >= 1.0.0
Requires:	php-symfony2-Console >= 2.7.7
Obsoletes:	php-phpunit-phploc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear Symfony/Component/.*

%description
phploc is a tool for quickly measuring the size of a PHP project.

The goal of phploc is not not to replace more sophisticated tools such
as phpcs, pdepend, or phpmd, but rather to provide an alternative to
them when you just need to get a quick understanding of a project's
size.

%prep
%setup -q
%patch0 -p1

%build
phpab -n -o src/autoload.php src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}/SebastianBergmann/PHPLOC}
install -p phploc $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a src/* $RPM_BUILD_ROOT%{php_pear_dir}/SebastianBergmann/PHPLOC

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/phploc
%{php_pear_dir}/SebastianBergmann/PHPLOC
