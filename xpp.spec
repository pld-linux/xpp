Summary:	X interface for cups
Summary(pl.UTF-8):	Interfejs dla cups pod X-y
Name:		xpp
Version:	1.5
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/cups/%{name}-%{version}.tar.gz
# Source0-md5:	775fd69c464515da0c3295d04d0c747f
Patch0:		%{name}-include.patch
Patch1:		%{name}-gcc4.patch
URL:		http://cups.sourceforge.net/xpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel >= 1.1.9
BuildRequires:	fltk-devel >= 1.1.3-2
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X interface for cups.

%description -l pl.UTF-8
Interfejs dla cups pod X-y.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
CUPSD="/usr/sbin/cupsd"; export CUPSD
%configure2_13 \
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
