# We begin with some basic  imports:

from astropy.io import fits
from astropy import units as u
import numpy as np
from matplotlib import pyplot as plt
from astropy.visualization import quantity_support
quantity_support()  # for getting units on the axes below # doctest: +ELLIPSIS
# <astropy.visualization.units.quantity_support...>

# Now we load the dataset from it's canonical source:

f = fits.open('https://dr14.sdss.org/optical/spectrum/view/data/format=fits/spec=lite?plateid=1323&mjd=52797&fiberid=12') # doctest: +ELLIPSIS
# Downloading ...
specdata = f[1].data
f.close()

# Then we re-format this dataset into astropy quantities, and create a
# `~specutils.Spectrum1D` object:

from specutils import Spectrum1D
lamb = 10**specdata['loglam'] * u.AA
flux = specdata['flux'] * 10**-17 *u.erg *u.s**-1*u.cm**-2 / u.AA
spec = Spectrum1D(spectral_axis=lamb, flux=flux)

# And we plot it:

lines = plt.step(spec.spectral_axis, spec.flux)
