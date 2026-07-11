%global tl_name regexpatch
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2f
Release:	%{tl_revision}.1
Summary:	High level patching of commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/regexpatch
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package generalises the macro patching commands provided by P.
Lehmann's etoolbox. The difference between this package and its sibling
xpatch is that this package sports a very powerful \regexpatchcmd based
on the l3regex module of the LaTeX3 experimental packages.

