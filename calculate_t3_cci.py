""""
study(title="FX Sniper:  T3-CCI Strategy", shorttitle="T3-CCI")
CCI_Period = input(14, minval=1)
T3_Period = input(5, minval=1)
b = input(0.618)
hline(0, color=purple, linestyle=line)
xPrice = close
b2 = b*b
b3 = b2*b
c1 = -b3
c2 = (3*(b2 + b3))
c3 = -3*(2*b2 + b + b3)
c4 = (1 + 3*b + b3 + 3*b2)
nn = iff(T3_Period < 1, 1, T3_Period)
nr = 1 + 0.5*(nn - 1)
w1 = 2 / (nr + 1)
w2 = 1 - w1
xcci = cci(xPrice, CCI_Period)
e1 = w1*xcci + w2*nz(e1[1])
e2 = w1*e1 + w2*nz(e2[1])
e3 = w1*e2 + w2*nz(e3[1])
e4 = w1*e3 + w2*nz(e4[1])
e5 = w1*e4 + w2*nz(e5[1])
e6 = w1*e5 + w2*nz(e6[1])
xccir = c1*e6 + c2*e5 + c3*e4 + c4*e3
cciHcolor = iff(xccir >= 0 , green,
        iff(xccir < 0, red, black))
pos = iff(xccir > 0, 1,
        iff(xccir < 0, -1, nz(pos[1], 0)))
barcolor(pos == -1 ? red: pos == 1 ? green : blue )
plot(xccir, color=blue, title="T3-CCI")
plot(xccir, color=cciHcolor, title="CCIH", style = histogram)
""""

CCI_PERIOD = 14
T3_PERIOD = 5
b = 0.618

b2 = b * b
b3 = b2 * b
c1 = -b3
c2 = (3*(b2 + b3))
c3 = -3*(2*b2 + b + b3)
c4 = (1 + 3*b + b3 + 3*b2)
nn = T3_PERIOD
nr = 1 + 0.5*(nn - 1)
w1 = 2 / (nr + 1)
w2 = 1 - w1
xPrice = 30380

xcci = cci(xPrice, CCI_PERIOD)
e1 = w1*xcci + w2*nz(e1[1])
e2 = w1*e1 + w2*nz(e2[1])
e3 = w1*e2 + w2*nz(e3[1])
e4 = w1*e3 + w2*nz(e4[1])
e5 = w1*e4 + w2*nz(e5[1])
e6 = w1*e5 + w2*nz(e6[1])
xccir = c1*e6 + c2*e5 + c3*e4 + c4*e3

