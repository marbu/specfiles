# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hspec

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        A Testing Framework for Haskell

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-core-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-meta-devel
BuildRequires:  ghc-stringbuilder-devel
%endif
# End cabal-rpm deps

%description
Hspec is a testing framework for Haskell. It is inspired by the Ruby library
RSpec. Some of Hspec's distinctive features are:

* a friendly DSL for defining tests

* integration with QuickCheck, SmallCheck, and HUnit

* parallel test execution

* automatic discovery of test files

The Hspec Manual is at <http://hspec.github.io/>.


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


%check
%if %{with tests}
%cabal test
%endif


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files


%changelog
* Sun Nov  1 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.2.0-1
- spec file generated by cabal-rpm-0.9.6
