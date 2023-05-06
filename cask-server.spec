%define libname %mklibname cask-server
%define devname %mklibname -d cask-server

Name:		cask-server
Version:	0.6.0
Release:	2
Summary:	Public server and API to interface with Cask features.
Url:		http://mauikit.org/
Source0:	https://github.com/Nitrux/cask-server/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:  appstream
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)

%description
Public server and API to interface with Cask features.

%package -n %{libname}
Summary:	Library files for cask-server
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library files for cask-server

%package -n %{devname}
Summary:	Development files for cask-server
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for public server and API to interface with Cask features.

%prep
%autosetup -p1 -n %{name}-%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/CaskServer
%{_datadir}/dbus-1/services/org.cask.Server.service

%files -n %{libname}
%{_libdir}/libCaskServerLib.so

%files -n %{devname}
%{_includedir}/CaskServer/
%{_libdir}/cmake/CaskServer/
