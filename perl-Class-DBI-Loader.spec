#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-Loader
Summary:	Class::DBI::Loader - Dynamic definition of Class::DBI sub classes
Summary(pl.UTF-8):	Class::DBI::Loader - dynamiczne definiowanie podklas Class::DBI
Name:		perl-Class-DBI-Loader
Version:	0.22
Release:	1
# same as perl 
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fdb246040add571cffc1134184e9ca0f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-DBI >= 0.89
BuildRequires:	perl-Class-DBI-SQLite >= 0.09
BuildRequires:	perl-Lingua-EN-Inflect
BuildRequires:	perl-Text-Balanced
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI::Loader automate the definition of Class::DBI sub-classes.
Is scans table schemas and setup columns, primary key.
Class::DBI::Loader supports MySQL, PostgreSQL and SQLite.

%description -l pl.UTF-8
Class::DBI::Loader automatyzuje definiowanie podklas Class::DBI. 
Skanuje schematy tabel i ustawia kolumny oraz klucz główny.
Class::DBI::Loader obsługuje MySQL-a, PostgreSQL-a oraz SQLite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/DBI/*.pm
# Class::DBI::Pg is not in PLD yet
%exclude %{perl_vendorlib}/Class/DBI/Loader/Pg.pm
%{perl_vendorlib}/Class/DBI/Loader
%exclude %{_mandir}/man3/*Pg*
%{_mandir}/man3/*
