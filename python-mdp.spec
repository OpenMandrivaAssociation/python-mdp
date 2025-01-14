%define tarname MDP

Summary:	Modular Data Processing Toolkit for Python

Name:		python-mdp
Version:	3.2
Release:	3
Source0:	%{tarname}-%{version}.tar.gz
Source1:	MDP-tutorial.pdf
License:	BSD
Group:		Development/Python
Url:		https://mdp-toolkit.sourceforge.net
BuildArch:	noarch
Requires:	python-numpy >= 1.1, python-scipy >= 0.7.0
Suggests:	python-scikits-learn
BuildRequires:	python-numpy-devel >= 1.1
BuildRequires:  python-devel

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
cp -p %{SOURCE1} .
chmod 644 *.pdf

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%clean

%files -f FILELIST
%doc README CHANGES COPY* TODO *.pdf

