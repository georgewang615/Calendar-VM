# Contributor:
# Maintainer:
pkgname=assignment2
pkgver=1.0
pkgrel=0
pkgdesc="Calendar program containg daemon written in python"
url=""
arch="all"
license=""
depends=""
makedepends=""
checkdepends=""
install="$pkgname.pre-install $pkgname.post-install"
subpackages="$pkgname-dev $pkgname-doc"
source="
	assignment2.initd
	assignment2.confd
	"
builddir="$srcdir/"

build() {
	make -C build
}

check() {
	make -C build start
}

package() {
	make -C build DESTDIR="pkgdir" install

	install -m755 -D "$srcdir"/$pkgname.initd \
		"$pkgdir"/etc/init.d/$pkgname
	install -m644 -D "$srcdir"/$pkgname.confd \
		"$pkgdir"/etc/conf.d/$pkgname
}

