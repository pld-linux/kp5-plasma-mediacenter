%define		kdeplasmaver	5.5.4
%define		qtver		5.5.1
%define		kpname		plasma-mediacenter
%define		kf5ver		5.5.0

Summary:	mediacenter
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	4a1a4a6b6196d3f115de53a6d220f9cd
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12

BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	gettext-devel
BuildRequires:	kf5-baloo-devel
BuildRequires:	kf5-kactivities-devel >= %{kf5ver}
BuildRequires:	kf5-kconfig-devel >= %{kf5ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf5ver}
BuildRequires:	kf5-kdeclarative-devel >= %{kf5ver}
BuildRequires:	kf5-kfilemetadata-devel >= %{kf5ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf5ver}
BuildRequires:	kf5-ki18n-devel >= %{kf5ver}
BuildRequires:	kf5-kio-devel >= %{kf5ver}
BuildRequires:	kf5-kservice-devel >= %{kf5ver}
BuildRequires:	kf5-plasma-framework-devel >= %{kf5ver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	taglib-devel
BuildRequires:	xz
Requires:	Qt5Multimedia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Mediacenter.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libplasmamediacenter.so.5
%attr(755,root,root) %{_libdir}/libplasmamediacenter.so.*.*
%dir %{_libdir}/qt5/plugins/plasma/mediacenter
%dir %{_libdir}/qt5/plugins/plasma/mediacenter/browsingbackends
%dir %{_libdir}/qt5/plugins/plasma/mediacenter/datasources
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/mediacenter/browsingbackends/pmc_metadatamusicbackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/mediacenter/browsingbackends/pmc_metadatapicturebackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/mediacenter/browsingbackends/pmc_metadatavideobackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/mediacenter/datasources/pmc_baloosearch.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/mediacenter/datasources/pmc_filesystemsearch.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/common
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/gridbrowser
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/listbrowser
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/AutoHide.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/CategoriesBrowser.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/MediaInfoPanel.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/common/ListMediaItem.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/common/MediaItem.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/common/MediaItemDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/gridbrowser/GridBrowser.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/listbrowser/ListBrowser.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/categoriesbar
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/imageviewer
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediabrowser
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediacontroller
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediaplayer
%dir %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/playlist
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/categoriesbar/CategoriesBar.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/categoriesbar/CategoriesList.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/categoriesbar/CategoriesListDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/imageviewer/ImageViewer.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/imageviewer/PictureStrip.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/imageviewer/PictureStripDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediabrowser/MediaBrowser.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediabrowser/PopupModel.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediacontroller/MediaController.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediaplayer/MediaPlayer.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediaplayer/MusicStats.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/mediaplayer/StatsLabel.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/playlist/MultiplePlaylists.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/playlist/Playlist.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/playlist/PlaylistDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/playlist/PlaylistDelegateLogic.js
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/elements/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/mediacenter/libmediacenterplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/mediacenter/qmldir
%{_desktopdir}/plasma-mediacenter.desktop
%{_iconsdir}/hicolor/64x64/actions/pmc-back.png
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.mediacenter.desktop
%{_datadir}/kservicetypes5/pmc_browsingbackend.desktop
%{_datadir}/kservicetypes5/pmc_datasource.desktop
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/applet
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/panelconfiguration
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/explorer
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/images
%dir %{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/views
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/applet/AppletError.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/applet/CompactApplet.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/applet/DefaultCompactRepresentation.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/AppletConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/ConfigCategoryDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/ConfigurationContainmentActions.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/ConfigurationContainmentAppearance.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/ConfigurationShortcuts.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/ContainmentConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/MouseEventInputButton.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/PanelConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/panelconfiguration/EdgeHandle.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/panelconfiguration/Ruler.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/panelconfiguration/SizeHandle.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/panelconfiguration/SliderHandle.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/configuration/panelconfiguration/ToolBar.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/defaults
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/explorer/AppletAlternatives.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/explorer/AppletDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/explorer/Tooltip.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/explorer/WidgetExplorer.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/images/shadow.png
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/layout.js
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/loader.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/views/Desktop.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/contents/views/Panel.qml
%{_datadir}/plasma/shells/org.kde.plasma.mediacenter/metadata.desktop
%{_datadir}/xsessions/plasma-mediacenter.desktop
