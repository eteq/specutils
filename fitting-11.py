import numpy as np
import matplotlib.pyplot as plt

from astropy.modeling import models
from astropy import units as u

from specutils.spectra import Spectrum1D, SpectralRegion
from specutils.fitting import fit_generic_continuum

np.random.seed(0)
x = np.linspace(0., 10., 200)
y = 3 * np.exp(-0.5 * (x - 6.3)**2 / 0.1**2)
y += np.random.normal(0., 0.2, x.shape)

y_continuum = 3.2 * np.exp(-0.5 * (x - 5.6)**2 / 4.8**2)
y += y_continuum

spectrum = Spectrum1D(flux=y*u.Jy, spectral_axis=x*u.um)

g1_fit = fit_generic_continuum(spectrum)

y_continuum_fitted = g1_fit(x)

plt.plot(x, y)
plt.plot(x, y_continuum_fitted)
plt.title('Continuum Fitting')
plt.grid('on')