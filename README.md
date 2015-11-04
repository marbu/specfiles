# Specfiles

Collection of rpm spec files I generated, modified or created from scratch.

This repository is expected to be cloned into `~/rpmbuild/SPECS` directory.

## Python

To package python projects from [PyPI](https://pypi.python.org/pypi) I use
`pyp2rpm` to generate initial specfile.

Important Python related Fedora wikipages:

 * [Python SIG](https://fedoraproject.org/wiki/SIGs/Python)
 * [Python Packaging Guidelines](https://fedoraproject.org/wiki/Packaging:Python)
 * [Python 3 as default](https://fedoraproject.org/wiki/Changes/Python_3_as_Default)

## Haskell

I use `cabal-rpm` tool to create initial spec file (and/or srpm) to package
haskell project from [Hackage](http://hackage.haskell.org/). For more details
see [Haskell SIG](https://fedoraproject.org/wiki/Haskell_SIG) and
[Haskell Packaging Guidelines](https://fedoraproject.org/wiki/Packaging:Haskell).

Builds of some haskell spec files from this repo can be found in
[my haskell copr](https://copr.fedoraproject.org/coprs/marbu/haskell/).
