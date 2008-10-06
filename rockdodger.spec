Summary:	Dodge the rocks baby!
Summary(pl.UTF-8):	Gra polegająca na omijaniu kamieni
Name:		rockdodger
Version:	0.6.0a
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/spacerocks/%{name}-%{version}.tar.gz
# Source0-md5:	dbeeabe6bbb57321ba221345d6390170
Source1:	%{name}.png
Patch0:		%{name}-FHS+DESTDIR.patch
Patch1:		%{name}-compile.patch
URL:		http://spacerocks.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dodge the rocks for as long as possible until you die. Kill greeblies
to make the universe safe for non-greeblie life once again.

%description -l pl.UTF-8
W tej grze trzeba omijać kamienie tak długo jak to możliwe, do
śmierci. Trzeba też zabijać potwory, aby uczynić świat z powrotem
bezpiecznym dla innych gatunków.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/lib/%{name}/.highscore

%clean
rm -rf $RPM_BUILD_ROOT
