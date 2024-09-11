%define name dyff
%define version 1.9.0
%define release 2%{?dist}

%global _missing_build_ids_terminate_build 0

Summary:  diff tool for YAML files, and sometimes JSON
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT license
URL:      https://github.com/homeport/dyff
Source0:  https://github.com/homeport/dyff/archive/refs/tags/v%{version}.tar.gz

BuildRequires: golang
BuildRequires: git

%description
diff tool for YAML files, and sometimes JSON

%prep
%setup -q -n dyff-%{version}

%build
go build ./cmd/dyff

%install
# Create the necessary directory structure in the buildroot
mkdir -p %{buildroot}/bin

# Copy the binary to /bin in the buildroot
install -m 755 dyff %{buildroot}/bin/%{name}

%files
# List all the files to be included in the package
/bin/%{name}

%changelog
* Wed Sep 11 2024 Sven Walter - 1.9.0-%{release}
- Initial RPM build
