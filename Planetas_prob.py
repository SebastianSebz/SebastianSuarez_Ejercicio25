import numpy as np
import matplotlib.pyplot as plt

#constantes

const_helio = 1.33e20
mass_earth = 5.972e24
mass_sun = 332950* mass_earth
un_astr = 1.496e+11

#Venus vector

Xven =-3.41E-01*un_astr
Yven = 6.38E-01*un_astr
Zven = 2.83E-02*un_astr

r_ven = np.sqrt(Xven**2+Yven**2+Zven**2)
#print r_ven

#Earth vector

Xearth =-6.86E-01*un_astr
Yearth =-7.33E-01*un_astr
Zearth =-6.64E-05*un_astr

r_earth = np.sqrt(Xearth**2+Yearth**2+Zearth**2)
#print r_earth

#Mercury vector

Xm = 2.88E+01*un_astr
Ym =-8.20E+00*un_astr
Zm =-4.95E-01*un_astr

r_merc = np.sqrt(Xm**2+Ym**2+Zm**2)
#print r_merc


#Valores aleatorios de alpha entre 0 y 4
alpha = np.random.random_sample()*4
#print alpha

Vobs_merc = 5.4778*1000

def beta(alpha):
	beta= (Vobs_merc**2)/(r_merc**(1-alpha))
	return beta

for i in range (1000):
	print i, beta(np.random.random_sample()*4)
	i = 1+i

	



	


















































