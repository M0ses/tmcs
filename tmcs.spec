#
# spec file for package tmcs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tmcs
Version:        0.0.1 
Release:        0
Summary:	The tmate configuration switcher
License:        GPL-3.0
Group:          Productivity/Networking/Other
Url:            https://github.com/M0ses/tmcs.git
Source:         %{name}-%{version}.tar.xz
#BuildRequires:  
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
tmcs - The tmate configuration switcher

%prep
%setup -q

%build

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%doc README.md
/usr/bin/tmcs

%changelog
