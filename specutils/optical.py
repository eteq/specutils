# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This package contains subclasses of specutils base classes exposing
interfaces like those typically expected for optical/NIR spectra.
"""
#this is not yet in the 
from .spectrum1d import Spectrum1D 

#This is an example class
class OpticalSpectrum1D(Spectrum1D):
    """
    A spectrum covering optical/NIR wavelengths.
    """
