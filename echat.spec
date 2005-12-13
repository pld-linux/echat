Summary:	Limited clone of Vypress Chat
Summary(pl):	Ograniczony klon Vypress Chat
Name:		echat
Version:	0.04beta1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://deep.perm.ru/files/echat/%{name}-%{version}.tar.gz
# Source0-md5:	dda3891d08f04dd266858380d404af15
Patch0:		%{name}-keys.patch
Patch1:		%{name}-plcharset.patch
Patch2:		%{name}-so_reuseport.patch
URL:		http://deep.perm.ru/echat/
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
%patch2 -p1

%build
%{__make} \
	CFLAGS="-I/usr/include/ncurses %{rpmcflags}" \
	DEFINES="-DLINUX -DEN -DCHARSET -DPORTREUSE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install echat $RPM_BUILD_ROOT%{_bindir}
install doc/echat.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{NEWS,README,TODO} doc/.*.sample
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
