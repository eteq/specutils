import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt
from specutils import Spectrum1D
flux = np.random.randn(200)*u.Jy
wavelength = np.arange(5100, 5300)*u.AA
spec1d = Spectrum1D(spectral_axis=wavelength, flux=flux)
ax = plt.subplots()[1]  # doctest: +SKIP
ax.plot(spec1d.spectral_axis, spec1d.flux)  # doctest: +SKIP
ax.set_xlabel("Dispersion")  # doctest: +SKIP
ax.set_ylabel("Flux")  # doctest: +SKIP
