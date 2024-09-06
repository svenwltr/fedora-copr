%define name jless
%define version 0.9.0
%define release 2%{?dist}

Summary:  jless is a command-line JSON viewer designed for reading, exploring, and searching through JSON data
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT license
URL:      https://github.com/PaulJuliusMartinez/jless
Source0:  https://github.com/PaulJuliusMartinez/jless/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: curl
BuildRequires: gcc
BuildRequires: xcb-util-renderutil-devel
BuildRequires: libxcb-devel
BuildRequires: python3

%description
jless is a command-line JSON viewer. Use it as a replacement for whatever combination of less, jq, cat and your editor you currently use for viewing JSON files.
It is written in Rust and can be installed as a single standalone binary.

%prep
%setup -q -n jless-%{version}

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
RUST_BACKTRACE=1 CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_DEBUG=true cargo build --release --locked
strip target/release/%{name}

%install
# Create the necessary directory structure in the buildroot
mkdir -p %{buildroot}/bin

# Copy the binary to /bin in the buildroot
install -m 755 target/release/%{name} %{buildroot}/bin/

%files
# List all the files to be included in the package
/bin/%{name}

%changelog
* Wed Jan 31 2024 Danie de Jager - 0.9.0-%{release}
- Initial RPM build
