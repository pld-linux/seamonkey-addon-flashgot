
%define		_realname	flashgot

Summary:	Download helper
Summary(pl.UTF-8):	Narzędzie pomagające w ściąganiu
Name:		seamonkey-addon-%{_realname}
Version:	0.5.97.03
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/mozilla.org/extensions/flashgot/%{_realname}-%{version}-fx+fl+mz+ns+zm+tb.xpi
# Source0-md5:	633e84506fcf8fce9d0285b07f6e0f24
Source1:	gen-installed-chrome.sh
URL:		http://flashgot.net/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	seamonkey >= 1.0
Requires:	seamonkey >= 1.0
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/seamonkey/chrome

%description
Download one link, selected links or all the links of a page together
at the maximum speed with a single click, using the most popular,
lightweight and reliable external download managers. Supported
download tools are dozens, see http://flashgot.net/ for details. This
extension offers also a Build Gallery functionality which helps to
collect in a single page serial movies and images scattered on several
pages, for easy and fast "download all".

%description -l pl.UTF-8
To rozszerzenie pozwala ściągnąć pojedynczy odnośnik, wybrane
odnośniki lub wszystkie odnośniki ze strony z maksymalną prędkością za
pomocą jednego kliknięcia, przy użyciu najbardziej popularnych,
lekkich i niezawodnych zarządcą ściągania. Obsługiwanych narzędzi jest
wiele, szczegóły na <http://flashgot.net/>. To rozszerzenie oferuje
także funkcjonalność budowania galerii pomagające przy zbieraniu na
jednej stronie wielu filmów i obrazów zgromadzonych z wielu stron przy
łatwym i szybkim "ściąganiu wszystkiego".

%prep
%setup -qc

# remove .exe file
zip -d chrome/%{_realname}.jar "content/flashgot/FlashGot*"

install %{SOURCE1} .
./gen-installed-chrome.sh locale chrome/%{_realname}.jar \
	| sed '/content/s/^locale/content/; /skin/s/^locale/skin/;' \
	> %{_realname}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_chromedir},%{_libdir}/seamonkey}

install chrome/%{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey
cp -r components $RPM_BUILD_ROOT%{_libdir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
%{_datadir}/seamonkey/defaults/preferences/flashgot.js
%{_libdir}/seamonkey/components/flashgotService.js
