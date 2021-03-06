#
# Conditional build:
%bcond_without	libghttp		# build without HTTP support
%bcond_without	libusb		# build without USB support
#
#%undefine extra_ver	

Summary:	One-wire weather
Summary(pl.UTF-8):	Pogoda 1-Wire (oww)
Name:		oww
Version:	0.81.7
Release:	0.1
License:	Artistic
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/oww/%{name}-%{version}.tar.gz
# Source0-md5:	69500ab1eb71e927b2bedf5be5b970c1
URL:		http://oww.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
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

%description -l pl.UTF-8
Oww jest linuksowym interfejsem do stacji pogody Dallas Semiconductor
/ AAGElectronica pracujących na szynie 1-Wire.

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
	%{!?with_libghttp:--without-libghttp} \
	%{!?with_libusb:--without-usb}

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
