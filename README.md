# grism_overlap
A tool to allow evaluation of of which telescope orientations may cause overlap for the NIRISS slitless spectroscopy modes (WFSS and SOSS). 

The code requires a set of FITS files containing PSF and occulting spot mask images.  These can be found on Box at

https://stsci.app.box.com/folder/140705149002

or 

https://stsci.box.com/s/ih166mw8ded6w0qeiw7znc7xuth7n531 

The full list of files needed is:

```
f090w_gr150c_psfimage.fits
f090w_gr150r_psfimage.fits
f115w_gr150c_psfimage.fits
f115w_gr150r_psfimage.fits
f140m_gr150c_psfimage.fits
f140m_gr150r_psfimage.fits
f150w_gr150c_psfimage.fits
f150w_gr150r_psfimage.fits
f158m_gr150c_psfimage.fits
f158m_gr150r_psfimage.fits
f200w_gr150c_psfimage.fits
f200w_gr150r_psfimage.fits
fits_image_display.py
general_utilities.py
gr700xd_psfimage.fits
grism_overlap_tool.py
mirage_format.py
mpfit.py
mpfitexpr.py
niriss_NIS_x1024_y1024_f090w_predicted_0_0p00_0p00.fits
niriss_NIS_x1024_y1024_f115w_predicted_0_0p00_0p00.fits
niriss_NIS_x1024_y1024_f140m_predicted_0_0p00_0p00.fits
niriss_NIS_x1024_y1024_f150w_predicted_0_0p00_0p00.fits
niriss_NIS_x1024_y1024_f158m_predicted_0_0p00_0p00.fits
niriss_NIS_x1024_y1024_f200w_predicted_0_0p00_0p00.fits
occulting_spots_mask.fits
scene_image.py
soss_scene.py
wfss_scene.py
```
# The Code

The file 'grism_overlap_tool.py" is the main program.  It imports the other codes: 'fits_image_display.py', 'general_utilities.py', 'scene_image.py', 
'soss_scene.py' and 'wfss_scene.py'.  If the code is being run in a directory besides the one where the files are, one needs to have that directory in 
the $PYTHONPATH environment variable.

The codes depend on the following python packages:  sys, os, math, tkinter, numpy, scipy, matplotlib, pysiaf, and astropy.

Astropy can be found at https://www.astropy.org/.  The pysiaf code is found at https://github.com/spacetelescope/pysiaf.  Note that installation of pysiaf should be done via cloning the github repository as described at the github page, rather than using "pip install pysiaf" because the latter currently gives one an out-of-date version of pysiaf.

# Running The Code

One simply invokes the main code 'grism_overlap_tool.py' from the command line, with no parameters.  To test the code one needs at minimum a Mirage NIRISS point source input file, so an example is provided in 'stars_bd601753_gaia_allfilters.list'.  This file is for the field of the photometric standard BD+30 1753, the star being source 312 on the list at sky position RA=261.217858, Dec=60.430781.  This is suitable for testing the SOSS mode case.  Another example more suitable for the WFSS case is provided in the file 'stars_wdfield_combined_allfilters.list'.  The target here is WD1657+343.  This star, another photometric standard, is star 158 in the list at sky position RA=254.713015, Dec=34.314677.
 
Documentation is available in the files grism_overlap.docx and grism_overlap.pdf which show how the code can be used.

