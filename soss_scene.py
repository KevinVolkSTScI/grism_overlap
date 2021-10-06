"""
The code here takes a scene image and convolves with the NIRISS SOSS "PSF"
image to produce a simulated dispersed scene.
"""
import numpy
from astropy.io import fits
from scipy import signal
# from numpy.fft import rfftn, irfftn, fftshift, ifftshift


def soss_scene(scene_image, sossoffset=True, path='./'):
    """
    Convolve a scene image with the WFSS PSF and return dispersed image over
    the 2322x2322 pixel POM image area.

    Parameters
    ----------

    scene_image:  A numpy 2-d image (float) of an imaging scene to disperse.
                  must be the full 4231x4231 pixel work scene image

    sossoffset:   A Boolean value, says whether to* offset the reference 
                  position to the SOSS acquisition position or not

    path:         An optional string value, the path to the SOSS PSF image

    Returns
    -------

    outimage:     A numpy 2-d image (float) of the dispersed scene; size
                  2322x2322 pixels, or None if there is an issue

    The scene image is multiplied by the spot mask before the convolution in
    the area that corresponds to the output pixels.
    """
    imshape = scene_image.shape
    if (imshape[0] != 4231) or (imshape[1] != 4231): 
        print('Error in soss_scene: wrong size image' + \
              '(%d, %d) passed to the routine.' % (imshape[1], imshape[0]))
        return None
    try:
        if path[-1] != '/':
            path = path+'/'
        spotmask = fits.getdata(path+'occulting_spots_mask.fits')
    except:
        print('Error: the occulting spot mask was not found.')
        spotmask = numpy.zeros((2048, 2048), dtype=numpy.float32)+1.
    psfname = 'gr700xd_psfimage.fits'
    try:
        psfimage = fits.getdata(path+psfname)
    except:
        print('Error: PSF image %s not found in directory %s.' % (
            psfname, path))
        return None
    if not sossoffset:
        new_image = scene_image
    else:
        new_image = scene_image*0.
        new_image[174:, 930:] = scene_image[0:4057, 0:3301]
    field_image = numpy.copy(new_image[955:3277, 955:3277])
    y1 = 137
    x1 = 137
    field_image[y1:y1+2048, x1:x1+2048] = \
        field_image[y1:y1+2048,x1:x1+2048]*spotmask
    outimage = signal.fftconvolve(field_image, psfimage, mode='same')
    # scale by the grism total throughput of 0.8
    outimage = outimage*0.8
    return outimage
