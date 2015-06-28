# Created by pyp2rpm-1.1.2
%global pypi_name kaptan

Name:           python-%{pypi_name}
Version:        0.5.8
Release:        1%{?dist}
Summary:        Configuration Manager for JSON, YAML and INI

License:        BSD
URL:            https://github.com/emre/kaptan
Source0:        https://pypi.python.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
Requires:       python-PyYAML
Requires:       python-setuptools

%description
## kaptan ##

[![Build Status](https://travis-ci.org/emre/kaptan.png)](https
://travis-ci.org/emre/kaptan)&nbsp; <img src=
"https://pypip.in/v/kaptan/badge.png"> &nbsp; <img
src="https://pypip.in/d/kaptan/badge.png">

configuration parser.

###
installation

```sh
$ pip install kaptan
```

or add kaptan directory to the
your path.

### usage ###

**supported handlers**

- dict
- json
- yaml
- ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc README.md LICENSE
%{_bindir}/kaptan
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Jun 28 2015  - 0.5.8-1
- Initial package.
