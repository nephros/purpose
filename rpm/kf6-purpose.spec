%global kf6_version 6.18.0

Name:    kf6-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version: 6.18.0
Release: 1%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
# most files LGPLv2+, configuration.cpp is KDE e.V. GPL variant
License: GPLv2 or GPLv3
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  gettext
BuildRequires:  intltool

BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kconfig-devel >= %{kf6_version}
BuildRequires: kf6-kcoreaddons-devel >= %{kf6_version}
BuildRequires: kf6-ki18n-devel >= %{kf6_version}
BuildRequires: kf6-kio-devel >= %{kf6_version}
BuildRequires: kf6-kirigami2-devel >= %{kf6_version}
BuildRequires: kf6-knotifications-devel >= %{kf6_version}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF6CoreAddons)
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/locale/
%{_kf6_datadir}/qlogging-categories5/purpose.*
%{_kf6_libdir}/libKF6Purpose.so.5*
%{_kf6_libdir}/libKF6PurposeWidgets.so.5*
%{_kf6_libdir}/libPhabricatorHelpers.so.5*
%{_kf6_libdir}/libReviewboardHelpers.so.5*
%{_kf6_libexecdir}/kf6/purposeprocess
%{_kf6_datadir}/purpose/
%{_opt_qt5_plugindir}/kf6/purpose/
%dir %{_opt_qt5_plugindir}/kf6/kfileitemaction/
%{_opt_qt5_plugindir}/kf6/kfileitemaction/sharefileitemaction.so
%{_kf6_qmldir}/org/kde/purpose/
%{_opt_qt5_datadir}/icons/hicolor/*/apps/*-purpose.*
#{_datadir}/icons/hicolor/*/actions/google-youtube.*

%files devel
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so
%{_kf6_includedir}/KF6/purpose/
%{_kf6_includedir}/KF6/purposewidgets/
%{_kf6_libdir}/cmake/KDEExperimentalPurpose/
%{_kf6_libdir}/cmake/KF6Purpose/
