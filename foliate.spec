# TODO: use gtk4-update-icon-cache
Summary:	Read books in style
Summary(pl.UTF-8):	Stylowe czytanie książek
Name:		foliate
Version:	3.3.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
#Source0Download: https://github.com/johnfactotum/foliate/releases
Source0:	https://github.com/johnfactotum/foliate/releases/download/%{version}/com.github.johnfactotum.Foliate-%{version}.tar.xz
# Source0-md5:	33f63e1333c482cfb87782103b827982
URL:		https://github.com/johnfactotum/foliate
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.76
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26
Requires:	gjs >= 1.76
Requires:	gtk-webkit6 >= 2.40.1
Requires:	gtk4 >= 4.12
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.7
Suggests:	speech-dispatcher
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read books in style.

%description -l pl.UTF-8
Stylowe czytanie książek.

%prep
%setup -q -n com.github.johnfactotum.Foliate-%{version}

%build
%meson \
	-Dcheck_runtime_deps=false

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{fa_IR,fa}

%find_lang com.github.johnfactotum.Foliate

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_desktop_database
%update_icon_cache hicolor

%files -f com.github.johnfactotum.Foliate.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/foliate
%{_datadir}/com.github.johnfactotum.Foliate
%{_datadir}/glib-2.0/schemas/com.github.johnfactotum.Foliate.gschema.xml
%{_datadir}/metainfo/com.github.johnfactotum.Foliate.metainfo.xml
%{_desktopdir}/com.github.johnfactotum.Foliate.desktop
%{_iconsdir}/hicolor/scalable/apps/com.github.johnfactotum.Foliate.svg
%{_iconsdir}/hicolor/symbolic/apps/com.github.johnfactotum.Foliate-symbolic.svg
