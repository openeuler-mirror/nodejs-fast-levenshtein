%{?nodejs_find_provides_and_requires}
%global packagename fast-levenshtein
%global enable_tests 1
Name:		nodejs-fast-levenshtein
Version:	1.1.3
Release:	1
Summary:	Efficient implementation of Levenshtein algorithm
License:	MIT
URL:		https://github.com/hiddentao/fast-levenshtein
Source0:	https://github.com/hiddentao/fast-levenshtein/archive/%{version}.tar.gz
Patch0:		fast-levenshtein_adjust-timeouts.patch
BuildArch:	noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       	nodejs-packaging 	uglify-js
%if 0%{?enable_tests}
BuildRequires:       	mocha 	npm(chai) 	npm(lodash)
%endif

%description
Efficient implementation of Levenshtein algorithm with asynchronous callback
support.

%prep
%autosetup -n fast-levenshtein-%{version} -S git

%build
%{_bindir}/uglifyjs levenshtein.js -o levenshtein.min.js

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Fri Aug 21 2020 leiju <leiju4@huawei.com> - 1.1.3-1
- Package init
