Name:		nagios-plugins-lcgsam
Version:	1.0.1
Release:	1%{?dist}
Summary:	Service Availability Monitoring for LCG sites

Group:		System/Monitoring
License:	GPLv2+
URL:		https://github.com/jcasals/
#Source0:	%{name}-%{version}-%{release}.tar.gz
Source0:	%{name}.tar.gz
BuildRoot:	%{_tmppath}/%{name}

Requires:	jq

%description
nagios-plugins-lcgsam is a generic plugin that checks the Services Availability for sites in the LHC Computing Grid.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/nagios/plugins
cp ./usr/lib64/nagios/plugins/check_lcgsam %{buildroot}/usr/lib64/nagios/plugins/check_lcgsam

%post
echo "===================================================="
echo ""
echo "Plugin installed succesfully!"
echo ""
echo "Please, take a look at the requirements in"
echo "the documentation to set up the plugin at:"
echo "https://github.com/jcasals/nagios-plugins-lcgsam"
echo ""
echo "Thank you and enjoy this plugin as much as we do :D"
echo ""
echo "===================================================="

%clean
rm -rf %{buildroot}

%files
%attr(0755, root,root) /usr/lib64/nagios/plugins/check_lcgsam
%defattr(-,root,root,-)
%doc

%changelog
* Mon Mar 18 2014 Jordi Casals <jcasals@pic.es> 1.0.1
- Added server error check
* Fri Mar 14 2014 Jordi Casals <jcasals@pic.es> 1.0.0
- First Release!
