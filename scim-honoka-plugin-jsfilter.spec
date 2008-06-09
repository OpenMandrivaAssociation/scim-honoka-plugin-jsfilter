%define version  0.9.2
%define release  %mkrel -c svn584 2
%define src_name honoka-plugin-jsfilter

%define honoka_version   0.9.1-2.svn585
%define plugin_version   0.9.0
%define anthy_version    6606

Name:       scim-honoka-plugin-jsfilter
Summary:    A java script filter plugin for honoka
Version:    %{version}
Release:    %{release}
Group:      System/Internationalization
License:    GPL
URL:        http://sourceforge.jp/projects/scim-imengine/
Source0:    %{src_name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:      anthy >= %{anthy_version}
Requires:      scim-honoka-plugin-anthy >= %{plugin_version}
Requires:      libjs1 >= 1.5-0.rc5a.10
BuildRequires: scim-honoka-devel >= %{honoka_version}
BuildRequires: automake
BuildRequires: libltdl-devel
BuildRequires: js-devel >= 1.5-0.rc5a.10

%description
A java script filter plugin for honoka.


%prep
# stable release
#%setup -q -n %{src_name}-%{version}

# svn snapshot
%setup -q -n jsfilter

%build
./bootstrap
%configure2_5x
# (tv) parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove devel files
rm -f $RPM_BUILD_ROOT/%{scim_plugins_dir}/honoka/*.{a,la}

%find_lang honoka-plugin-jsfilter

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -f honoka-plugin-jsfilter.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{scim_plugins_dir}/honoka/*.so
