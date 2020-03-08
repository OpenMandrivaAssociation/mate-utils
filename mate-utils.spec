%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major 6
%define libname %mklibname matedict %{major}
%define devname %mklibname matedict -d

Summary:	MATE utility programs such as file search and calculator
Name:		mate-utils
Version:	1.24.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	gtk-doc
BuildRequires:	inkscape
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	librsvg
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xmu)
BuildRequires:  usermode
BuildRequires:	yelp-tools

Requires:	mate-dictionary = %{version}-%{release}
Requires:	mate-screenshot = %{version}-%{release}
Requires:	mate-search-tool = %{version}-%{release}
Requires:	mate-system-log = %{version}-%{release}
Requires:	mate-disk-usage-analyzer = %{version}-%{release}
#Requires:	typelib(MatePanelApplet)

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a collection of small applications all there to make
your day for the MATE Desktop:

  * mate-system-log
  * mate-search-tool
  * mate-dictionary
  * mate-screenshot
  * mate-disk-usage-analyzer

%files

#---------------------------------------------------------------------------

%package common
Summary:	Common files for %{name}
BuildArch:	noarch
Requires:	mate-desktop

%description common
This package provides common files for Mate Desktop Utils.

This package is part of Mate Desktop Utils.

%files common -f %{name}-common.lang
%doc AUTHORS COPYING COPYING.libs ChangeLog NEWS README

#---------------------------------------------------------------------------

%package -n mate-dictionary
Summary:	A dictionary for MATE Desktop
Requires:	%{name}-common = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n mate-dictionary
A dictionary application for MATE Desktop.

This package is part of Mate Desktop Utils.

%files -n mate-dictionary
%doc mate-dictionary/AUTHORS
%doc mate-dictionary/README
%{_bindir}/mate-dictionary
%{_libexecdir}/mate-dictionary-applet
%{_datadir}/metainfo/mate-dictionary.appdata.xml
%{_datadir}/applications/mate-dictionary.desktop
%dir %{_datadir}/mate-dict/
%dir %{_datadir}/mate-dict/sources/
%{_datadir}/mate-dict/sources/default.desktop
%{_datadir}/mate-dict/sources/thai.desktop
%dir %{_datadir}/mate-dictionary/
%{_datadir}/mate-dictionary/*
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_mandir}/man1/mate-dictionary.1.*

#---------------------------------------------------------------------------

%package -n mate-disk-usage-analyzer
Summary:	A disk usage analyzing tool for MATE Desktop
Requires:	%{name}-common = %{version}-%{release}

%description -n mate-disk-usage-analyzer
This package provides an application able to scan either specific
directories or the whole filesystem, in order to give the user a graphical
tree representation including each directory size or percentage in the
branch. It also auto-detects in real-time any change made to your home
folder as far as any mounted/unmounted device.

This package is part of Mate Desktop Utils.

%files -n mate-disk-usage-analyzer
%doc baobab/AUTHORS baobab/README
%{_bindir}/mate-disk-usage-analyzer
%{_datadir}/metainfo/mate-disk-usage-analyzer.appdata.xml
%{_datadir}/applications/mate-disk-usage-analyzer.desktop
%dir %{_datadir}/mate-disk-usage-analyzer/
%{_datadir}/mate-disk-usage-analyzer/*
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_iconsdir}/hicolor/*/apps/mate-disk-usage-analyzer.png
%{_iconsdir}/hicolor/scalable/apps/mate-disk-usage-analyzer.svg
%{_mandir}/man1/mate-disk-usage-analyzer.1.*

#---------------------------------------------------------------------------

%package -n mate-screenshot
Summary:	A utility to take a screen-shot of the desktop
Requires:	%{name}-common = %{version}-%{release}

%description -n mate-screenshot
An application that let you take a screen-shot of your desktop.

This package is part of Mate Desktop Utils.

%files -n mate-screenshot
%{_bindir}/mate-screenshot
%{_bindir}/mate-panel-screenshot
%{_datadir}/metainfo/mate-screenshot.appdata.xml
%{_datadir}/applications/mate-screenshot.desktop
%dir %{_datadir}/mate-screenshot/
%{_datadir}/mate-screenshot/*
%{_mandir}/man1/mate-screenshot.1.*
%{_mandir}/man1/mate-panel-screenshot.1.*
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml

#---------------------------------------------------------------------------

%package -n mate-search-tool
Summary:	A file searching tool for MATE Desktop
Requires:	%{name}-common = %{version}-%{release}

%description -n mate-search-tool
An application to search for files on your computer.

This package is part of Mate Desktop Utils.

%files -n mate-search-tool
%{_bindir}/mate-search-tool
%{_datadir}/metainfo/mate-search-tool.appdata.xml
%{_datadir}/applications/mate-search-tool.desktop
%{_mandir}/man1/mate-search-tool.1.*
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/pixmaps/mate-search-tool/

#---------------------------------------------------------------------------

%package -n mate-system-log
Summary:	A log file viewer for the MATE desktop
Requires:	%{name}-common = %{version}-%{release}
Requires:	usermode-consoleonly
Requires:	polkit-agent

%description -n mate-system-log
An application that lets you view various system log files.

This package is part of Mate Desktop Utils.

%files -n mate-system-log
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_bindir}/mate-system-log
%{_sbindir}/mate-system-log
%dir %{_datadir}/mate-utils/
%{_datadir}/mate-utils/*
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/applications/mate-system-log.desktop
%{_mandir}/man1/mate-system-log.1.*
%{_iconsdir}/hicolor/*/apps/mate-system-log.png
%{_iconsdir}/hicolor/scalable/apps/mate-system-log-symbolic.svg

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	MATE dictionary shared library
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries used by the MATE Dictionary.

%files -n %{libname}
%{_libdir}/libmatedict.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	MATE dictionary library development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libmatedict-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}matedict1.0-devel < 1.16.0

%description -n %{devname}
This package contains libraries and includes files for developing programs
based on the MATE Dictionary.

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/mate-dict/
%{_libdir}/libmatedict*.so
%{_libdir}/pkgconfig/mate-dict*.pc
%{_includedir}/mate-dict*

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--enable-gdict-applet \
	%{nil}
%make_build

%install
%make_install

#rm -rf %{buildroot}/var
#rm -fv %{buildroot}%{_bindir}/test-reader

# force mate-system-log to use polkit:
install -dm 0755 %{buildroot}%{_sysconfdir}/pam.d
cat <<EOF >%{buildroot}%{_sysconfdir}/pam.d/mate-system-log
#%%PAM-1.0
auth		include		system-auth
account		include		system-auth
session		include		system-auth
EOF

mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
cat <<EOF >%{buildroot}%{_sysconfdir}/security/console.apps/mate-system-log
USER=root
PROGRAM=/usr/sbin/mate-system-log
SESSION=true
FALLBACK=true
EOF

mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/mate-system-log %{buildroot}%{_sbindir}
ln -s /usr/bin/consolehelper %{buildroot}%{_bindir}/mate-system-log

# locales
%find_lang %{name}-common --with-gnome --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/mate-dictionary.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/mate-disk-usage-analyzer.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/mate-screenshot.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/mate-search-tool.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/mate-system-log.desktop
