%define upstream_name    Test-MockDBI
Name:       perl-%{upstream_name}
Version:    0.65
Release:    5
Summary:    Test by mocking-up DBI 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/A/AF/AFF/%{upstream_name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl(DBI)
BuildRequires:  perl(Test::MockObject)
Requires:       perl(DBI)
BuildArch: noarch

%description
Test::MockDBI provides a way to test DBI interfaces by creating rules for
changing the DBI\'s behavior, then examining the standard output for
matching patterns. 

%prep
%setup -q -n %{upstream_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files
%defattr(-,root,root,755)
%doc Changes HISTORY README TODO
%{_mandir}/man3/*
%{perl_vendorlib}/*
