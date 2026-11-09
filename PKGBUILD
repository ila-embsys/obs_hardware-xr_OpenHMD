basename=openhmd
pkgname=$basename-git
pkgver=0
pkgrel=1
pkgdesc="Free and Open Source API and drivers for immersive technology."
arch=(x86_64 i686)
url="https://github.com/OpenHMD/OpenHMD"
license=(Boost)
depends=(hidapi glibc)
conflicts=($basename)
provides=($basename)
makedepends=(meson)

optdepends=(
  'xr-hardware: Udev rules for accessing XR (VR and AR) hardware devices',
  'oculus-udev: Udev rule for Oculus Rift',
  'vive-udev: Udev rule for HTC Vive'
)

source=(OpenHMD-${pkgver}.tar.gz)
sha256sums=("SKIP")

prepare() {
  patch --forward --strip=1 --input="${srcdir}/0001-nreal-add-driver-from-monado.patch"
  patch --forward --strip=1 --input="${srcdir}/0002-nreal-remove-maybe-unused.patch"
  patch --forward --strip=1 --input="${srcdir}/0003-nreal-use-teardown-in-close-device.patch"
  patch --forward --strip=1 --input="${srcdir}/0004-nreal-cleanup-semantic-and-mutex-init.patch"
}

build() {
  arch-meson -Dexamples='' build "OpenHMD-${pkgver}"
  ninja -C build
}

check() {
  ninja -C build test
}

package() {
  DESTDIR="$pkgdir" ninja install -C build
}
