Name:		texlive-tapir
Version:	20484
Release:	2
Summary:	A simple geometrical font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/tapir
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tapir.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tapir.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Tapir is a simple geometrical font mostly created of line and
circular segments with constant thickness. The font is
available as MetaFont source and in Adobe Type 1 format. The
character set contains all characters in the range 0-127 (as in
cmr10), accented characters used in the Czech, Slovak and
Polish languages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/tapir/tap-enc.mf
%{_texmfdistdir}/fonts/source/public/tapir/tap.mf
%{_texmfdistdir}/fonts/type1/public/tapir/tap.pfb
%doc %{_texmfdistdir}/doc/fonts/tapir/readme
%doc %{_texmfdistdir}/doc/fonts/tapir/readme.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
