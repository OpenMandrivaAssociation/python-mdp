%define tarname MDP
%define name	python-mdp
%define version 3.2
%define release %mkrel 1

Summary:	Modular Data Processing Toolkit for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
Source1:	MDP-tutorial.pdf
License:	BSD
Group:		Development/Python
Url:		http://mdp-toolkit.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-numpy >= 1.1, python-scipy >= 0.7.0
Suggests:	python-scikits-learn
BuildRequires:	python-numpy-devel >= 1.1
%py_requires -d

%description
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

From the user's perspective, MDP is a collection of supervised and
unsupervised learning algorithms and other data processing units that
can be combined into data processing sequences and more complex
feed-forward network architectures.

From the scientific developer's perspective, MDP is a modular
framework, which can easily be expanded. The implementation of new
algorithms is easy and intuitive. The new implemented units are then
automatically integrated with the rest of the library.

The base of available algorithms is steadily increasing and includes
signal processing methods (Principal Component Analysis, Independent
Component Analysis, Slow Feature Analysis), manifold learning methods
([Hessian] Locally Linear Embedding), several classifiers,
probabilistic methods (Factor Analysis, RBM), data pre-processing
methods, and many others.

%prep 
%setup -q -n %{tarname}-%{version}
cp -p %SOURCE1 .
chmod 644 *.pdf

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc README CHANGES COPY* TODO *.pdf



%changelog
* Mon Oct 24 2011 Lev Givon <lev@mandriva.org> 3.2-1mdv2011.0
+ Revision: 705906
- Update to 3.2.

* Wed Mar 30 2011 Lev Givon <lev@mandriva.org> 3.1-1
+ Revision: 649255
- Update to 3.1.

* Mon Jan 17 2011 Lev Givon <lev@mandriva.org> 3.0-1
+ Revision: 631275
- Update to 3.0.

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 2.6-2mdv2011.0
+ Revision: 591347
- rebuild for py 2.7

* Fri May 14 2010 Lev Givon <lev@mandriva.org> 2.6-1mdv2011.0
+ Revision: 544824
- Update to 2.6.

* Tue Mar 23 2010 Lev Givon <lev@mandriva.org> 2.5-2mdv2010.1
+ Revision: 526968
- Require python-scipy 0.7.* instead of python-symeig
  (the former now contains symeig).

* Tue Jun 30 2009 Lev Givon <lev@mandriva.org> 2.5-1mdv2010.0
+ Revision: 390983
- Update to 2.5.

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 2.4-2mdv2009.1
+ Revision: 323908
- rebuild

* Thu Oct 23 2008 Lev Givon <lev@mandriva.org> 2.4-1mdv2009.1
+ Revision: 296626
- Update to 2.4.

* Sun Oct 12 2008 Lev Givon <lev@mandriva.org> 2.3-1mdv2009.1
+ Revision: 293040
- import python-mdp

