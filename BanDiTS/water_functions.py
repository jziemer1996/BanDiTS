################################ WORKING FUNCTIONS #############################
import skimage
import skimage.filters as sf
from skimage.filters import *
from scipy.signal import find_peaks

def count_threshold(arr1d, lower, upper):
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=(lower, upper))
    return len(peaks[0])


def count_threshold1(arr1d, threshold):
    from scipy.signal import find_peaks
    import numpy as np
    peaks = find_peaks(arr1d, height=threshold)
    return len(peaks)


def count_threshold2(arr1d, threshold):
    from scipy.signal import find_peaks
    import numpy as np
    peaks = find_peaks(arr1d, height=threshold)
    if len(peaks[0]) >= 1:
        return np.int32(peaks[0][0])
    if len(peaks[0]) == 0:
        return np.int32(peaks[0][0])


def threshold_otsu(arr1d):
    """
    https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.threshold_otsu
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_otsu(arr1d, nbins=256)
    #print(thresh)
    return thresh


def threshold_li(arr1d):
    """
    works with errors
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_li(arr1d, tolerance=None,
                             initial_guess=None, iter_callback=None)
    return thresh


def threshold_yen(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_yen(arr1d, nbins=256)
    return thresh


def threshold_mean(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_mean(arr1d)
    return thresh


def threshold_triangle(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_triangle(arr1d, nbins=256)
    return thresh

################################ NOT WORKING FUNCTIONS #############################


def threshold_local(arr1d):
    """
    doesnt work because its no 2D array
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_local(arr1d, block_size=9, method='gaussian',
                                offset=0, mode='reflect')
    return thresh


def threshold_minimum(arr1d):
    """
    doesnt work: Unable to find two maxima in histogram
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_minimum(arr1d, nbins=256, max_iter=1000)
    return thresh


def threshold_niblack(arr1d):
    """
    doesnt work: TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_niblack(arr1d, window_size=15, k=0.2)
    return thresh


def threshold_sauvola(arr1d):
    """
    doesnt work: TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_sauvola(arr1d, window_size=15, k=0.2, r=None)
    return thresh


def threshold_multiotsu(arr1d, classes):
    """
    TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_multiotsu(arr1d, classes, nbins=256)
    return thresh


def apply_hysteresis_threshold(arr1d):
    """
    TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.apply_hysteresis_threshold(arr1d, low=-25.0, high=-23.0)
    return thresh


def unsharp_mask(arr1d):
    """
    TypeError: ndarray() missing required argument 'shape' (pos 1)
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.unsharp_mask(arr1d, radius=1.0, amount=1.0, multichannel=False,
                             preserve_range=False)
    return thresh


################################ LETS GIVIT A TRY FUNCTIONS #############################

def inverse(arr1d):
    import skimage.filters as sf
    skimage.filters.inverse(arr1d, impulse_response=None,
                        filter_params={}, max_gain=2, predefined_filter=None)

def try_all_threshold(arr1d):
    import skimage.filters as sf
    skimage.filters.try_all_threshold(arr1d, figsize=(8, 5), verbose=True)