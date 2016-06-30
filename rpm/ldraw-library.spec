#
# spec file for package ldraw-library
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# Workaround a bug in SLES11SP3 build environment
%if 0%{?suse_version} <= 1140
%define _libexecdir /usr/lib
%endif

Name:           ldraw-library
Version:	__UPSTREAM_VERSION__
Release:	__RELEASE_VERSION__
License:	CC BY 2.0
Summary:	LDraw Parts Library
Url:		http://www.ldraw.org
Group:		Productivity/Graphics/CAD
Source:		ldraw-library_%{version}.orig.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch
__PATCHES_DECLARE__

%description
This is the parts library shared by LDraw applications.

LDraw is an open standard for LEGO CAD programs that allow the user to create
virtual LEGO models and scenes.

%prep
%setup -q

__PATCHES_APPLY__

%build
cd ldraw/parts
chmod a+x ../../ldraw-mklist
sh -c ../../ldraw-mklist > ../parts.lst

%install
mkdir -p %{buildroot}%{_datadir}/ldraw
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}
mv ldraw/p ldraw/parts ldraw/ldconfig.ldr ldraw/ldcfgalt.ldr ldraw/ldconfig_tlg.ldr ldraw/parts.lst %{buildroot}%{_datadir}/ldraw
cp ldraw-mklist %{buildroot}%{_bindir}/
cp ldraw-wrapper %{buildroot}%{_libexecdir}/

%files
%defattr(-,root,root)
%{_datadir}/ldraw
%attr(755, root, root) %{_bindir}/ldraw-mklist
%attr(755, root, root) %{_libexecdir}/ldraw-wrapper

%changelog