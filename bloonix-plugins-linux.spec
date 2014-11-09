Summary: Bloonix plugins for Linux.
Name: bloonix-plugins-linux
Version: 0.23
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core
AutoReqProv: no

%description
bloonix-plugins-linux provides plugins to check Linux vitals.

%define blxdir /usr/lib/bloonix
%define docdir %{_docdir}/%{name}-%{version}

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Configure.PL --prefix /usr
%{__make}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{docdir}
install -c -m 0444 LICENSE ${RPM_BUILD_ROOT}%{docdir}/
install -c -m 0444 ChangeLog ${RPM_BUILD_ROOT}%{docdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Sat Nov 08 2014 Jonny Schulz <js@bloonix.de> - 0.23-1
- Fixed typo in check-ping description (20ms -> 2000ms).
* Wed Nov 05 2014 Jonny Schulz <js@bloonix.de> - 0.22-1
- Implemented a timeout for check-smart-health and
  check-linux-updates.
- Added zypper to check-linux-updates.
* Tue Nov 04 2014 Jonny Schulz <js@bloonix.de> - 0.21-1
- Fixed check-linux-updates. Intercept errors from apt.
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.20-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.19-1
- Fixed the ping check parser.
- An mtr result is added if the extern checks fails.
- Licence added and old releases deleted.
* Mon May 12 2014 Jonny Schulz <js@bloonix.de> - 0.18-1
- Added check-mtr.
- Added check-linux-updates.
* Wed Apr 23 2014 Jonny Schulz <js@bloonix.de> - 0.17-1
- Added check-smart-health.
* Sat Apr 12 2014 Jonny Schulz <js@bloonix.de> - 0.16-1
- Fixed units in check-memstat.
- Renamed check-filestat to check-open-files.
- Fixed units from kilobytes to bytes for plugin memstats.
- Added field "quest" to check-cpustat.
* Sat Mar 23 2014 Jonny Schulz <js@bloonix.de> - 0.15-1
- Complete rewrite of all plugins.
* Sat Feb 23 2013 Jonny Schulz <js@bloonix.de> - 0.12-1
- Fixed check-ifstat - the initial statistics
  are always marked as corrupt.
- Fixed check-bonding - now active-active setups
  are parsed correclty.
* Sun Sep 16 2012 Jonny Schulz <js@bloonix.de> - 0.10-1
- Added plugin check-netstat-port.
- Added NFS plugins check-nfs3, check-nfs4, and
  check-nfs4-client.
- Fixed the undefined bug in check-bonding.
- Added a lot of new statistics to check-netstat.
- Added plugin check-iflink.
- Fixed a bug in check-procstat. If the script runs
  the first time or the yaml file does not exists
  then $init->{time} was undef.
- Improved check-cpustat, check-ifstat, check-iostat,
  check-netstat, check-pgswstat, check-procstat.
  If the YAML data are broken then the temporary
  file will be overwritten.
* Tue Jan 03 2012 Jonny Schulz <js@bloonix.de> - 0.7-1
- Updated the plugin-* files.
- Added key memrealfree to check-memstat.
- Added check-bonding.
* Mon Jul 11 2011 Jonny Schulz <js@bloonix.de> - 0.5-1
- Added ipv6 to the parameter list in usage().
- Fixed type commited -> committed in check-memstats.
* Fri Jul 01 2011 Jonny Schulz <js@bloonix.de> - 0.4-1
- Renamed environment variable YAML_FILE_BASEDIR to
  PLUGIN_LIBDIR.
- Kicked unused option o_stat.
* Mon Dec 27 2010 Jonny Schulz <js@bloonix.de> - 0.3-1
- Fixed a bug in check-netstat at line 154 and
  renamed recv_udp_pcks to sent_udp_pcks.
- Renamed all plugin files from *.plugin to plugin-*.
* Wed Nov 17 2010 Jonny Schulz <js@bloonix.de> - 0.2-1
- Kicked option --stat from all plugins, because
  statistics will be printed by default on stdout.
* Mon Aug 02 2010 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.