Summary:	Dodge the rocks baby!
Summary(pl):	Gra polegaj±ca na omijaniu kamieni
Name:		rockdodger
Version:	0.6
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/spacerocks/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}-FHS+DESTDIR.patch
URL:		http://spacerocks.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Dodge the rocks for as long as possible until you die. Kill greeblies
to make the universe safe for non-greeblie life once again.

%description -l pl
W tej grze trzeba omijaæ kamienie tak d³ugo jak to mo¿liwe, do
¶mierci. Trzeba te¿ zabijaæ potwory, aby uczyniæ ¶wiat z powrotem
bezpiecznym dla innych gatunków.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	prefix="%{_prefix}" \
	vardir="%{_localstatedir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix="%{_prefix}" \
	vardir="%{_localstatedir}" \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_localstatedir}/lib/%{name}
%attr(0664,root,games) %config(noreplace) %verify(not md5 size mtime) %{_localstatedir}/lib/%{name}/.highscore

%clean
rm -rf $RPM_BUILD_ROOT
