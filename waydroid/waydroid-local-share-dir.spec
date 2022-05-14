Name:           waydroid-local-share-dir
Version:        1.1
Release:        1%{?dist}
Summary:        %{name}
License:        none
URL:            localhost
Source0:        waydroid.png
 
BuildArch:      noarch
 
%description
%{name}
 
%prep
 
%build
# Nothing to build
 
%install
 
install -D -m 0644 %{SOURCE0} %{buildroot}%{_datadir}/icons/waydroid.png

%post
mkdir -p %{buildroot}/usr/local/share/waydroid-extra/images
ln -sf /usr/local/share/waydroid-extra %{_datadir}/
 
%files
%{_datadir}/icons/waydroid.png
 
%changelog
* Sun Apr 24 2022 os <example@example.com> - 1.0.0-3
- Initial package
