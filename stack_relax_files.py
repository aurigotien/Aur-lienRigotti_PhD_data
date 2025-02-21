import numpy as np
import scipy.optimize as sc
import math as math
#import random as r # load random package

# Exponential fit functions #
def moving_average(val, window): # compute the moving average over a window "window" on a vector "val"
    return np.convolve(val, np.ones(window), 'valid') / window

def power_exp(xval,slope,t_relax,b,y_c):
    return slope*np.exp(-(xval/t_relax)**b) + y_c

def power_exp_fit(xval,t_relax,b):
    return np.exp(-(xval/t_relax)**b)

def deviation_run(val,N):
    return (val[:] - val.mean())

def gamma_function(val):
    return math.gamma((1/val))

def ponderation(val,error,N,to_ponder):
    # Function variable
    # Scalar
    ponder, output = 0, 0

    # Vector
    std = deviation_run(val,N) # compute distance to the mean for each run

    # Ponderation computation
    for i in range(N):
        if to_ponder == 'mean': output, ponder = output + abs(val[i]/std[i]), ponder + abs(1/std[i])
        elif to_ponder == 'std': output, ponder = output + abs(error[i]/std[i]), ponder + abs(1/std[i])
    return output / ponder

def data_fit(val_x,val_y,no_coeff,module,no_stack,no_ela):
    # Function variable
    # Scalar
    max_it = 10**6 # max of iteration for the fit
    len_vec = len(val_y)

    # Vector
    val_fit, val_t_fit, param = np.zeros(len_vec), np.zeros(len_vec), np.zeros(no_coeff)
    error = np.zeros(4) # error on beta and t_relax
    param_bound = [(0,0),(1E2,2)] # format bound = [(min t*,min beta), (max t*, max beta)]

    if no_ela < 5 :
        val_0 = np.array((10,1.2)) # First guess prep_no_fric
        #val_0  = np.array((500,2))
    elif no_ela >= 5 :
        val_0 = np.array((5,1.2)) # First guess prep_no_fric
        #val_0  = np.array((100,2))
    # end if

    # yield stress and slope
    if val_y[len_vec-1] >= 0 : y_c = val_y[len_vec-1] # common for all the stacks
    else : y_c = 0 # end if

    slope = abs(val_y[1] - y_c) # prep_no_fric

    for i in range(len_vec):
        val_fit[i] = (val_y[i] - y_c) / slope
        #if val_fit[i] == 0 : val_t_fit[i] = np.log(1E-6)
    # end of i for loop

    coeff, cv = sc.curve_fit(power_exp_fit, np.float64(val_x), np.float64(val_fit), p0 = np.float64(val_0), bounds = param_bound, method = 'trf', maxfev=max_it)
    #param, cv = sc.curve_fit(power_exp, np.float64(val_x), np.float64(val_y), bounds = param_bound, maxfev=max_it)
    error[1], error[2] = cv[0,0], cv[1,1] # determine quality of the fit

    # parameter value
    param[0], param[1], param[2], param[3] = slope, coeff[0], coeff[1], y_c

    #print('\n', 'first guess : slope = ', slope,' ; t* = ', val_0[0],' ; b = ', val_0[1] ,' ; S_c = ', y_c)
    #print('fit parameters : slope = ', param[0],' ; t* = ', param[1],' ; b = ', param[2], ' ; S_c = ',param[3])
    #print('error = ', fit_error, '\n')
    return param[:], error

# Data treatment functions #
# compute the reduced elastic relaxation matrix and compute the coefficient for an exponential fit
def ela_relax_fit(data,no_coeff,module,no_stack,no_ela):
    # Function variables
    # Scalar
    dt = 1E-4
    step = 7500
    len_fit = 401 # fit on first half of the datas

    # Vectors
    # exponential fit coefficient f(x) = exp[-A*(X/B)^b] + C
    coeff, time = np.zeros(no_coeff), np.zeros(len_fit)

    # Computation
    # compute the x axis (time value)
    for i in range(len_fit): time[i] = (dt*step*i)
    coeff,d_coeff = data_fit(time[:],data[:],no_coeff,module,no_stack,no_ela)

    return coeff[:],d_coeff

# Function computing mean stress, volume and volumetric deformation from ela_comp files
def val_ela_relax(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,module,n):
    # Function variables #
    # Scalar
    N = 30 # number of files
    dt = 1E-4 # discretisation time

    # Matrix
    ave_std = np.zeros((n,14))  # matrix to store averaged values and standard deviation

    val = np.zeros((n,N)) # matrix to store the shear stress values, 1 col/simulation
    S_xx  = np.zeros((n,N)) # matrix to store the S_xx stress values, 1 col/simulation
    S_yy = np.zeros((n,N)) # matrix to store the S_yy stress values, 1 col/simulation
    press = np.zeros((n,N)) # matrix to store the pressure, 1 col/simulation
    vol = np.zeros((n,N)) # matrix to store volume of the system, 1 col / simulation
    l = np.zeros((n,N)) # matrix to store length of the system, 1 col / simulation
    z = np.zeros((n,N)) # matrix to store coordination number value, 1 col / simulation
    moy_vel = np.zeros((n,N)) # matrix to store the computed average velocity value, 1 col / simulation

    # create valN file to extract the value from the 30 dataN file
    val1 = np.zeros((n,N))
    val2 = np.zeros((n,N))
    val3 = np.zeros((n,N))
    val4 = np.zeros((n,N))
    val5 = np.zeros((n,N))
    val6 = np.zeros((n,N))
    val7 = np.zeros((n,N))
    val8 = np.zeros((n,N))
    val9 = np.zeros((n,N))
    val10 = np.zeros((n,N))
    val11 = np.zeros((n,N))
    val12 = np.zeros((n,N))
    val13 = np.zeros((n,N))
    val14 = np.zeros((n,N))
    val15 = np.zeros((n,N))
    val16 = np.zeros((n,N))
    val17 = np.zeros((n,N))
    val18 = np.zeros((n,N))
    val19 = np.zeros((n,N))
    val20 = np.zeros((n,N))
    val21 = np.zeros((n,N))
    val22 = np.zeros((n,N))
    val23 = np.zeros((n,N))
    val24 = np.zeros((n,N))
    val25 = np.zeros((n,N))
    val25 = np.zeros((n,N))
    val26 = np.zeros((n,N))
    val27 = np.zeros((n,N))
    val28 = np.zeros((n,N))
    val29 = np.zeros((n,N))
    val30 = np.zeros((n,N))

    # Read the datas #
    data1.readline()
    data2.readline()
    data3.readline()
    data4.readline()
    data5.readline()
    data6.readline()
    data7.readline()
    data8.readline()
    data9.readline()
    data10.readline()
    data11.readline()
    data12.readline()
    data13.readline()
    data14.readline()
    data15.readline()
    data16.readline()
    data17.readline()
    data18.readline()
    data19.readline()
    data20.readline()
    data21.readline()
    data22.readline()
    data23.readline()
    data24.readline()
    data25.readline()
    data26.readline()
    data27.readline()
    data28.readline()
    data29.readline()
    data30.readline()

    # Attribution of the values #
    val1 = np.loadtxt(data1)
    val2 = np.loadtxt(data2)
    val3 = np.loadtxt(data3)
    val4 = np.loadtxt(data4)
    val5 = np.loadtxt(data5)
    val6 = np.loadtxt(data6)
    val7 = np.loadtxt(data7)
    val8 = np.loadtxt(data8)
    val9 = np.loadtxt(data9)
    val10 = np.loadtxt(data10)
    val11 = np.loadtxt(data11)
    val12 = np.loadtxt(data12)
    val13 = np.loadtxt(data13)
    val14 = np.loadtxt(data14)
    val15 = np.loadtxt(data15)
    val16 = np.loadtxt(data16)
    val17 = np.loadtxt(data17)
    val18 = np.loadtxt(data18)
    val19 = np.loadtxt(data19)
    val20 = np.loadtxt(data20)
    val21 = np.loadtxt(data21)
    val22 = np.loadtxt(data22)
    val23 = np.loadtxt(data23)
    val24 = np.loadtxt(data24)
    val25 = np.loadtxt(data25)
    val26 = np.loadtxt(data26)
    val27 = np.loadtxt(data27)
    val28 = np.loadtxt(data28)
    val29 = np.loadtxt(data29)
    val30 = np.loadtxt(data30)

    # Volume
    for i in range(n): # Volume computation for each simulation
        vol[i,0] = (val1[i,4]*val1[i,5])
        vol[i,1] = (val2[i,4]*val2[i,5])
        vol[i,2] = (val3[i,4]*val3[i,5])
        vol[i,3] = (val4[i,4]*val4[i,5])
        vol[i,4] = (val5[i,4]*val5[i,5])
        vol[i,5] = (val6[i,4]*val6[i,5])
        vol[i,6] = (val7[i,4]*val7[i,5])
        vol[i,7] = (val8[i,4]*val8[i,5])
        vol[i,8] = (val9[i,4]*val9[i,5])
        vol[i,9] = (val10[i,4]*val10[i,5])
        vol[i,10] = (val11[i,4]*val11[i,5])
        vol[i,11] = (val12[i,4]*val12[i,5])
        vol[i,12] = (val13[i,4]*val13[i,5])
        vol[i,13] = (val14[i,4]*val14[i,5])
        vol[i,14] = (val15[i,4]*val15[i,5])
        vol[i,15] = (val16[i,4]*val16[i,5])
        vol[i,16] = (val17[i,4]*val17[i,5])
        vol[i,17] = (val18[i,4]*val18[i,5])
        vol[i,18] = (val19[i,4]*val19[i,5])
        vol[i,19] = (val20[i,4]*val20[i,5])
        vol[i,20] = (val21[i,4]*val21[i,5])
        vol[i,21] = (val22[i,4]*val22[i,5])
        vol[i,22] = (val23[i,4]*val23[i,5])
        vol[i,23] = (val24[i,4]*val24[i,5])
        vol[i,24] = (val25[i,4]*val25[i,5])
        vol[i,25] = (val26[i,4]*val26[i,5])
        vol[i,26] = (val27[i,4]*val27[i,5])
        vol[i,27] = (val28[i,4]*val28[i,5])
        vol[i,28] = (val29[i,4]*val29[i,5])
        vol[i,29] = (val30[i,4]*val30[i,5])

    # Sample height
        l[i,0] = val1[i,4]
        l[i,1] = val2[i,4]
        l[i,2] = val3[i,4]
        l[i,3] = val4[i,4]
        l[i,4] = val5[i,4]
        l[i,5] = val6[i,4]
        l[i,6] = val7[i,4]
        l[i,7] = val8[i,4]
        l[i,8] = val9[i,4]
        l[i,9] = val10[i,4]
        l[i,10] = val11[i,4]
        l[i,11] = val12[i,4]
        l[i,12] = val13[i,4]
        l[i,13] = val14[i,4]
        l[i,14] = val15[i,4]
        l[i,15] = val16[i,4]
        l[i,16] = val17[i,4]
        l[i,17] = val18[i,4]
        l[i,18] = val19[i,4]
        l[i,19] = val20[i,4]
        l[i,20] = val21[i,4]
        l[i,21] = val22[i,4]
        l[i,22] = val23[i,4]
        l[i,23] = val24[i,4]
        l[i,24] = val25[i,4]
        l[i,25] = val26[i,4]
        l[i,26] = val27[i,4]
        l[i,27] = val28[i,4]
        l[i,28] = val29[i,4]
        l[i,29] = val30[i,4]

    # Shear stress (Pa)
    for i in range(n): # Mean shear stress computation (LAMMPS P = mean stress * volume)
        if module == 'deviatoric':
            val[i,0] = np.sqrt(((((val1[i,7]/vol[i,0])-(val1[i,8]/vol[i,0]))/2)**2)+((val1[i,9]/vol[i,0])**2))
            val[i,1] = np.sqrt(((((val2[i,7]/vol[i,1])-(val2[i,8]/vol[i,1]))/2)**2)+((val2[i,9]/vol[i,1])**2))
            val[i,2] = np.sqrt(((((val3[i,7]/vol[i,2])-(val3[i,8]/vol[i,2]))/2)**2)+((val3[i,9]/vol[i,2])**2))
            val[i,3] = np.sqrt(((((val4[i,7]/vol[i,3])-(val4[i,8]/vol[i,3]))/2)**2)+((val4[i,9]/vol[i,3])**2))
            val[i,4] = np.sqrt(((((val5[i,7]/vol[i,4])-(val5[i,8]/vol[i,4]))/2)**2)+((val5[i,9]/vol[i,4])**2))
            val[i,5] = np.sqrt(((((val6[i,7]/vol[i,5])-(val6[i,8]/vol[i,5]))/2)**2)+((val6[i,9]/vol[i,5])**2))
            val[i,6] = np.sqrt(((((val7[i,7]/vol[i,6])-(val7[i,8]/vol[i,6]))/2)**2)+((val7[i,9]/vol[i,6])**2))
            val[i,7] = np.sqrt(((((val8[i,7]/vol[i,7])-(val8[i,8]/vol[i,7]))/2)**2)+((val8[i,9]/vol[i,7])**2))
            val[i,8] = np.sqrt(((((val9[i,7]/vol[i,8])-(val9[i,8]/vol[i,8]))/2)**2)+((val9[i,9]/vol[i,8])**2))
            val[i,9] = np.sqrt(((((val10[i,7]/vol[i,9])-(val10[i,8]/vol[i,9]))/2)**2)+((val10[i,9]/vol[i,9])**2))
            val[i,10] = np.sqrt(((((val11[i,7]/vol[i,10])-(val11[i,8]/vol[i,10]))/2)**2)+((val11[i,9]/vol[i,10])**2))
            val[i,11] = np.sqrt(((((val12[i,7]/vol[i,11])-(val12[i,8]/vol[i,11]))/2)**2)+((val12[i,9]/vol[i,11])**2))
            val[i,12] = np.sqrt(((((val13[i,7]/vol[i,12])-(val13[i,8]/vol[i,12]))/2)**2)+((val13[i,9]/vol[i,12])**2))
            val[i,13] = np.sqrt(((((val14[i,7]/vol[i,13])-(val14[i,8]/vol[i,13]))/2)**2)+((val14[i,9]/vol[i,13])**2))
            val[i,14] = np.sqrt(((((val15[i,7]/vol[i,14])-(val15[i,8]/vol[i,14]))/2)*2)+((val15[i,9]/vol[i,14])**2))
            val[i,15] = np.sqrt(((((val16[i,7]/vol[i,15])-(val16[i,8]/vol[i,15]))/2)**2)+((val16[i,9]/vol[i,15])**2))
            val[i,16] = np.sqrt(((((val17[i,7]/vol[i,16])-(val17[i,8]/vol[i,16]))/2)**2)+((val17[i,9]/vol[i,16])**2))
            val[i,17] = np.sqrt(((((val18[i,7]/vol[i,17])-(val18[i,8]/vol[i,17]))/2)**2)+((val18[i,9]/vol[i,17])**2))
            val[i,18] = np.sqrt(((((val19[i,7]/vol[i,18])-(val19[i,8]/vol[i,18]))/2)**2)+((val19[i,9]/vol[i,18])**2))
            val[i,19] = np.sqrt(((((val20[i,7]/vol[i,19])-(val20[i,8]/vol[i,19]))/2)**2)+((val20[i,9]/vol[i,19])**2))
            val[i,20] = np.sqrt(((((val21[i,7]/vol[i,20])-(val21[i,8]/vol[i,20]))/2)**2)+((val21[i,9]/vol[i,20])**2))
            val[i,21] = np.sqrt(((((val22[i,7]/vol[i,21])-(val22[i,8]/vol[i,21]))/2)**2)+((val22[i,9]/vol[i,21])**2))
            val[i,22] = np.sqrt(((((val23[i,7]/vol[i,22])-(val23[i,8]/vol[i,22]))/2)**2)+((val23[i,9]/vol[i,22])**2))
            val[i,23] = np.sqrt(((((val24[i,7]/vol[i,23])-(val24[i,8]/vol[i,23]))/2)**2)+((val24[i,9]/vol[i,23])**2))
            val[i,24] = np.sqrt(((((val25[i,7]/vol[i,24])-(val25[i,8]/vol[i,24]))/2)**2)+((val25[i,9]/vol[i,24])**2))
            val[i,25] = np.sqrt(((((val26[i,7]/vol[i,25])-(val26[i,8]/vol[i,25]))/2)**2)+((val26[i,9]/vol[i,25])**2))
            val[i,26] = np.sqrt(((((val27[i,7]/vol[i,26])-(val27[i,8]/vol[i,26]))/2)**2)+((val27[i,9]/vol[i,26])**2))
            val[i,27] = np.sqrt(((((val28[i,7]/vol[i,27])-(val28[i,8]/vol[i,27]))/2)**2)+((val28[i,9]/vol[i,27])**2))
            val[i,28] = np.sqrt(((((val29[i,7]/vol[i,28])-(val29[i,8]/vol[i,28]))/2)**2)+((val29[i,9]/vol[i,28])**2))
            val[i,29] = np.sqrt(((((val30[i,7]/vol[i,29])-(val30[i,8]/vol[i,29]))/2)**2)+((val30[i,9]/vol[i,29])**2))
        elif module == 'shear':
            val[i,0] = val1[i,9]/vol[i,0]
            val[i,1] = val2[i,9]/vol[i,1]
            val[i,2] = val3[i,9]/vol[i,2]
            val[i,3] = val4[i,9]/vol[i,3]
            val[i,4] = val5[i,9]/vol[i,4]
            val[i,5] = val6[i,9]/vol[i,5]
            val[i,6] = val7[i,9]/vol[i,6]
            val[i,7] = val8[i,9]/vol[i,7]
            val[i,8] = val9[i,9]/vol[i,8]
            val[i,9] = val10[i,9]/vol[i,9]
            val[i,10] = val11[i,9]/vol[i,10]
            val[i,11] = val12[i,9]/vol[i,11]
            val[i,12] = val13[i,9]/vol[i,12]
            val[i,13] = val14[i,9]/vol[i,13]
            val[i,14] = val15[i,9]/vol[i,14]
            val[i,15] = val16[i,9]/vol[i,15]
            val[i,16] = val17[i,9]/vol[i,16]
            val[i,17] = val18[i,9]/vol[i,17]
            val[i,18] = val19[i,9]/vol[i,18]
            val[i,19] = val20[i,9]/vol[i,19]
            val[i,20] = val21[i,9]/vol[i,20]
            val[i,21] = val22[i,9]/vol[i,21]
            val[i,22] = val23[i,9]/vol[i,22]
            val[i,23] = val24[i,9]/vol[i,23]
            val[i,24] = val25[i,9]/vol[i,24]
            val[i,25] = val26[i,9]/vol[i,25]
            val[i,26] = val27[i,9]/vol[i,26]
            val[i,27] = val28[i,9]/vol[i,27]
            val[i,28] = val29[i,9]/vol[i,28]
            val[i,29] = val30[i,9]/vol[i,29]
        # end if

    # Stress S_xx
    for i in range(n): # Mean shear stress computation (LAMMPS P = mean stress * volume)
        S_xx[i,0] = val1[i,7]/vol[i,0]
        S_xx[i,1] = val2[i,7]/vol[i,1]
        S_xx[i,2] = val3[i,7]/vol[i,2]
        S_xx[i,3] = val4[i,7]/vol[i,3]
        S_xx[i,4] = val5[i,7]/vol[i,4]
        S_xx[i,5] = val6[i,7]/vol[i,5]
        S_xx[i,6] = val7[i,7]/vol[i,6]
        S_xx[i,7] = val8[i,7]/vol[i,7]
        S_xx[i,8] = val9[i,7]/vol[i,8]
        S_xx[i,9] = val10[i,7]/vol[i,9]
        S_xx[i,10] = val11[i,7]/vol[i,10]
        S_xx[i,11] = val12[i,7]/vol[i,11]
        S_xx[i,12] = val13[i,7]/vol[i,12]
        S_xx[i,13] = val14[i,7]/vol[i,13]
        S_xx[i,14] = val15[i,7]/vol[i,14]
        S_xx[i,15] = val16[i,7]/vol[i,15]
        S_xx[i,16] = val17[i,7]/vol[i,16]
        S_xx[i,17] = val18[i,7]/vol[i,17]
        S_xx[i,18] = val19[i,7]/vol[i,18]
        S_xx[i,19] = val20[i,7]/vol[i,19]
        S_xx[i,20] = val21[i,7]/vol[i,20]
        S_xx[i,21] = val22[i,7]/vol[i,21]
        S_xx[i,22] = val23[i,7]/vol[i,22]
        S_xx[i,23] = val24[i,7]/vol[i,23]
        S_xx[i,24] = val25[i,7]/vol[i,24]
        S_xx[i,25] = val26[i,7]/vol[i,25]
        S_xx[i,26] = val27[i,7]/vol[i,26]
        S_xx[i,27] = val28[i,7]/vol[i,27]
        S_xx[i,28] = val29[i,7]/vol[i,28]
        S_xx[i,29] = val30[i,7]/vol[i,29]

    # Stress S_yy
    for i in range(n): # Mean shear stress computation (LAMMPS P = mean stress * volume)
        S_yy[i,0] = val1[i,8]/vol[i,0]
        S_yy[i,1] = val2[i,8]/vol[i,1]
        S_yy[i,2] = val3[i,8]/vol[i,2]
        S_yy[i,3] = val4[i,8]/vol[i,3]
        S_yy[i,4] = val5[i,8]/vol[i,4]
        S_yy[i,5] = val6[i,8]/vol[i,5]
        S_yy[i,6] = val7[i,8]/vol[i,6]
        S_yy[i,7] = val8[i,8]/vol[i,7]
        S_yy[i,8] = val9[i,8]/vol[i,8]
        S_yy[i,9] = val10[i,8]/vol[i,9]
        S_yy[i,10] = val11[i,8]/vol[i,10]
        S_yy[i,11] = val12[i,8]/vol[i,11]
        S_yy[i,12] = val13[i,8]/vol[i,12]
        S_yy[i,13] = val14[i,8]/vol[i,13]
        S_yy[i,14] = val15[i,8]/vol[i,14]
        S_yy[i,15] = val16[i,8]/vol[i,15]
        S_yy[i,16] = val17[i,8]/vol[i,16]
        S_yy[i,17] = val18[i,8]/vol[i,17]
        S_yy[i,18] = val19[i,8]/vol[i,18]
        S_yy[i,19] = val20[i,8]/vol[i,19]
        S_yy[i,20] = val21[i,8]/vol[i,20]
        S_yy[i,21] = val22[i,8]/vol[i,21]
        S_yy[i,22] = val23[i,8]/vol[i,22]
        S_yy[i,23] = val24[i,8]/vol[i,23]
        S_yy[i,24] = val25[i,8]/vol[i,24]
        S_yy[i,25] = val26[i,8]/vol[i,25]
        S_yy[i,26] = val27[i,8]/vol[i,26]
        S_yy[i,27] = val28[i,8]/vol[i,27]
        S_yy[i,28] = val29[i,8]/vol[i,28]
        S_yy[i,29] = val30[i,8]/vol[i,29]

    # Pressure P (Pa)
    for i in range(n): # pressure Pyy computation (LAMMPS P = mean stress * volume)
        press[i,0] = (1/2)*((val1[i,7] + val1[i,8])/vol[i,0])
        press[i,1] = (1/2)*((val2[i,7] + val2[i,8])/vol[i,1])
        press[i,2] = (1/2)*((val3[i,7] + val3[i,8])/vol[i,2])
        press[i,3] = (1/2)*((val4[i,7] + val4[i,8])/vol[i,3])
        press[i,4] = (1/2)*((val5[i,7] + val5[i,8])/vol[i,4])
        press[i,5] = (1/2)*((val6[i,7] + val6[i,8])/vol[i,5])
        press[i,6] = (1/2)*((val7[i,7] + val7[i,8])/vol[i,6])
        press[i,7] = (1/2)*((val8[i,7] + val8[i,8])/vol[i,7])
        press[i,8] = (1/2)*((val9[i,7] + val9[i,8])/vol[i,8])
        press[i,9] = (1/2)*((val10[i,7] + val10[i,8])/vol[i,9])
        press[i,10] = (1/2)*((val11[i,7] + val11[i,8])/vol[i,10])
        press[i,11] = (1/2)*((val12[i,7] + val12[i,8])/vol[i,11])
        press[i,12] = (1/2)*((val13[i,7] + val13[i,8])/vol[i,12])
        press[i,13] = (1/2)*((val14[i,7] + val14[i,8])/vol[i,13])
        press[i,14] = (1/2)*((val15[i,7] + val15[i,8])/vol[i,14])
        press[i,15] = (1/2)*((val16[i,7] + val16[i,8])/vol[i,15])
        press[i,16] = (1/2)*((val17[i,7] + val17[i,8])/vol[i,16])
        press[i,17] = (1/2)*((val18[i,7] + val18[i,8])/vol[i,17])
        press[i,18] = (1/2)*((val19[i,7] + val19[i,8])/vol[i,18])
        press[i,19] = (1/2)*((val20[i,7] + val20[i,8])/vol[i,19])
        press[i,20] = (1/2)*((val21[i,7] + val21[i,8])/vol[i,20])
        press[i,21] = (1/2)*((val22[i,7] + val22[i,8])/vol[i,21])
        press[i,22] = (1/2)*((val23[i,7] + val23[i,8])/vol[i,22])
        press[i,23] = (1/2)*((val24[i,7] + val24[i,8])/vol[i,23])
        press[i,24] = (1/2)*((val25[i,7] + val25[i,8])/vol[i,24])
        press[i,25] = (1/2)*((val26[i,7] + val26[i,8])/vol[i,25])
        press[i,26] = (1/2)*((val27[i,7] + val27[i,8])/vol[i,26])
        press[i,27] = (1/2)*((val28[i,7] + val28[i,8])/vol[i,27])
        press[i,28] = (1/2)*((val29[i,7] + val29[i,8])/vol[i,28])
        press[i,29] = (1/2)*((val30[i,7] + val30[i,8])/vol[i,29])

    for i in range (n): # Coordination number computation
        z[i,0] = val1[i,2]
        z[i,1] = val2[i,2]
        z[i,2] = val3[i,2]
        z[i,3] = val4[i,2]
        z[i,4] = val5[i,2]
        z[i,5] = val6[i,2]
        z[i,6] = val7[i,2]
        z[i,7] = val8[i,2]
        z[i,8] = val9[i,2]
        z[i,9] = val10[i,2]
        z[i,10] = val11[i,2]
        z[i,11] = val12[i,2]
        z[i,12] = val13[i,2]
        z[i,13] = val14[i,2]
        z[i,14] = val15[i,2]
        z[i,15] = val16[i,2]
        z[i,16] = val17[i,2]
        z[i,17] = val18[i,2]
        z[i,18] = val19[i,2]
        z[i,19] = val20[i,2]
        z[i,20] = val21[i,2]
        z[i,21] = val22[i,2]
        z[i,22] = val23[i,2]
        z[i,23] = val24[i,2]
        z[i,24] = val25[i,2]
        z[i,25] = val26[i,2]
        z[i,26] = val27[i,2]
        z[i,27] = val28[i,2]
        z[i,28] = val29[i,2]
        z[i,29] = val30[i,2]

    # a modifier après changement des fichiers en input
    for i in range (n-1): # velocity computation
        if i == n-1 :
            moy_vel[:,0] = 0
        else :
            moy_vel[i,0] = (1/dt)*(((val1[i+1,10] - val1[i,10])**2)+((val1[i+1,11] - val1[i,11])**2))**0.5
            moy_vel[i,1] = (1/dt)*(((val2[i+1,10] - val2[i,10])**2)+((val2[i+1,11] - val2[i,11])**2))**0.5
            moy_vel[i,2] = (1/dt)*(((val3[i+1,10] - val3[i,10])**2)+((val3[i+1,11] - val3[i,11])**2))**0.5
            moy_vel[i,3] = (1/dt)*(((val4[i+1,10] - val4[i,10])**2)+((val4[i+1,11] - val4[i,11])**2))**0.5
            moy_vel[i,4] = (1/dt)*(((val5[i+1,10] - val5[i,10])**2)+((val5[i+1,11] - val5[i,11])**2))**0.5
            moy_vel[i,5] = (1/dt)*(((val6[i+1,10] - val6[i,10])**2)+((val6[i+1,11] - val6[i,11])**2))**0.5
            moy_vel[i,6] = (1/dt)*(((val7[i+1,10] - val7[i,10])**2)+((val7[i+1,11] - val7[i,11])**2))**0.5
            moy_vel[i,7] = (1/dt)*(((val8[i+1,10] - val8[i,10])**2)+((val8[i+1,11] - val8[i,11])**2))**0.5
            moy_vel[i,8] = (1/dt)*(((val9[i+1,10] - val9[i,10])**2)+((val9[i+1,11] - val9[i,11])**2))**0.5
            moy_vel[i,9] = (1/dt)*(((val10[i+1,10] - val10[i,10])**2)+((val10[i+1,11] - val10[i,11])**2))**0.5
            moy_vel[i,10] = (1/dt)*(((val11[i+1,10] - val11[i,10])**2)+((val11[i+1,11] - val11[i,11])**2))**0.5
            moy_vel[i,11] = (1/dt)*(((val12[i+1,10] - val12[i,10])**2)+((val12[i+1,11] - val12[i,11])**2))**0.5
            moy_vel[i,12] = (1/dt)*(((val13[i+1,10] - val13[i,10])**2)+((val13[i+1,11] - val13[i,11])**2))**0.5
            moy_vel[i,13] = (1/dt)*(((val14[i+1,10] - val14[i,10])**2)+((val14[i+1,11] - val14[i,11])**2))**0.5
            moy_vel[i,14] = (1/dt)*(((val15[i+1,10] - val15[i,10])**2)+((val15[i+1,11] - val15[i,11])**2))**0.5
            moy_vel[i,15] = (1/dt)*(((val16[i+1,10] - val16[i,10])**2)+((val16[i+1,11] - val16[i,11])**2))**0.5
            moy_vel[i,16] = (1/dt)*(((val17[i+1,10] - val17[i,10])**2)+((val17[i+1,11] - val17[i,11])**2))**0.5
            moy_vel[i,17] = (1/dt)*(((val18[i+1,10] - val18[i,10])**2)+((val18[i+1,11] - val18[i,11])**2))**0.5
            moy_vel[i,18] = (1/dt)*(((val19[i+1,10] - val19[i,10])**2)+((val19[i+1,11] - val19[i,11])**2))**0.5
            moy_vel[i,19] = (1/dt)*(((val20[i+1,10] - val20[i,10])**2)+((val20[i+1,11] - val20[i,11])**2))**0.5
            moy_vel[i,20] = (1/dt)*(((val21[i+1,10] - val21[i,10])**2)+((val21[i+1,11] - val21[i,11])**2))**0.5
            moy_vel[i,21] = (1/dt)*(((val22[i+1,10] - val22[i,10])**2)+((val22[i+1,11] - val22[i,11])**2))**0.5
            moy_vel[i,22] = (1/dt)*(((val23[i+1,10] - val23[i,10])**2)+((val23[i+1,11] - val23[i,11])**2))**0.5
            moy_vel[i,23] = (1/dt)*(((val24[i+1,10] - val24[i,10])**2)+((val24[i+1,11] - val24[i,11])**2))**0.5
            moy_vel[i,24] = (1/dt)*(((val25[i+1,10] - val25[i,10])**2)+((val25[i+1,11] - val25[i,11])**2))**0.5
            moy_vel[i,25] = (1/dt)*(((val26[i+1,10] - val26[i,10])**2)+((val26[i+1,11] - val26[i,11])**2))**0.5
            moy_vel[i,26] = (1/dt)*(((val27[i+1,10] - val27[i,10])**2)+((val27[i+1,11] - val27[i,11])**2))**0.5
            moy_vel[i,27] = (1/dt)*(((val28[i+1,10] - val28[i,10])**2)+((val28[i+1,11] - val28[i,11])**2))**0.5
            moy_vel[i,28] = (1/dt)*(((val29[i+1,10] - val29[i,10])**2)+((val29[i+1,11] - val29[i,11])**2))**0.5
            moy_vel[i,29] = (1/dt)*(((val30[i+1,10] - val30[i,10])**2)+((val30[i+1,11] - val30[i,11])**2))**0.5
    # end of i for loop

    for i in range(n): # scan the lines
        # mean value computation
        ave_std[i,0] = np.average(val[i,:]) # shear stress
        ave_std[i,2] = np.average(vol[i,:]) # volume
        ave_std[i,4] = abs(np.average(press[i,:])) # mean stress
        ave_std[i,6] = np.average(z[i,:]) # coordination number
        ave_std[i,8] = np.average(moy_vel[i,:]) # moy_velocity
        ave_std[i,10] = np.average(S_xx[i,:]) # normal stress S_xx
        ave_std[i,12] = np.average(S_yy[i,:]) # normal stress S_yy
    # end of i for loop

    for i in range(n):
        # standard deviation computation
        ave_std[i,1] = np.std(val[i,:])
        ave_std[i,3] = np.std(vol[i,:])
        ave_std[i,5] = np.std(press[i,:])
        ave_std[i,7] = np.std(z[i,:])
        ave_std[i,9] = np.std(moy_vel[i,:])
        ave_std[i,11] = np.std(S_xx[i,:])
        ave_std[i,13] = np.std(S_yy[i,:])
    # end of i for loop
    return ave_std, np.average(l[0,:]) # length ly # return ave_std = M(n,6)

def val_gran(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30):
    # Function variables #
    # Scalar
    N = 30 # number of stacks

    # Matrix
    ave_std, val = np.zeros(2), np.zeros((N))

    # create valN file to extract the value from the 30 dataN file
    val1 = np.zeros(11)
    val2 = np.zeros(11)
    val3 = np.zeros(11)
    val4 = np.zeros(11)
    val5 = np.zeros(11)
    val6 = np.zeros(11)
    val7 = np.zeros(11)
    val8 = np.zeros(11)
    val9 = np.zeros(11)
    val10 = np.zeros(11)
    val11 = np.zeros(11)
    val12 = np.zeros(11)
    val13 = np.zeros(11)
    val14 = np.zeros(11)
    val15 = np.zeros(11)
    val16 = np.zeros(11)
    val17 = np.zeros(11)
    val18 = np.zeros(11)
    val19 = np.zeros(11)
    val20 = np.zeros(11)
    val21 = np.zeros(11)
    val22 = np.zeros(11)
    val23 = np.zeros(11)
    val24 = np.zeros(11)
    val25 = np.zeros(11)
    val25 = np.zeros(11)
    val26 = np.zeros(11)
    val27 = np.zeros(11)
    val28 = np.zeros(11)
    val29 = np.zeros(11)
    val30 = np.zeros(11)

    # Read the datas #
    data1.readline()
    data2.readline()
    data3.readline()
    data4.readline()
    data5.readline()
    data6.readline()
    data7.readline()
    data8.readline()
    data9.readline()
    data10.readline()
    data11.readline()
    data12.readline()
    data13.readline()
    data14.readline()
    data15.readline()
    data16.readline()
    data17.readline()
    data18.readline()
    data19.readline()
    data20.readline()
    data21.readline()
    data22.readline()
    data23.readline()
    data24.readline()
    data25.readline()
    data26.readline()
    data27.readline()
    data28.readline()
    data29.readline()
    data30.readline()

    # Attribution of the values #
    val1 = np.loadtxt(data1)
    val2 = np.loadtxt(data2)
    val3 = np.loadtxt(data3)
    val4 = np.loadtxt(data4)
    val5 = np.loadtxt(data5)
    val6 = np.loadtxt(data6)
    val7 = np.loadtxt(data7)
    val8 = np.loadtxt(data8)
    val9 = np.loadtxt(data9)
    val10 = np.loadtxt(data10)
    val11 = np.loadtxt(data11)
    val12 = np.loadtxt(data12)
    val13 = np.loadtxt(data13)
    val14 = np.loadtxt(data14)
    val15 = np.loadtxt(data15)
    val16 = np.loadtxt(data16)
    val17 = np.loadtxt(data17)
    val18 = np.loadtxt(data18)
    val19 = np.loadtxt(data19)
    val20 = np.loadtxt(data20)
    val21 = np.loadtxt(data21)
    val22 = np.loadtxt(data22)
    val23 = np.loadtxt(data23)
    val24 = np.loadtxt(data24)
    val25 = np.loadtxt(data25)
    val26 = np.loadtxt(data26)
    val27 = np.loadtxt(data27)
    val28 = np.loadtxt(data28)
    val29 = np.loadtxt(data29)
    val30 = np.loadtxt(data30)

    # Granulence (J)
    val[0] = val1[10]
    val[1] = val2[10]
    val[2] = val3[10]
    val[3] = val4[10]
    val[4] = val5[10]
    val[5] = val6[10]
    val[6] = val7[10]
    val[7] = val8[10]
    val[8] = val9[10]
    val[9] = val10[10]
    val[10] = val11[10]
    val[11] = val12[10]
    val[12] = val13[10]
    val[13] = val14[10]
    val[14] = val15[10]
    val[15] = val16[10]
    val[16] = val17[10]
    val[17] = val18[10]
    val[18] = val19[10]
    val[19] = val20[10]
    val[20] = val21[10]
    val[21] = val22[10]
    val[22] = val23[10]
    val[23] = val24[10]
    val[24] = val25[10]
    val[25] = val26[10]
    val[26] = val27[10]
    val[27] = val28[10]
    val[28] = val29[10]
    val[29] = val30[10]

    # mean value computation
    ave_std[0] = np.average(val[:]) # granulence

    # standard deviation computation
    ave_std[1] = np.std(val[:])

    return ave_std # return ave_std = M(1,6)

def error_matrix_relax(error_1, error_2, error_3, error_4, error_5, error_6, error_7, error_8, error_9, error_10, error_11, error_12, error_13, error_14, error_15, error_16, error_17, error_18, error_19, error_20, error_21, error_22, error_23, error_24, error_25, error_26, error_27, error_28, error_29, error_30, no_coeff, N):
    # Function variables
    # Matrix
    error = np.zeros((no_coeff,N))

    for i in range(no_coeff):
        error[i,0] = error_1[i]
        error[i,1] = error_2[i]
        error[i,2] = error_3[i]
        error[i,3] = error_4[i]
        error[i,4] = error_5[i]
        error[i,5] = error_6[i]
        error[i,6] = error_7[i]
        error[i,7] = error_8[i]
        error[i,8] = error_9[i]
        error[i,9] = error_10[i]
        error[i,10] = error_11[i]
        error[i,11] = error_12[i]
        error[i,12] = error_13[i]
        error[i,13] = error_14[i]
        error[i,14] = error_15[i]
        error[i,15] = error_16[i]
        error[i,16] = error_17[i]
        error[i,17] = error_18[i]
        error[i,18] = error_19[i]
        error[i,19] = error_20[i]
        error[i,20] = error_21[i]
        error[i,21] = error_22[i]
        error[i,22] = error_23[i]
        error[i,23] = error_24[i]
        error[i,24] = error_25[i]
        error[i,25] = error_26[i]
        error[i,26] = error_27[i]
        error[i,27] = error_28[i]
        error[i,28] = error_29[i]
        error[i,29] = error_30[i]
    # end of i for loop
    return error

def val_ela_relax_fit(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,n,step,simu,no_coeff,module):
    # Function variables #
    # Scalar
    N = 30 # number of files

    # Vector
    relax_coeff, std = np.zeros(no_coeff), np.zeros(no_coeff)

    # Matrix
    val, vol, relax_mod = np.zeros((n,N)), np.zeros((n,N)), np.zeros((no_coeff,N))

    # create valN file to extract the value from the 30 dataN file
    val1 = np.zeros((n,N))
    val2 = np.zeros((n,N))
    val3 = np.zeros((n,N))
    val4 = np.zeros((n,N))
    val5 = np.zeros((n,N))
    val6 = np.zeros((n,N))
    val7 = np.zeros((n,N))
    val8 = np.zeros((n,N))
    val9 = np.zeros((n,N))
    val10 = np.zeros((n,N))
    val11 = np.zeros((n,N))
    val12 = np.zeros((n,N))
    val13 = np.zeros((n,N))
    val14 = np.zeros((n,N))
    val15 = np.zeros((n,N))
    val16 = np.zeros((n,N))
    val17 = np.zeros((n,N))
    val18 = np.zeros((n,N))
    val19 = np.zeros((n,N))
    val20 = np.zeros((n,N))
    val21 = np.zeros((n,N))
    val22 = np.zeros((n,N))
    val23 = np.zeros((n,N))
    val24 = np.zeros((n,N))
    val25 = np.zeros((n,N))
    val25 = np.zeros((n,N))
    val26 = np.zeros((n,N))
    val27 = np.zeros((n,N))
    val28 = np.zeros((n,N))
    val29 = np.zeros((n,N))
    val30 = np.zeros((n,N))

    # Read the datas #
    data1.readline()
    data2.readline()
    data3.readline()
    data4.readline()
    data5.readline()
    data6.readline()
    data7.readline()
    data8.readline()
    data9.readline()
    data10.readline()
    data11.readline()
    data12.readline()
    data13.readline()
    data14.readline()
    data15.readline()
    data16.readline()
    data17.readline()
    data18.readline()
    data19.readline()
    data20.readline()
    data21.readline()
    data22.readline()
    data23.readline()
    data24.readline()
    data25.readline()
    data26.readline()
    data27.readline()
    data28.readline()
    data29.readline()
    data30.readline()

    # Attribution of the values #
    val1 = np.loadtxt(data1)
    val2 = np.loadtxt(data2)
    val3 = np.loadtxt(data3)
    val4 = np.loadtxt(data4)
    val5 = np.loadtxt(data5)
    val6 = np.loadtxt(data6)
    val7 = np.loadtxt(data7)
    val8 = np.loadtxt(data8)
    val9 = np.loadtxt(data9)
    val10 = np.loadtxt(data10)
    val11 = np.loadtxt(data11)
    val12 = np.loadtxt(data12)
    val13 = np.loadtxt(data13)
    val14 = np.loadtxt(data14)
    val15 = np.loadtxt(data15)
    val16 = np.loadtxt(data16)
    val17 = np.loadtxt(data17)
    val18 = np.loadtxt(data18)
    val19 = np.loadtxt(data19)
    val20 = np.loadtxt(data20)
    val21 = np.loadtxt(data21)
    val22 = np.loadtxt(data22)
    val23 = np.loadtxt(data23)
    val24 = np.loadtxt(data24)
    val25 = np.loadtxt(data25)
    val26 = np.loadtxt(data26)
    val27 = np.loadtxt(data27)
    val28 = np.loadtxt(data28)
    val29 = np.loadtxt(data29)
    val30 = np.loadtxt(data30)

    # Volume
    for i in range(n): # Volume computation for each simulation
        vol[i,0] = (val1[i,4]*val1[i,5])
        vol[i,1] = (val2[i,4]*val2[i,5])
        vol[i,2] = (val3[i,4]*val3[i,5])
        vol[i,3] = (val4[i,4]*val4[i,5])
        vol[i,4] = (val5[i,4]*val5[i,5])
        vol[i,5] = (val6[i,4]*val6[i,5])
        vol[i,6] = (val7[i,4]*val7[i,5])
        vol[i,7] = (val8[i,4]*val8[i,5])
        vol[i,8] = (val9[i,4]*val9[i,5])
        vol[i,9] = (val10[i,4]*val10[i,5])
        vol[i,10] = (val11[i,4]*val11[i,5])
        vol[i,11] = (val12[i,4]*val12[i,5])
        vol[i,12] = (val13[i,4]*val13[i,5])
        vol[i,13] = (val14[i,4]*val14[i,5])
        vol[i,14] = (val15[i,4]*val15[i,5])
        vol[i,15] = (val16[i,4]*val16[i,5])
        vol[i,16] = (val17[i,4]*val17[i,5])
        vol[i,17] = (val18[i,4]*val18[i,5])
        vol[i,18] = (val19[i,4]*val19[i,5])
        vol[i,19] = (val20[i,4]*val20[i,5])
        vol[i,20] = (val21[i,4]*val21[i,5])
        vol[i,21] = (val22[i,4]*val22[i,5])
        vol[i,22] = (val23[i,4]*val23[i,5])
        vol[i,23] = (val24[i,4]*val24[i,5])
        vol[i,24] = (val25[i,4]*val25[i,5])
        vol[i,25] = (val26[i,4]*val26[i,5])
        vol[i,26] = (val27[i,4]*val27[i,5])
        vol[i,27] = (val28[i,4]*val28[i,5])
        vol[i,28] = (val29[i,4]*val29[i,5])
        vol[i,29] = (val30[i,4]*val30[i,5])

    # Shear stress (Pa)
    if module == 'shear' or module == 'deviatoric':
        for i in range(n): # Mean shear stress computation (LAMMPS P = mean stress * volume)
            if module == 'deviatoric':
                val[i,0] = np.sqrt(((((val1[i,7]/vol[i,0])-(val1[i,8]/vol[i,0]))/2)**2)+((val1[i,9]/vol[i,0])**2))
                val[i,1] = np.sqrt(((((val2[i,7]/vol[i,1])-(val2[i,8]/vol[i,1]))/2)**2)+((val2[i,9]/vol[i,1])**2))
                val[i,2] = np.sqrt(((((val3[i,7]/vol[i,2])-(val3[i,8]/vol[i,2]))/2)**2)+((val3[i,9]/vol[i,2])**2))
                val[i,3] = np.sqrt(((((val4[i,7]/vol[i,3])-(val4[i,8]/vol[i,3]))/2)**2)+((val4[i,9]/vol[i,3])**2))
                val[i,4] = np.sqrt(((((val5[i,7]/vol[i,4])-(val5[i,8]/vol[i,4]))/2)**2)+((val5[i,9]/vol[i,4])**2))
                val[i,5] = np.sqrt(((((val6[i,7]/vol[i,5])-(val6[i,8]/vol[i,5]))/2)**2)+((val6[i,9]/vol[i,5])**2))
                val[i,6] = np.sqrt(((((val7[i,7]/vol[i,6])-(val7[i,8]/vol[i,6]))/2)**2)+((val7[i,9]/vol[i,6])**2))
                val[i,7] = np.sqrt(((((val8[i,7]/vol[i,7])-(val8[i,8]/vol[i,7]))/2)**2)+((val8[i,9]/vol[i,7])**2))
                val[i,8] = np.sqrt(((((val9[i,7]/vol[i,8])-(val9[i,8]/vol[i,8]))/2)**2)+((val9[i,9]/vol[i,8])**2))
                val[i,9] = np.sqrt(((((val10[i,7]/vol[i,9])-(val10[i,8]/vol[i,9]))/2)**2)+((val10[i,9]/vol[i,9])**2))
                val[i,10] = np.sqrt(((((val11[i,7]/vol[i,10])-(val11[i,8]/vol[i,10]))/2)**2)+((val11[i,9]/vol[i,10])**2))
                val[i,11] = np.sqrt(((((val12[i,7]/vol[i,11])-(val12[i,8]/vol[i,11]))/2)**2)+((val12[i,9]/vol[i,11])**2))
                val[i,12] = np.sqrt(((((val13[i,7]/vol[i,12])-(val13[i,8]/vol[i,12]))/2)**2)+((val13[i,9]/vol[i,12])**2))
                val[i,13] = np.sqrt(((((val14[i,7]/vol[i,13])-(val14[i,8]/vol[i,13]))/2)**2)+((val14[i,9]/vol[i,13])**2))
                val[i,14] = np.sqrt(((((val15[i,7]/vol[i,14])-(val15[i,8]/vol[i,14]))/2)*2)+((val15[i,9]/vol[i,14])**2))
                val[i,15] = np.sqrt(((((val16[i,7]/vol[i,15])-(val16[i,8]/vol[i,15]))/2)**2)+((val16[i,9]/vol[i,15])**2))
                val[i,16] = np.sqrt(((((val17[i,7]/vol[i,16])-(val17[i,8]/vol[i,16]))/2)**2)+((val17[i,9]/vol[i,16])**2))
                val[i,17] = np.sqrt(((((val18[i,7]/vol[i,17])-(val18[i,8]/vol[i,17]))/2)**2)+((val18[i,9]/vol[i,17])**2))
                val[i,18] = np.sqrt(((((val19[i,7]/vol[i,18])-(val19[i,8]/vol[i,18]))/2)**2)+((val19[i,9]/vol[i,18])**2))
                val[i,19] = np.sqrt(((((val20[i,7]/vol[i,19])-(val20[i,8]/vol[i,19]))/2)**2)+((val20[i,9]/vol[i,19])**2))
                val[i,20] = np.sqrt(((((val21[i,7]/vol[i,20])-(val21[i,8]/vol[i,20]))/2)**2)+((val21[i,9]/vol[i,20])**2))
                val[i,21] = np.sqrt(((((val22[i,7]/vol[i,21])-(val22[i,8]/vol[i,21]))/2)**2)+((val22[i,9]/vol[i,21])**2))
                val[i,22] = np.sqrt(((((val23[i,7]/vol[i,22])-(val23[i,8]/vol[i,22]))/2)**2)+((val23[i,9]/vol[i,22])**2))
                val[i,23] = np.sqrt(((((val24[i,7]/vol[i,23])-(val24[i,8]/vol[i,23]))/2)**2)+((val24[i,9]/vol[i,23])**2))
                val[i,24] = np.sqrt(((((val25[i,7]/vol[i,24])-(val25[i,8]/vol[i,24]))/2)**2)+((val25[i,9]/vol[i,24])**2))
                val[i,25] = np.sqrt(((((val26[i,7]/vol[i,25])-(val26[i,8]/vol[i,25]))/2)**2)+((val26[i,9]/vol[i,25])**2))
                val[i,26] = np.sqrt(((((val27[i,7]/vol[i,26])-(val27[i,8]/vol[i,26]))/2)**2)+((val27[i,9]/vol[i,26])**2))
                val[i,27] = np.sqrt(((((val28[i,7]/vol[i,27])-(val28[i,8]/vol[i,27]))/2)**2)+((val28[i,9]/vol[i,27])**2))
                val[i,28] = np.sqrt(((((val29[i,7]/vol[i,28])-(val29[i,8]/vol[i,28]))/2)**2)+((val29[i,9]/vol[i,28])**2))
                val[i,29] = np.sqrt(((((val30[i,7]/vol[i,29])-(val30[i,8]/vol[i,29]))/2)**2)+((val30[i,9]/vol[i,29])**2))
            elif module == 'shear':
                val[i,0] = val1[i,9]/vol[i,0]
                val[i,1] = val2[i,9]/vol[i,1]
                val[i,2] = val3[i,9]/vol[i,2]
                val[i,3] = val4[i,9]/vol[i,3]
                val[i,4] = val5[i,9]/vol[i,4]
                val[i,5] = val6[i,9]/vol[i,5]
                val[i,6] = val7[i,9]/vol[i,6]
                val[i,7] = val8[i,9]/vol[i,7]
                val[i,8] = val9[i,9]/vol[i,8]
                val[i,9] = val10[i,9]/vol[i,9]
                val[i,10] = val11[i,9]/vol[i,10]
                val[i,11] = val12[i,9]/vol[i,11]
                val[i,12] = val13[i,9]/vol[i,12]
                val[i,13] = val14[i,9]/vol[i,13]
                val[i,14] = val15[i,9]/vol[i,14]
                val[i,15] = val16[i,9]/vol[i,15]
                val[i,16] = val17[i,9]/vol[i,16]
                val[i,17] = val18[i,9]/vol[i,17]
                val[i,18] = val19[i,9]/vol[i,18]
                val[i,19] = val20[i,9]/vol[i,19]
                val[i,20] = val21[i,9]/vol[i,20]
                val[i,21] = val22[i,9]/vol[i,21]
                val[i,22] = val23[i,9]/vol[i,22]
                val[i,23] = val24[i,9]/vol[i,23]
                val[i,24] = val25[i,9]/vol[i,24]
                val[i,25] = val26[i,9]/vol[i,25]
                val[i,26] = val27[i,9]/vol[i,26]
                val[i,27] = val28[i,9]/vol[i,27]
                val[i,28] = val29[i,9]/vol[i,28]
                val[i,29] = val30[i,9]/vol[i,29]
            # end if
        # end of i for loop
    # end of if

    # Pressure P (Pa)
    if module == 'pressure':
        for i in range(n): # pressure Pyy computation (LAMMPS P = mean stress * volume)
            val[i,0] = (1/2)*((val1[i,7] + val1[i,8])/vol[i,0])
            val[i,1] = (1/2)*((val2[i,7] + val2[i,8])/vol[i,1])
            val[i,2] = (1/2)*((val3[i,7] + val3[i,8])/vol[i,2])
            val[i,3] = (1/2)*((val4[i,7] + val4[i,8])/vol[i,3])
            val[i,4] = (1/2)*((val5[i,7] + val5[i,8])/vol[i,4])
            val[i,5] = (1/2)*((val6[i,7] + val6[i,8])/vol[i,5])
            val[i,6] = (1/2)*((val7[i,7] + val7[i,8])/vol[i,6])
            val[i,7] = (1/2)*((val8[i,7] + val8[i,8])/vol[i,7])
            val[i,8] = (1/2)*((val9[i,7] + val9[i,8])/vol[i,8])
            val[i,9] = (1/2)*((val10[i,7] + val10[i,8])/vol[i,9])
            val[i,10] = (1/2)*((val11[i,7] + val11[i,8])/vol[i,10])
            val[i,11] = (1/2)*((val12[i,7] + val12[i,8])/vol[i,11])
            val[i,12] = (1/2)*((val13[i,7] + val13[i,8])/vol[i,12])
            val[i,13] = (1/2)*((val14[i,7] + val14[i,8])/vol[i,13])
            val[i,14] = (1/2)*((val15[i,7] + val15[i,8])/vol[i,14])
            val[i,15] = (1/2)*((val16[i,7] + val16[i,8])/vol[i,15])
            val[i,16] = (1/2)*((val17[i,7] + val17[i,8])/vol[i,16])
            val[i,17] = (1/2)*((val18[i,7] + val18[i,8])/vol[i,17])
            val[i,18] = (1/2)*((val19[i,7] + val19[i,8])/vol[i,18])
            val[i,19] = (1/2)*((val20[i,7] + val20[i,8])/vol[i,19])
            val[i,20] = (1/2)*((val21[i,7] + val21[i,8])/vol[i,20])
            val[i,21] = (1/2)*((val22[i,7] + val22[i,8])/vol[i,21])
            val[i,22] = (1/2)*((val23[i,7] + val23[i,8])/vol[i,22])
            val[i,23] = (1/2)*((val24[i,7] + val24[i,8])/vol[i,23])
            val[i,24] = (1/2)*((val25[i,7] + val25[i,8])/vol[i,24])
            val[i,25] = (1/2)*((val26[i,7] + val26[i,8])/vol[i,25])
            val[i,26] = (1/2)*((val27[i,7] + val27[i,8])/vol[i,26])
            val[i,27] = (1/2)*((val28[i,7] + val28[i,8])/vol[i,27])
            val[i,28] = (1/2)*((val29[i,7] + val29[i,8])/vol[i,28])
            val[i,29] = (1/2)*((val30[i,7] + val30[i,8])/vol[i,29])
        # end of i for loop
        val = abs(val)
    # end of if

    relax_mod[:,0], error_1 = ela_relax_fit(val[:,0],no_coeff,module,simu,step)
    relax_mod[:,1], error_2 = ela_relax_fit(val[:,1],no_coeff,module,simu,step)
    relax_mod[:,2], error_3 = ela_relax_fit(val[:,2],no_coeff,module,simu,step)
    relax_mod[:,3], error_4 = ela_relax_fit(val[:,3],no_coeff,module,simu,step)
    relax_mod[:,4], error_5 = ela_relax_fit(val[:,4],no_coeff,module,simu,step)
    relax_mod[:,5], error_6 = ela_relax_fit(val[:,5],no_coeff,module,simu,step)
    relax_mod[:,6], error_7 = ela_relax_fit(val[:,6],no_coeff,module,simu,step)
    relax_mod[:,7], error_8 = ela_relax_fit(val[:,7],no_coeff,module,simu,step)
    relax_mod[:,8], error_9 = ela_relax_fit(val[:,8],no_coeff,module,simu,step)
    relax_mod[:,9], error_10 = ela_relax_fit(val[:,9],no_coeff,module,simu,step)
    relax_mod[:,10], error_11 = ela_relax_fit(val[:,10],no_coeff,module,simu,step)
    relax_mod[:,11], error_12 = ela_relax_fit(val[:,11],no_coeff,module,simu,step)
    relax_mod[:,12], error_13 = ela_relax_fit(val[:,12],no_coeff,module,simu,step)
    relax_mod[:,13], error_14 = ela_relax_fit(val[:,13],no_coeff,module,simu,step)
    relax_mod[:,14], error_15 = ela_relax_fit(val[:,14],no_coeff,module,simu,step)
    relax_mod[:,15], error_16 = ela_relax_fit(val[:,15],no_coeff,module,simu,step)
    relax_mod[:,16], error_17 = ela_relax_fit(val[:,16],no_coeff,module,simu,step)
    relax_mod[:,17], error_18 = ela_relax_fit(val[:,17],no_coeff,module,simu,step)
    relax_mod[:,18], error_19 = ela_relax_fit(val[:,18],no_coeff,module,simu,step)
    relax_mod[:,19], error_20 = ela_relax_fit(val[:,19],no_coeff,module,simu,step)
    relax_mod[:,20], error_21 = ela_relax_fit(val[:,20],no_coeff,module,simu,step)
    relax_mod[:,21], error_22 = ela_relax_fit(val[:,21],no_coeff,module,simu,step)
    relax_mod[:,22], error_23 = ela_relax_fit(val[:,22],no_coeff,module,simu,step)
    relax_mod[:,23], error_24 = ela_relax_fit(val[:,23],no_coeff,module,simu,step)
    relax_mod[:,24], error_25 = ela_relax_fit(val[:,24],no_coeff,module,simu,step)
    relax_mod[:,25], error_26 = ela_relax_fit(val[:,25],no_coeff,module,simu,step)
    relax_mod[:,26], error_27 = ela_relax_fit(val[:,26],no_coeff,module,simu,step)
    relax_mod[:,27], error_28 = ela_relax_fit(val[:,27],no_coeff,module,simu,step)
    relax_mod[:,28], error_29 = ela_relax_fit(val[:,28],no_coeff,module,simu,step)
    relax_mod[:,29], error_30 = ela_relax_fit(val[:,29],no_coeff,module,simu,step)

    # value of the modules
    for i in range(no_coeff):
        if i == 0 : relax_coeff[i] = val[1,:].mean() - val[len(val)-1,:].mean()
        if i == 1 or i == 2 : relax_coeff[i] = relax_mod[i,:].mean() # mean value
        if i == 3 : relax_coeff[i] = val[len(val)-1,:].mean()
    # end of i for loop

    # standard deviation computation
    for i in range(no_coeff):
        if i == 0 : std[i] = np.std(val[i,:])
        if i == 1 or i == 2 : std[i] = np.std(relax_mod[i,:])
        if i == 3 : std[i] = np.std(val[len(val)-1,:])
    # end of i for loop
    return relax_coeff[:],std[:]

def file_ela_relax_data(step,line_ela_relax,shear_s,path):
    # Function variables
    # Scalar
    no_it = 1
    # Matrix
    file_ela_relax = np.zeros((line_ela_relax,6)) # matrix to store ela_relax averaged values

    # Open the 30 simulation files for the elastic files no = step
    ela_relax_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    file_ela_relax, ly = val_ela_relax(ela_relax_1,ela_relax_2,ela_relax_3,ela_relax_4,ela_relax_5,ela_relax_6,ela_relax_7,ela_relax_8,ela_relax_9,ela_relax_10,ela_relax_11,ela_relax_12,ela_relax_13,ela_relax_14,ela_relax_15,ela_relax_16,ela_relax_17,ela_relax_18,ela_relax_19,ela_relax_20,ela_relax_21,ela_relax_22,ela_relax_23,ela_relax_24,ela_relax_25,ela_relax_26,ela_relax_27,ela_relax_28,ela_relax_29,ela_relax_30,shear_s,line_ela_relax)

    # Closure of the files
    ela_relax_1.close()
    ela_relax_2.close()
    ela_relax_3.close()
    ela_relax_4.close()
    ela_relax_5.close()
    ela_relax_6.close()
    ela_relax_7.close()
    ela_relax_8.close()
    ela_relax_9.close()
    ela_relax_10.close()
    ela_relax_11.close()
    ela_relax_12.close()
    ela_relax_13.close()
    ela_relax_14.close()
    ela_relax_15.close()
    ela_relax_16.close()
    ela_relax_17.close()
    ela_relax_18.close()
    ela_relax_19.close()
    ela_relax_20.close()
    ela_relax_21.close()
    ela_relax_22.close()
    ela_relax_23.close()
    ela_relax_24.close()
    ela_relax_25.close()
    ela_relax_26.close()
    ela_relax_27.close()
    ela_relax_28.close()
    ela_relax_29.close()
    ela_relax_30.close()
    return file_ela_relax, ly  # return matrix file_ela_relax = M(n,6) for the elastic simulation no = step

def file_granulence_data(step,path):
    # Function variables
    # Scalar
    no_it = 1

    # Matrix
    file_gran = np.zeros((1,10)) # matrix to store granulence averaged values

    # Open the 30 simulation files for the elastic files no = step
    gran_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")
    gran_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_gran_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    file_gran = val_gran(gran_1,gran_2,gran_3,gran_4,gran_5,gran_6,gran_7,gran_8,gran_9,gran_10,gran_11,gran_12,gran_13,gran_14,gran_15,gran_16,gran_17,gran_18,gran_19,gran_20,gran_21,gran_22,gran_23,gran_24,gran_25,gran_26,gran_27,gran_28,gran_29,gran_30)
    gran_1.close()

    # Closure of the files
    gran_1.close()
    gran_2.close()
    gran_3.close()
    gran_4.close()
    gran_5.close()
    gran_6.close()
    gran_7.close()
    gran_8.close()
    gran_9.close()
    gran_10.close()
    gran_11.close()
    gran_12.close()
    gran_13.close()
    gran_14.close()
    gran_15.close()
    gran_16.close()
    gran_17.close()
    gran_18.close()
    gran_19.close()
    gran_20.close()
    gran_21.close()
    gran_22.close()
    gran_23.close()
    gran_24.close()
    gran_25.close()
    gran_26.close()
    gran_27.close()
    gran_28.close()
    gran_29.close()
    gran_30.close()
    return file_gran # return matrix file_gran = M(n,6) for the elastic simulation no = step

def file_ela_relax_param(step,line_ela_relax,path,module,simu):
    # Function variables
    # Scalar
    no_it, no_coeff = 1, 4

    # Matrix
    fit_param, error_param = np.zeros(no_coeff), np.zeros(no_coeff)

    # Open the 30 simulation files for the elastic files no = step
    ela_relax_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")
    ela_relax_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_ela_relax_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    fit_param, error_param = val_ela_relax_fit(ela_relax_1,ela_relax_2,ela_relax_3,ela_relax_4,ela_relax_5,ela_relax_6,ela_relax_7,ela_relax_8,ela_relax_9,ela_relax_10,ela_relax_11,ela_relax_12,ela_relax_13,ela_relax_14,ela_relax_15,ela_relax_16,ela_relax_17,ela_relax_18,ela_relax_19,ela_relax_20,ela_relax_21,ela_relax_22,ela_relax_23,ela_relax_24,ela_relax_25,ela_relax_26,ela_relax_27,ela_relax_28,ela_relax_29,ela_relax_30,line_ela_relax,step,simu,no_coeff,module)

    ela_relax_1.close()
    ela_relax_2.close()
    ela_relax_3.close()
    ela_relax_4.close()
    ela_relax_5.close()
    ela_relax_6.close()
    ela_relax_7.close()
    ela_relax_8.close()
    ela_relax_9.close()
    ela_relax_10.close()
    ela_relax_11.close()
    ela_relax_12.close()
    ela_relax_13.close()
    ela_relax_14.close()
    ela_relax_15.close()
    ela_relax_16.close()
    ela_relax_17.close()
    ela_relax_18.close()
    ela_relax_19.close()
    ela_relax_20.close()
    ela_relax_21.close()
    ela_relax_22.close()
    ela_relax_23.close()
    ela_relax_24.close()
    ela_relax_25.close()
    ela_relax_26.close()
    ela_relax_27.close()
    ela_relax_28.close()
    ela_relax_29.close()
    ela_relax_30.close()
    return fit_param, error_param

## Data Analysis ##
def ela_matrix(ela_1,ela_2,ela_3,ela_4,ela_5,ela_6,ela_7,ela_8,ela_9,ela_10,adim,no_ela_file,matrix_type,no_stack):
    # Function variables
    # Matrix
    ela_mat = np.zeros((no_ela_file,no_stack))

    if matrix_type == 'elastic modulus':
        for i in range(no_ela_file):
            if no_stack == 5 : ela_mat[i,0], ela_mat[i,1], ela_mat[i,2], ela_mat[i,3], ela_mat[i,4] = ela_1[i,0], ela_2[i,0], ela_3[i,0], ela_4[i,0], ela_5[i,0]
            elif no_stack == 10 : ela_mat[i,5], ela_mat[i,6], ela_mat[i,7], ela_mat[i,8], ela_mat[i,9] = ela_6[i,0], ela_7[i,0], ela_8[i,0], ela_9[i,0], ela_10[i,0]
        # end of i for loop
    elif matrix_type == 'std':
        for i in range(no_ela_file):
            if no_stack == 5 : ela_mat[i,0], ela_mat[i,1], ela_mat[i,2], ela_mat[i,3], ela_mat[i,4] = ela_1[i,1], ela_2[i,1], ela_3[i,1], ela_4[i,1], ela_5[i,1]
            elif no_stack == 10 : ela_mat[i,5], ela_mat[i,6], ela_mat[i,7], ela_mat[i,8], ela_mat[i,9] = ela_6[i,1], ela_7[i,1], ela_8[i,1], ela_9[i,1], ela_10[i,1]
        # end of i for loop
    return ela_mat / adim

def mean_time_relax_comp(t_relax,beta,adim):
    return ((t_relax/beta)*(math.gamma(1/beta)))/adim

def relax_plt(coeff_sh,coeff_p,E,t,cis,ela_file,type_data,analysis):
    # Function variable #
    # Scalar
    # value index
    t_i = 1 # relaxation time
    b_i = 2 # beta coeff
    sc_i = 3 # residual stress
    no_col = 6 # number of column of the matrix

    # Adimensionement variable
    if analysis == 'strain': adim = E
    elif analysis == 'pressure': adim = cis[:,12].mean()

    # Matrix
    plt = np.zeros((ela_file,no_col))

    # took the residual value of stress of the relaxation test
    for j in range(no_col): # scan the column
        if j == 0 : # save the value of the caracteristic time of relaxation
            # shear stress relaxation time
            for i in range(ela_file):
                if type_data == 'val': plt[i,j] = mean_time_relax_comp(coeff_sh[i,t_i], coeff_sh[i,b_i],t)
                elif type_data == 'err': plt[i,j] = coeff_sh[i,t_i]/t
            # end of i for loop
        if j == 1 :
            # mean stress relaxation time
            for i in range(ela_file):
                if type_data == 'val': plt[i,j] = mean_time_relax_comp(coeff_p[i,t_i], coeff_p[i,b_i],t)
                elif type_data == 'err': plt[i,j] = coeff_p[i,t_i]/t
        if j == 2 :
            # residual shear stress value
            for i in range(ela_file): plt[i,j] = coeff_sh[i,sc_i]/adim
        if j == 3 :
            # residual mean stress value
            for i in range(ela_file): plt[i,j] = coeff_p[i,sc_i]/adim
        if j == 4 : # save the value of the beta coeff for shear stress relaxation
            # beta coeff_sh
            for i in range(ela_file): plt[i,j] = coeff_sh[i,b_i]
        if j == 5 : # beta coeff_p
            for i in range(ela_file): plt[i,j] = coeff_p[i,b_i]
        # end if
    # end of j for loop
    return plt[:,:], coeff_sh, coeff_p

def variable_matrix_relax(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,no_ela,stack,col,line,mod): # create a matrix to save evolution of phi at the shear strain level of elastics/relaxation simulation
    # Variable
    # Scalar
    j_4_sav, j_5_sav = -1, -1

    if mod == 's_xy': save_it = 0
    if mod == 'std_s_xy': save_it = 1
    if mod == 'phi': save_it = 2
    if mod == 'std_phi': save_it = 3
    if mod == 'z': save_it = 4
    if mod == 'std_z': save_it = 5
    if mod == 'press': save_it = 10
    if mod == 'std_press': save_it = 11
    # end if

    # Vector
    def_val = [0,2,4,6,24,49,74,99,149,199,249,299,399,499,599,699,799,899,999]
    ratio = [1,1,1,0.62,1,1,1,1,0.95,0.41]

    # Matrix
    var = np.zeros((no_ela,col))

    # Computation
    for i in range(no_ela): # scan the N lines of the variable file
        for j in range(stack):
            # compute the step to sav the value
            per = round(ratio[j]*def_val[i])

            # if the same value is taken for cut simulation then skip to next step
            if j+1 == 4 :
                if per == j_4_sav : per, j_4_sav = j_4_sav + 1, per
                else : j_4_sav = per
            elif j +1 == 5 :
                if per == j_5_sav : per, j_5_sav = j_5_sav + 1, per
                else : j_5_sav = per
            # end if

            # value save
            if j == 0 : var[i,j] = val1[per,save_it]
            elif j == 1 : var[i,j] = val2[per,save_it]
            elif j == 2 : var[i,j] = val3[per,save_it]
            elif j == 3 : var[i,j] = val4[per,save_it]
            elif j == 4 : var[i,j] = val5[per,save_it]
            # end of if
            per = 0
    # end of i for loop
    return var

def gran_matrix(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,no_line,val_type,l,strain_rate,d,rho,stacks):
    # Function variable
    # Scalar
    if val_type == 'granulence': val_index = 0
    if val_type == 'std_gran': val_index = 1

    # Vector
    val = np.zeros(no_line)
    adim = np.zeros(no_line)

    # stack the values
    val[0] = val1[val_index]
    val[1] = val2[val_index]
    val[2] = val3[val_index]
    val[3] = val4[val_index]
    val[4] = val5[val_index]
    val[5] = val6[val_index]
    val[6] = val7[val_index]
    val[7] = val8[val_index]
    val[8] = val9[val_index]
    val[9] = val10[val_index]
    val[10] = val11[val_index]
    val[11] = val12[val_index]
    val[12] = val13[val_index]
    val[13] = val14[val_index]
    val[14] = val15[val_index]
    val[15] = val16[val_index]
    val[16] = val17[val_index]
    val[17] = val18[val_index]
    val[18] = val19[val_index]

    # adim vec
    for i in range(no_line):
        if i == 0 : adim[i] = ((l[i,stacks-1]**2)*rho*d**2)
        else : adim[i] = (((l[i,stacks-1]*strain_rate[stacks-1])**2)*rho*d**2)
    return val[:] / adim[:]

def simu_relax_phase(r_d,d_G,d_K,max_stack):
    # Function variable
    # Matrix
    dam_regim_G = np.zeros((3,max_stack))
    dam_regim_K = np.zeros((3,max_stack))

    for j in range(max_stack):
        for i in range(3):
            idx = int(r_d[i,j])
            dam_regim_G[i,j], dam_regim_K[i,j] = d_G[idx,j], d_K[idx,j]
        # end of i for loop
    # end of j for loop
    return dam_regim_G, dam_regim_K

def ela_relax_it_plt(data):
    # Function variables
    # Scalar
    # data dimmension variables
    len_data = len(data) # number of line of the data file

    # iteration search variables
    it_min = 10 # minimal increment to search when T - T_plt -> 0 Pa
    it_plt = 0 # value of the simulation step when T- T_plt -> 0 Pa
    find = 0 # if search = 1 stop the search of the it_plt

    # Shear stress variables
    T_plt = data[len_data-1] # value of the plateau (T val at the end of the simulation)
    error = 1*10**(-3) # error to the plateau value

    # Computation
    # search the iteration when T - T_plt -> 0 Pa
    for i in range(it_min,len_data,1): # search between it_min and len_data with step = 1
        if abs(data[i] - T_plt) < error and find == 0 : it_plt, find = i, 1
    # end of i for loop
    return it_plt

# compute the Viscosity eta (t* = eta/ elasti modulus)
def visc(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,error_fit_1,error_fit_2,error_fit_3,error_fit_4,error_fit_5,mod_ela,dmod_ela,visco):
    # Function variable
    # Scalar
    no_ela_file = 19
    no_stack = 5

    # select the ref time value to compute the viscosity
    if visco == 'shear': aim_t = 1
    if visco == 'pressure': aim_t = 3

    # Matrix
    eta = np.zeros((no_ela_file,no_stack))
    d_eta = np.zeros((no_ela_file,no_stack))
    t_relax = np.zeros((no_ela_file,no_stack)) # store B value

    for i in range(no_ela_file):
        # compute the dynamic viscosity eta
        eta[i,0] = plt_ela_relax_1[i,aim_t]*mod_ela[i,0]
        eta[i,1] = plt_ela_relax_2[i,aim_t]*mod_ela[i,1]
        eta[i,2] = plt_ela_relax_3[i,aim_t]*mod_ela[i,2]
        eta[i,3] = plt_ela_relax_4[i,aim_t]*mod_ela[i,3]
        eta[i,4] = plt_ela_relax_5[i,aim_t]*mod_ela[i,4]

        # compute fit model B
        t_relax[i,0] = plt_ela_relax_1[i,aim_t]
        t_relax[i,1] = plt_ela_relax_2[i,aim_t]
        t_relax[i,2] = plt_ela_relax_3[i,aim_t]
        t_relax[i,3] = plt_ela_relax_4[i,aim_t]
        t_relax[i,4] = plt_ela_relax_5[i,aim_t]

        # compute error on the dynamic viscosity
        d_eta[i,0] = ((abs(error_fit_1[i,1]/t_relax[i,0])) + abs((dmod_ela[i,0]/mod_ela[i,0])))*eta[i,0]
        d_eta[i,1] = ((abs(error_fit_2[i,1]/t_relax[i,1])) + abs((dmod_ela[i,1]/mod_ela[i,1])))*eta[i,1]
        d_eta[i,2] = ((abs(error_fit_3[i,1]/t_relax[i,2])) + abs((dmod_ela[i,2]/mod_ela[i,2])))*eta[i,2]
        d_eta[i,3] = ((abs(error_fit_4[i,1]/t_relax[i,3])) + abs((dmod_ela[i,3]/mod_ela[i,3])))*eta[i,3]
        d_eta[i,4] = ((abs(error_fit_5[i,1]/t_relax[i,4])) + abs((dmod_ela[i,4]/mod_ela[i,4])))*eta[i,4]
    # end of i for loop
    return eta, d_eta

def relax_matrix(val1,val2,val3,val4,val5,mod,no_stack): # create a matrix to save evolution of phi at the shear strain level of elastics/relaxation simulation
    # Function variable
    # Scalar
    no_ela = 19 # number of ela file restart

    if mod == 'sh relax': save_it = 0 # relaxation time
    elif mod == 'p relax': save_it = 1 # mean stress relaxation time
    elif mod == 'sh stress': save_it = 2 # residual stress value
    elif mod == 'p stress': save_it = 3 # residual mean stress value
    elif mod == 'sh beta': save_it = 4 # beta value
    elif mod == 'p beta': save_it = 5 # beta value

    # Matrix
    relax = np.zeros((no_ela,no_stack))

    # Computation
    relax[:,0], relax[:,1], relax[:,2], relax[:,3], relax[:,4] = val1[:,save_it], val2[:,save_it], val3[:,save_it], val4[:,save_it], val5[:,save_it]
    return relax

def d_stack_relax(dam,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,val,stack):
    # Function variable
    # Scalar
    line = len(dam) # number of elastic files

    # Computation
    if val == 'damage': j = 0 # stack the damage values
    elif val == 'std': j = 1 # stack the damage std values

    for i in range(line): # scan the 16 values of damage
        if stack <= 5 : dam[i,0], dam[i,1], dam[i,2], dam[i,3], dam[i,4] = d1[i,j], d2[i,j], d3[i,j], d4[i,j], d5[i,j]
        elif stack > 5 : dam[i,5], dam[i,6], dam[i,7], dam[i,8], dam[i,9] = d6[i,j], d7[i,j], d8[i,j], d9[i,j], d10[i,j]
    # end of i for loop
    return dam