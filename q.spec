# Something that need for rpm-4.1
%define _missing_doc_files_terminate_build 0
%undefine _missing_build_ids_terminate_build 
%define debug_package %{nil}
%define use_date %(date "+%F")

Name:          q
Version:       0.19.2
Release:       1
License:       GNU GPL-3.0 
Group:         DNS
Summary:       A tiny CLI DNS client library with support for UDP, TCP, DoT, DoH, and DoQ.
URL:           https://natesales.net/
Vendor:        Nate Sales
Packager:      Jeam-Philippe Pialasse <jpp@koozali.org>
Source:	       q-%{version}.tar.gz
Source1:       vendor.tar.gz
Provides:      q = %{version}
BuildRequires: golang
BuildArch:     x86_64
AutoProv: no
AutoReq: no

%description
A tiny CLI DNS client library with support for UDP, TCP, DoT, DoH, and DoQ.

%prep
%setup -a 1
# NB to prepare new package first download the q tar.gz
# then uncompress
# then go inside and do
# cd %{name}-%{version}/
# go mod vendor
# tar -czf ../vendor.tar.gz vendor


%build
go build -ldflags="-s -w -X main.version=%{version} -X main.commit=Koozali_SME_Server -X main.date=${use_date}"

%install
mkdir -p %{buildroot}/usr/bin/
install -m 0755 q %{buildroot}/usr/bin/q

%files
%attr(0755, root, root) "/usr/bin/q"


%changelog
* Thu Jan 02 2025 Jean-Philippe Pialasse <jpp@koozali.org> 0.19.2-1.sme
- bump version and initial import to SME 11 core

* Sun Aug 14 2022 Jean-Philippe Pialasse <tests@pialasse.com> 0.8.2-2.sme
- initial import in SME 10 contribs

