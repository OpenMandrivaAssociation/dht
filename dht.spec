%define _empty_manifest_terminate_build 0

Name:           dht
Version:        0.27
Release:        2
Summary:        BitTorrent DHT library
License:        MIT
URL:            https://www.irif.fr/~jch/software/bittorrent/
Source0:         https://github.com/jech/dht/archive/refs/tags/%{version}/dht-dht-%{version}.tar.gz

# Patch from Transmission to allow compiling with Cmake.
Patch0:         https://github.com/transmission/dht/commit/b02da598.patch

BuildRequires:  make
BuildRequires:  cmake

%description
The files dht.c and dht.h implement the variant of the Kademlia Distributed
Hash Table (DHT) used in the Bittorrent network (``mainline'' variant).

The file dht-example.c is a stand-alone program that participates in the
DHT.  Another example is a patch against Transmission, which you might or
might not be able to find somewhere.

The code is designed to work well in both event-driven and threaded code.
The caller, which is either an event-loop or a dedicated thread, must
periodically call the function dht_periodic.  In addition, it must call
dht_periodic whenever any data has arrived from the network.

All functions return -1 in case of failure, in which case errno is set, or
a positive value in case of success.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%build
%cmake \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_INCLUDEDIR=include/dht
	
%make_build

%install
%make_install -C build


%files
%doc %{_datadir}/doc/DHT/
%{_includedir}/dht/dht.h
%{_libdir}/cmake/DHT/
%{_libdir}/libdht.a
