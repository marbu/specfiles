# Created by pyp2rpm-1.1.2
%global pypi_name tmuxp
%global with_python3 1

Name:           %{pypi_name}
Version:        0.9.0
Release:        1%{?dist}
Summary:        Save and load tmux sessions thru JSON, YAML configs. Control tmux through Python objects

License:        BSD
URL:            https://github.com/tony/tmuxp/
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
%if %{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # if with_python3
 
Requires:       python-setuptools
Requires:       tmux>=1.8
Requires:       python>=2.6
Requires:       python-kaptan>=0.5.7
Requires:       python-argcomplete
Requires:       python-colorama

%description
tmuxp, a novel approach to manage `tmux(1)`_ (>= 1.8) workspaces through
`python objects`_, JSON or YAML.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Save and load tmux sessions thru JSON, YAML configs. Control tmux through Python objects
 
Requires:       python3-setuptools
Requires:       tmux>=1.8
Requires:       python3>=3.3
Requires:       python3-kaptan>=0.5.7
Requires:       python3-argcomplete
Requires:       python3-colorama

%description -n python3-%{pypi_name}
tmuxp, a novel approach to manage `tmux(1)`_ (>= 1.8) workspaces through
`python objects`_, JSON or YAML.

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
mv %{buildroot}%{_bindir}/tmuxp.bash %{buildroot}/%{_bindir}/python3-tmuxp.bash
mv %{buildroot}%{_bindir}/tmuxp.zsh %{buildroot}/%{_bindir}/python3-tmuxp.zsh
mv %{buildroot}%{_bindir}/tmuxp.tcsh %{buildroot}/%{_bindir}/python3-tmuxp.tcsh
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}


%check
%{__python2} setup.py test

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test
popd
%endif # with_python3


%files
%doc README.rst LICENSE
%{_bindir}/tmuxp
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3


%changelog
* Tue Jul 28 2015 makerpm - 0.9.0-1
- Initial package.
