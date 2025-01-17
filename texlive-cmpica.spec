Name:		texlive-cmpica
Version:	15878
Release:	2
Summary:	A Computer Modern Pica variant
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cmpica
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpica.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpica.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An approximate equivalent of the Xerox Pica typeface; the font
is optimised for submitting fiction manuscripts to mainline
publishers. The font is a fixed-width one, rather less heavy
than Computer Modern typewriter. Emphasis for bold-face comes
from a wavy underline of each letter. The two fonts are
supplied as MetaFont source.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cmpica/cmpica.mf
%{_texmfdistdir}/fonts/source/public/cmpica/cmpicab.mf
%{_texmfdistdir}/fonts/source/public/cmpica/cmpicati.mf
%{_texmfdistdir}/fonts/source/public/cmpica/pcpunct.mf
%{_texmfdistdir}/fonts/source/public/cmpica/pica.mf
%{_texmfdistdir}/fonts/tfm/public/cmpica/cmpica.tfm
%{_texmfdistdir}/fonts/tfm/public/cmpica/cmpicab.tfm
%{_texmfdistdir}/fonts/tfm/public/cmpica/cmpicati.tfm
%doc %{_texmfdistdir}/doc/latex/cmpica/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
