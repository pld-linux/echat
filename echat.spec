Summary:	Limited clone of Vypress Chat
Summary(pl):	Ograniczony klon Vypress Chat
Name:		echat
Version:	0.02r.beta4
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://www.vypress.com/ftp/clones/vyc/echat-0.02r.beta4.tgz
# Source0-md5:	789faa94ce8340adc2b240bf5de705b1
Patch0:		%{name}-keys.patch
Patch1:		%{name}-plcharset.patch
BuildRequires:	ncurses-devel >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Limited clone of Vypress Chat.

%description -l pl
Ograniczony klon Vypress Chat.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CFLAGS="-I%{_includedir}/ncurses %{rpmcflags}" \
	DEFINES="-DLINUX -DEN -DPACKET_QCHAT -DCHARSET -DSOUND -DPORTREUSE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install echat $RPM_BUILD_ROOT%{_bindir}
install echat.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO .*.sample
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
