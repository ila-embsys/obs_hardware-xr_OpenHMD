#
# spec file for package OpenHMD
#
# Copyright (c) 2022 Sasi Olin <hellcp@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%global _sover 0

Name:           OpenHMD
Version:        0
Release:        0
Summary:        Free and Open Source API and drivers for immersive technology
License:        BSL-1.0
Url:            http://www.openhmd.net
Source:         %{name}-%{version}.tar.gz
Patch1:         0001-nreal-add-driver-from-monado.patch
Patch2:         0002-nreal-remove-maybe-unused.patch
Patch3:         0003-nreal-use-teardown-in-close-device.patch
Patch4:         0004-nreal-cleanup-semantic-and-mutex-init.patch
BuildRequires:  meson
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  glslang-devel
BuildRequires:  graphviz
BuildRequires:  libstdc++-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  spirv-headers
BuildRequires:  vulkan-headers

%description
This project aims to provide a Free and Open Source API and drivers for immersive technology, such as head mounted displays with built in head tracking.

%package -n libopenhmd%{_sover}
Summary:        OpenHMD library

%description -n libopenhmd%{_sover}
This project aims to provide a Free and Open Source API and drivers for immersive technology, such as head mounted displays with built in head tracking.

%package devel
Summary:        OpenHMD development files
Requires:       libopenhmd%{_sover} = %{version}

%description devel
Those are the development files OpenHMD

%prep
%setup -q
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

%build
%meson -Dexamples=['']
%meson_build

%install
%meson_install

%post -n libopenhmd%{_sover} -p /sbin/ldconfig
%postun -n libopenhmd%{_sover} -p /sbin/ldconfig

%files -n libopenhmd%{_sover}
%{_libdir}/libopenhmd.so.*

%files devel
%dir %{_includedir}/openhmd
%{_includedir}/openhmd/openhmd.h
%{_libdir}/libopenhmd.so
%{_libdir}/pkgconfig/openhmd.pc

%changelog
