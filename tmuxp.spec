# Created by pyp2rpm-3.3.2
%global pypi_name tmuxp
%global srcname tmuxp

Name:           %{srcname}
Version:        1.4.0
Release:        1%{?dist}
Summary:        tmux session manager

License:        MIT
URL:            http://github.com/tmux-python/tmuxp/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(click) = 6.7
BuildRequires:  python3dist(colorama) = 0.3.9
BuildRequires:  python3dist(kaptan) >= 0.5.7
BuildRequires:  python3dist(libtmux) = 0.8.0
BuildRequires:  python3dist(pytest) = 3.4.2
BuildRequires:  python3dist(pytest-rerunfailures) = 4.0
BuildRequires:  python3dist(setuptools)

%description
tmuxp, tmux session manager. built on libtmux_.|pypi| |docs| |build-status|
|coverage| |license|**New to tmux?** The Tao of tmux < is available on Leanpub
and Amazon Kindle_. Read and browse the book for free on the web_.Installation
.. code-block:: shell $ pip install --user tmuxpLoad a tmux session -Load tmux
sessions via json and YAML, tmuxinator_ and teamocil_ style... code-block::
yaml...

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
Requires:       python3dist(click) = 6.7
Requires:       python3dist(colorama) = 0.3.9
Requires:       python3dist(kaptan) >= 0.5.7
Requires:       python3dist(libtmux) = 0.8.0
Requires:       python3dist(setuptools)
%description -n python3-%{srcname}
tmuxp, tmux session manager. built on libtmux_.|pypi| |docs| |build-status|
|coverage| |license|**New to tmux?** The Tao of tmux < is available on Leanpub
and Amazon Kindle_. Read and browse the book for free on the web_.Installation
.. code-block:: shell $ pip install --user tmuxpLoad a tmux session -Load tmux
sessions via json and YAML, tmuxinator_ and teamocil_ style... code-block::
yaml...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/tmuxp
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Sep 20 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 1.4.0-1
- Initial package.
- Based on spec file created by pyp2rpm-3.3.2
