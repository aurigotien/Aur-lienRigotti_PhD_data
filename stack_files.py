import numpy as np
import matplotlib.pyplot as plt

def affine(x,A,B):
    return A*x+B

def power_fit(x,A_0,b):
    return A_0 + x**b

def applied_shear(analyse,prep,s_yy):
    color_1, color_2 = plt.get_cmap('jet'), plt.get_cmap('brg')

    # basic datas
    if s_yy == 'P_90kPa': dgdt = np.array([5E-4,1E-4,5E-5,1E-5,5E-6,0,0,0,0,0]) # S_yy = 90 kPa
    elif prep == 'no_fric' and s_yy == 'P_50kPa': dgdt = np.array([3.75E-4,7.5E-5,3.75E-5,7.5E-6,3.75E-6,0,0,0,0,0]) # S_yy = 50 kPa
    elif s_yy == 'P_5kPa': dgdt = np.array([1.2E-4,2.5E-5,1.2E-5,2.5E-6,1.2E-6,0,0,0,0,0]) # S_yy = 5 kPa

    # mixed datas
    elif s_yy == 'size': dgdt = np.array([7.5E-6,7.5E-6,7.5E-6,7.5E-6,0,0,0,0,0,0]) # size
    elif s_yy == 'I_cste': dgdt = np.array([3.75E-4,5E-4,3.75E-5,5E-5,3.75E-6,5E-6,0,0]) # I_cst
    elif prep == 'fric' and s_yy == 'P_50kPa': dgdt = np.array([3.75E-4,7.5E-5,3.75E-5,7.5E-6,3.75E-4,7.5E-5,3.75E-5,7.5E-6,0,0]) # S_yy = 50 kPa
    elif s_yy == 'P_50_90_kPa': dgdt = np.array([3.75E-4,7.5E-5,3.75E-5,7.5E-6,3.75E-6,5E-4,1E-4,5E-5,1E-5,5E-6]) # S_yy = 50,90 kPa
    elif s_yy == 'P_50_90_kPa_I': dgdt = np.array([3.75E-4,5E-4,3.75E-5,5E-5,3.75E-6,5E-6,1,1,1,1]) # S_yy = 50,90 kPa
    elif s_yy == 'P_5_50_90_kPa': dgdt = np.array([1.2E-4,3.75E-4,5E-4,1.2E-5,3.75E-5,5E-5,1,1,1,1]) # S_yy = 5,50,90 kPa
    #elif s_yy == '5x10^{-3}': dgdt = np.array([5E-4,3.75E-4,1,1,1]) # I = 5 10^(-3)
    #elif s_yy == '5x10^{-4}': dgdt = np.array([5E-5,3.75E-5,1,1,1]) # I = 5 10^(-4)
    return dgdt, color_1, color_2

def plot_tag(analy,stress,prep):
    if analy == 'strain':
        tag1 = '$I(\.{\gamma})$  = $5 \cdot 10^{-3}$'
        tag2 = '$I(\.{\gamma})$  = $1 \cdot 10^{-3}$'
        tag3 = '$I(\.{\gamma})$  = $5 \cdot 10^{-4}$'
        tag4 = '$I(\.{\gamma})$  = $1 \cdot 10^{-4}$'
        tag5 = '$I(\.{\gamma})$  = $5 \cdot 10^{-5}$'
        tag6 = '$I(\.{\gamma})$  = $5 \cdot 10^{-3}$'
        tag7 = '$I(\.{\gamma})$  = $1 \cdot 10^{-3}$'
        tag8 = '$I(\.{\gamma})$  = $5 \cdot 10^{-4}$'
        tag9 = '$I(\.{\gamma})$  = $1 \cdot 10^{-4}$'
        tag10 = '$I(\.{\gamma})$  = $5 \cdot 10^{-5}$'
    elif analy == 'pressure':
        tag1 = '$I(\u03c3_{yy}/ E_{g} = 1.036 \cdot 10^{-4})$  = $5 \cdot 10^{-3}$' # tag for stack 1 graph output
        tag2 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $5 \cdot 10^{-3}$' # tag for stack 2 graph output
        tag3 = '$I(\u03c3_{yy}/ E_{g} = 1.036 \cdot 10^{-4})$  = $5 \cdot 10^{-4}$' # tag for stack 3 graph output
        tag4 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $5 \cdot 10^{-4}$' # tag for stack 4 graph output
        tag5 = '$I(\u03c3_{yy}/ E_{g} = 1.036 \cdot 10^{-4})$  = $5 \cdot 10^{-5}$' # tag for stack 5 graph output
        tag6 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $5 \cdot 10^{-5}$'
        tag7 = ''
        tag8 = ''
        tag9 = ''
        tag10 = ''
    elif prep == 'fric' or prep == 'fric_1':
        tag1 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-3}$' # tag for stack 1 graph output
        tag2 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-3}$' # tag for stack 2 graph output
        tag3 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-4}$' # tag for stack 3 graph output
        tag4 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-4}$' # tag for stack 4 graph output
        tag5 = '$I(\u03bc_{g} = 0.7)$  = $5 \cdot 10^{-3}$'
        tag6 = '$I(\u03bc_{g} = 0.7)$  = $1 \cdot 10^{-3}$'
        tag7 = '$I(\u03bc_{g} = 0.7)$  = $5 \cdot 10^{-4}$'
        tag8 = '$I(\u03bc_{g} = 0.7)$  = $1 \cdot 10^{-4}$'
        tag9 = ''
        tag10 = ''
    return tag1, tag2, tag3, tag4, tag5, tag6, tag7, tag8, tag9, tag10

def final_value(data):
    fin_val = np.zeros(4) # value of maximum of : shear strain, shear stress, mean stress
    it_fin = 0 # store the iteration of max of shear strain

    # take maximum value of shear strain
    for i in range(len(data)):
        exy_max = fin_val[0]
        if exy_max < data[i,8]:
            exy_max = data[i,8]
            it_fin = i
    # end of i for loop

    # final value of shear strain, volumetric strain, mean stress and shear stress at iteration it_max
    fin_val[0] = exy_max
    fin_val[1] = ((data[0,6] - data[it_fin,6])/data[0,6])
    fin_val[2] = data[it_fin,0]
    fin_val[3] = data[it_fin,10]
    return fin_val

def deviation_run(val,N):
    return (val[:] - val.mean())

def ponderation(val,error,N,to_ponder):
    # Function variable
    # Scalar
    ponder = 0
    output = 0

    # Vector
    std = deviation_run(val,N) # compute distance to the mean for each run

    # Ponderation computation
    for i in range(N):
        if to_ponder == 'mean':
            output = output + abs(val[i]/std[i])
            ponder = ponder + abs(1/std[i])
        elif to_ponder == 'std':
            output = output + abs(error[i]/std[i])**2
            ponder = ponder + abs(1/std[i])
        # end if
    # end of i for loop
    if to_ponder == 'std':
        output = output**0.5
    return output / ponder

def error_matrix(error_1,error_2,error_3,error_4,error_5,error_6,error_7,error_8,error_9,error_10,error_11,error_12,error_13,error_14,error_15,error_16,error_17,error_18,error_19,error_20,error_21,error_22,error_23,error_24,error_25,error_26,error_27,error_28,error_29,error_30,N):
    # Function variable
    error = np.zeros(N)

    error[0] = error_1[0,0]
    error[1] = error_2[0,0]
    error[2] = error_3[0,0]
    error[3] = error_4[0,0]
    error[4] = error_5[0,0]
    error[5] = error_6[0,0]
    error[6] = error_7[0,0]
    error[7] = error_8[0,0]
    error[8] = error_9[0,0]
    error[9] = error_10[0,0]
    error[10] = error_11[0,0]
    error[11] = error_12[0,0]
    error[12] = error_13[0,0]
    error[13] = error_14[0,0]
    error[14] = error_15[0,0]
    error[15] = error_16[0,0]
    error[16] = error_17[0,0]
    error[17] = error_18[0,0]
    error[18] = error_19[0,0]
    error[19] = error_20[0,0]
    error[20] = error_21[0,0]
    error[21] = error_22[0,0]
    error[22] = error_23[0,0]
    error[23] = error_24[0,0]
    error[24] = error_25[0,0]
    error[25] = error_26[0,0]
    error[26] = error_27[0,0]
    error[27] = error_28[0,0]
    error[28] = error_29[0,0]
    error[29] = error_30[0,0]
    return error[:]**(0.5)

# Function averging packing fraction, coordination number and computing shear stress from cis files
def val_relax(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,n):
    # function variables #
    # Scalar
    N = 30 # number of files
    dt = 1E-3 # discretization time

    # Matrix
    ave_std = np.zeros((n,11)) # matrix to store averaged values and standard deviation
    P_relax = np.zeros((n,N)) # tensor of the mean stress values, 1 simulation/column
    packing_frac = np.zeros((n,N)) # matrix to store packing fraction value, 1 col / simulation
    z = np.zeros((n,N)) # matrix to store coordination number value, 1 col / simulation
    vol = np.zeros((n,N)) # matrix to store volume of the system, 1 col / simulation
    cis = np.zeros((n,N))
    step = np.zeros((n)) # step of simulation

    # Create valN file to extract the value from the 30 dataN file
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

    for i in range(n):  # mean stress computation (LAMMPS P = mean stress * volume)
        P_relax[i,0] = val1[i,9]/vol[i,0]
        P_relax[i,1] = val2[i,9]/vol[i,1]
        P_relax[i,2] = val3[i,9]/vol[i,2]
        P_relax[i,3] = val4[i,9]/vol[i,3]
        P_relax[i,4] = val5[i,9]/vol[i,4]
        P_relax[i,5] = val6[i,9]/vol[i,5]
        P_relax[i,6] = val7[i,9]/vol[i,6]
        P_relax[i,7] = val8[i,9]/vol[i,7]
        P_relax[i,8] = val9[i,9]/vol[i,8]
        P_relax[i,9] = val10[i,9]/vol[i,9]
        P_relax[i,10] = val11[i,9]/vol[i,9]
        P_relax[i,11] = val12[i,9]/vol[i,11]
        P_relax[i,12] = val13[i,9]/vol[i,12]
        P_relax[i,13] = val14[i,9]/vol[i,13]
        P_relax[i,14] = val15[i,9]/vol[i,14]
        P_relax[i,15] = val16[i,9]/vol[i,15]
        P_relax[i,16] = val17[i,9]/vol[i,16]
        P_relax[i,17] = val18[i,9]/vol[i,17]
        P_relax[i,18] = val19[i,9]/vol[i,18]
        P_relax[i,19] = val20[i,9]/vol[i,19]
        P_relax[i,20] = val21[i,9]/vol[i,20]
        P_relax[i,21] = val22[i,9]/vol[i,21]
        P_relax[i,22] = val23[i,9]/vol[i,22]
        P_relax[i,23] = val24[i,9]/vol[i,23]
        P_relax[i,24] = val25[i,9]/vol[i,24]
        P_relax[i,25] = val26[i,9]/vol[i,25]
        P_relax[i,26] = val27[i,9]/vol[i,26]
        P_relax[i,27] = val28[i,9]/vol[i,27]
        P_relax[i,28] = val29[i,9]/vol[i,28]
        P_relax[i,29] = val30[i,9]/vol[i,29]

    for i in range(n):  # shear stress computation (LAMMPS P = mean stress * volume)
        cis[i,0] = val1[i,8]/vol[i,0]
        cis[i,1] = val2[i,8]/vol[i,1]
        cis[i,2] = val3[i,8]/vol[i,2]
        cis[i,3] = val4[i,8]/vol[i,3]
        cis[i,4] = val5[i,8]/vol[i,4]
        cis[i,5] = val6[i,8]/vol[i,5]
        cis[i,6] = val7[i,8]/vol[i,6]
        cis[i,7] = val8[i,8]/vol[i,7]
        cis[i,8] = val9[i,8]/vol[i,8]
        cis[i,9] = val10[i,8]/vol[i,9]
        cis[i,10] = val11[i,8]/vol[i,9]
        cis[i,11] = val12[i,8]/vol[i,11]
        cis[i,12] = val13[i,8]/vol[i,12]
        cis[i,13] = val14[i,8]/vol[i,13]
        cis[i,14] = val15[i,8]/vol[i,14]
        cis[i,15] = val16[i,8]/vol[i,15]
        cis[i,16] = val17[i,8]/vol[i,16]
        cis[i,17] = val18[i,8]/vol[i,17]
        cis[i,18] = val19[i,8]/vol[i,18]
        cis[i,19] = val20[i,8]/vol[i,19]
        cis[i,20] = val21[i,8]/vol[i,20]
        cis[i,21] = val22[i,8]/vol[i,21]
        cis[i,22] = val23[i,8]/vol[i,22]
        cis[i,23] = val24[i,8]/vol[i,23]
        cis[i,24] = val25[i,8]/vol[i,24]
        cis[i,25] = val26[i,8]/vol[i,25]
        cis[i,26] = val27[i,8]/vol[i,26]
        cis[i,27] = val28[i,8]/vol[i,27]
        cis[i,28] = val29[i,8]/vol[i,28]
        cis[i,29] = val30[i,8]/vol[i,29]

    for i in range (n): # Packing fraction computation
       packing_frac[i,0] = val1[i,3]
       packing_frac[i,1] = val2[i,3]
       packing_frac[i,2] = val3[i,3]
       packing_frac[i,3] = val4[i,3]
       packing_frac[i,4] = val5[i,3]
       packing_frac[i,5] = val6[i,3]
       packing_frac[i,6] = val7[i,3]
       packing_frac[i,7] = val8[i,3]
       packing_frac[i,8] = val9[i,3]
       packing_frac[i,9] = val10[i,3]
       packing_frac[i,10] = val11[i,3]
       packing_frac[i,11] = val12[i,3]
       packing_frac[i,12] = val13[i,3]
       packing_frac[i,13] = val14[i,3]
       packing_frac[i,14] = val15[i,3]
       packing_frac[i,15] = val16[i,3]
       packing_frac[i,16] = val17[i,3]
       packing_frac[i,17] = val18[i,3]
       packing_frac[i,18] = val19[i,3]
       packing_frac[i,19] = val20[i,3]
       packing_frac[i,20] = val21[i,3]
       packing_frac[i,21] = val22[i,3]
       packing_frac[i,22] = val23[i,3]
       packing_frac[i,23] = val24[i,3]
       packing_frac[i,24] = val25[i,3]
       packing_frac[i,25] = val26[i,3]
       packing_frac[i,26] = val27[i,3]
       packing_frac[i,27] = val28[i,3]
       packing_frac[i,28] = val29[i,3]
       packing_frac[i,29] = val30[i,3]

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

    for i in range(n): # time of simulation
        step[i] = val1[i,0]*dt

    for i in range(n):
        # compute mean value
        ave_std[i,0] = np.average(P_relax[i,:])
        ave_std[i,2] = np.average(packing_frac[i,:])
        ave_std[i,4] = np.average(z[i,:])
        ave_std[i,6] = np.average(vol[i,:])
        ave_std[i,8] = np.average(cis[i,:])
        ave_std[i,10] = step[i]
    # end of i for loop

    for i in range(n):
        # standard deviation computation
        ave_std[i,1] = np.std(P_relax[i,:])
        ave_std[i,3] = np.std(packing_frac[i,:])
        ave_std[i,5] = np.std(z[i,:])
        ave_std[i,7] = np.std(vol[i,:])
        ave_std[i,9] = np.std(cis[i,:])
    # end of i for loop

    return ave_std # return ave_std = M(n,9)

def val_pre_comp(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,n):
    # function variables #
    # Scalar
    N = 30 # number of files
    dt = 1E-3 # discretization time

    # Matrix
    ave_std = np.zeros((n,11)) # matrix to store averaged values and standard deviation
    P_relax = np.zeros((n,N)) # tensor of the mean stress values, 1 simulation/column
    cis = np.zeros((n,N))
    packing_frac = np.zeros((n,N)) # matrix to store packing fraction value, 1 col / simulation
    z = np.zeros((n,N)) # matrix to store coordination number value, 1 col / simulation
    vol = np.zeros((n,N)) # matrix to store volume of the system, 1 col / simulation
    step = np.zeros((n)) # step of simulation

    # Create valN file to extract the value from the 30 dataN file
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

    for i in range(n):  # mean stress computation (LAMMPS P = mean stress * volume)
        P_relax[i,0] = val1[i,9]/vol[i,0]
        P_relax[i,1] = val2[i,9]/vol[i,1]
        P_relax[i,2] = val3[i,9]/vol[i,2]
        P_relax[i,3] = val4[i,9]/vol[i,3]
        P_relax[i,4] = val5[i,9]/vol[i,4]
        P_relax[i,5] = val6[i,9]/vol[i,5]
        P_relax[i,6] = val7[i,9]/vol[i,6]
        P_relax[i,7] = val8[i,9]/vol[i,7]
        P_relax[i,8] = val9[i,9]/vol[i,8]
        P_relax[i,9] = val10[i,9]/vol[i,9]
        P_relax[i,10] = val11[i,9]/vol[i,9]
        P_relax[i,11] = val12[i,9]/vol[i,11]
        P_relax[i,12] = val13[i,9]/vol[i,12]
        P_relax[i,13] = val14[i,9]/vol[i,13]
        P_relax[i,14] = val15[i,9]/vol[i,14]
        P_relax[i,15] = val16[i,9]/vol[i,15]
        P_relax[i,16] = val17[i,9]/vol[i,16]
        P_relax[i,17] = val18[i,9]/vol[i,17]
        P_relax[i,18] = val19[i,9]/vol[i,18]
        P_relax[i,19] = val20[i,9]/vol[i,19]
        P_relax[i,20] = val21[i,9]/vol[i,20]
        P_relax[i,21] = val22[i,9]/vol[i,21]
        P_relax[i,22] = val23[i,9]/vol[i,22]
        P_relax[i,23] = val24[i,9]/vol[i,23]
        P_relax[i,24] = val25[i,9]/vol[i,24]
        P_relax[i,25] = val26[i,9]/vol[i,25]
        P_relax[i,26] = val27[i,9]/vol[i,26]
        P_relax[i,27] = val28[i,9]/vol[i,27]
        P_relax[i,28] = val29[i,9]/vol[i,28]
        P_relax[i,29] = val30[i,9]/vol[i,29]

    for i in range(n):  # shear stress computation (LAMMPS P = mean stress * volume)
        cis[i,0] = val1[i,8]/vol[i,0]
        cis[i,1] = val2[i,8]/vol[i,1]
        cis[i,2] = val3[i,8]/vol[i,2]
        cis[i,3] = val4[i,8]/vol[i,3]
        cis[i,4] = val5[i,8]/vol[i,4]
        cis[i,5] = val6[i,8]/vol[i,5]
        cis[i,6] = val7[i,8]/vol[i,6]
        cis[i,7] = val8[i,8]/vol[i,7]
        cis[i,8] = val9[i,8]/vol[i,8]
        cis[i,9] = val10[i,8]/vol[i,9]
        cis[i,10] = val11[i,8]/vol[i,9]
        cis[i,11] = val12[i,8]/vol[i,11]
        cis[i,12] = val13[i,8]/vol[i,12]
        cis[i,13] = val14[i,8]/vol[i,13]
        cis[i,14] = val15[i,8]/vol[i,14]
        cis[i,15] = val16[i,8]/vol[i,15]
        cis[i,16] = val17[i,8]/vol[i,16]
        cis[i,17] = val18[i,8]/vol[i,17]
        cis[i,18] = val19[i,8]/vol[i,18]
        cis[i,19] = val20[i,8]/vol[i,19]
        cis[i,20] = val21[i,8]/vol[i,20]
        cis[i,21] = val22[i,8]/vol[i,21]
        cis[i,22] = val23[i,8]/vol[i,22]
        cis[i,23] = val24[i,8]/vol[i,23]
        cis[i,24] = val25[i,8]/vol[i,24]
        cis[i,25] = val26[i,8]/vol[i,25]
        cis[i,26] = val27[i,8]/vol[i,26]
        cis[i,27] = val28[i,8]/vol[i,27]
        cis[i,28] = val29[i,8]/vol[i,28]
        cis[i,29] = val30[i,8]/vol[i,29]

    for i in range (n): # Packing fraction computation
       packing_frac[i,0] = val1[i,3]
       packing_frac[i,1] = val2[i,3]
       packing_frac[i,2] = val3[i,3]
       packing_frac[i,3] = val4[i,3]
       packing_frac[i,4] = val5[i,3]
       packing_frac[i,5] = val6[i,3]
       packing_frac[i,6] = val7[i,3]
       packing_frac[i,7] = val8[i,3]
       packing_frac[i,8] = val9[i,3]
       packing_frac[i,9] = val10[i,3]
       packing_frac[i,10] = val11[i,3]
       packing_frac[i,11] = val12[i,3]
       packing_frac[i,12] = val13[i,3]
       packing_frac[i,13] = val14[i,3]
       packing_frac[i,14] = val15[i,3]
       packing_frac[i,15] = val16[i,3]
       packing_frac[i,16] = val17[i,3]
       packing_frac[i,17] = val18[i,3]
       packing_frac[i,18] = val19[i,3]
       packing_frac[i,19] = val20[i,3]
       packing_frac[i,20] = val21[i,3]
       packing_frac[i,21] = val22[i,3]
       packing_frac[i,22] = val23[i,3]
       packing_frac[i,23] = val24[i,3]
       packing_frac[i,24] = val25[i,3]
       packing_frac[i,25] = val26[i,3]
       packing_frac[i,26] = val27[i,3]
       packing_frac[i,27] = val28[i,3]
       packing_frac[i,28] = val29[i,3]
       packing_frac[i,29] = val30[i,3]

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

    for i in range(n): # time of simulation
        step[i] = val1[i,0]*dt

    for i in range(n):
        # compute mean value
        ave_std[i,0] = np.average(P_relax[i,:])
        ave_std[i,2] = np.average(packing_frac[i,:])
        ave_std[i,4] = np.average(z[i,:])
        ave_std[i,6] = np.average(vol[i,:])
        ave_std[i,8] = np.average(cis[i,:])
        ave_std[i,10] = step[i]
    # end of i for loop

    for i in range(n):
        # standard deviation computation
        ave_std[i,1] = np.std(P_relax[i,:])
        ave_std[i,3] = np.std(packing_frac[i,:])
        ave_std[i,5] = np.std(z[i,:])
        ave_std[i,7] = np.std(vol[i,:])
        ave_std[i,9] = np.std(cis[i,:])
    # end of i for loop

    return ave_std # return ave_std = M(n,9)

# Function averging packing fraction, coordination number and computing shear stress from cis files
def val_cis(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,sh_typ,dg_dt,n):
    # function variables #
    # Scalar
    N = 30 # number of files
    no_col = 10 # number of column in the files
    no_return_col = 18 # number of column of the returned file
    dt = 1E-4

    # Matrix
    ave_std = np.zeros((n,no_return_col)) # matrix to store averaged values and standard deviation
    S_cis = np.zeros((n,N)) # tensor of the shear stress values, 1 simulation/column
    P_cis = np.zeros((n,N)) # tensor of the mean stress vlaues, 1 simulation/column
    z = np.zeros((n,N)) # matrix to store coordination number value, 1 col / simulation
    packing_frac = np.zeros((n,N)) # matrix to store packing fraction value, 1 col / simulation

    vol = np.zeros((n,N)) # tensor of the volumetric strain values, 1 simulation/column
    E_cis = np.zeros((n,N)) # tensor of the shear strain values, 1 simulation/column
    E_q = np.zeros((n,N)) # tensor of the deviatoric deformation, 1 simulation/column
    S_yy = np.zeros((n,N)) # tensor of the yy normal stress values, 1 simulation/column
    S_xx = np.zeros((n,N)) # tensor of the xx normal stress values, 1 simulation/column

    # Create valN file to extract the value from the 30 dataN file
    val1 = np.zeros((n,no_col))
    val2 = np.zeros((n,no_col))
    val3 = np.zeros((n,no_col))
    val4 = np.zeros((n,no_col))
    val5 = np.zeros((n,no_col))
    val6 = np.zeros((n,no_col))
    val7 = np.zeros((n,no_col))
    val8 = np.zeros((n,no_col))
    val9 = np.zeros((n,no_col))
    val10 = np.zeros((n,no_col))
    val11 = np.zeros((n,no_col))
    val12 = np.zeros((n,no_col))
    val13 = np.zeros((n,no_col))
    val14 = np.zeros((n,no_col))
    val15 = np.zeros((n,no_col))
    val16 = np.zeros((n,no_col))
    val17 = np.zeros((n,no_col))
    val18 = np.zeros((n,no_col))
    val19 = np.zeros((n,no_col))
    val20 = np.zeros((n,no_col))
    val21 = np.zeros((n,no_col))
    val22 = np.zeros((n,no_col))
    val23 = np.zeros((n,no_col))
    val24 = np.zeros((n,no_col))
    val25 = np.zeros((n,no_col))
    val26 = np.zeros((n,no_col))
    val27 = np.zeros((n,no_col))
    val28 = np.zeros((n,no_col))
    val29 = np.zeros((n,no_col))
    val30 = np.zeros((n,no_col))

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

    for i in range(n):  # Shear stress computation (LAMMPS P = shear stress * volume)
        if sh_typ == 'shear':
            S_cis[i,0] = val1[i,9]/vol[i,0]
            S_cis[i,1] = val2[i,9]/vol[i,1]
            S_cis[i,2] = val3[i,9]/vol[i,2]
            S_cis[i,3] = val4[i,9]/vol[i,3]
            S_cis[i,4] = val5[i,9]/vol[i,4]
            S_cis[i,5] = val6[i,9]/vol[i,5]
            S_cis[i,6] = val7[i,9]/vol[i,6]
            S_cis[i,7] = val8[i,9]/vol[i,7]
            S_cis[i,8] = val9[i,9]/vol[i,8]
            S_cis[i,9] = val10[i,9]/vol[i,9]
            S_cis[i,10] = val11[i,9]/vol[i,9]
            S_cis[i,11] = val12[i,9]/vol[i,11]
            S_cis[i,12] = val13[i,9]/vol[i,12]
            S_cis[i,13] = val14[i,9]/vol[i,13]
            S_cis[i,14] = val15[i,9]/vol[i,14]
            S_cis[i,15] = val16[i,9]/vol[i,15]
            S_cis[i,16] = val17[i,9]/vol[i,16]
            S_cis[i,17] = val18[i,9]/vol[i,17]
            S_cis[i,18] = val19[i,9]/vol[i,18]
            S_cis[i,19] = val20[i,9]/vol[i,19]
            S_cis[i,20] = val21[i,9]/vol[i,20]
            S_cis[i,21] = val22[i,9]/vol[i,21]
            S_cis[i,22] = val23[i,9]/vol[i,22]
            S_cis[i,23] = val24[i,9]/vol[i,23]
            S_cis[i,24] = val25[i,9]/vol[i,24]
            S_cis[i,25] = val26[i,9]/vol[i,25]
            S_cis[i,26] = val27[i,9]/vol[i,26]
            S_cis[i,27] = val28[i,9]/vol[i,27]
            S_cis[i,28] = val29[i,9]/vol[i,28]
            S_cis[i,29] = val30[i,9]/vol[i,29]

        elif sh_typ == 'deviatoric':
            S_cis[i,0] = np.sqrt((((val1[i,7]/vol[i,0])-(val1[i,8]/vol[i,0]))**2)+((val1[i,9]/vol[i,0])**2))
            S_cis[i,1] = np.sqrt((((val2[i,7]/vol[i,1])-(val2[i,8]/vol[i,1]))**2)+((val2[i,9]/vol[i,1])**2))
            S_cis[i,2] = np.sqrt((((val3[i,7]/vol[i,2])-(val3[i,8]/vol[i,2]))**2)+((val3[i,9]/vol[i,2])**2))
            S_cis[i,3] = np.sqrt((((val4[i,7]/vol[i,3])-(val4[i,8]/vol[i,3]))**2)+((val4[i,9]/vol[i,3])**2))
            S_cis[i,4] = np.sqrt((((val5[i,7]/vol[i,4])-(val5[i,8]/vol[i,4]))**2)+((val5[i,9]/vol[i,4])**2))
            S_cis[i,5] = np.sqrt((((val6[i,7]/vol[i,5])-(val6[i,8]/vol[i,5]))**2)+((val6[i,9]/vol[i,5])**2))
            S_cis[i,6] = np.sqrt((((val7[i,7]/vol[i,6])-(val7[i,8]/vol[i,6]))**2)+((val7[i,9]/vol[i,6])**2))
            S_cis[i,7] = np.sqrt((((val8[i,7]/vol[i,7])-(val8[i,8]/vol[i,7]))**2)+((val8[i,9]/vol[i,7])**2))
            S_cis[i,8] = np.sqrt((((val9[i,7]/vol[i,8])-(val9[i,8]/vol[i,8]))**2)+((val9[i,9]/vol[i,8])**2))
            S_cis[i,9] = np.sqrt((((val10[i,7]/vol[i,9])-(val10[i,8]/vol[i,9]))**2)+((val10[i,9]/vol[i,9])**2))
            S_cis[i,10] = np.sqrt((((val11[i,7]/vol[i,10])-(val11[i,8]/vol[i,10]))**2)+((val11[i,9]/vol[i,10])**2))
            S_cis[i,11] = np.sqrt((((val12[i,7]/vol[i,11])-(val12[i,8]/vol[i,11]))**2)+((val12[i,9]/vol[i,11])**2))
            S_cis[i,12] = np.sqrt((((val13[i,7]/vol[i,12])-(val13[i,8]/vol[i,12]))**2)+((val13[i,9]/vol[i,12])**2))
            S_cis[i,13] = np.sqrt((((val14[i,7]/vol[i,13])-(val14[i,8]/vol[i,13]))**2)+((val14[i,9]/vol[i,13])**2))
            S_cis[i,14] = np.sqrt((((val15[i,7]/vol[i,14])-(val15[i,8]/vol[i,14]))**2)+((val15[i,9]/vol[i,14])**2))
            S_cis[i,15] = np.sqrt((((val16[i,7]/vol[i,15])-(val16[i,8]/vol[i,15]))**2)+((val16[i,9]/vol[i,15])**2))
            S_cis[i,16] = np.sqrt((((val17[i,7]/vol[i,16])-(val17[i,8]/vol[i,16]))**2)+((val17[i,9]/vol[i,16])**2))
            S_cis[i,17] = np.sqrt((((val18[i,7]/vol[i,17])-(val18[i,8]/vol[i,17]))**2)+((val18[i,9]/vol[i,17])**2))
            S_cis[i,18] = np.sqrt((((val19[i,7]/vol[i,18])-(val19[i,8]/vol[i,18]))**2)+((val19[i,9]/vol[i,18])**2))
            S_cis[i,19] = np.sqrt((((val20[i,7]/vol[i,19])-(val20[i,8]/vol[i,19]))**2)+((val20[i,9]/vol[i,19])**2))
            S_cis[i,20] = np.sqrt((((val21[i,7]/vol[i,20])-(val21[i,8]/vol[i,20]))**2)+((val21[i,9]/vol[i,20])**2))
            S_cis[i,21] = np.sqrt((((val22[i,7]/vol[i,21])-(val22[i,8]/vol[i,21]))**2)+((val22[i,9]/vol[i,21])**2))
            S_cis[i,22] = np.sqrt((((val23[i,7]/vol[i,22])-(val23[i,8]/vol[i,22]))**2)+((val23[i,9]/vol[i,22])**2))
            S_cis[i,23] = np.sqrt((((val24[i,7]/vol[i,23])-(val24[i,8]/vol[i,23]))**2)+((val24[i,9]/vol[i,23])**2))
            S_cis[i,24] = np.sqrt((((val25[i,7]/vol[i,24])-(val25[i,8]/vol[i,24]))**2)+((val25[i,9]/vol[i,24])**2))
            S_cis[i,25] = np.sqrt((((val26[i,7]/vol[i,25])-(val26[i,8]/vol[i,25]))**2)+((val26[i,9]/vol[i,25])**2))
            S_cis[i,26] = np.sqrt((((val27[i,7]/vol[i,26])-(val27[i,8]/vol[i,26]))**2)+((val27[i,9]/vol[i,26])**2))
            S_cis[i,27] = np.sqrt((((val28[i,7]/vol[i,27])-(val28[i,8]/vol[i,27]))**2)+((val28[i,9]/vol[i,27])**2))
            S_cis[i,28] = np.sqrt((((val29[i,7]/vol[i,28])-(val29[i,8]/vol[i,28]))**2)+((val29[i,9]/vol[i,28])**2))
            S_cis[i,29] = np.sqrt((((val30[i,7]/vol[i,29])-(val30[i,8]/vol[i,29]))**2)+((val30[i,9]/vol[i,29])**2))

    for i in range(n):  # Mean stress computation (LAMMPS P = shear stress * volume)
        P_cis[i,0] = ((val1[i,7]/vol[i,0]) + (val1[i,8]/vol[i,0]))/2
        P_cis[i,1] = ((val2[i,7]/vol[i,1]) + (val2[i,8]/vol[i,1]))/2
        P_cis[i,2] = ((val3[i,7]/vol[i,2]) + (val3[i,8]/vol[i,2]))/2
        P_cis[i,3] = ((val4[i,7]/vol[i,3]) + (val4[i,8]/vol[i,3]))/2
        P_cis[i,4] = ((val5[i,7]/vol[i,4]) + (val5[i,8]/vol[i,4]))/2
        P_cis[i,5] = ((val6[i,7]/vol[i,5]) + (val6[i,8]/vol[i,5]))/2
        P_cis[i,6] = ((val7[i,7]/vol[i,6]) + (val5[i,8]/vol[i,6]))/2
        P_cis[i,7] = ((val8[i,7]/vol[i,7]) + (val7[i,8]/vol[i,7]))/2
        P_cis[i,8] = ((val9[i,7]/vol[i,8]) + (val8[i,8]/vol[i,8]))/2
        P_cis[i,9] = ((val10[i,7]/vol[i,9]) + (val9[i,8]/vol[i,9]))/2
        P_cis[i,10] = ((val11[i,7]/vol[i,9]) + (val10[i,8]/vol[i,10]))/2
        P_cis[i,11] = ((val12[i,7]/vol[i,11]) + (val11[i,8]/vol[i,11]))/2
        P_cis[i,12] = ((val13[i,7]/vol[i,12]) + (val12[i,8]/vol[i,12]))/2
        P_cis[i,13] = ((val14[i,7]/vol[i,13]) + (val13[i,8]/vol[i,13]))/2
        P_cis[i,14] = ((val15[i,7]/vol[i,14]) + (val14[i,8]/vol[i,14]))/2
        P_cis[i,15] = ((val16[i,7]/vol[i,15]) + (val15[i,8]/vol[i,15]))/2
        P_cis[i,16] = ((val17[i,7]/vol[i,16]) + (val16[i,8]/vol[i,16]))/2
        P_cis[i,17] = ((val18[i,7]/vol[i,17]) + (val17[i,8]/vol[i,17]))/2
        P_cis[i,18] = ((val19[i,7]/vol[i,18]) + (val18[i,8]/vol[i,18]))/2
        P_cis[i,19] = ((val20[i,7]/vol[i,19]) + (val19[i,8]/vol[i,19]))/2
        P_cis[i,20] = ((val21[i,7]/vol[i,20]) + (val20[i,8]/vol[i,20]))/2
        P_cis[i,21] = ((val22[i,7]/vol[i,21]) + (val21[i,8]/vol[i,21]))/2
        P_cis[i,22] = ((val23[i,7]/vol[i,22]) + (val22[i,8]/vol[i,22]))/2
        P_cis[i,23] = ((val24[i,7]/vol[i,23]) + (val23[i,8]/vol[i,23]))/2
        P_cis[i,24] = ((val25[i,7]/vol[i,24]) + (val24[i,8]/vol[i,24]))/2
        P_cis[i,25] = ((val26[i,7]/vol[i,25]) + (val25[i,8]/vol[i,25]))/2
        P_cis[i,26] = ((val27[i,7]/vol[i,26]) + (val26[i,8]/vol[i,26]))/2
        P_cis[i,27] = ((val28[i,7]/vol[i,27]) + (val27[i,8]/vol[i,27]))/2
        P_cis[i,28] = ((val29[i,7]/vol[i,28]) + (val28[i,8]/vol[i,28]))/2
        P_cis[i,29] = ((val30[i,7]/vol[i,29]) + (val29[i,8]/vol[i,29]))/2

    for i in range(n):  # Mean S_yy stress computation (LAMMPS P = shear stress * volume)
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
        S_yy[i,10] = val11[i,8]/vol[i,9]
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

    for i in range(n):  # Mean S_yy stress computation (LAMMPS P = shear stress * volume)
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
        S_xx[i,10] = val11[i,7]/vol[i,9]
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

    for i in range (n): # Packing fraction computation
        packing_frac[i,0] = val1[i,3]*np.sin((val1[i,6]*np.pi)/180)
        packing_frac[i,1] = val2[i,3]*np.sin((val2[i,6]*np.pi)/180)
        packing_frac[i,2] = val3[i,3]*np.sin((val3[i,6]*np.pi)/180)
        packing_frac[i,3] = val4[i,3]*np.sin((val4[i,6]*np.pi)/180)
        packing_frac[i,4] = val5[i,3]*np.sin((val5[i,6]*np.pi)/180)
        packing_frac[i,5] = val6[i,3]*np.sin((val6[i,6]*np.pi)/180)
        packing_frac[i,6] = val7[i,3]*np.sin((val7[i,6]*np.pi)/180)
        packing_frac[i,7] = val8[i,3]*np.sin((val8[i,6]*np.pi)/180)
        packing_frac[i,8] = val9[i,3]*np.sin((val9[i,6]*np.pi)/180)
        packing_frac[i,9] = val10[i,3]*np.sin((val10[i,6]*np.pi)/180)
        packing_frac[i,10] = val11[i,3]*np.sin((val11[i,6]*np.pi)/180)
        packing_frac[i,11] = val12[i,3]*np.sin((val12[i,6]*np.pi)/180)
        packing_frac[i,12] = val13[i,3]*np.sin((val13[i,6]*np.pi)/180)
        packing_frac[i,13] = val14[i,3]*np.sin((val14[i,6]*np.pi)/180)
        packing_frac[i,14] = val15[i,3]*np.sin((val15[i,6]*np.pi)/180)
        packing_frac[i,15] = val16[i,3]*np.sin((val16[i,6]*np.pi)/180)
        packing_frac[i,16] = val17[i,3]*np.sin((val17[i,6]*np.pi)/180)
        packing_frac[i,17] = val18[i,3]*np.sin((val18[i,6]*np.pi)/180)
        packing_frac[i,18] = val19[i,3]*np.sin((val19[i,6]*np.pi)/180)
        packing_frac[i,19] = val20[i,3]*np.sin((val20[i,6]*np.pi)/180)
        packing_frac[i,20] = val21[i,3]*np.sin((val21[i,6]*np.pi)/180)
        packing_frac[i,21] = val22[i,3]*np.sin((val22[i,6]*np.pi)/180)
        packing_frac[i,22] = val23[i,3]*np.sin((val23[i,6]*np.pi)/180)
        packing_frac[i,23] = val24[i,3]*np.sin((val24[i,6]*np.pi)/180)
        packing_frac[i,24] = val25[i,3]*np.sin((val25[i,6]*np.pi)/180)
        packing_frac[i,25] = val26[i,3]*np.sin((val26[i,6]*np.pi)/180)
        packing_frac[i,26] = val27[i,3]*np.sin((val27[i,6]*np.pi)/180)
        packing_frac[i,27] = val28[i,3]*np.sin((val28[i,6]*np.pi)/180)
        packing_frac[i,28] = val29[i,3]*np.sin((val29[i,6]*np.pi)/180)
        packing_frac[i,29] = val30[i,3]*np.sin((val30[i,6]*np.pi)/180)

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

    for i in range(n):# Imposed shear strain computation
        E_cis[i,0] = dt*val1[i,0]*dg_dt
        E_cis[i,1] = dt*val2[i,0]*dg_dt
        E_cis[i,2] = dt*val3[i,0]*dg_dt
        E_cis[i,3] = dt*val4[i,0]*dg_dt
        E_cis[i,4] = dt*val5[i,0]*dg_dt
        E_cis[i,5] = dt*val6[i,0]*dg_dt
        E_cis[i,6] = dt*val7[i,0]*dg_dt
        E_cis[i,7] = dt*val8[i,0]*dg_dt
        E_cis[i,8] = dt*val9[i,0]*dg_dt
        E_cis[i,9] = dt*val10[i,0]*dg_dt
        E_cis[i,10] = dt*val11[i,0]*dg_dt
        E_cis[i,11] = dt*val12[i,0]*dg_dt
        E_cis[i,12] = dt*val13[i,0]*dg_dt
        E_cis[i,13] = dt*val14[i,0]*dg_dt
        E_cis[i,14] = dt*val15[i,0]*dg_dt
        E_cis[i,15] = dt*val16[i,0]*dg_dt
        E_cis[i,16] = dt*val17[i,0]*dg_dt
        E_cis[i,17] = dt*val18[i,0]*dg_dt
        E_cis[i,18] = dt*val19[i,0]*dg_dt
        E_cis[i,19] = dt*val20[i,0]*dg_dt
        E_cis[i,20] = dt*val21[i,0]*dg_dt
        E_cis[i,21] = dt*val22[i,0]*dg_dt
        E_cis[i,22] = dt*val23[i,0]*dg_dt
        E_cis[i,23] = dt*val24[i,0]*dg_dt
        E_cis[i,24] = dt*val25[i,0]*dg_dt
        E_cis[i,25] = dt*val26[i,0]*dg_dt
        E_cis[i,26] = dt*val27[i,0]*dg_dt
        E_cis[i,27] = dt*val28[i,0]*dg_dt
        E_cis[i,28] = dt*val29[i,0]*dg_dt
        E_cis[i,29] = dt*val30[i,0]*dg_dt

    for i in range(n): # Deviatoric strain computation for each simulation
        E_q[i,0] = ((val1[0,4]-val1[i,4])/val1[0,4])-((val1[0,5]-val1[i,5])/val1[0,5])
        E_q[i,1] = ((val2[0,4]-val2[i,4])/val2[0,4])-((val2[0,5]-val2[i,5])/val2[0,5])
        E_q[i,2] = ((val3[0,4]-val3[i,4])/val3[0,4])-((val3[0,5]-val3[i,5])/val3[0,5])
        E_q[i,3] = ((val4[0,4]-val4[i,4])/val4[0,4])-((val4[0,5]-val4[i,5])/val4[0,5])
        E_q[i,4] = ((val5[0,4]-val5[i,4])/val5[0,4])-((val5[0,5]-val5[i,5])/val5[0,5])
        E_q[i,5] = ((val6[0,4]-val6[i,4])/val6[0,4])-((val6[0,5]-val6[i,5])/val6[0,5])
        E_q[i,6] = ((val7[0,4]-val7[i,4])/val7[0,4])-((val7[0,5]-val7[i,5])/val7[0,5])
        E_q[i,7] = ((val8[0,4]-val8[i,4])/val8[0,4])-((val8[0,5]-val8[i,5])/val8[0,5])
        E_q[i,8] = ((val9[0,4]-val9[i,4])/val9[0,4])-((val8[0,5]-val9[i,5])/val9[0,5])
        E_q[i,9] = ((val10[0,4]-val10[i,4])/val10[0,4])-((val10[0,5]-val10[i,5])/val10[0,5])
        E_q[i,10] = ((val11[0,4]-val11[i,4])/val11[0,4])-((val11[0,5]-val11[i,5])/val11[0,5])
        E_q[i,11] = ((val12[0,4]-val12[i,4])/val12[0,4])-((val12[0,5]-val12[i,5])/val12[0,5])
        E_q[i,12] = ((val13[0,4]-val13[i,4])/val13[0,4])-((val13[0,5]-val13[i,5])/val13[0,5])
        E_q[i,13] = ((val14[0,4]-val14[i,4])/val14[0,4])-((val14[0,5]-val14[i,5])/val14[0,5])
        E_q[i,14] = ((val15[0,4]-val15[i,4])/val15[0,4])-((val15[0,5]-val15[i,5])/val15[0,5])
        E_q[i,15] = ((val16[0,4]-val13[i,4])/val16[0,4])-((val16[0,5]-val16[i,5])/val16[0,5])
        E_q[i,16] = ((val17[0,4]-val17[i,4])/val17[0,4])-((val17[0,5]-val17[i,5])/val17[0,5])
        E_q[i,17] = ((val18[0,4]-val18[i,4])/val18[0,4])-((val18[0,5]-val18[i,5])/val18[0,5])
        E_q[i,18] = ((val19[0,4]-val19[i,4])/val19[0,4])-((val19[0,5]-val19[i,5])/val19[0,5])
        E_q[i,19] = ((val20[0,4]-val20[i,4])/val20[0,4])-((val20[0,5]-val20[i,5])/val20[0,5])
        E_q[i,20] = ((val21[0,4]-val21[i,4])/val21[0,4])-((val21[0,5]-val21[i,5])/val21[0,5])
        E_q[i,21] = ((val22[0,4]-val22[i,4])/val22[0,4])-((val22[0,5]-val22[i,5])/val22[0,5])
        E_q[i,22] = ((val23[0,4]-val23[i,4])/val23[0,4])-((val23[0,5]-val23[i,5])/val23[0,5])
        E_q[i,23] = ((val24[0,4]-val24[i,4])/val24[0,4])-((val24[0,5]-val24[i,5])/val24[0,5])
        E_q[i,24] = ((val25[0,4]-val25[i,4])/val25[0,4])-((val25[0,5]-val25[i,5])/val25[0,5])
        E_q[i,25] = ((val26[0,4]-val26[i,4])/val26[0,4])-((val26[0,5]-val26[i,5])/val26[0,5])
        E_q[i,26] = ((val27[0,4]-val27[i,4])/val27[0,4])-((val27[0,5]-val27[i,5])/val27[0,5])
        E_q[i,27] = ((val28[0,4]-val28[i,4])/val28[0,4])-((val28[0,5]-val28[i,5])/val28[0,5])
        E_q[i,28] = ((val29[0,4]-val29[i,4])/val29[0,4])-((val29[0,5]-val29[i,5])/val29[0,5])
        E_q[i,29] = ((val30[0,4]-val30[i,4])/val30[0,4])-((val30[0,5]-val30[i,5])/val30[0,5])

    for i in range(n):
       # standard deviation computation
       ave_std[i,1] = np.std(S_cis[i,:])
       ave_std[i,3] = np.std(packing_frac[i,:])
       ave_std[i,5] = np.std(z[i,:])
       ave_std[i,7] = np.std(vol[i,:])
       ave_std[i,9] = np.std(E_cis[i,:])
       ave_std[i,11] = np.std(P_cis[i,:])
       ave_std[i,13] = np.std(S_yy[i,:])
       ave_std[i,15] = np.std(S_xx[i,:])
       ave_std[i,17] = np.std(E_q[i,:])
    # end of i for loop

    for i in range(n):
       # compute mean value
       ave_std[i,0] = np.average(S_cis[i,:]) # average the shear stress
       ave_std[i,2] = np.average(packing_frac[i,:]) # average the packing fraction
       ave_std[i,4] = np.average(z[i,:]) # average coordination number
       ave_std[i,6] = np.average(vol[i,:]) # average volume
       ave_std[i,8] = np.average(E_cis[i,:]) # average shear strain
       ave_std[i,10] = np.average(abs(P_cis[i,:])) # average the mean stress
       ave_std[i,12] = np.average(abs(S_yy[i,:])) # average the normal stress S_yy
       ave_std[i,14] = np.average(abs(S_xx[i,:])) # average the normal stress S_xx
       ave_std[i,16] = np.average(E_q[i,:]) # average the deviatoric strain E_q
    # end of i for loop
    return ave_std # return ave_std = M(n,10)

# Function computing mean stress, volume and volumetric deformation from ela_comp files
def val_ela_comp(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,n):
    # function variables #

    # Scalar
    N = 30 # number of files

    # Matrix
    ave_std = np.zeros((n,8))  # matrix to store averaged values and standard deviation

    val = np.zeros((n,N)) # matrix to stor the mean stress values, 1 col/simulation
    vol = np.zeros((n,N)) # matrix to store volume of the system, 1 col / simulation
    E_comp = np.zeros((n,N)) # matrix to store volumetric deformation of the system, 1 col / simulation
    z = np.zeros((n,N)) # matrix to store coordination number value, 1 col / simulation

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

    # Reduced mean stress P (Pa)
    for i in range(n): # Mean stress computation (LAMMPS P = mean stress * volume)
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

    # Volumetric deformation
    for i in range(n):# Imposed volumetric deformation computation
        E_comp[i,0] = ((vol[0,0] - vol[i,0])/vol[0,0])
        E_comp[i,1] = ((vol[0,1] - vol[i,1])/vol[0,1])
        E_comp[i,2] = ((vol[0,2] - vol[i,2])/vol[0,2])
        E_comp[i,3] = ((vol[0,3] - vol[i,3])/vol[0,3])
        E_comp[i,4] = ((vol[0,4] - vol[i,4])/vol[0,4])
        E_comp[i,5] = ((vol[0,5] - vol[i,5])/vol[0,5])
        E_comp[i,6] = ((vol[0,6] - vol[i,6])/vol[0,6])
        E_comp[i,7] = ((vol[0,7] - vol[i,7])/vol[0,7])
        E_comp[i,8] = ((vol[0,8] - vol[i,8])/vol[0,8])
        E_comp[i,9] = ((vol[0,9] - vol[i,9])/vol[0,9])
        E_comp[i,10] = ((vol[0,10] - vol[i,10])/vol[0,10])
        E_comp[i,11] = ((vol[0,11] - vol[i,11])/vol[0,11])
        E_comp[i,12] = ((vol[0,12] - vol[i,12])/vol[0,12])
        E_comp[i,13] = ((vol[0,13] - vol[i,13])/vol[0,13])
        E_comp[i,14] = ((vol[0,14] - vol[i,14])/vol[0,14])
        E_comp[i,15] = ((vol[0,15] - vol[i,15])/vol[0,15])
        E_comp[i,16] = ((vol[0,16] - vol[i,16])/vol[0,16])
        E_comp[i,17] = ((vol[0,17] - vol[i,17])/vol[0,17])
        E_comp[i,18] = ((vol[0,18] - vol[i,18])/vol[0,18])
        E_comp[i,19] = ((vol[0,19] - vol[i,19])/vol[0,19])
        E_comp[i,20] = ((vol[0,20] - vol[i,20])/vol[0,20])
        E_comp[i,21] = ((vol[0,21] - vol[i,21])/vol[0,21])
        E_comp[i,22] = ((vol[0,22] - vol[i,22])/vol[0,22])
        E_comp[i,23] = ((vol[0,23] - vol[i,23])/vol[0,23])
        E_comp[i,24] = ((vol[0,24] - vol[i,24])/vol[0,24])
        E_comp[i,25] = ((vol[0,25] - vol[i,25])/vol[0,25])
        E_comp[i,26] = ((vol[0,26] - vol[i,26])/vol[0,29])
        E_comp[i,27] = ((vol[0,27] - vol[i,27])/vol[0,27])
        E_comp[i,28] = ((vol[0,28] - vol[i,28])/vol[0,28])
        E_comp[i,29] = ((vol[0,29] - vol[i,29])/vol[0,29])

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

    for i in range(n): # scan the lines
        # Mean value computation #
        ave_std[i,0] = np.average(val[i,:]) # average the mean stress
        ave_std[i,2] = np.average(vol[i,:]) # average the volume
        ave_std[i,4] = np.average(E_comp[i,:]) # average the volumetric deformation
        ave_std[i,6] = np.average(z[i,:]) # average coordination number
    # end of i for loop

    for i in range(n): # scan the lines
        # standard deviation value computation #
        ave_std[i,1] = np.std(val[i,:]) # compute the mean stress standard deviation
        ave_std[i,3] = np.std(vol[i,:]) # compute the volume standard deviation
        ave_std[i,5] = np.std(E_comp[i,:]) # compute the volumetric deformation standard deviation
        ave_std[i,7] = np.std(z[i,:]) # compute the coordination number standard deviation
    # end of i for loop

    return ave_std # return ave_std = M(n,6)

# Function averging mean stress, volume and shear deformation from ela_cis files
def val_ela_cis(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,n):
    # function variables #
    # Scalar variable
    N = 30 # number of files
    dt = 1E-6 # discretisation time

    # Matrix variable
    ave_std = np.zeros((n,8)) # matrix to store averaged values and standard deviation
    val = np.zeros((n,N)) # tensor of the shear stress values, 1 col / simulationn
    vol = np.zeros((n,N)) # volume of the simulation, 1 col / simulation
    E_cis = np.zeros((n,N)) # shear strain value, 1 col / simulation
    z = np.zeros((n,N)) # matrix to store coordination number value, 1 col / simulation

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
    val26 = np.zeros((n,N))
    val27 = np.zeros((n,N))
    val28 = np.zeros((n,N))
    val29 = np.zeros((n,N))
    val30 = np.zeros((n,N))

    # read the datas #
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

    # Shear stress
    for i in range(n): # Shear stress computation for each simulation
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

    # Shear strain
    for i in range(n): # shear strain computation for each simulation
        E_cis[i,0] = ((90 - val1[i,6])*(np.pi)/180)
        E_cis[i,1] = ((90 - val2[i,6])*(np.pi)/180)
        E_cis[i,2] = ((90 - val3[i,6])*(np.pi)/180)
        E_cis[i,3] = ((90 - val4[i,6])*(np.pi)/180)
        E_cis[i,4] = ((90 - val5[i,6])*(np.pi)/180)
        E_cis[i,5] = ((90 - val6[i,6])*(np.pi)/180)
        E_cis[i,6] = ((90 - val7[i,6])*(np.pi)/180)
        E_cis[i,7] = ((90 - val8[i,6])*(np.pi)/180)
        E_cis[i,8] = ((90 - val9[i,6])*(np.pi)/180)
        E_cis[i,9] = ((90 - val10[i,6])*(np.pi)/180)
        E_cis[i,10] = ((90 - val11[i,6])*(np.pi)/180)
        E_cis[i,11] = ((90 - val12[i,6])*(np.pi)/180)
        E_cis[i,12] = ((90 - val13[i,6])*(np.pi)/180)
        E_cis[i,13] = ((90 - val14[i,6])*(np.pi)/180)
        E_cis[i,14] = ((90 - val15[i,6])*(np.pi)/180)
        E_cis[i,15] = ((90 - val16[i,6])*(np.pi)/180)
        E_cis[i,16] = ((90 - val17[i,6])*(np.pi)/180)
        E_cis[i,17] = ((90 - val18[i,6])*(np.pi)/180)
        E_cis[i,18] = ((90 - val19[i,6])*(np.pi)/180)
        E_cis[i,19] = ((90 - val20[i,6])*(np.pi)/180)
        E_cis[i,20] = ((90 - val21[i,6])*(np.pi)/180)
        E_cis[i,21] = ((90 - val22[i,6])*(np.pi)/180)
        E_cis[i,22] = ((90 - val23[i,6])*(np.pi)/180)
        E_cis[i,23] = ((90 - val24[i,6])*(np.pi)/180)
        E_cis[i,24] = ((90 - val25[i,6])*(np.pi)/180)
        E_cis[i,25] = ((90 - val26[i,6])*(np.pi)/180)
        E_cis[i,26] = ((90 - val27[i,6])*(np.pi)/180)
        E_cis[i,27] = ((90 - val28[i,6])*(np.pi)/180)
        E_cis[i,28] = ((90 - val29[i,6])*(np.pi)/180)
        E_cis[i,29] = ((90 - val30[i,6])*(np.pi)/180)

    for i in range(n): # Coordination number computation
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

    for i in range(n): # scan the lines
        # Mean value computation #
        ave_std[i,0] = np.average(val[i,:]) # average the shear stress
        ave_std[i,2] = np.average(vol[i,:]) # average the volume
        ave_std[i,4] = np.average(E_cis[i,:]) # average the shear strain
        ave_std[i,6] = np.average(z[i,:]) # average coordination number
    # end of i for loop

    for i in range(n): # scan the lines
        # standard deviation value computation #
        ave_std[i,1] = np.std(val[i,:]) # compute the mean stress standard deviation
        ave_std[i,3] = np.std(vol[i,:]) # compute the volume standard deviation
        ave_std[i,5] = np.std(E_cis[i,:]) # compute the shear strain standard deviation
        ave_std[i,7] = np.std(z[i,:]) # compute the coordination number standard deviation
    # end of i for loop
    return ave_std # return ave_std = M(n,6)

def ela_mod_val(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,n,zoom,module):
    # Function variables #
    # Scalar
    N = 30 # number of files
    dt = 1E-6 # discretisation time

    # Vector
    ela_r = np.zeros(N) # vector to store the 30 errors of the fit
    ela_mod = np.zeros(2) # vector to store the elastic moduli

    # Matrix
    ela = np.zeros((N,2)) # store the module of elasticity and intersection with y axis

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
    val26 = np.zeros((n,N))
    val27 = np.zeros((n,N))
    val28 = np.zeros((n,N))
    val29 = np.zeros((n,N))
    val30 = np.zeros((n,N))

    # save the covariance matrix of each fit
    error_1 = np.zeros((2,2))
    error_2 = np.zeros((2,2))
    error_3 = np.zeros((2,2))
    error_4 = np.zeros((2,2))
    error_5 = np.zeros((2,2))
    error_6 = np.zeros((2,2))
    error_7 = np.zeros((2,2))
    error_8 = np.zeros((2,2))
    error_9 = np.zeros((2,2))
    error_10 = np.zeros((2,2))
    error_11 = np.zeros((2,2))
    error_12 = np.zeros((2,2))
    error_13 = np.zeros((2,2))
    error_14 = np.zeros((2,2))
    error_15 = np.zeros((2,2))
    error_16 = np.zeros((2,2))
    error_17 = np.zeros((2,2))
    error_18 = np.zeros((2,2))
    error_19 = np.zeros((2,2))
    error_20 = np.zeros((2,2))
    error_21 = np.zeros((2,2))
    error_22 = np.zeros((2,2))
    error_23 = np.zeros((2,2))
    error_24 = np.zeros((2,2))
    error_25 = np.zeros((2,2))
    error_26 = np.zeros((2,2))
    error_27 = np.zeros((2,2))
    error_28 = np.zeros((2,2))
    error_29 = np.zeros((2,2))
    error_30 = np.zeros((2,2))

    vol = np.zeros((n,N)) # volume of the simulation
    E_comp = np.zeros((n,N)) # volumetric deformation
    E_cis = np.zeros((n,N)) # shear strain
    x_val = np.zeros((n,N)) # x values for linear feat
    y_val = np.zeros((n,N)) # y values for linear feet

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

    # Attribution of the elaues #
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

    # Compute volume for each simulation
    for i in range(n):
        vol[i,0] = val1[i,4]*val1[i,5]
        vol[i,1] = val2[i,4]*val2[i,5]
        vol[i,2] = val3[i,4]*val3[i,5]
        vol[i,3] = val4[i,4]*val4[i,5]
        vol[i,4] = val5[i,4]*val5[i,5]
        vol[i,5] = val6[i,4]*val6[i,5]
        vol[i,6] = val7[i,4]*val7[i,5]
        vol[i,7] = val8[i,4]*val8[i,5]
        vol[i,8] = val9[i,4]*val9[i,5]
        vol[i,9] = val10[i,4]*val10[i,5]
        vol[i,10] = val11[i,4]*val11[i,5]
        vol[i,11] = val12[i,4]*val12[i,5]
        vol[i,12] = val13[i,4]*val13[i,5]
        vol[i,13] = val14[i,4]*val14[i,5]
        vol[i,14] = val15[i,4]*val15[i,5]
        vol[i,15] = val16[i,4]*val16[i,5]
        vol[i,16] = val17[i,4]*val17[i,5]
        vol[i,17] = val18[i,4]*val18[i,5]
        vol[i,18] = val19[i,4]*val19[i,5]
        vol[i,19] = val20[i,4]*val20[i,5]
        vol[i,20] = val21[i,4]*val21[i,5]
        vol[i,21] = val22[i,4]*val22[i,5]
        vol[i,22] = val23[i,4]*val23[i,5]
        vol[i,23] = val24[i,4]*val24[i,5]
        vol[i,24] = val25[i,4]*val25[i,5]
        vol[i,25] = val26[i,4]*val26[i,5]
        vol[i,26] = val27[i,4]*val27[i,5]
        vol[i,27] = val28[i,4]*val28[i,5]
        vol[i,28] = val29[i,4]*val29[i,5]
        vol[i,29] = val30[i,4]*val30[i,5]
    # end of i for loop

    # Volumetric deformation
    if module == 'bulk':
        for i in range(n):
            E_comp[i,0] = ((-vol[i,0] + vol[0,0])/vol[0,0])
            E_comp[i,1] = ((-vol[i,1] + vol[0,1])/vol[0,1])
            E_comp[i,2] = ((-vol[i,2] + vol[0,2])/vol[0,2])
            E_comp[i,3] = ((-vol[i,3] + vol[0,3])/vol[0,3])
            E_comp[i,4] = ((-vol[i,4] + vol[0,4])/vol[0,4])
            E_comp[i,5] = ((-vol[i,5] + vol[0,5])/vol[0,5])
            E_comp[i,6] = ((-vol[i,6] + vol[0,6])/vol[0,6])
            E_comp[i,7] = ((-vol[i,7] + vol[0,7])/vol[0,7])
            E_comp[i,8] = ((-vol[i,8] + vol[0,8])/vol[0,8])
            E_comp[i,9] = ((-vol[i,9] + vol[0,9])/vol[0,9])
            E_comp[i,10] = ((-vol[i,10] + vol[0,10])/vol[0,10])
            E_comp[i,11] = ((-vol[i,11] + vol[0,11])/vol[0,11])
            E_comp[i,12] = ((-vol[i,12] + vol[0,12])/vol[0,12])
            E_comp[i,13] = ((-vol[i,13] + vol[0,13])/vol[0,13])
            E_comp[i,14] = ((-vol[i,14] + vol[0,14])/vol[0,14])
            E_comp[i,15] = ((-vol[i,15] + vol[0,15])/vol[0,15])
            E_comp[i,16] = ((-vol[i,16] + vol[0,16])/vol[0,16])
            E_comp[i,17] = ((-vol[i,17] + vol[0,17])/vol[0,17])
            E_comp[i,18] = ((-vol[i,18] + vol[0,18])/vol[0,18])
            E_comp[i,19] = ((-vol[i,19] + vol[0,19])/vol[0,19])
            E_comp[i,20] = ((-vol[i,20] + vol[0,20])/vol[0,20])
            E_comp[i,21] = ((-vol[i,21] + vol[0,21])/vol[0,21])
            E_comp[i,22] = ((-vol[i,22] + vol[0,22])/vol[0,22])
            E_comp[i,23] = ((-vol[i,23] + vol[0,23])/vol[0,23])
            E_comp[i,24] = ((-vol[i,24] + vol[0,24])/vol[0,24])
            E_comp[i,25] = ((-vol[i,25] + vol[0,25])/vol[0,25])
            E_comp[i,26] = ((-vol[i,26] + vol[0,26])/vol[0,29])
            E_comp[i,27] = ((-vol[i,27] + vol[0,27])/vol[0,27])
            E_comp[i,28] = ((-vol[i,28] + vol[0,28])/vol[0,28])
            E_comp[i,29] = ((-vol[i,29] + vol[0,29])/vol[0,29])
        # end of i for loop
    # end if

    # Shear strain
    if module == 'shear':
        for i in range(n): # shear strain computation for each simulation
            E_cis[i,0] = ((90 - val1[i,6])*(np.pi)/180)
            E_cis[i,1] = ((90 - val2[i,6])*(np.pi)/180)
            E_cis[i,2] = ((90 - val3[i,6])*(np.pi)/180)
            E_cis[i,3] = ((90 - val4[i,6])*(np.pi)/180)
            E_cis[i,4] = ((90 - val5[i,6])*(np.pi)/180)
            E_cis[i,5] = ((90 - val6[i,6])*(np.pi)/180)
            E_cis[i,6] = ((90 - val7[i,6])*(np.pi)/180)
            E_cis[i,7] = ((90 - val8[i,6])*(np.pi)/180)
            E_cis[i,8] = ((90 - val9[i,6])*(np.pi)/180)
            E_cis[i,9] = ((90 - val10[i,6])*(np.pi)/180)
            E_cis[i,10] = ((90 - val11[i,6])*(np.pi)/180)
            E_cis[i,11] = ((90 - val12[i,6])*(np.pi)/180)
            E_cis[i,12] = ((90 - val13[i,6])*(np.pi)/180)
            E_cis[i,13] = ((90 - val14[i,6])*(np.pi)/180)
            E_cis[i,14] = ((90 - val15[i,6])*(np.pi)/180)
            E_cis[i,15] = ((90 - val16[i,6])*(np.pi)/180)
            E_cis[i,16] = ((90 - val17[i,6])*(np.pi)/180)
            E_cis[i,17] = ((90 - val18[i,6])*(np.pi)/180)
            E_cis[i,18] = ((90 - val19[i,6])*(np.pi)/180)
            E_cis[i,19] = ((90 - val20[i,6])*(np.pi)/180)
            E_cis[i,20] = ((90 - val21[i,6])*(np.pi)/180)
            E_cis[i,21] = ((90 - val22[i,6])*(np.pi)/180)
            E_cis[i,22] = ((90 - val23[i,6])*(np.pi)/180)
            E_cis[i,23] = ((90 - val24[i,6])*(np.pi)/180)
            E_cis[i,24] = ((90 - val25[i,6])*(np.pi)/180)
            E_cis[i,25] = ((90 - val26[i,6])*(np.pi)/180)
            E_cis[i,26] = ((90 - val27[i,6])*(np.pi)/180)
            E_cis[i,27] = ((90 - val28[i,6])*(np.pi)/180)
            E_cis[i,28] = ((90 - val29[i,6])*(np.pi)/180)
            E_cis[i,29] = ((90 - val30[i,6])*(np.pi)/180)
        # end of i for loop
    # end if

    # Determine elastic properties
    if module == 'bulk' :
        for i in range(n):
            x_val[i,0] = E_comp[i,0]
            x_val[i,1] = E_comp[i,1]
            x_val[i,2] = E_comp[i,2]
            x_val[i,3] = E_comp[i,3]
            x_val[i,4] = E_comp[i,4]
            x_val[i,5] = E_comp[i,5]
            x_val[i,6] = E_comp[i,6]
            x_val[i,7] = E_comp[i,7]
            x_val[i,8] = E_comp[i,8]
            x_val[i,9] = E_comp[i,9]
            x_val[i,10] = E_comp[i,10]
            x_val[i,11] = E_comp[i,11]
            x_val[i,12] = E_comp[i,12]
            x_val[i,13] = E_comp[i,13]
            x_val[i,14] = E_comp[i,14]
            x_val[i,15] = E_comp[i,15]
            x_val[i,16] = E_comp[i,16]
            x_val[i,17] = E_comp[i,17]
            x_val[i,18] = E_comp[i,18]
            x_val[i,19] = E_comp[i,19]
            x_val[i,20] = E_comp[i,20]
            x_val[i,21] = E_comp[i,21]
            x_val[i,22] = E_comp[i,22]
            x_val[i,23] = E_comp[i,23]
            x_val[i,24] = E_comp[i,24]
            x_val[i,25] = E_comp[i,25]
            x_val[i,26] = E_comp[i,26]
            x_val[i,27] = E_comp[i,27]
            x_val[i,28] = E_comp[i,28]
            x_val[i,29] = E_comp[i,29]

            y_val[i,0] = val1[i,9]/vol[i,0]
            y_val[i,1] = val2[i,9]/vol[i,1]
            y_val[i,2] = val3[i,9]/vol[i,2]
            y_val[i,3] = val4[i,9]/vol[i,3]
            y_val[i,4] = val5[i,9]/vol[i,4]
            y_val[i,5] = val6[i,9]/vol[i,5]
            y_val[i,6] = val7[i,9]/vol[i,6]
            y_val[i,7] = val8[i,9]/vol[i,7]
            y_val[i,8] = val9[i,9]/vol[i,8]
            y_val[i,9] = val10[i,9]/vol[i,9]
            y_val[i,10] = val11[i,9]/vol[i,10]
            y_val[i,11] = val12[i,9]/vol[i,11]
            y_val[i,12] = val13[i,9]/vol[i,12]
            y_val[i,13] = val14[i,9]/vol[i,13]
            y_val[i,14] = val15[i,9]/vol[i,14]
            y_val[i,15] = val16[i,9]/vol[i,15]
            y_val[i,16] = val17[i,9]/vol[i,16]
            y_val[i,17] = val18[i,9]/vol[i,17]
            y_val[i,18] = val19[i,9]/vol[i,18]
            y_val[i,19] = val20[i,9]/vol[i,19]
            y_val[i,20] = val21[i,9]/vol[i,20]
            y_val[i,21] = val22[i,9]/vol[i,21]
            y_val[i,22] = val23[i,9]/vol[i,22]
            y_val[i,23] = val24[i,9]/vol[i,23]
            y_val[i,24] = val25[i,9]/vol[i,24]
            y_val[i,25] = val26[i,9]/vol[i,25]
            y_val[i,26] = val27[i,9]/vol[i,26]
            y_val[i,27] = val28[i,9]/vol[i,27]
            y_val[i,28] = val29[i,9]/vol[i,28]
            y_val[i,29] = val30[i,9]/vol[i,29]
        # end of i for loop

    elif module =='shear':
        for i in range(n):
            x_val[i,0] = E_cis[i,0]
            x_val[i,1] = E_cis[i,1]
            x_val[i,2] = E_cis[i,2]
            x_val[i,3] = E_cis[i,3]
            x_val[i,4] = E_cis[i,4]
            x_val[i,5] = E_cis[i,5]
            x_val[i,6] = E_cis[i,6]
            x_val[i,7] = E_cis[i,7]
            x_val[i,8] = E_cis[i,8]
            x_val[i,9] = E_cis[i,9]
            x_val[i,10] = E_cis[i,10]
            x_val[i,11] = E_cis[i,11]
            x_val[i,12] = E_cis[i,12]
            x_val[i,13] = E_cis[i,13]
            x_val[i,14] = E_cis[i,14]
            x_val[i,15] = E_cis[i,15]
            x_val[i,16] = E_cis[i,16]
            x_val[i,17] = E_cis[i,17]
            x_val[i,18] = E_cis[i,18]
            x_val[i,19] = E_cis[i,19]
            x_val[i,20] = E_cis[i,20]
            x_val[i,21] = E_cis[i,21]
            x_val[i,22] = E_cis[i,22]
            x_val[i,23] = E_cis[i,23]
            x_val[i,24] = E_cis[i,24]
            x_val[i,25] = E_cis[i,25]
            x_val[i,26] = E_cis[i,26]
            x_val[i,27] = E_cis[i,27]
            x_val[i,28] = E_cis[i,28]
            x_val[i,29] = E_cis[i,29]

            y_val[i,0] = val1[i,9]/vol[i,0]
            y_val[i,1] = val2[i,9]/vol[i,1]
            y_val[i,2] = val3[i,9]/vol[i,2]
            y_val[i,3] = val4[i,9]/vol[i,3]
            y_val[i,4] = val5[i,9]/vol[i,4]
            y_val[i,5] = val6[i,9]/vol[i,5]
            y_val[i,6] = val7[i,9]/vol[i,6]
            y_val[i,7] = val8[i,9]/vol[i,7]
            y_val[i,8] = val9[i,9]/vol[i,8]
            y_val[i,9] = val10[i,9]/vol[i,9]
            y_val[i,10] = val11[i,9]/vol[i,10]
            y_val[i,11] = val12[i,9]/vol[i,11]
            y_val[i,12] = val13[i,9]/vol[i,12]
            y_val[i,13] = val14[i,9]/vol[i,13]
            y_val[i,14] = val15[i,9]/vol[i,14]
            y_val[i,15] = val16[i,9]/vol[i,15]
            y_val[i,16] = val17[i,9]/vol[i,16]
            y_val[i,17] = val18[i,9]/vol[i,17]
            y_val[i,18] = val19[i,9]/vol[i,18]
            y_val[i,19] = val20[i,9]/vol[i,19]
            y_val[i,20] = val21[i,9]/vol[i,20]
            y_val[i,21] = val22[i,9]/vol[i,21]
            y_val[i,22] = val23[i,9]/vol[i,22]
            y_val[i,23] = val24[i,9]/vol[i,23]
            y_val[i,24] = val25[i,9]/vol[i,24]
            y_val[i,25] = val26[i,9]/vol[i,25]
            y_val[i,26] = val27[i,9]/vol[i,26]
            y_val[i,27] = val28[i,9]/vol[i,27]
            y_val[i,28] = val29[i,9]/vol[i,28]
            y_val[i,29] = val30[i,9]/vol[i,29]

    # Elastic moduli
    ela[0,:], error_1[:,:] = np.polyfit(x_val[zoom:,0],y_val[zoom:,0], 1, full = False, cov = True)
    ela[1,:], error_2[:,:] = np.polyfit(x_val[zoom:,1],y_val[zoom:,1], 1, full = False, cov = True)
    ela[2,:], error_3[:,:] = np.polyfit(x_val[zoom:,2],y_val[zoom:,2], 1, full = False, cov = True)
    ela[3,:], error_4[:,:] = np.polyfit(x_val[zoom:,3],y_val[zoom:,3], 1, full = False, cov = True)
    ela[4,:], error_5[:,:] = np.polyfit(x_val[zoom:,4],y_val[zoom:,4], 1, full = False, cov = True)
    ela[5,:], error_6[:,:] = np.polyfit(x_val[zoom:,5],y_val[zoom:,5], 1, full = False, cov = True)
    ela[6,:], error_7[:,:] = np.polyfit(x_val[zoom:,6],y_val[zoom:,6], 1, full = False, cov = True)
    ela[7,:], error_8[:,:] = np.polyfit(x_val[zoom:,7],y_val[zoom:,7], 1, full = False, cov = True)
    ela[8,:], error_9[:,:] = np.polyfit(x_val[zoom:,8],y_val[zoom:,8], 1, full = False, cov = True)
    ela[9,:], error_10[:,:] = np.polyfit(x_val[zoom:,9],y_val[zoom:,9], 1, full = False, cov = True)
    ela[10,:], error_11[:,:] = np.polyfit(x_val[zoom:,10],y_val[zoom:,10], 1, full = False, cov = True)
    ela[11,:], error_12[:,:] = np.polyfit(x_val[zoom:,11],y_val[zoom:,11], 1, full = False, cov = True)
    ela[12,:], error_13[:,:] = np.polyfit(x_val[zoom:,12],y_val[zoom:,12], 1, full = False, cov = True)
    ela[13,:], error_14[:,:] = np.polyfit(x_val[zoom:,13],y_val[zoom:,13], 1, full = False, cov = True)
    ela[14,:], error_15[:,:] = np.polyfit(x_val[zoom:,14],y_val[zoom:,14], 1, full = False, cov = True)
    ela[15,:], error_16[:,:] = np.polyfit(x_val[zoom:,15],y_val[zoom:,15], 1, full = False, cov = True)
    ela[16,:], error_17[:,:] = np.polyfit(x_val[zoom:,16],y_val[zoom:,16], 1, full = False, cov = True)
    ela[17,:], error_18[:,:] = np.polyfit(x_val[zoom:,17],y_val[zoom:,17], 1, full = False, cov = True)
    ela[18,:], error_19[:,:] = np.polyfit(x_val[zoom:,18],y_val[zoom:,18], 1, full = False, cov = True)
    ela[19,:], error_20[:,:] = np.polyfit(x_val[zoom:,19],y_val[zoom:,19], 1, full = False, cov = True)
    ela[20,:], error_21[:,:] = np.polyfit(x_val[zoom:,20],y_val[zoom:,20], 1, full = False, cov = True)
    ela[21,:], error_22[:,:] = np.polyfit(x_val[zoom:,21],y_val[zoom:,21], 1, full = False, cov = True)
    ela[22,:], error_23[:,:] = np.polyfit(x_val[zoom:,22],y_val[zoom:,22], 1, full = False, cov = True)
    ela[23,:], error_24[:,:] = np.polyfit(x_val[zoom:,23],y_val[zoom:,23], 1, full = False, cov = True)
    ela[24,:], error_25[:,:] = np.polyfit(x_val[zoom:,24],y_val[zoom:,24], 1, full = False, cov = True)
    ela[25,:], error_26[:,:] = np.polyfit(x_val[zoom:,25],y_val[zoom:,25], 1, full = False, cov = True)
    ela[26,:], error_27[:,:] = np.polyfit(x_val[zoom:,26],y_val[zoom:,26], 1, full = False, cov = True)
    ela[27,:], error_28[:,:] = np.polyfit(x_val[zoom:,27],y_val[zoom:,27], 1, full = False, cov = True)
    ela[28,:], error_29[:,:] = np.polyfit(x_val[zoom:,28],y_val[zoom:,28], 1, full = False, cov = True)
    ela[29,:], error_30[:,:] = np.polyfit(x_val[zoom:,29],y_val[zoom:,29], 1, full = False, cov = True)

    # Save the error of the first value of fit in a matrix
    ela_r = error_matrix(error_1, error_2, error_3, error_4, error_5, error_6, error_7, error_8, error_9, error_10, error_11, error_12, error_13, error_14, error_15, error_16, error_17, error_18, error_19, error_20, error_21, error_22, error_23, error_24, error_25, error_26, error_27, error_28, error_29, error_30, N)

    # Mean value computation ponderated by fit error
    ela_mod[0] = 0.5*ponderation(ela[:,0], ela_r[:], N, 'mean')

    # Std value computation ponderated by fit error
    ela_mod[1] = ponderation(ela[:,0], ela_r[:], N, 'std')
    return ela_mod

def restart_def(data,dg_dt,no_restart,n):
    # Function variable
    # Variable
    inc = 1 # zero the value for ini.restart.500000
    N = 30 # number of stacks
    dt = 1E-4

    # file read
    val = np.zeros((n,N))
    data.readline()
    val = np.loadtxt(data)

    # Extraction
    if no_restart == 1 :
        inc = 0 # gamma = 0 for no restart 1
    # end if
    return inc*dt*val[0,0]*dg_dt

# Function to open the simulation files of shearing and averaged it in a variable
def file_data_relax(line,path,num_simu): # read the 30 files and compile it in a single file + close the used files
    # Function variable #
    # Scalar
    no_it = 1 # use to open the 30 simulation files

    # Matrix
    values = np.zeros((line,10)) # matrix to store the shearing averaged values

    # Shearing step file opening
    relax1 = open(f"{path}/run_{no_it}/extr_data/data/data_relax.txt","r")
    relax2 = open(f"{path}/run_{no_it+1}/extr_data/data/data_relax.txt","r")
    relax3 = open(f"{path}/run_{no_it+2}/extr_data/data/data_relax.txt","r")
    relax4 = open(f"{path}/run_{no_it+3}/extr_data/data/data_relax.txt","r")
    relax5 = open(f"{path}/run_{no_it+4}/extr_data/data/data_relax.txt","r")
    relax6 = open(f"{path}/run_{no_it+5}/extr_data/data/data_relax.txt","r")
    relax7 = open(f"{path}/run_{no_it+6}/extr_data/data/data_relax.txt","r")
    relax8 = open(f"{path}/run_{no_it+7}/extr_data/data/data_relax.txt","r")
    relax9 = open(f"{path}/run_{no_it+8}/extr_data/data/data_relax.txt","r")
    relax10 = open(f"{path}/run_{no_it+9}/extr_data/data/data_relax.txt","r")
    relax11 = open(f"{path}/run_{no_it+10}/extr_data/data/data_relax.txt","r")
    relax12 = open(f"{path}/run_{no_it+11}/extr_data/data/data_relax.txt","r")
    relax13 = open(f"{path}/run_{no_it+12}/extr_data/data/data_relax.txt","r")
    relax14 = open(f"{path}/run_{no_it+13}/extr_data/data/data_relax.txt","r")
    relax15 = open(f"{path}/run_{no_it+14}/extr_data/data/data_relax.txt","r")
    relax16 = open(f"{path}/run_{no_it+15}/extr_data/data/data_relax.txt","r")
    relax17 = open(f"{path}/run_{no_it+16}/extr_data/data/data_relax.txt","r")
    relax18 = open(f"{path}/run_{no_it+17}/extr_data/data/data_relax.txt","r")
    relax19 = open(f"{path}/run_{no_it+18}/extr_data/data/data_relax.txt","r")
    relax20 = open(f"{path}/run_{no_it+19}/extr_data/data/data_relax.txt","r")
    relax21 = open(f"{path}/run_{no_it+20}/extr_data/data/data_relax.txt","r")
    relax22 = open(f"{path}/run_{no_it+21}/extr_data/data/data_relax.txt","r")
    relax23 = open(f"{path}/run_{no_it+22}/extr_data/data/data_relax.txt","r")
    relax24 = open(f"{path}/run_{no_it+23}/extr_data/data/data_relax.txt","r")
    relax25 = open(f"{path}/run_{no_it+24}/extr_data/data/data_relax.txt","r")
    relax26 = open(f"{path}/run_{no_it+25}/extr_data/data/data_relax.txt","r")
    relax27 = open(f"{path}/run_{no_it+26}/extr_data/data/data_relax.txt","r")
    relax28 = open(f"{path}/run_{no_it+27}/extr_data/data/data_relax.txt","r")
    relax29 = open(f"{path}/run_{no_it+28}/extr_data/data/data_relax.txt","r")
    relax30 = open(f"{path}/run_{no_it+29}/extr_data/data/data_relax.txt","r")

    # store the averaged values of val_cis in variable values = M(n,10)
    values = val_relax(relax1,relax2,relax3,relax4,relax5,relax6,relax7,relax8,relax9,relax10,relax11,relax12,relax13,relax14,relax15,relax16,relax17,relax18,relax19,relax20,relax21,relax22,relax23,relax24,relax25,relax26,relax27,relax28,relax29,relax30,line)

    # Closure of the openned files
    relax1.close()
    relax2.close()
    relax3.close()
    relax4.close()
    relax5.close()
    relax6.close()
    relax7.close()
    relax8.close()
    relax9.close()
    relax10.close()
    relax11.close()
    relax12.close()
    relax13.close()
    relax14.close()
    relax15.close()
    relax16.close()
    relax17.close()
    relax18.close()
    relax19.close()
    relax20.close()
    relax21.close()
    relax22.close()
    relax23.close()
    relax24.close()
    relax25.close()
    relax26.close()
    relax27.close()
    relax28.close()
    relax29.close()
    relax30.close()
    return values # return matrix values = M(n,10)

def file_data_pre_comp(path,num_simu): # read the 30 files and compile it in a single file + close the used files
    # Function variable #
    # Scalar
    no_it = 1 # use to open the 30 simulation files
    line = 50 # number of lines in precomp.txt

    # Matrix
    values = np.zeros((line,10)) # matrix to store the shearing averaged values

    # Shearing step file opening
    pre_comp1 = open(f"{path}/run_{no_it}/extr_data/data/data_pre_comp.txt","r")
    pre_comp2 = open(f"{path}/run_{no_it+1}/extr_data/data/data_pre_comp.txt","r")
    pre_comp3 = open(f"{path}/run_{no_it+2}/extr_data/data/data_pre_comp.txt","r")
    pre_comp4 = open(f"{path}/run_{no_it+3}/extr_data/data/data_pre_comp.txt","r")
    pre_comp5 = open(f"{path}/run_{no_it+4}/extr_data/data/data_pre_comp.txt","r")
    pre_comp6 = open(f"{path}/run_{no_it+5}/extr_data/data/data_pre_comp.txt","r")
    pre_comp7 = open(f"{path}/run_{no_it+6}/extr_data/data/data_pre_comp.txt","r")
    pre_comp8 = open(f"{path}/run_{no_it+7}/extr_data/data/data_pre_comp.txt","r")
    pre_comp9 = open(f"{path}/run_{no_it+8}/extr_data/data/data_pre_comp.txt","r")
    pre_comp10 = open(f"{path}/run_{no_it+9}/extr_data/data/data_pre_comp.txt","r")
    pre_comp11 = open(f"{path}/run_{no_it+10}/extr_data/data/data_pre_comp.txt","r")
    pre_comp12 = open(f"{path}/run_{no_it+11}/extr_data/data/data_pre_comp.txt","r")
    pre_comp13 = open(f"{path}/run_{no_it+12}/extr_data/data/data_pre_comp.txt","r")
    pre_comp14 = open(f"{path}/run_{no_it+13}/extr_data/data/data_pre_comp.txt","r")
    pre_comp15 = open(f"{path}/run_{no_it+14}/extr_data/data/data_pre_comp.txt","r")
    pre_comp16 = open(f"{path}/run_{no_it+15}/extr_data/data/data_pre_comp.txt","r")
    pre_comp17 = open(f"{path}/run_{no_it+16}/extr_data/data/data_pre_comp.txt","r")
    pre_comp18 = open(f"{path}/run_{no_it+17}/extr_data/data/data_pre_comp.txt","r")
    pre_comp19 = open(f"{path}/run_{no_it+18}/extr_data/data/data_pre_comp.txt","r")
    pre_comp20 = open(f"{path}/run_{no_it+19}/extr_data/data/data_pre_comp.txt","r")
    pre_comp21 = open(f"{path}/run_{no_it+20}/extr_data/data/data_pre_comp.txt","r")
    pre_comp22 = open(f"{path}/run_{no_it+21}/extr_data/data/data_pre_comp.txt","r")
    pre_comp23 = open(f"{path}/run_{no_it+22}/extr_data/data/data_pre_comp.txt","r")
    pre_comp24 = open(f"{path}/run_{no_it+23}/extr_data/data/data_pre_comp.txt","r")
    pre_comp25 = open(f"{path}/run_{no_it+24}/extr_data/data/data_pre_comp.txt","r")
    pre_comp26 = open(f"{path}/run_{no_it+25}/extr_data/data/data_pre_comp.txt","r")
    pre_comp27 = open(f"{path}/run_{no_it+26}/extr_data/data/data_pre_comp.txt","r")
    pre_comp28 = open(f"{path}/run_{no_it+27}/extr_data/data/data_pre_comp.txt","r")
    pre_comp29 = open(f"{path}/run_{no_it+28}/extr_data/data/data_pre_comp.txt","r")
    pre_comp30 = open(f"{path}/run_{no_it+29}/extr_data/data/data_pre_comp.txt","r")

    # store the averaged values of val_cis in variable values = M(n,10)
    values = val_pre_comp(pre_comp1,pre_comp2,pre_comp3,pre_comp4,pre_comp5,pre_comp6,pre_comp7,pre_comp8,pre_comp9,pre_comp10,pre_comp11,pre_comp12,pre_comp13,pre_comp14,pre_comp15,pre_comp16,pre_comp17,pre_comp18,pre_comp19,pre_comp20,pre_comp21,pre_comp22,pre_comp23,pre_comp24,pre_comp25,pre_comp26,pre_comp27,pre_comp28,pre_comp29,pre_comp30,line)

    # Closure of the openned files
    pre_comp1.close()
    pre_comp2.close()
    pre_comp3.close()
    pre_comp4.close()
    pre_comp5.close()
    pre_comp6.close()
    pre_comp7.close()
    pre_comp8.close()
    pre_comp9.close()
    pre_comp10.close()
    pre_comp11.close()
    pre_comp12.close()
    pre_comp13.close()
    pre_comp14.close()
    pre_comp15.close()
    pre_comp16.close()
    pre_comp17.close()
    pre_comp18.close()
    pre_comp19.close()
    pre_comp20.close()
    pre_comp21.close()
    pre_comp22.close()
    pre_comp23.close()
    pre_comp24.close()
    pre_comp25.close()
    pre_comp26.close()
    pre_comp27.close()
    pre_comp28.close()
    pre_comp29.close()
    pre_comp30.close()

    return values # return matrix values = M(n,10)

# Function to open the simulation files of shearing and averaged it in a variable
def file_data(line,path,num_simu,sh_type,dg_dt): # read the 30 files and compile it in a single file + close the used files
    # Function variable #
    # Scalar
    no_it = 1 # use to open the 30 simulation files

    # Matrix
    values = np.zeros((line,14)) # matrix to store the shearing averaged values

    # Shearing step file opening
    cis1 = open(f"{path}/run_{no_it}/extr_data/data/data_cis.txt","r")
    cis2 = open(f"{path}/run_{no_it+1}/extr_data/data/data_cis.txt","r")
    cis3 = open(f"{path}/run_{no_it+2}/extr_data/data/data_cis.txt","r")
    cis4 = open(f"{path}/run_{no_it+3}/extr_data/data/data_cis.txt","r")
    cis5 = open(f"{path}/run_{no_it+4}/extr_data/data/data_cis.txt","r")
    cis6 = open(f"{path}/run_{no_it+5}/extr_data/data/data_cis.txt","r")
    cis7 = open(f"{path}/run_{no_it+6}/extr_data/data/data_cis.txt","r")
    cis8 = open(f"{path}/run_{no_it+7}/extr_data/data/data_cis.txt","r")
    cis9 = open(f"{path}/run_{no_it+8}/extr_data/data/data_cis.txt","r")
    cis10 = open(f"{path}/run_{no_it+9}/extr_data/data/data_cis.txt","r")
    cis11 = open(f"{path}/run_{no_it+10}/extr_data/data/data_cis.txt","r")
    cis12 = open(f"{path}/run_{no_it+11}/extr_data/data/data_cis.txt","r")
    cis13 = open(f"{path}/run_{no_it+12}/extr_data/data/data_cis.txt","r")
    cis14 = open(f"{path}/run_{no_it+13}/extr_data/data/data_cis.txt","r")
    cis15 = open(f"{path}/run_{no_it+14}/extr_data/data/data_cis.txt","r")
    cis16 = open(f"{path}/run_{no_it+15}/extr_data/data/data_cis.txt","r")
    cis17 = open(f"{path}/run_{no_it+16}/extr_data/data/data_cis.txt","r")
    cis18 = open(f"{path}/run_{no_it+17}/extr_data/data/data_cis.txt","r")
    cis19 = open(f"{path}/run_{no_it+18}/extr_data/data/data_cis.txt","r")
    cis20 = open(f"{path}/run_{no_it+19}/extr_data/data/data_cis.txt","r")
    cis21 = open(f"{path}/run_{no_it+20}/extr_data/data/data_cis.txt","r")
    cis22 = open(f"{path}/run_{no_it+21}/extr_data/data/data_cis.txt","r")
    cis23 = open(f"{path}/run_{no_it+22}/extr_data/data/data_cis.txt","r")
    cis24 = open(f"{path}/run_{no_it+23}/extr_data/data/data_cis.txt","r")
    cis25 = open(f"{path}/run_{no_it+24}/extr_data/data/data_cis.txt","r")
    cis26 = open(f"{path}/run_{no_it+25}/extr_data/data/data_cis.txt","r")
    cis27 = open(f"{path}/run_{no_it+26}/extr_data/data/data_cis.txt","r")
    cis28 = open(f"{path}/run_{no_it+27}/extr_data/data/data_cis.txt","r")
    cis29 = open(f"{path}/run_{no_it+28}/extr_data/data/data_cis.txt","r")
    cis30 = open(f"{path}/run_{no_it+29}/extr_data/data/data_cis.txt","r")

    # store the averaged values of val_cis in variable values = M(n,10)
    values = val_cis(cis1,cis2,cis3,cis4,cis5,cis6,cis7,cis8,cis9,cis10,cis11,cis12,cis13,cis14,cis15,cis16,cis17,cis18,cis19,cis20,cis21,cis22,cis23,cis24,cis25,cis26,cis27,cis28,cis29,cis30,sh_type,dg_dt,line)

    # Closure of the openned files
    cis1.close()
    cis2.close()
    cis3.close()
    cis4.close()
    cis5.close()
    cis6.close()
    cis7.close()
    cis8.close()
    cis9.close()
    cis10.close()
    cis11.close()
    cis12.close()
    cis13.close()
    cis14.close()
    cis15.close()
    cis16.close()
    cis17.close()
    cis18.close()
    cis19.close()
    cis20.close()
    cis21.close()
    cis22.close()
    cis23.close()
    cis24.close()
    cis25.close()
    cis26.close()
    cis27.close()
    cis28.close()
    cis29.close()
    cis30.close()
    return values # return matrix values = M(n,10)

# Function to open the 16 simulations files of elastic compression and averaged it in a variable
# Function need to be called 16 times with step = 1...16
def file_ela_comp_data(step,line_ela_comp,path):
    # Function variables
    # Scalar
    no_it = 1

    # Matrix
    file_ela_comp = np.zeros((line_ela_comp,6)) # matrix to store ela_comp averaged values

    ela_comp_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    file_ela_comp = val_ela_comp(ela_comp_1,ela_comp_2,ela_comp_3,ela_comp_4,ela_comp_5,ela_comp_6,ela_comp_7,ela_comp_8,ela_comp_9,ela_comp_10,ela_comp_11,ela_comp_12,ela_comp_13,ela_comp_14,ela_comp_15,ela_comp_16,ela_comp_17,ela_comp_18,ela_comp_19,ela_comp_20,ela_comp_21,ela_comp_22,ela_comp_23,ela_comp_24,ela_comp_25,ela_comp_26,ela_comp_27,ela_comp_28,ela_comp_29,ela_comp_30,line_ela_comp)

    # Closure of the files
    ela_comp_1.close()
    ela_comp_2.close()
    ela_comp_3.close()
    ela_comp_4.close()
    ela_comp_5.close()
    ela_comp_6.close()
    ela_comp_7.close()
    ela_comp_8.close()
    ela_comp_9.close()
    ela_comp_10.close()
    ela_comp_11.close()
    ela_comp_12.close()
    ela_comp_13.close()
    ela_comp_14.close()
    ela_comp_15.close()
    ela_comp_16.close()
    ela_comp_17.close()
    ela_comp_18.close()
    ela_comp_19.close()
    ela_comp_20.close()
    ela_comp_21.close()
    ela_comp_22.close()
    ela_comp_23.close()
    ela_comp_24.close()
    ela_comp_25.close()
    ela_comp_26.close()
    ela_comp_27.close()
    ela_comp_28.close()
    ela_comp_29.close()
    ela_comp_30.close()

    return file_ela_comp  # return matrix file_ela_comp = M(n,6) for the elastic simulation no = step

# Function to open the 16 simulation files of elastic cisression and averaged it in a variable
# Function need to be called 16 times with step = 1...16
def file_ela_cis_data(step,line_ela_cis,path):
    # Function variable #
    # Scalar
    no_it = 1

    # Matrix
    file_ela_cis = np.zeros((line_ela_cis,6)) # matrix to store ela_cis averaged values

    ela_cis_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    file_ela_cis = val_ela_cis(ela_cis_1,ela_cis_2,ela_cis_3,ela_cis_4,ela_cis_5,ela_cis_6,ela_cis_7,ela_cis_8,ela_cis_9,ela_cis_10,ela_cis_11,ela_cis_12,ela_cis_13,ela_cis_14,ela_cis_15,ela_cis_16,ela_cis_17,ela_cis_18,ela_cis_19,ela_cis_20,ela_cis_21,ela_cis_22,ela_cis_23,ela_cis_24,ela_cis_25,ela_cis_26,ela_cis_27,ela_cis_28,ela_cis_29,ela_cis_30,line_ela_cis)

    # Closure of the files
    ela_cis_1.close()
    ela_cis_2.close()
    ela_cis_3.close()
    ela_cis_4.close()
    ela_cis_5.close()
    ela_cis_6.close()
    ela_cis_7.close()
    ela_cis_8.close()
    ela_cis_9.close()
    ela_cis_10.close()
    ela_cis_11.close()
    ela_cis_12.close()
    ela_cis_13.close()
    ela_cis_14.close()
    ela_cis_15.close()
    ela_cis_16.close()
    ela_cis_17.close()
    ela_cis_18.close()
    ela_cis_19.close()
    ela_cis_20.close()
    ela_cis_21.close()
    ela_cis_22.close()
    ela_cis_23.close()
    ela_cis_24.close()
    ela_cis_25.close()
    ela_cis_26.close()
    ela_cis_27.close()
    ela_cis_28.close()
    ela_cis_29.close()
    ela_cis_30.close()
    return file_ela_cis  # return matrix file_ela_cis = M(n,6) for the elastic simulation no = step

## Data Analysis ##
def file_K_data(step,line_ela_comp,path,zoom):
    # Function variable #
    # Scalar
    no_it = 1
    module = 'bulk'

    # Vector
    K_ela = np.zeros(2) # matrix to store ela_comp averaged values

    ela_comp_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")
    ela_comp_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_ela_comp_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    K_ela = ela_mod_val(ela_comp_1,ela_comp_2,ela_comp_3,ela_comp_4,ela_comp_5,ela_comp_6,ela_comp_7,ela_comp_8,ela_comp_9,ela_comp_10,ela_comp_11,ela_comp_12,ela_comp_13,ela_comp_14,ela_comp_15,ela_comp_16,ela_comp_17,ela_comp_18,ela_comp_19,ela_comp_20,ela_comp_21,ela_comp_22,ela_comp_23,ela_comp_24,ela_comp_25,ela_comp_26,ela_comp_27,ela_comp_28,ela_comp_29,ela_comp_30,line_ela_comp,zoom,module)

    # Closure of the files
    ela_comp_1.close()
    ela_comp_2.close()
    ela_comp_3.close()
    ela_comp_4.close()
    ela_comp_5.close()
    ela_comp_6.close()
    ela_comp_7.close()
    ela_comp_8.close()
    ela_comp_9.close()
    ela_comp_10.close()
    ela_comp_11.close()
    ela_comp_12.close()
    ela_comp_13.close()
    ela_comp_14.close()
    ela_comp_15.close()
    ela_comp_16.close()
    ela_comp_17.close()
    ela_comp_18.close()
    ela_comp_19.close()
    ela_comp_20.close()
    ela_comp_21.close()
    ela_comp_22.close()
    ela_comp_23.close()
    ela_comp_24.close()
    ela_comp_25.close()
    ela_comp_26.close()
    ela_comp_27.close()
    ela_comp_28.close()
    ela_comp_29.close()
    ela_comp_30.close()
    return K_ela  # return a pure 2D compression "bulk" modulus + std

def file_G_data(step,line_ela_cis,dgdt,path,zoom):
    # Function variable #
    # Scalar
    no_it = 1
    module = 'shear'

    # Vector
    G_ela = np.zeros(2) # matrix to store ela_cis averaged values
    gamma = np.zeros(16) # vector to store the initial shear deformation of the restart files

    ela_cis_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    ela_cis_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    G_ela = ela_mod_val(ela_cis_1,ela_cis_2,ela_cis_3,ela_cis_4,ela_cis_5,ela_cis_6,ela_cis_7,ela_cis_8,ela_cis_9,ela_cis_10,ela_cis_11,ela_cis_12,ela_cis_13,ela_cis_14,ela_cis_15,ela_cis_16,ela_cis_17,ela_cis_18,ela_cis_19,ela_cis_20,ela_cis_21,ela_cis_22,ela_cis_23,ela_cis_24,ela_cis_25,ela_cis_26,ela_cis_27,ela_cis_28,ela_cis_29,ela_cis_30,line_ela_cis,zoom,module)

    # Extraction of the initial deformation
    ela_cis_1.close()
    ela_cis_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_cis_{step}.txt","r")
    gamma = restart_def(ela_cis_1,dgdt,step,line_ela_cis)

    # Closure of the files
    ela_cis_1.close()
    ela_cis_2.close()
    ela_cis_3.close()
    ela_cis_4.close()
    ela_cis_5.close()
    ela_cis_6.close()
    ela_cis_7.close()
    ela_cis_8.close()
    ela_cis_9.close()
    ela_cis_10.close()
    ela_cis_11.close()
    ela_cis_12.close()
    ela_cis_13.close()
    ela_cis_14.close()
    ela_cis_15.close()
    ela_cis_16.close()
    ela_cis_17.close()
    ela_cis_18.close()
    ela_cis_19.close()
    ela_cis_20.close()
    ela_cis_21.close()
    ela_cis_22.close()
    ela_cis_23.close()
    ela_cis_24.close()
    ela_cis_25.close()
    ela_cis_26.close()
    ela_cis_27.close()
    ela_cis_28.close()
    ela_cis_29.close()
    ela_cis_30.close()
    return G_ela, gamma # return shear modulus + std (1/2 => Makse et al, shear modulus in uniaxial test)

def file_d_ref_data(file,s_yy,ana,no_stack,max_stacks):
    # Function variable
    path = '/home/rigottia/Nextcloud/Documents/python/stack_files/ref_modulus'

    # Matrix
    mod = np.zeros((max_stacks,2))

    if file == 'shear':
        mod_val,dmod_val = open(f"{path}/{ana}/G0_{s_yy}.txt"), open(f"{path}/{ana}/dG0_{s_yy}.txt")
        mod_val.readline()
        dmod_val.readline()
    elif file == 'bulk':
        mod_val,dmod_val = open(f"{path}/{ana}/K0_{s_yy}.txt"), open(f"{path}/{ana}/dK0_{s_yy}.txt")
        mod_val.readline()
        dmod_val.readline()
    # end if
    mod[:,0] = np.loadtxt(mod_val)
    mod[:,1] = np.loadtxt(dmod_val)
    return mod[no_stack,0], mod[no_stack,1]

def file_d_data(step,line_ela_file,path,zoom,file):
    # Function variable #
    # Scalar
    no_it = 1
    N = 30 # number of stacks

    # string
    file_path = ''

    # Matrix
    mod = np.zeros((N,2))

    if file == 'shear':
        file_path = 'cis'
    if file == 'bulk':
        file_path = 'comp'
    # end if

    ela_file_1 = open(f"{path}/run_{no_it}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_2 = open(f"{path}/run_{no_it+1}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_3 = open(f"{path}/run_{no_it+2}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_4 = open(f"{path}/run_{no_it+3}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_5 = open(f"{path}/run_{no_it+4}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_6 = open(f"{path}/run_{no_it+5}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_7 = open(f"{path}/run_{no_it+6}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_8 = open(f"{path}/run_{no_it+7}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_9 = open(f"{path}/run_{no_it+8}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_10 = open(f"{path}/run_{no_it+9}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_11 = open(f"{path}/run_{no_it+10}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_12 = open(f"{path}/run_{no_it+11}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_13 = open(f"{path}/run_{no_it+12}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_14 = open(f"{path}/run_{no_it+13}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_15 = open(f"{path}/run_{no_it+14}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_16 = open(f"{path}/run_{no_it+15}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_17 = open(f"{path}/run_{no_it+16}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_18 = open(f"{path}/run_{no_it+17}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_19 = open(f"{path}/run_{no_it+18}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_20 = open(f"{path}/run_{no_it+19}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_21 = open(f"{path}/run_{no_it+20}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_22 = open(f"{path}/run_{no_it+21}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_23 = open(f"{path}/run_{no_it+22}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_24 = open(f"{path}/run_{no_it+23}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_25 = open(f"{path}/run_{no_it+24}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_26 = open(f"{path}/run_{no_it+25}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_27 = open(f"{path}/run_{no_it+26}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_28 = open(f"{path}/run_{no_it+27}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_29 = open(f"{path}/run_{no_it+28}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")
    ela_file_30 = open(f"{path}/run_{no_it+29}/extr_data/data_ela/data_ela_{step}/data_ela_{file_path}_{step}.txt","r")

    # Extraction of the values from the files for simulation N and store in a variable
    if file == 'shear':
        mod = ela_mod_val(ela_file_1,ela_file_2,ela_file_3,ela_file_4,ela_file_5,ela_file_6,ela_file_7,ela_file_8,ela_file_9,ela_file_10,ela_file_11,ela_file_12,ela_file_13,ela_file_14,ela_file_15,ela_file_16,ela_file_17,ela_file_18,ela_file_19,ela_file_20,ela_file_21,ela_file_22,ela_file_23,ela_file_24,ela_file_25,ela_file_26,ela_file_27,ela_file_28,ela_file_29,ela_file_30,line_ela_file,zoom,file)
    if file == 'bulk':
        mod = ela_mod_val(ela_file_1,ela_file_2,ela_file_3,ela_file_4,ela_file_5,ela_file_6,ela_file_7,ela_file_8,ela_file_9,ela_file_10,ela_file_11,ela_file_12,ela_file_13,ela_file_14,ela_file_15,ela_file_16,ela_file_17,ela_file_18,ela_file_19,ela_file_20,ela_file_21,ela_file_22,ela_file_23,ela_file_24,ela_file_25,ela_file_26,ela_file_27,ela_file_28,ela_file_29,ela_file_30,line_ela_file,zoom,file)

    # Closure of the files
    ela_file_1.close()
    ela_file_2.close()
    ela_file_3.close()
    ela_file_4.close()
    ela_file_5.close()
    ela_file_6.close()
    ela_file_7.close()
    ela_file_8.close()
    ela_file_9.close()
    ela_file_10.close()
    ela_file_11.close()
    ela_file_12.close()
    ela_file_13.close()
    ela_file_14.close()
    ela_file_15.close()
    ela_file_16.close()
    ela_file_17.close()
    ela_file_18.close()
    ela_file_19.close()
    ela_file_20.close()
    ela_file_21.close()
    ela_file_22.close()
    ela_file_23.close()
    ela_file_24.close()
    ela_file_25.close()
    ela_file_26.close()
    ela_file_27.close()
    ela_file_28.close()
    ela_file_29.close()
    ela_file_30.close()
    return mod[0], mod[1]  # return shear modulus + std (1/2 => Makse et al, shear modulus in uniaxial test)

def d_comp(nb_ela_file,line_ela_cis,path,press,analyse,file,num,lenght,zoom,ref):
    # Function variables
    # Matrix
    mod = np.zeros(nb_ela_file) # store the modulus
    dmod = np.zeros(nb_ela_file) # store the std modulus
    d = np.zeros((nb_ela_file,2)) # store damage

    # Computation
    if ref == 'idealise': ref, dref = file_d_ref_data(file,press,analyse,num-1,lenght)
    if ref == 'val_0': ref, dref = file_d_data(1,line_ela_cis,path,zoom,file)

    mod[0], dmod[0] = file_d_data(1,line_ela_cis,path,zoom,file)
    mod[1], dmod[1] = file_d_data(2,line_ela_cis,path,zoom,file)
    mod[2], dmod[2] = file_d_data(3,line_ela_cis,path,zoom,file)
    mod[3], dmod[3] = file_d_data(4,line_ela_cis,path,zoom,file)
    mod[4], dmod[4] = file_d_data(5,line_ela_cis,path,zoom,file)
    mod[5], dmod[5] = file_d_data(6,line_ela_cis,path,zoom,file)
    mod[6], dmod[6] = file_d_data(7,line_ela_cis,path,zoom,file)
    mod[7], dmod[7] = file_d_data(8,line_ela_cis,path,zoom,file)
    mod[8], dmod[8] = file_d_data(9,line_ela_cis,path,zoom,file)
    mod[9], dmod[9] = file_d_data(10,line_ela_cis,path,zoom,file)
    mod[10], dmod[10] = file_d_data(11,line_ela_cis,path,zoom,file)
    mod[11], dmod[11] = file_d_data(12,line_ela_cis,path,zoom,file)
    mod[12], dmod[12] = file_d_data(13,line_ela_cis,path,zoom,file)
    mod[13], dmod[13] = file_d_data(14,line_ela_cis,path,zoom,file)
    mod[14], dmod[14] = file_d_data(15,line_ela_cis,path,zoom,file)
    mod[15], dmod[15] = file_d_data(16,line_ela_cis,path,zoom,file)
    mod[16], dmod[16] = file_d_data(17,line_ela_cis,path,zoom,file)
    mod[17], dmod[17] = file_d_data(18,line_ela_cis,path,zoom,file)
    mod[18], dmod[18] = file_d_data(19,line_ela_cis,path,zoom,file)

    for i in range(nb_ela_file): # scan the nb_ela_file col
        d[i,0] = 1 - (mod[i]/ref)
    # end of i for loop

    # compute the std
    for i in range(nb_ela_file):
       d[i,1] = ((dmod[i]/mod[i]) + (dref/ref))*d[i,0]
    # end of i for loop
    return d

def d_stack(dam,d1,d2,d3,d4,d5,val):
    # Function variable
    # Scalar
    line = len(dam) # number of elastic files

    # Computation
    if val == 'damage': # stack the damage values
        j = 0
    elif val == 'std': # stack the damage std values
        j = 1
    # end if

    for i in range(line): # scan the 16 values of damage
            dam[i,0] = d1[i,j]
            dam[i,1] = d2[i,j]
            dam[i,2] = d3[i,j]
            dam[i,3] = d4[i,j]
            dam[i,4] = d5[i,j]
    # end of i for loop
    return dam

def ela_matrix(ela_1,ela_2,ela_3,ela_4,ela_5,ela_6,ela_7,ela_8,ela_9,ela_10,no_ela_file,matrix_type,no_stack):
    # Function variables
    #Matrix
    ela_mat = np.zeros((no_ela_file,no_stack))

    # Computation
    if matrix_type == 'elastic modulus':
        for i in range(no_ela_file):
            ela_mat[i,0] = ela_1[i,0]
            ela_mat[i,1] = ela_2[i,0]
            ela_mat[i,2] = ela_3[i,0]
            ela_mat[i,3] = ela_4[i,0]
            ela_mat[i,4] = ela_5[i,0]

            if no_stack > 5 :
                ela_mat[i,5] = ela_6[i,0]
                ela_mat[i,6] = ela_7[i,0]
                ela_mat[i,7] = ela_8[i,0]
                ela_mat[i,8] = ela_9[i,0]
                ela_mat[i,9] = ela_10[i,0]
        # end of i for loop
    elif matrix_type == 'std':
        for i in range(no_ela_file):
            ela_mat[i,0] = ela_1[i,1]
            ela_mat[i,1] = ela_2[i,1]
            ela_mat[i,2] = ela_3[i,1]
            ela_mat[i,3] = ela_4[i,1]
            ela_mat[i,4] = ela_5[i,1]

            if no_stack > 5 :
                ela_mat[i,5] = ela_6[i,1]
                ela_mat[i,6] = ela_7[i,1]
                ela_mat[i,7] = ela_8[i,1]
                ela_mat[i,8] = ela_9[i,1]
                ela_mat[i,9] = ela_10[i,1]
        # end of i for loop
    # end if
    return ela_mat

# Moving average tool #
def moving_average(val, window): # compute the moving average over a window "window" on a vector "val"
    return np.convolve(val, np.ones(window), 'valid') / window

# search the plateau of stress of the shearing test #
def sh_plt(data,G_ela,dG_ela,d_G1,d_G2,d_G3,d_G4,d_G5,d_K1,d_K2,d_K3,d_K4,d_K5,stack,no_ela,N):
    # Function variable #
    # Scalar
    window = 5 # window of value to investigate
    window_d = 3  # window of value to investigate damage
    error = 10 # maximum variability of the plateau of stress
    error_d = 0.05 # maximum variability of the plateau of damage
    line = len(data) # length of the data file

    # Vector
    plt = np.zeros(no_ela) # save all the variables values
    plt[8] = 4 # inital value of minimum coordination number
    # Computation #

    mean_sh = moving_average(data[:,0],window) # compute the moving average of the datas for shear stress
    std_sh = moving_average(data[:,1],window) # compute std moving average
    mean_p = moving_average(data[:,12],window) # compute the moving average of the datas for imposed pressure pressure
    std_p = moving_average(data[:,13],window) # compute std moving average
    mean_phi = moving_average(data[:,2],window) # compute the moving average of the datas for packing fraction
    std_phi = moving_average(data[:,3],window) # compute std moving average
    mean_z = moving_average(data[:,4],window) # compute the moving average of the datas for coordination number
    std_z = moving_average(data[:,5],window) # compute std moving average

    if stack >= 1 :
        mean_d_G1 = moving_average(d_G1[:,0],window_d) # compute the moving average of the datas for damage
        std_d_G1 = moving_average(d_G1[:,1],window_d) # compute std moving average

        mean_d_K1 = moving_average(d_K1[:,0],window_d) # compute the moving average of the datas for damage
        std_d_K1 = moving_average(d_K1[:,1],window_d) # compute std moving average

        for i in range(len(mean_d_G1)-1):
            if (abs(mean_d_G1[i]-mean_d_G1[i+1]) < error_d):
                plt[12] = mean_d_G1[i]
                plt[13] = std_d_G1[i]
            if (abs(mean_d_K1[i]-mean_d_K1[i+1]) < error_d):
                plt[14] = mean_d_K1[i]
                plt[15] = std_d_K1[i]
            # end if
        # end of for loop

    if stack >= 2 :
        mean_d_G2 = moving_average(d_G2[:,0],window_d) # compute the moving average of the datas for damage
        std_d_G2 = moving_average(d_G2[:,1],window_d) # compute std moving average

        mean_d_K2 = moving_average(d_K2[:,0],window_d) # compute the moving average of the datas for damage
        std_d_K2 = moving_average(d_K2[:,1],window_d) # compute std moving average

        for i in range(len(mean_d_G2)-1):
            if (abs(mean_d_G2[i]-mean_d_G2[i+1]) < error_d):
                plt[12] = mean_d_G2[i]
                plt[13] = std_d_G2[i]
            if (abs(mean_d_K2[i]-mean_d_K2[i+1]) < error_d):
                plt[14] = mean_d_K2[i]
                plt[15] = std_d_K2[i]
            # end if
        # end of for loop

    if stack >= 3 :
        mean_d_G3 = moving_average(d_G3[:,0],window_d) # compute the moving average of the datas for damage
        std_d_G3 = moving_average(d_G3[:,1],window_d) # compute std moving average

        mean_d_K3 = moving_average(d_K3[:,0],window_d) # compute the moving average of the datas for damage
        std_d_K3 = moving_average(d_K3[:,1],window_d) # compute std moving average

        for i in range(len(mean_d_G3)-1):
            if (abs(mean_d_G3[i]-mean_d_G3[i+1]) < error_d):
                plt[12] = mean_d_G3[i]
                plt[13] = std_d_G3[i]
            if (abs(mean_d_K3[i]-mean_d_K3[i+1]) < error_d):
                plt[14] = mean_d_K3[i]
                plt[15] = std_d_K3[i]
            # end if
        # end of for loop

    if stack >= 4 :
        mean_d_G4 = moving_average(d_G4[:,0],window_d) # compute the moving average of the datas for damage
        std_d_G4 = moving_average(d_G4[:,1],window_d) # compute std moving average

        mean_d_K4 = moving_average(d_K4[:,0],window_d) # compute the moving average of the datas for damage
        std_d_K4 = moving_average(d_K4[:,1],window_d) # compute std moving average

        for i in range(len(mean_d_G4)-1):
            if (abs(mean_d_G4[i]-mean_d_G4[i+1]) < error_d):
                plt[12] = mean_d_G4[i]
                plt[13] = std_d_G4[i]
            if (abs(mean_d_K4[i]-mean_d_K4[i+1]) < error_d):
                plt[14] = mean_d_K4[i]
                plt[15] = std_d_K4[i]
            # end if
        # end of for loop

    if stack >= 5 :
        mean_d_G5 = moving_average(d_G5[:,0],window_d) # compute the moving average of the datas for damage
        std_d_G5 = moving_average(d_G5[:,1],window_d) # compute std moving average

        mean_d_K5 = moving_average(d_K5[:,0],window_d) # compute the moving average of the datas for damage
        std_d_K5 = moving_average(d_K5[:,1],window_d) # compute std moving average

        for i in range(len(mean_d_G5)-1):
            if (abs(mean_d_G5[i]-mean_d_G5[i+1]) < error_d):
                plt[12] = mean_d_G5[i]
                plt[13] = std_d_G5[i]
            if (abs(mean_d_K5[i]-mean_d_K5[i+1]) < error_d):
                plt[14] = mean_d_K5[i]
                plt[15] = std_d_K5[i]
            # end if
        # end of for loop

    # Search plateau value
    for i in range(len(mean_sh)-1): # scan the lines of the vector
        if (abs(mean_sh[i] - mean_sh[i+1]) < error) : # if variation < error
            plt[0] = mean_sh[i] # save the value
            plt[1] = std_sh[i]
            plt[2] = mean_p[i]
            plt[3] = std_p[i]
            plt[4] = mean_phi[i]
            plt[5] = std_phi[i]
            plt[6] = mean_z[i]
            plt[7] = std_z[i]
        # end if
    # end of for loop

    for i in range(line): # search maximum of shear stress and minimum of coordination number

        if plt[8] > data[i,4]: # max of coordination number
            plt[8] = data[i,4]
            plt[9] = data[i,5]
        if plt[10] < data[i,0]: # max of shear stress
            plt[10] = data[i,0]
            plt[11] = data[i,1]
    # end of i for loop

    # if no value find, take the last value
    if (plt[0] == 0):
        plt[0] = data[line-1,0]
        plt[1] = data[line-1,1]
    if (plt[2] == 0):
        plt[2] = data[line-1,12]
        plt[3] = data[line-1,13]
    if (plt[4] == 0):
        plt[4] = data[line-1,2]
        plt[5] = data[line-1,3]
    if (plt[6] == 0):
        plt[6] = data[line-1,4]
        plt[7] = data[line-1,5]
    # end if
    return plt # return a scalar plt

# Simulations phasis search
def simu_phase(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,max_stack,no_line):
    # Function variable
    # Scalar
    search_lin = int(no_line/50) # search the end of linear regime
    search_pst_lin = int(no_line/10) # search the post linear regime
    search_stat = int(no_line/2) # search the begining of stationary regime

    err = 1E-3 # criterion
    count_pst_lin = 0
    count_stat = 0 # number of time the criterion is statisfied

    sxy_i = 0 # value index

    # iteration index
    n = search_pst_lin
    o = search_stat

    # Vector
    strain_lvl = np.array([0,2.5E-3,5E-3,7.5E-3,2.5E-2,5E-2,7.5E-2,1E-1,1.5E-1,2E-1,2.5E-1,3E-1,4E-1,5E-1,6E-1,7E-1,8E-1,9E-1,1])

    # stress overshoot search
    tau_max = np.zeros(max_stack) # max val record for stress overshoot search
    lin_idx = np.zeros(max_stack) # index of linear regime end
    pst_lin_idx = np.zeros(max_stack) # index of post linear regime end
    stat_idx = np.zeros(max_stack) # index of begining of stationary regime

    # Matrix
    r = np.zeros((3,max_stack))
    r_disc = np.zeros((3,max_stack))

    # Computation
    for k in range(max_stack):
        if k == 0 : val = val1
        if k == 1 : val = val2
        if k == 2 : val = val3
        if k == 3 : val = val4
        if k == 4 : val = val5
        if k == 5 : val = val6
        if k == 6 : val = val7
        if k == 7 : val = val8
        if k == 8 : val = val9
        if k == 9 : val = val10

        tau_max = val[:search_lin,sxy_i].max() # max value of shear stress
        for m in range(search_lin): # Search the end of linear regime
            if tau_max == val[m,sxy_i] : lin_idx[k] = m
        # end of i for loop

        while count_pst_lin > 1 and n > search_pst_lin :
            d_val = (abs(val[n-1,sxy_i] - val[n,sxy_i]))/val[n-1,sxy_i]
            if d_val < err:
                count_pst_lin =+1
            # end if
            n =+1
        pst_lin_idx[k] = n

        while count_stat > 1 and o > no_line:
            d_val = (abs(val[o-1,sxy_i] - val[o,sxy_i])/val[o-1,sxy_i])/val[o-1,sxy_i]
            if d_val < err :
                count_stat = + 1
            else :
                count_stat = 0
            # end if
            o =+ 1
        # end of while loop
        stat_idx[k] = o
    # end of k for loop

    r = np.array([lin_idx,pst_lin_idx,stat_idx])

    for i in range(3):
        for j in range(max_stack):
            r_disc[i,j] = int((r[i,j]/1000)*18)+1
            disc = r[i,j]/1000
            if r_disc[i,j] == r_disc[i-1,j] and i < 2 :
                r_disc[i,j] =+1
            else :
                for k in range(len(strain_lvl)):
                    if disc == strain_lvl[k]:
                        r_disc[i,j] = k
                    # end if
                # end of j for loop
            # end if
        # end of j for loop
    # end of i for loop
    return r, r_disc

def variable_matrix(val1,val2,val3,val4,val5,no_ela,stack,col,line,prep,s_imp,mod): # create a matrix to save evolution of phi at the shear strain level of elastics/relaxation simulation
    # Variable
    # Scalar
    j_4_sav = -1
    j_5_sav = -1

    if mod == 's_xy':
        save_it = 0
    if mod == 'std_s_xy':
        save_it = 1
    if mod == 'phi':
        save_it = 2
    if mod == 'std_phi':
        save_it = 3
    if mod == 'z':
        save_it = 4
    if mod == 'std_z':
        save_it = 5
    if mod == 'press':
        save_it = 10
    if mod == 'std_press':
        save_it = 11
    # end if

    # Vector
    def_val = [0,2,4,6,24,49,74,99,149,199,249,299,399,499,599,699,799,899,999]
    if prep == 'no_fric':
        if s_imp == 'P_90kPa': ratio = [1,1,1,0.95,0.41]
        elif s_imp == 'P_50kPa': ratio = [1,1,1,0.62,1]
        elif s_imp == 'P_5kPa': ratio = [1,1,1,1,0] # end if
    elif prep == 'fric': ratio = [1,1,1,1,0] # end if

    # Matrix
    var = np.zeros((no_ela,col))

    # Computation
    for i in range(no_ela): # scan the N lines of the variable file
        for j in range(stack):
            # compute the step to sav the value
            per = round(ratio[j]*def_val[i])

            # if the same value is taken for cut simulation then skip to next step
            if j+1 == 4 :
                if per == j_4_sav :
                    per = j_4_sav + 1
                    j_4_sav = per
                else :
                    j_4_sav = per
            elif j +1 == 5 :
                if per == j_5_sav :
                    per = j_5_sav + 1
                    j_5_sav = per
                else :
                    j_5_sav = per
                # end if
            # end if

            # value save
            if j == 0 :
                var[i,j] = val1[per,save_it]
            elif j == 1 :
                var[i,j] = val2[per,save_it]
            elif j == 2 :
                var[i,j] = val3[per,save_it]
            elif j == 3 :
                var[i,j] = val4[per,save_it]
            elif j == 4 :
                var[i,j] = val5[per,save_it]
            # end of if
            per = 0
    # end of i for loop
    return var

def adim_cis(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,analysis,s_adim):
    # Function variable
    # Scalar
    # Index
    no_idx = 4

    xy_idx = 0 # shear stress index
    std_xy_idx = 1 # shear stress index

    press_idx = 10 # pressure index
    std_press_idx = 11 # std pressure index

    yy_idx = 12 # yy stress index
    std_yy_idx = 13 # std yy stress index

    xx_idx = 14 # xx stress
    std_xx_idx = 15 # std xx stress

    # Vector
    idx = np.array([xy_idx,press_idx,yy_idx,xx_idx])
    idx_std = np.array([std_xy_idx,std_press_idx,std_yy_idx,std_xx_idx])

    # Computation
    for i in range(no_idx):
        # define the index to adimmension
        index = idx[i]
        d_index = idx_std[i]

        if analysis == 'strain':
            # mean value adimmensionnement
            val1[:,index] = val1[:,index]/s_adim
            val2[:,index] = val2[:,index]/s_adim
            val3[:,index] = val3[:,index]/s_adim
            val4[:,index] = val4[:,index]/s_adim
            val5[:,index] = val5[:,index]/s_adim
            val6[:,index] = val6[:,index]/s_adim
            val7[:,index] = val7[:,index]/s_adim
            val8[:,index] = val8[:,index]/s_adim
            val9[:,index] = val9[:,index]/s_adim
            val10[:,index] = val10[:,index]/s_adim

            # std value adimmensionnement
            val1[:,d_index] = val1[:,d_index]/s_adim
            val2[:,d_index] = val2[:,d_index]/s_adim
            val3[:,d_index] = val3[:,d_index]/s_adim
            val4[:,d_index] = val4[:,d_index]/s_adim
            val5[:,d_index] = val5[:,d_index]/s_adim
            val6[:,d_index] = val6[:,d_index]/s_adim
            val7[:,d_index] = val7[:,d_index]/s_adim
            val8[:,d_index] = val8[:,d_index]/s_adim
            val9[:,d_index] = val9[:,d_index]/s_adim
            val10[:,d_index] = val10[:,d_index]/s_adim

        elif analysis == 'pressure':
            # mean value adimmensionnement
            if index != yy_idx :
                val1[:,index] = val1[:,index]/val1[:,yy_idx]
                val2[:,index] = val2[:,index]/val2[:,yy_idx]
                val3[:,index] = val3[:,index]/val3[:,yy_idx]
                val4[:,index] = val4[:,index]/val4[:,yy_idx]
                val5[:,index] = val5[:,index]/val5[:,yy_idx]
                val6[:,index] = val6[:,index]/val6[:,yy_idx]
                val7[:,index] = val7[:,index]/val7[:,yy_idx]
                val8[:,index] = val8[:,index]/val8[:,yy_idx]
                val9[:,index] = val9[:,index]/val9[:,yy_idx]
                val10[:,index] = val10[:,index]/val10[:,yy_idx]

                # stds value adimmensionnement
                val1[:,d_index] = ((val1[:,d_index]/val1[:,index]) + (val1[:,std_yy_idx]/val1[:,yy_idx]))*(val1[:,index]/val1[:,yy_idx])
                val2[:,d_index] = ((val2[:,d_index]/val2[:,index]) + (val2[:,std_yy_idx]/val2[:,yy_idx]))*(val2[:,index]/val2[:,yy_idx])
                val3[:,d_index] = ((val3[:,d_index]/val3[:,index]) + (val3[:,std_yy_idx]/val3[:,yy_idx]))*(val3[:,index]/val3[:,yy_idx])
                val4[:,d_index] = ((val4[:,d_index]/val4[:,index]) + (val4[:,std_yy_idx]/val4[:,yy_idx]))*(val4[:,index]/val4[:,yy_idx])
                val5[:,d_index] = ((val5[:,d_index]/val5[:,index]) + (val5[:,std_yy_idx]/val5[:,yy_idx]))*(val5[:,index]/val5[:,yy_idx])
                val6[:,d_index] = ((val6[:,d_index]/val6[:,index]) + (val6[:,std_yy_idx]/val6[:,yy_idx]))*(val6[:,index]/val6[:,yy_idx])
                val7[:,d_index] = ((val7[:,d_index]/val7[:,index]) + (val7[:,std_yy_idx]/val7[:,yy_idx]))*(val7[:,index]/val7[:,yy_idx])
                val8[:,d_index] = ((val8[:,d_index]/val8[:,index]) + (val8[:,std_yy_idx]/val8[:,yy_idx]))*(val8[:,index]/val8[:,yy_idx])
                val9[:,d_index] = ((val9[:,d_index]/val9[:,index]) + (val9[:,std_yy_idx]/val9[:,yy_idx]))*(val9[:,index]/val9[:,yy_idx])
                val10[:,d_index] = ((val10[:,d_index]/val10[:,index]) + (val10[:,std_yy_idx]/val10[:,yy_idx]))*(val10[:,index]/val10[:,yy_idx])
            # end if
        # end
        if analysis == 'pressure':
            # mean value adimmensionnement
            val1[:,yy_idx] = val1[:,yy_idx]/val1[:,yy_idx]
            val2[:,yy_idx] = val2[:,yy_idx]/val2[:,yy_idx]
            val3[:,yy_idx] = val3[:,yy_idx]/val3[:,yy_idx]
            val4[:,yy_idx] = val4[:,yy_idx]/val4[:,yy_idx]
            val5[:,yy_idx] = val5[:,yy_idx]/val5[:,yy_idx]
            val6[:,yy_idx] = val6[:,yy_idx]/val6[:,yy_idx]
            val7[:,yy_idx] = val7[:,yy_idx]/val7[:,yy_idx]
            val8[:,yy_idx] = val8[:,yy_idx]/val8[:,yy_idx]
            val9[:,yy_idx] = val9[:,yy_idx]/val9[:,yy_idx]
            val10[:,yy_idx] = val10[:,yy_idx]/val10[:,yy_idx]

            # stds value adimmensionnement
            val1[:,d_yy_idx] = ((val1[:,d_yy_idx]/val1[:,yy_idx]))
            val2[:,d_yy_idx] = ((val2[:,d_yy_idx]/val2[:,yy_idx]))
            val3[:,d_yy_idx] = ((val3[:,d_yy_idx]/val3[:,yy_idx]))
            val4[:,d_yy_idx] = ((val4[:,d_yy_idx]/val4[:,yy_idx]))
            val5[:,d_yy_idx] = ((val5[:,d_yy_idx]/val5[:,yy_idx]))
            val6[:,d_yy_idx] = ((val6[:,d_yy_idx]/val6[:,yy_idx]))
            val7[:,d_yy_idx] = ((val7[:,d_yy_idx]/val7[:,yy_idx]))
            val8[:,d_yy_idx] = ((val8[:,d_yy_idx]/val8[:,yy_idx]))
            val9[:,d_yy_idx] = ((val9[:,d_yy_idx]/val9[:,yy_idx]))
            val10[:,d_yy_idx] = ((val10[:,d_yy_idx]/val10[:,yy_idx]))
    # end of i for loop
    return val1,val2,val3,val4,val5,val6,val7,val8,val9,val10

def adim_ela(mod,dmod,cis1,cis2,cis3,cis4,cis5,cis6,cis7,cis8,cis9,cis10,stack,analysis,s_adim,val_type,no_val):
    # Function variable
    # Scalar
    yy_idx = 12

    len_vec = 19 # length of the values matrix
    adim = np.zeros((len_vec,no_val))
    val_adim = np.zeros((len_vec,no_val))
    # Vector
    if no_val == 5 :
        cis = np.array([cis1[0,yy_idx],cis2[0,yy_idx],cis3[0,yy_idx],cis4[0,yy_idx],cis5[0,yy_idx]])
        d_cis = np.array([cis1[0,yy_idx+1],cis2[0,yy_idx+1],cis3[0,yy_idx+1],cis4[0,yy_idx+1],cis5[0,yy_idx+1]])
    else :
        cis = np.array([cis1[0,yy_idx],cis2[0,yy_idx],cis3[0,yy_idx],cis4[0,yy_idx],cis5[0,yy_idx],cis6[0,yy_idx],cis7[0,yy_idx],cis8[0,yy_idx],cis9[0,yy_idx],cis10[0,yy_idx]])
        d_cis = np.array([cis1[0,yy_idx+1],cis2[0,yy_idx+1],cis3[0,yy_idx+1],cis4[0,yy_idx+1],cis5[0,yy_idx+1],cis6[0,yy_idx+1],cis7[0,yy_idx+1],cis8[0,yy_idx+1],cis9[0,yy_idx+1],cis10[0,yy_idx+1]])
    # end if

    # Computation
    for i in range(len_vec):
        for j in range(no_val):
            if analysis == 'strain':
                adim[i,j] = s_adim
            # end if

            elif analysis == 'pressure':
                if val_type == 'ela':
                    if cis[j] != 0:
                        adim[i,j] = cis[j]
                    else :
                        adim[i,j] = 1
                    # end if

                elif val_type == 'std':
                    if cis[j] != 0 :
                        adim[i,j] = ((dmod[i,j]/mod[i,j]) + (d_cis[j]/cis[j]))*(mod[i,j]/cis[j])
                    else :
                        adim[i,j] = 1
                    # end if
                # end if
            # end if
        # end of j for loop
    # end of i for loop

    for i in range(no_val):
        if val_type == 'ela':
            val_adim[:,i] = mod[:,i]/adim[:,i]
        elif val_type == 'std':
            if analysis == 'strain':
                val_adim[:,i] = dmod[:,i]/adim[:,i]
            else :
                val_adim[:,i] = adim[:,i]
        # end if
    # end of i for loop
    return val_adim
# End