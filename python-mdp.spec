%define tarname MDP
%define name	python-mdp
%define version 2.5
%define release %mkrel 1

Summary:	Modular Data Processing Toolkit for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
Source1:	MDP2_5_tutorial.pdf
License:	LGPLv3+
Group:		Development/Python
Url:		http://mdp-toolkit.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.4, python-numpy >= 1.1, python-symeig
BuildRequires:	python-devel >= 2.4, python-numpy-devel >= 1.1, python-symeig
BuildArch:	noarch

%description
The Modular toolkit for Data Processing (MDP) is a Python data
processing framework. Implemented algorithms include: Principal
Component Analysis (PCA), Independent Component Analysis (ICA), Slow
Feature Analysis (SFA), Independent Slow Feature Analysis (ISFA),
Growing Neural Gas (GNG), Factor Analysis, Fisher Discriminant
Analysis (FDA), Gaussian Classifiers, and Restricted Boltzmann
Machines.  

%prep 
%setup -q -n %{tarname}-%{version}
cp -p %SOURCE1 .
chmod 644 *.pdf

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc README CHANGES COPY* *.pdf

