# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name network-uri

Name:           ghc-%{pkg_name}
Version:        2.5.0.0
Release:        1%{?dist}
Summary:        URI manipulation

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

%description
This package provides an URI manipulation interface.

Version 2.5 (unlike the following versions) is a dummy package that prevents
module name clashes between network-uri and network, if used together with a
Cabal flag as described below.

In network-2.6 the 'Network.URI' module was split off from the network package
into this package. If you're using the 'Network.URI' module you can
automatically get it from the right package by adding this to your .cabal file:

> flag network-uri > description: Get Network.URI from the network-uri package
> default: True > > library > -- ... > if flag(network-uri) > build-depends:
network-uri >= 2.6, network >= 2.6 > else > build-depends: network-uri < 2.6,
network < 2.6

That is, get the module from either network < 2.6 or from network-uri >= 2.6.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files


%changelog
* Sun Nov  1 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.5.0.0-1
- spec file generated by cabal-rpm-0.9.6
