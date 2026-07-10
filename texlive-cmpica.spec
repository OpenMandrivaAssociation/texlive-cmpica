%global tl_name cmpica
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Computer Modern Pica variant
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cmpica
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpica.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpica.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An approximate equivalent of the Xerox Pica typeface; the font is
optimised for submitting fiction manuscripts to mainline publishers. The
font is a fixed-width one, rather less heavy than Computer Modern
typewriter. Emphasis for bold-face comes from a wavy underline of each
letter. The two fonts are supplied as Metafont source.

