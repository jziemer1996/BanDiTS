def count_threshold(arr1d, lower, upper):
    from scipy.signal import find_peaks
    peaks = find_peaks(arr1d, height=(lower, upper))
    return len(peaks[0])



def count_threshold1(arr1d, threshold):
    from scipy.signal import find_peaks
    import numpy as np
    peaks = find_peaks(arr1d, height=threshold)
    return len(peaks)


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
    thresh = sf.threshold_minimum(arr1d, nbins=256, max_iter=100)
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


def threshold_triangle(arr1d):
    """
    WORKS !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_triangle(arr1d, nbins=256)
    return thresh


def threshold_multiotsu(arr1d):
    """
    takes its time !!!
    :param arr1d:
    :return:
    """
    import skimage.filters as sf
    thresh = sf.threshold_multiotsu(arr1d, classes=3, nbins=256)
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