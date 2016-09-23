#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-SSLeay
Version  : 0.72
Release  : 13
URL      : http://www.cpan.org/CPAN/authors/id/N/NA/NANIS/Crypt-SSLeay-0.72.tar.gz
Source0  : http://www.cpan.org/CPAN/authors/id/N/NA/NANIS/Crypt-SSLeay-0.72.tar.gz
Summary  : 'OpenSSL support for LWP'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Crypt-SSLeay-lib
Requires: perl-Crypt-SSLeay-doc
BuildRequires : openssl-dev
BuildRequires : perl(LWP::Protocol::https)
BuildRequires : perl(Path::Class)
BuildRequires : perl(Try::Tiny)
BuildRequires : zlib-dev

%description
# Crypt::SSLeay - OpenSSL support for LWP
## Do you need Crypt::SSLeay?
Since version 6.02, [LWP](https://metacpan.org/pod/LWP) depends on [LWP::Protocol::https](https://metacpan.org/pod/LWP::Protocol::https) which pulls in [IO::Socket::SSL](https://metacpan.org/pod/IO::Socket::SSL) which is then automatically used by [LWP::UserAgent](https://metacpan.org/pod/LWP::UserAgent) unless you explicitly override it. So, you might no longer need `Crypt::SSLeay`. `IO::Socket::SSL` is preferable anyway because it allows hostname verification which `Crypt::SSLeay` does not support.

%package doc
Summary: doc components for the perl-Crypt-SSLeay package.
Group: Documentation

%description doc
doc components for the perl-Crypt-SSLeay package.


%package lib
Summary: lib components for the perl-Crypt-SSLeay package.
Group: Libraries

%description lib
lib components for the perl-Crypt-SSLeay package.


%prep
%setup -q -n Crypt-SSLeay-0.72

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Crypt/SSLeay.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Crypt/SSLeay/CTX.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Crypt/SSLeay/Conn.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Crypt/SSLeay/Err.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Crypt/SSLeay/MainContext.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Crypt/SSLeay/Version.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Crypt/SSLeay/X509.pm
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Net/SSL.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/auto/Crypt/SSLeay/SSLeay.so
