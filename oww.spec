#
# Conditional build:
%bcond_without	libghttp		# build without HTTP support
%bcond_without	libusb		# build without USB support
#
%define extra_ver	a

Summary:	One-wire weather
Summary(pl):	Pogoda 1-Wire (oww)
Name:		oww
Version:	0.81.4
Release:	0.1
License:	Artistic
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/oww/%{name}-%{version}%{extra_ver}.tar.gz
# Source0-md5:	73ca211ce94fca8734272e3cead590dd
URL:		http://oww.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
%{?with_libghttp:BuildRequires:	libghttp-devel}
BuildRequires:	libtool
%{?with_libusb:BuildRequires:	libusb-devel >= 0.1.5}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oww is a Linux interface to the Dallas Semiconductor / AAGElectronica
1-Wire weather station kits.

%description -l pl
Oww jest linuksowym interfejsem do stacji pogody Dallas Semiconductor
/ AAGElectronica pracuj±cych na szynie 1-Wire.

%prep
%setup -q

%{__perl} -pi -e 's/nb_NO/nb/' configure.in
%{__perl} -pi -e 's,(packagedatadir=share),$1/oww,' configure.in
mv -f po/{nb_NO,nb}.po

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?without_libghttp:--without-libghttp} \
	%{?without_libusb:--without-usb}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/oww
