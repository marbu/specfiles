# Created by pyp2rpm-1.1.2
%global pypi_name kaptan
%global with_python3 1

Name:           python-%{pypi_name}
Version:        0.5.8
Release:        1%{?dist}
Summary:        Configuration Manager for JSON, YAML and INI

License:        
URL:            https://github.com/emre/kaptan
Source0:        https://pypi.python.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
%if %{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # if with_python3
 
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

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Configuration Manager for JSON, YAML and INI
 
Requires:       python3-PyYAML
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
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
%endif # with_python3


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%endif # with_python3


%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
mv %{buildroot}%{_bindir}/kaptan %{buildroot}/%{_bindir}/python3-kaptan
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc README.md LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.md LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3


%changelog
* Tue Jul 28 2015 makerpm - 0.5.8-1
- Initial package.