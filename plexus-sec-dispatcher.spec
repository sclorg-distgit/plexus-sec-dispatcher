%{?scl:%scl_package plexus-sec-dispatcher}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}plexus-sec-dispatcher
Version:        1.4
Release:        22.2%{?dist}
Summary:        Plexus Security Dispatcher Component
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-sec-dispatcher
BuildArch:      noarch

# svn export http://svn.sonatype.org/spice/tags/plexus-sec-dispatcher-1.4/
# tar jcf plexus-sec-dispatcher-1.4.tar.bz2 plexus-sec-dispatcher-1.4/
Source0:        %{pkg_name}-%{version}.tar.bz2

# Removed maven-compiler-plugin configuration version in the pom as annotations isn't available in version 1.4.
Patch0:         %{pkg_name}-pom.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.plexus:plexus-cipher)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.spice:spice-parent:pom:)

%description
Plexus Security Dispatcher Component

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1
%mvn_file : plexus/%{pkg_name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1.4-22.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.4-22.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-19
- Cleanup spec file

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-18
- Update upstream URL

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-17
- Update to current packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-15
- Rebuild to regenerete Maven metadata

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-14
- Use .mfiles generated during build

* Mon Mar 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-13
- Add missing BR: modello

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-12
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-10
- Remove unneeded BR: plexus-container-default

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-9
- Remove unneeded R: spice-parent, resolves: rhbz#908584
- Remove RPM bug workaround

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-6
- Replace plexus-maven-plugin with plexus-component-metadata

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-4
- Fixes according to new guidelines
- Add spice-parent to Requires
- Versionless jars & javadocs
- Use maven3 to build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 04 2010 Hui Wang <huwang@redhat.com> - 1.4-2
- Fixed url

* Fri May 21 2010 Hui Wang <huwang@redhat.com> - 1.4-1
- Initial version of the package
