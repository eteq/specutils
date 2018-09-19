from specutils import SpectralRegion
from specutils.analysis import equivalent_width
cont_norm_spec = spec / np.median(spec.flux)  # TODO: replace this with fit_generic_continuum
fig = plt.figure()
lines = plt.step(cont_norm_spec.wavelength, cont_norm_spec.flux)
plt.xlim(654*u.nm, 660*u.nm)
equivalent_width(spec, regions=SpectralRegion(6562*u.AA, 6575*u.AA))
# <Quantity -10.58691406 Angstrom>
