#
# Conditional build:
%bcond_without libghttp		# build without tests
%bcond_without libusb		# build without tests
%define extra_ver	a

Summary:	One-wire weather
Summary(pl):	Pogoda 1-Wire (oww)
Name:		oww
Version:	0.81.4
Release:	0.1
License:	The "Artistic License"
#Vendor:		-
Group:		Applications
#Icon:		-
Source0:	http://dl.sourceforge.net/oww/%{name}-%{version}%{extra_ver}.tar.gz
URL:		http://oww.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	gtk+2-devel
%{?with_libghttp:BuildRequires:	libghttp-devel}
%{?with_libusb:BuildRequires:	libusb-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oww is a Linux interface to the Dallas Semiconductor / AAGElectronica 
1-Wire weather station kits.

%description -l pl
Oww jest linuksowym interfejsem do stacji pogody Dallas Semiconductor 
/ AAGElectronica pracuj±cych na szynie 1-Wire.

%if 0
%package devel
Summary:	Development libraries and header files for termcap library
Group:		Development/Libraries

%description devel
This is the package containing the development libaries and header
files for ...

%package static
Summary:	Static ... library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static ... library.
%endif

Static ... library.
%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure	\
%{?without_libghttp: --without-libghttp}
%{?without_libusb:		--without-usb}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
