Summary:	Dodge the rocks baby!
Name:		rockdodger
Version:	0.6
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/spacerocks/%{name}-%{version}.tar.gz
Source1:	%{name}.png
URL:		http://spacerocks.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dodge the rocks for as long as possible until you die. Kill greeblies
to make the universe safe for non-greeblie life once again.

%prep

%setup -q

%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/*

%clean
rm -f $RPM_BUILD_ROOT
