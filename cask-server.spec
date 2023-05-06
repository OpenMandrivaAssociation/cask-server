Name:		cask-server
Version:	0.6.0
Release:	1
Summary:	Public server and API to interface with Cask features.
Url:		http://mauikit.org/
Source0:	https://github.com/Nitrux/cask-server/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)

%description
Public server and API to interface with Cask features.

%prep
%autosetup -p1 -n %{name}-%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
