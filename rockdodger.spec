Summary:	Dodge the rocks baby!
Name:		rockdodger
Version:	0.6
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/spacerocks/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}-FHS+DESTDIR.patch
URL:		http://spacerocks.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dodge the rocks for as long as possible until you die. Kill greeblies
to make the universe safe for non-greeblie life once again.

%prep

%setup -q
%patch0 -p1

%build

%{__make} \
	bindir="%{_bindir}" \
	datadir="%{_datadir}/%{name}" \
	vardir="%{_localstatedir}/lib/%{name}" 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir="%{_bindir}" \
	datadir="%{_datadir}/%{name}" \
	vardir="%{_localstatedir}/lib/%{name}" \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_localstatedir}/lib/%{name}
%attr(0664,root,games) %{_localstatedir}/lib/%{name}/.highscore

%clean
rm -rf $RPM_BUILD_ROOT
