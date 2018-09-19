import numpy as np
from astropy import units as u
from astropy.nddata import StdDevUncertainty
from astropy.modeling import models
from specutils import Spectrum1D, SpectralRegion
np.random.seed(42)
spectral_axis = np.linspace(0., 10., 200) * u.GHz
spectral_model = models.Gaussian1D(amplitude=3*u.Jy, mean=5*u.GHz, stddev=0.8*u.GHz)
flux = spectral_model(spectral_axis)
flux += np.random.normal(0., 0.2, spectral_axis.shape) * u.Jy
uncertainty = StdDevUncertainty(0.2*np.ones(flux.shape)*u.Jy)
noisy_gaussian = Spectrum1D(spectral_axis=spectral_axis, flux=flux, uncertainty=uncertainty)
import matplotlib.pyplot as plt #doctest:+SKIP
plt.plot(noisy_gaussian.spectral_axis, noisy_gaussian.flux) #doctest:+SKIP
