%define		package	CssSelector
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 CssSelector Component
Name:		php-symfony2-CssSelector
Version:	2.7.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	dea659cbfd85cfd6b478b0b16b36626f
URL:		http://symfony.com/doc/2.7/components/css_selector.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CssSelector Component converts CSS selectors to XPath expressions.

%prep
%setup -q -n css-selector-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/CssSelector
%{php_data_dir}/Symfony/Component/CssSelector/*.php
%{php_data_dir}/Symfony/Component/CssSelector/Exception
%{php_data_dir}/Symfony/Component/CssSelector/Node
%{php_data_dir}/Symfony/Component/CssSelector/Parser
%{php_data_dir}/Symfony/Component/CssSelector/XPath
