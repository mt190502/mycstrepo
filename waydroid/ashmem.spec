Name:           ashmem
Version:        1.0.0
Release:        1%{?dist}
Summary:        Kernel module (kmod) for %{prjname}
License:        Google
URL:            https://github.com/choff/anbox-modules
Source0:        anbox.conf
Source1:	99-anbox.rules
 
# For kmod package
Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{name}-kmod >= %{version}
 
BuildArch:      noarch
 
%description
%{prjname} kernel module
 
%prep
 
%build
# Nothing to build
 
%install
 
install -D -m 0644 %{SOURCE0} %{buildroot}%{_modulesloaddir}/anbox.conf
install -D -m 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-anbox.rules
 
%files
%{_modulesloaddir}/anbox.conf
%{_udevrulesdir}/99-anbox.rules
 
%changelog
* Sun Apr 24 2022 os <example@example.com> - 1.0.0-3
- Initial package
