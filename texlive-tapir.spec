# revision 20484
# category Package
# catalog-ctan /fonts/tapir
# catalog-date 2007-03-12 14:32:12 +0100
# catalog-license gpl
# catalog-version 0.2
Name:		texlive-tapir
Version:	0.2
Release:	5
Summary:	A simple geometrical font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/tapir
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tapir.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tapir.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 756512
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719656
- texlive-tapir
- texlive-tapir
- texlive-tapir

