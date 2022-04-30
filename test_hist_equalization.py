import cv2
import numpy as np
import matplotlib.pyplot as plt


img_test = cv2.imread("test.jpg")
img_test_gray = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)

img_ref = cv2.imread("test2.jpg")
img_ref_gray = cv2.cvtColor(img_ref, cv2.COLOR_BGR2GRAY)

hist_test = cv2.calcHist([img_test_gray], [0], None, [256], [0, 256])
hist_ref = cv2.calcHist([img_ref_gray], [0], None, [256], [0, 256])


def calc_cdf(hist):
    cdf = np.zeros_like(hist)
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i] = cdf[i - 1] + hist[i]
    return cdf


def hist_normalize(hist):
    # h(v): conversion function. Maps color v to h(v)
    h = np.zeros_like(hist)
    # hist of image after this conversion will be new_hist
    new_hist = np.zeros_like(hist)
    cdf = calc_cdf(hist)
    cdf_min = np.min(cdf)
    image_size = np.sum(hist)
    for i in range(256):
        h[i] = np.round((cdf[i] - cdf_min) / (image_size - cdf_min) * 255)
        new_hist[np.int(h[i])] = hist[i]
    return h, new_hist


def hist_map(hist_1, hist_ref):
    # maps hist to hist_ref
    h = np.zeros_like(hist_1)
    cdf_1 = calc_cdf(hist_1)
    cdf_ref = calc_cdf(hist_ref)

    for i in range(256):
        w = np.argmin(np.abs(cdf_ref - cdf_1[i]))
        h[i] = w
    return h


def apply_hist(image, h):
    out = np.zeros_like(image)
    for i in range(256):
        mask = (image == i)
        out[mask] = h[i]
    return out


# # hist normalization for gray scale images
# plt.subplot(1, 2, 1)
# plt.plot(hist_test)
# plt.title('Original hist')
# plt.subplot(1, 2, 2)
# h, new_hist = hist_normalize(hist_test)
# plt.plot(new_hist)
# plt.title('Normalized hist')
# plt.show()

# plt.subplot(1, 2, 1)
# plt.imshow(img_test_gray, cmap='gray')
# plt.subplot(1, 2, 2)
# plt.imshow(apply_hist(img_test_gray, h), cmap='gray')
# plt.show()

# histgram for chanels of the ref image
chs = cv2.split(img_ref)
hist_ref_b = cv2.calcHist([chs[0]], [0], None, [256], [0, 256])
hist_ref_g = cv2.calcHist([chs[1]], [0], None, [256], [0, 256])
hist_ref_r = cv2.calcHist([chs[2]], [0], None, [256], [0, 256])

# histogram normzalization/matching for BGR image
chs = cv2.split(img_test)
hist_b = cv2.calcHist([chs[0]], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([chs[1]], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([chs[2]], [0], None, [256], [0, 256])

# hb, new_hist_b = hist_normalize(hist_b)
# hg, new_hist_g = hist_normalize(hist_g)
# hr, new_hist_r = hist_normalize(hist_r)
hb = hist_map(hist_b, hist_ref_b)
hg = hist_map(hist_g, hist_ref_g)
hr = hist_map(hist_r, hist_ref_r)

new_chb = apply_hist(chs[0], hb)
new_chg = apply_hist(chs[1], hg)
new_chr = apply_hist(chs[2], hr)
new_image = cv2.merge([new_chb, new_chg, new_chr])

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()


# # Histogram matching for bgr using skilit
# matched = match_histograms(img_test, img_ref, multichannel=True)

# fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
#                                     sharex=True, sharey=True)
# for aa in (ax1, ax2, ax3):
#     aa.set_axis_off()

# ax1.imshow(cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB))
# ax1.set_title('Source')
# ax2.imshow(cv2.cvtColor(img_ref, cv2.COLOR_BGR2RGB))
# ax2.set_title('Reference')
# ax3.imshow(cv2.cvtColor(matched, cv2.COLOR_BGR2RGB))
# ax3.set_title('Matched')

# plt.tight_layout()
# plt.show()
