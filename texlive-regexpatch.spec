# revision 29543
# category Package
# catalog-ctan /macros/latex/contrib/regexpatch
# catalog-date 2013-03-28 17:44:41 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-regexpatch
Epoch:		1
Version:	0.2
Release:	4
Summary:	High level patching of commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/regexpatch
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package generalises the macro patching commands provided by
P. Lehmann's etoolbox. The difference between this package and
its sibling xpatch is that this package sports a very powerful
\regexpatchcmd based on the l3regex module of the LaTeX3
experimental packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/regexpatch/regexpatch.sty
%doc %{_texmfdistdir}/doc/latex/regexpatch/README
%doc %{_texmfdistdir}/doc/latex/regexpatch/regexpatch.pdf
#- source
%doc %{_texmfdistdir}/source/latex/regexpatch/regexpatch.dtx
%doc %{_texmfdistdir}/source/latex/regexpatch/regexpatch.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
