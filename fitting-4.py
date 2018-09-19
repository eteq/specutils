import numpy as np
import matplotlib.pyplot as plt

from astropy.modeling import models
from astropy import units as u

from specutils.spectra import Spectrum1D
from specutils.fitting import fit_lines

# Create a simple spectrum with a Gaussian.
np.random.seed(0)
x = np.linspace(0., 10., 200)
y = 3 * np.exp(-0.5 * (x- 6.3)**2 / 0.8**2)
y += np.random.normal(0., 0.2, x.shape)

# Create the spectrum
spectrum = Spectrum1D(flux=y*u.Jy, spectral_axis=x*u.um)

# Fit the spectrum
g_init = models.Gaussian1D(amplitude=3.*u.Jy, mean=5.5*u.um, stddev=1.*u.um)
g_fit = fit_lines(spectrum, g_init, window=(6*u.um, 7*u.um))
y_fit = g_fit(x*u.um)

plt.plot(x, y)
plt.plot(x, y_fit)
plt.title('Single fit peak window')
plt.grid('on')