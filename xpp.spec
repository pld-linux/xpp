Summary:	X interface for cups
Summary(pl):	Interfejs dla cups pod X-y
Name:		xpp
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/cups/%{name}-%{version}.tar.gz
# Source0-md5:	abf4634edf3ff15c6f4db436d68fa835
Patch0:		%{name}-acam.patch
Patch1:		%{name}-c++.patch
URL:		http://cups.sourceforge.net/xpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel >= 1.1.9
BuildRequires:	fltk-devel >= 1.1.3-2
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X interface for cups.

%description -l pl
Interfejs dla cups pod X-y.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CUPSD="/usr/sbin/cupsd" \
	%{?debug:--enable-more-warnings} \
	%{!?debug:--disable-more-warnings}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xpp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
