#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-SSLeay
Version  : 0.72
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/N/NA/NANIS/Crypt-SSLeay-0.72.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NA/NANIS/Crypt-SSLeay-0.72.tar.gz
Summary  : 'OpenSSL support for LWP'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Crypt-SSLeay-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : openssl-dev
BuildRequires : perl(IO::Interactive::Tiny)
BuildRequires : perl(LWP::Protocol::https)
BuildRequires : perl(Path::Class)
BuildRequires : perl(Try::Tiny)
BuildRequires : zlib-dev
Patch1: build.patch
Patch2: Crypt-SSLeay-use_TLS_instead_of_SSL.patch

%description
# Crypt::SSLeay - OpenSSL support for LWP
## Do you need Crypt::SSLeay?
Since version 6.02, [LWP](https://metacpan.org/pod/LWP) depends on [LWP::Protocol::https](https://metacpan.org/pod/LWP::Protocol::https) which pulls in [IO::Socket::SSL](https://metacpan.org/pod/IO::Socket::SSL) which is then automatically used by [LWP::UserAgent](https://metacpan.org/pod/LWP::UserAgent) unless you explicitly override it. So, you might no longer need `Crypt::SSLeay`. `IO::Socket::SSL` is preferable anyway because it allows hostname verification which `Crypt::SSLeay` does not support.

%package dev
Summary: dev components for the perl-Crypt-SSLeay package.
Group: Development
Provides: perl-Crypt-SSLeay-devel = %{version}-%{release}
Requires: perl-Crypt-SSLeay = %{version}-%{release}

%description dev
dev components for the perl-Crypt-SSLeay package.


%package perl
Summary: perl components for the perl-Crypt-SSLeay package.
Group: Default
Requires: perl-Crypt-SSLeay = %{version}-%{release}

%description perl
perl components for the perl-Crypt-SSLeay package.


%prep
%setup -q -n Crypt-SSLeay-0.72
cd %{_builddir}/Crypt-SSLeay-0.72
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::SSLeay.3
/usr/share/man/man3/Crypt::SSLeay::Version.3
/usr/share/man/man3/Net::SSL.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/SSLeay.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/SSLeay/CTX.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/SSLeay/Conn.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/SSLeay/Err.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/SSLeay/MainContext.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/SSLeay/Version.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/SSLeay/X509.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Net/SSL.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Crypt/SSLeay/SSLeay.so
