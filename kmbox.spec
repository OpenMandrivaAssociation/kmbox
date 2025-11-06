#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6Mbox
%define devname %mklibname KPim6Mbox -d

Name: kmbox
Version:	25.08.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kmbox/-/archive/%{gitbranch}/kmbox-%{gitbranchd}.tar.bz2#/kmbox-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kmbox-%{version}.tar.xz
%endif
Summary: KDE library for accessing MBOX mail files
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(KPim6Mime)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

# Renamed after 6.0 2025-05-09
%rename plasma6-kmbox

%description
KDE library for accessing MBOX mail files

%package -n %{libname}
Summary: KDE library for accessing MBOX mail files
Group: System/Libraries

%description -n %{libname}
KDE library for accessing MBOX mail files

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{libname}
%{_datadir}/qlogging-categories6/kmbox.categories
%{_datadir}/qlogging-categories6/kmbox.renamecategories
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
