Nagios Plugin for LCG SAM
=========================

### Overview
This is a Nagios plugin to check Service Availability Monitoring required test meant to be used by the sites forming [ALICE](http://home.web.cern.ch/about/experiments/alice), [ATLAS](http://home.web.cern.ch/about/experiments/atlas), [CMS](http://home.web.cern.ch/about/experiments/cms) and [LHCb](http://home.web.cern.ch/about/experiments/lhcb) experiments.

This check uses the dashboard data for these experiments based on the Nagios Site Usability tests (SUM).

### Authors
Mindcrafted by Pablo Saiz (CERN) and Pepe Flix ([PIC](www.pic.es)). Handcrafted by Jordi Casals ([PIC](www.pic.es)).

Contact: jcasals (at) pic (dot) es

### Requirements
It consists on a Bash script and the only requirement is to have [JQ](http://stedolan.github.io/jq/) package installed, a simple and flexible JSON processor for bash.

### Installation
You just have to install it via RPM and, if you don't have JQ on your server, it will install it as requirement.
```
$ yum install nagios-plugins-lcgsam
```

### Usage
```
$ /usr/lib64/nagios/plugins/check_lcgsam -v <vo> -p <profile> -s <site> [-f <flavour1[,flavour2,...]>]
```
As you can see it has four parameters. 
- vo (-v), profile (-p) and site (-s) are mandatory. 
- flavour (-f) is optional. You can specify multiple flavours, one, or none. 

\* If you specify no flavour, this will return all flavours for this vo, profile and site combination.

You can see an example of how it works by running it on your command line:
```
$ /usr/lib64/nagios/plugins/check_lcgsam -v atlas -p ATLAS_CRITICAL -s pic -f CREAM-CE,SRMv2
CREAM-CE: OK // SRMv2: OK

HOSTS
======
CREAM-CE
ce07.pic.es: OK
ce08.pic.es: OK
ce09.pic.es: OK
ce10.pic.es: OK
ce11.pic.es: OK
SRMv2
srmatlas.pic.es: OK

All hosts in flavour/s CREAM-CE,SRMv2 OK!
```

### Setup for Nagios
To add the plugin to your Nagios System you just have to create a command as you usually do with other plugins. A sample of command line input on the NagiosQL setup can be:
```
$USER1$/check_lcgsam -v $ARG1$ -p $ARG2$ -s $ARG3$ -f $ARG4$
```
Or if you prefer, you can create this command on your commands
```
define command {
    command_name    check_lcgsam
    command_line    $USER1$/check_lcgsam -v $ARG1$ -p $ARG2$ -s $ARG3$ -f $ARG4$
}
```

### Optional Setup for Nagios
We tried to add a little more information to the Nagios output, so we added the option to have a link that points out to the error information, in case there is an error. For some reason (we can imagine it's for security) there are some characters not admitted, and in addition the HTML is disabled in the output. To change this you have to modify two files.

***/usr/local/nagios/etc/cgi.cfg*** *or your equivalent cgi.cfg*
```
# escape_html_tags=1
escape_html_tags=0
```
***/usr/local/nagios/etc/nagios.cfg*** *or your equivalent nagios.cfg or icinga.cfg*
```
# illegal_object_name_chars=`~!$%^&*|'"<>?,()=
illegal_object_name_chars=`~!$%^&*|'"?,()=
```

