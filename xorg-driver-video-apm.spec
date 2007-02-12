Summary:	X.org video driver for Alliance ProMotion video adapters
Summary(pl.UTF-8):   Sterownik obrazu X.org do kart graficznych Alliance ProMotion
Name:		xorg-driver-video-apm
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-apm-%{version}.tar.bz2
# Source0-md5:	ac7e05f0dfc7e02cac0bf17b9eb89b11
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
# temporary
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86rushproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Alliance ProMotion video adapters. It supports
PCI and ISA video cards based on the following chipsets: ProMotion
6420, ProMotion 6422, AT24, AT3D, AT25.

%description -l pl.UTF-8
Sterownik obrazu X.org do kart graficznych Alliance ProMotion.
Obsługuje karty PCI i ISA oparte na następujących układach: ProMotion
6420, ProMotion 6422, AT24, AT3D, AT25.

%prep
%setup -q -n xf86-video-apm-%{version}

# wrong test
sed -i -e 's/xxf86rush/xf86rushproto/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/apm_drv.so
%{_mandir}/man4/apm.4*
