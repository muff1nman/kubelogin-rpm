# Generated by go2rpm 1.15.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/int128/kubelogin
%global goipath         github.com/int128/kubelogin
%global binary          kubectl-oidc_login
Version:                1.31.1

%gometa -L -f

%global common_description %{expand:
Kubectl plugin for Kubernetes OpenID Connect authentication (kubectl oidc-
login).}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           golang-github-int128-kubelogin
Release:        %autorelease
Summary:        Kubectl plugin for Kubernetes OpenID Connect authentication (kubectl oidc-login)

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
export LDFLAGS='-X main.version=v%{version}'
%gobuild -o %{gobuilddir}/bin/%{binary} %{goipath}
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc docs README.md
%{_bindir}/%{binary}
%endif

%gopkgfiles

%changelog
%autochangelog
