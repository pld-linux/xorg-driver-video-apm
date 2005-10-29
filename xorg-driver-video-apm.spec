Summary:	X.org video driver for Alliance ProMotion video adapters
Summary(pl):	Sterownik obrazu X.org do kart graficznych Alliance ProMotion
Name:		xorg-driver-video-apm
Version:	1.0.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-apm-%{version}.tar.bz2
# Source0-md5:	ba7a921c0740f0f44c0ad572eca04d0b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
#BuildRequires:	xxf86rush (wrong pkgconfig test should be xf86rushproto???)
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Alliance ProMotion video adapters. It supports
PCI and ISA video cards based on the following chipsets: ProMotion
6420, ProMotion 6422, AT24, AT3D, AT25.

%description -l pl
Sterownik obrazu X.org do kart graficznych Alliance ProMotion.
Obs³uguje karty PCI i ISA oparte na nastêpuj±cych uk³adach: ProMotion
6420, ProMotion 6422, AT24, AT3D, AT25.

%prep
%setup -q -n xf86-video-apm-%{version}

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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/apm_drv.so
%{_mandir}/man4/apm.4x*
