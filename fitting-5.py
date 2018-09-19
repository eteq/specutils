import numpy as np
import matplotlib.pyplot as plt

from astropy.modeling import models
from astropy import units as u

from specutils.spectra import Spectrum1D
from specutils.fitting import fit_lines

# Create a simple spectrum with a Gaussian.
np.random.seed(42)

g1 = models.Gaussian1D(1, 4.6, 0.2)
g2 = models.Gaussian1D(2.5, 5.5, 0.1)
x = np.linspace(0, 10, 200)
y = g1(x) + g2(x) + np.random.normal(0., 0.2, x.shape)

# Create the spectrum to fit
spectrum = Spectrum1D(flux=y*u.Jy, spectral_axis=x*u.um)

# Fit the spectrum
g1_init = models.Gaussian1D(amplitude=2.3*u.Jy, mean=5.6*u.um, stddev=0.1*u.um)
g2_init = models.Gaussian1D(amplitude=1.*u.Jy, mean=4.4*u.um, stddev=0.1*u.um)
g12_fit = fit_lines(spectrum, g1_init+g2_init)
y_fit = g12_fit(x*u.um)

plt.plot(x, y)
plt.plot(x, y_fit)
plt.title('Double Peak Fit')
plt.grid('on')