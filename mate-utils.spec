%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major 6
%define libname %mklibname matedict %{major}
%define devname %mklibname -d matedict

Summary:	MATE utility programs such as file search and calculator
Name:		mate-utils
Version:	1.8.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)

%description
MATE is the GNU Network Object Model Environment. This powerful
environment is both easy to use and easy to configure.

MATE Utilities is a collection of small applications all there to make
your day just that little bit brighter - System Log Viewer, 
Search Tool, Dictionary.

%package -n %{libname}
Group:		System/Libraries
Summary:	MATE dictionary shared library

%description -n %{libname}
This is the shared library required by the MATE Dictionary.

%package -n %{devname}
Group:		Development/C
Summary:	MATE dictionary library development files
Requires:	%{libname} = %{version}-%{release}
Provides:	libgdict1.0-devel = %{version}-%{release}

%description -n %{devname}
This is the shared library required by the MATE Dictionary.

%prep
%setup -q
NOCONFIGURE=yes ./autogen.sh

%build
%configure \
	--enable-gdict-applet

%make

%install
%makeinstall_std
rm -rf %{buildroot}/var
rm -fv %{buildroot}%{_bindir}/test-reader

# make mate-system-log use consolehelper until it starts using polkit
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
/bin/cat <<EOF >%{buildroot}%{_sysconfdir}/pam.d/mate-system-log
#%%PAM-1.0
auth		include		system-auth
account		include		system-auth
session		include		system-auth
EOF

mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
/bin/cat <<EOF >%{buildroot}%{_sysconfdir}/security/console.apps/mate-system-log
USER=root
PROGRAM=/usr/sbin/mate-system-log
SESSION=true
FALLBACK=true
EOF

mkdir -p %{buildroot}%{_sbindir}
/bin/mv %{buildroot}%{_bindir}/mate-system-log %{buildroot}%{_sbindir}
/bin/ln -s /usr/bin/consolehelper %{buildroot}%{_bindir}/mate-system-log

# remove unneeded converter
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang %{name}-2.0 --with-gnome --all-name

%files -f %{name}-2.0.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_bindir}/mate-dictionary
%{_bindir}/mate-disk-usage-analyzer
%{_bindir}/mate-panel-screenshot
%{_bindir}/mate-screenshot
%{_bindir}/mate-search-tool
%{_bindir}/mate-system-log
%{_sbindir}/mate-system-log
%{_libexecdir}/mate-dictionary-applet
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/mate-dict/sources/default.desktop
%{_datadir}/mate-dict/sources/spanish.desktop
%{_datadir}/mate-dict/sources/thai.desktop
%{_datadir}/mate-disk-usage-analyzer/*
%{_datadir}/mate-dictionary/
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
%{_datadir}/mate-screenshot
%{_datadir}/mate-utils
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libmatedict.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc
%{_libdir}/libmatedict*.so
%{_libdir}/pkgconfig/mate-dict*.pc
%{_includedir}/mate-dict*

