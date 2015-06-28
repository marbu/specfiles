# Created by pyp2rpm-1.1.2
%global pypi_name tmuxp

Name:           %{pypi_name}
Version:        0.8.1
Release:        1%{?dist}
Summary:        Save and load tmux sessions thru JSON, YAML configs. Control tmux through Python objects

License:        BSD
URL:            http://github.com/tony/tmuxp/
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
Requires:       python-setuptools

%description
tmuxp, a novel approach to manage `tmux(1)`_ (>= 1.8) workspaces through
`python objects`_, JSON or YAML.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
%{__python2} setup.py test


%files
%doc README.rst LICENSE
%{_bindir}/tmuxp.bash
%{_bindir}/tmuxp.zsh
%{_bindir}/tmuxp.tcsh
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Jun 28 2015  - 0.8.1-1
- Initial package.
