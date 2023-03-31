Name:		texlive-regexpatch
Epoch:		1
Version:	58668
Release:	2
Summary:	High level patching of commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/regexpatch
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regexpatch.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
