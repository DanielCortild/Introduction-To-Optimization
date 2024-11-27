import numpy as np
from scipy.fftpack import dct, idct

# Black Box, Not Important how it works
def R(X):
    s = 4
    size_filter = size = 9
    PSF = np.array([[np.exp(-0.5*((i-4)/s)**2 - 0.5*((j-4)/s)**2)
                    for j in range(size)] for i in range(size)])
    PSF /= np.sum(PSF)
    def dctshift(PSF, center):
        m, n = PSF.shape
        i, j = center
        l = min(i, m-i-1, j, n-j-1)
        PP = PSF[i-l:i+l+1, j-l:j+l+1]
        Z1 = np.diag(np.ones(l+1), k=l  )
        Z2 = np.diag(np.ones(l)  , k=l+1)
        PP = Z1 @ PP @ Z1.T + Z1 @ PP @ Z2.T + Z2 @ PP @ Z1.T + \
             Z2 @ PP @ Z2.T
        Ps = np.zeros_like(PSF)
        Ps[0:2*l+1, 0:2*l+1] = PP
        return Ps
    dct2 = lambda a: dct(dct(a.T, norm='ortho').T, norm='ortho')
    idct2 = lambda a:  idct(idct(a.T,norm='ortho').T,norm='ortho')
    Pbig = np.zeros_like(X)
    Pbig[0:size_filter , 0:size_filter] = PSF
    e1 = np.zeros_like(X)
    e1[0][0] = 1
    S = np.divide( dct2(dctshift(Pbig, (4,4))), dct2(e1) )
    return idct2( np.multiply(S, dct2(X)))

R_T = R
