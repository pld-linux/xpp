Summary:	X interface for cups
Summary(pl):	Interfejs dla cups pod X-y
Name:		xpp
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.sourceforge.net/cups/%{name}-%{version}.tar.gz
# Source0-md5:	fc2649b2db29a3ae4bec6842ccd8e268
URL:		http://www.phy.uni-bayreuth.de/till/xpp/
BuildRequires:	fltk-devel >= 1.0.10
BuildRequires:	cups-devel >= 1.1.9
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
X interface for cups.

%description -l pl
Interfejs dla cups pod X-y.

%prep
%setup -q

%build
rm -f missing
%{__automake}
CFLAGS="%{rpmcflags}"
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
%doc README LICENSE ChangeLog
%attr(755,root,root) %{_bindir}/*
