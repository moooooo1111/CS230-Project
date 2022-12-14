# encoding: utf-8
# module matplotlib._ttconv calls itself ttconv
# from C:\Users\mr855\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\matplotlib\_ttconv.cp310-win_amd64.pyd
# by generator 1.147
""" Module to handle converting and subsetting TrueType fonts to Postscript Type 3, Postscript Type 42 and Pdf Type 3 fonts. """
# no imports

# functions

def convert_ttf_to_ps(filename, output, fonttype, glyph_ids): # real signature unknown; restored from __doc__
    """
    convert_ttf_to_ps(filename, output, fonttype, glyph_ids)
    
    Converts the Truetype font into a Type 3 or Type 42 Postscript font, optionally subsetting the font to only the desired set of characters.
    
    filename is the path to a TTF font file.
    output is a Python file-like object with a write method that the Postscript font data will be written to.
    fonttype may be either 3 or 42.  Type 3 is a "raw Postscript" font. Type 42 is an embedded Truetype font.  Glyph subsetting is not supported for Type 42 fonts within this module (needs to be done externally).
    glyph_ids (optional) is a list of glyph ids (integers) to keep when subsetting to a Type 3 font.  If glyph_ids is not provided or is None, then all glyphs will be included.  If any of the glyphs specified are composite glyphs, then the component glyphs will also be included.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E1242814E0>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._ttconv', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E1242814E0>, origin='C:\\\\Users\\\\mr855\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python310\\\\site-packages\\\\matplotlib\\\\_ttconv.cp310-win_amd64.pyd')"

