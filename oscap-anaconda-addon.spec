Name:           oscap-anaconda-addon
Version:        0.5
Release:        1%{?dist}
Summary:        Anaconda addon integrating OpenSCAP to the installation process

License:        GPLv2+
URL:            https://git.fedorahosted.org/cgit/oscap-anaconda-addon.git

# This is a Red Hat maintained package which is specific to
# our distribution.
#
# The source is thus available only from within this SRPM
# or via direct git checkout:
# git clone git://git.fedorahosted.org/oscap-anaconda-addon.git
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	python2-devel
BuildRequires:  python-mock
BuildRequires:  python-nose
BuildRequires:  python-cpio
BuildRequires:  anaconda >= 19
Requires:       anaconda >= 19
Requires:       openscap openscap-utils openscap-python
Requires:       python-cpio

%description
This is an addon that integrates OpenSCAP utilities with the Anaconda installer
and allows installation of systems following restrictions given by a SCAP
content.

%prep
%setup -q


%build

%check
make test


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/anaconda/addons/org_fedora_oscap

%doc COPYING ChangeLog README

%changelog
* Fri Feb 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.5-1
- Allow users to change content
- Show and hide control buttons properly
- Fix sensitivity of the URL entry and fetch button
- Add the button allowing users to use SSG content if available
- Fix listing python sources when creating potfile and regenerate it
- Omit the %addon section from kickstart in dry-run mode
- Implement the dry-run mode in the GUI (trac#2)
- Add UI elements for content changing and dry-run mode
- Check content_defined instead of content_url in the GUI code
- First select the profile, then update the message store
- Remove unused import
- Ignore some more temporary/backup files
- If no content is specified and SSG is available, use it
- New special content type -- SCAP Security Guide
- Fix name of the property used when doing fingerprint check
- Get rid of an unused variable
- Fix data fetch locking to work properly with kickstart installations
- Use 'anonymous:' if no username and password is given for FTP
- Initial version of the translations template file
- First steps to dry-run mode
- Fix main notebook tabs
- Make translations work
- Manipulation with the i18n related files
- If no profile is given, default to default
- Ignore updates.img and its auxiliary directory
- Catch only fetching errors from the fetching thread
- Do not allow multiple simultaneous fetches/initializations
- Prevent user from changing the URL while we try to fetch from it
- Add support for the Default profile
- Support FTP as a content source (#1050980)
- React properly on archive extraction failure
- Refactor the code pre-processing the fetched content
- Unify exceptions from archive extraction
- Make pylint check mandatory to pass
- Support for hash based content integrity checking

* Tue Jan 14 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.4-1
- Beware of running Gtk actions from a non-main thread
- Fix path to the tailoring file when getting rules
- A git hook for running tests when pushing
- Inform user if no profile is selected
- Visually mark the selected profile
- Better UX with content URL entry and progress label
- React on invalid content properly (#1032846)
- Stop spinner when data fetching is finished
- Make the data fetching thread non-fatal (#1049989)
- Exit code 2 from the oscap tool is not an error for us (#1050913)
- Be ready to work with archives/RPMs containing data streams
- Add unit tests for the keep_type_map function
- Add support for namedtuples to keep_type_map
- Add target for running pylint check
- Add target for running just unittests
- On the way to tailoring
- Tests for kickstart XCCDF tailoring handling
- Kickstart support for XCCDF tailoring
- Check session validity also when using XCCDF benchmark

* Tue Dec 10 2013 Vratislav Podzimek <vpodzime@redhat.com> - 0.3-1
- Implement and use our own better function for joining paths
- The content entry should have focus if there is no content
- RPM is just a weird archive in the pre-installation phase
- Ignore RPM files as well
- Adapt tests to dir constants now ending with "/"
- CpioArchive cannot be created from a piped output
- Fix namespace definitions in the testing XCCDF file
- Prevent putting None into xccdf_session_is_sds
- Fix the __all__ variable in the common module
- Strip content dir prefix when setting xccdf/cpe paths
- Inform user we now support archive URLs as well
- Ignore various file types in the git repository
- Try to find content files in the fetched archive or RPM
- Run pylint -E as part of the test target
- Return list of extracted files/directories when extracting archive
- Do not try to search for empty file paths in archives
- Properly set the content type based on the URL's suffix
- Switch profiles on double-click
- Hook urlEntry's activate signal to fetchButton click
- Save the spoke's glade file with a new Glade
- The addon now requires the python-cpio package
- Use really_hide for the UI elements for datastream-id and xccdf-id
- Support for RPM content in the GUI spoke
- RPM content support for kickstart processing
- Add property for the raw post-installation content path
- Make content type case insensitive
- Rest of the code needed for RPM extraction
- Actually look for the file path in entry names
- Basic stuff needed for the RPM content support
- Run tests in paralel
- Specify files in a better way in spec

* Mon Oct 21 2013 Vratislav Podzimek <vpodzime@redhat.com> - 0.2-1
- Initial RPM for the oscap-anaconda-addon
