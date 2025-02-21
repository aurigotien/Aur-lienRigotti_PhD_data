import matplotlib.pyplot as plt
import numpy as np

## Fonctions ##

def hysteresis(xval,yval,i): # compute hysteresis of a cycle
    # Function variable
    # Scalar
    it_cycle = 10 # number of step per cycle

    # hysteresis variable
    h = 0 # hysteresis value
    ar_norm = 0 # value of the ref area
    ar_cycle = 0 # area of the hysteresis loop
    h_1 = 0 # first half of the cycle
    h_2 = 0 # second half of the cycle

    T_max = 0 # max of the cycle
    T_min = 0 # min of the cycle
    g_max = 0 # max of the cycle
    g_min = 0 # min of the cycle

    # search min and max of strain
    it_min = 0
    it_max = 0

    # Vector
    xval_cycle = xval[i*it_cycle:(i*it_cycle)+it_cycle]
    yval_cycle = yval[i*it_cycle:(i*it_cycle)+it_cycle]

    # max and min of strain (shear of volumetric)
    g_max = max(xval_cycle)
    g_min = min(xval_cycle)

    # computation
    for k in range(it_cycle):
        if xval_cycle[k] == g_min :
            it_min = k
        if xval_cycle[k] == g_max :
            it_max = k
        # end if
    # end of k for loop

    # stress of the min and max of strain
    T_max = yval_cycle[it_max]
    T_min = yval_cycle[it_min]

    """
    plt.scatter(xval[i*it_cycle:(i*it_cycle)+it_cycle],yval[i*it_cycle:(i*it_cycle)+it_cycle])
    plt.plot(xval[i*it_cycle:(i*it_cycle)+it_cycle],yval[i*it_cycle:(i*it_cycle)+it_cycle])
    plt.scatter(g_min,T_min,color = 'r')
    plt.scatter(g_max,T_max, color = 'r')
    plt.show()
    input()
    #"""

    for j in range((i*it_cycle),(i*it_cycle)+(it_cycle),1):
        ar_cycle = ar_cycle + (min(yval[j+1],yval[j])*(xval[j]-xval[j+1]) + 0.5*(max(yval[j+1],yval[j])-min(yval[j],yval[j+1]))*(xval[j+1]-xval[j]))
    # end of j for lop

    ar_norm = min(T_min,T_max)*(g_max-g_min) + (0.5*max(T_min,T_max)*(g_max-g_min))
    #ar_cycle = abs(h_1 - h_2)

    h = ar_cycle / ar_norm

    # value of hysteresis
    return h

def data_ela_read(data1,data2,data3,data4,data5,data6):
    data1.readline()
    val1 = np.loadtxt(data1)

    data2.readline()
    val2 = np.loadtxt(data2)

    data3.readline()
    val3 = np.loadtxt(data3)

    data4.readline()
    val4 = np.loadtxt(data4)

    data5.readline()
    val5 = np.loadtxt(data5)

    data6.readline()
    val6 = np.loadtxt(data6)
    return val1,val2,val3,val4,val5,val6

def plot_traitement(x_val,y_val,g_color,g_label,x_label,y_label): # plot function
    # size of the graphs
    graph_len = 10
    graph_wid = 6
    font_title = 20
    font_axes = 16
    font_legend = 12
    label_space = 0.5
    linew = 1

    plt.figure(figsize= (graph_len,graph_wid))

    plt.plot(x_val, y_val, color = g_color, label = g_label, linewidth = linew) # creare the plot

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.xlabel(x_label, fontsize = font_title) # x label
    plt.ylabel(y_label, fontsize = font_title) # y label
    plt.legend(fontsize = font_legend, frameon=False, loc = 'upper right', labelspacing = label_space)
    plt.show()
    return

def plot_ela_traitement(x_val,y_val,g_color,g_label,x_label,y_label,ela_num): # plot function ela /!\ g_color = vector
    # size of the graphs
    graph_len = 10
    graph_wid = 6
    font_title = 20
    font_axes = 16
    font_legend = 12
    label_space = 0.5
    linew = 1

    if ela_num == 1:
        plt.figure(figsize= (graph_len,graph_wid))
    # end if

    plt.plot(x_val, y_val, color = g_label[ela_num], label = g_label, linewidth = linew) # creare the plot

    if ela_num == 19:
        plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
        plt.rc('xtick', labelsize = font_axes)
        plt.rc('ytick', labelsize = font_axes)

        plt.xlabel(x_label, fontsize = font_title) # x label
        plt.ylabel(y_label, fontsize = font_title) # y label
        plt.legend(fontsize = font_legend, frameon=False, loc = 'upper right', labelspacing = label_space)
    # end if
    return

def graph_comp(data): # plot for the compression step

    # read line
    data.readline() # read data file line by line
    valeur = np.loadtxt(data) # data of the line into the variable 'valeur'

    # variable initilisation
    time_step = 1E-3
    time = (valeur[:,0] - valeur[0,0])*time_step # absciss of the curve
    vol = (valeur[:,4]*valeur[:,5]) # computation of the volume (1/packing fraction)

    # Plot graph #
    # Coordination number
    plot_traitement(time,valeur[:,2],'black','','t (s)','$Z_{comp}$')
    #plt.savefig('comp_z_vs_time.png') # save the plot into a file

    # Packing fraction
    plot_traitement(time,valeur[:,3],'black','','t (s)','$\u03d5_{comp}$')
    #plt.savefig('comp_dens_vs_time.png')

    # Evolution of the stress P
    plot_traitement(time,valeur[:,9]/vol[:],'red','','t (s)','$P_{comp}$ (Pa)')

    # Evolution of S_xy
    plot_traitement(time,valeur[:,8]/vol[:],'red','','t (s)','$\u03c4_{comp}$ (Pa)')
    return

def graph_relax(data): # plot for the compression step

    # read file
    data.readline() # read data file line by line
    valeur = np.loadtxt(data) # data of the line into the variable 'valeur'

    # variable initialisation
    time_step = 1E-3
    time = (valeur[:,0] - valeur[0,0])*time_step/2 # absciss of the curve
    vol = (valeur[:,8]*valeur[:,9]) # computation of the volume (1/packing fraction)

    time_step = 1E-3
    time = (valeur[:,0] - valeur[0,0])*time_step # absciss of the curve
    vol = (valeur[:,4]*valeur[:,5]) # computation of the volume (1/packing fraction)

    # Plot graph
    # Coordination number
    plot_traitement(time,valeur[:,2],'black','','t (s)','$Z_{relax}$')
    #plt.savefig('comp_z_vs_time.png') # save the plot into a file

    # Packing fraction
    plot_traitement(time,valeur[:,3],'black','','t (s)','$\u03d5_{relax}$')
    #plt.savefig('comp_dens_vs_time.png')

    # Evolution of the stress P
    plot_traitement(time,valeur[:,9]/vol[:],'red','','t (s)','$P_{relax}$ (Pa)')

    # Evolution of S_xy
    plot_traitement(time,valeur[:,8]/vol[:],'red','','t (s)','$\u03c4_{relax}$ (Pa)')
    return

def graph_cis(data): # plot for the shearing step

     # read data
    data.readline()
    valeur = np.loadtxt(data)

    # Variable computation
    vol = (valeur[:,4]*valeur[:,5]) # computation of the volume (1/packing fraction)
    cis = np.tan(((90 - valeur[:,6])*np.pi)/180) # imposed shear strain E_xy

    # Plot graph
    # Coordination number
    plot_traitement(cis,valeur[:,2],'black','','\u03b3','$Z_{sh}$')

    # Packing fraction
    plot_traitement(cis,valeur[:,3],'black','','\u03b3','$\u03d5_{sh}$')

    # Evolution of the stress P
    plot_traitement(cis,abs((valeur[:,7]+valeur[:,8])/(2*vol[:])),'red','','\u03b3','$P_{sh}$ (Pa)')

    # Evolution of S_xy
    plot_traitement(cis,valeur[:,9]/vol[:],'red','','\u03b3','$\u03c4_{sh}$ (Pa)')

    print('\n Initial state \n')
    print('$\u03c3_{yy}$ = ', valeur[0,8]/vol[0])
    print('$\u03c3_{xy}$ = ', valeur[0,9]/vol[0])
    print('P = ', (valeur[0,7]+valeur[0,8])/vol[0])
    print('Z = ', valeur[0,2])
    print('\u03d5 = ', valeur[0,3])
    return

def graph_ela_comp(data1,data3,data5,data8,data11,data19): # plot for the elastic compression

    # read data
    valeur1,valeur2,valeur3,valeur4,valeur5,valeur6 = data_ela_read(data1,data3,data5,data8,data11,data19)

    # Variable initialisation
    # Scalar
    len_vec = len(valeur1)
    no_valeur = 6
    no_cycle = 40
    time_step = 1E-6

    # Vector
    cycle = np.zeros(no_cycle)
    color = plt.get_cmap('jet')

    # Matrix
    time = np.zeros((len_vec,no_valeur))
    vol = np.zeros((len_vec,no_valeur))
    defo = np.zeros((len_vec,no_valeur))
    h = np.zeros((no_cycle,no_valeur))

    # time matrix computation
    time[:,0] = (valeur1[:,0] - valeur1[0,0])*time_step
    time[:,1] = (valeur2[:,0] - valeur2[0,0])*time_step
    time[:,2] = (valeur3[:,0] - valeur3[0,0])*time_step
    time[:,3] = (valeur4[:,0] - valeur4[0,0])*time_step
    time[:,4] = (valeur5[:,0] - valeur5[0,0])*time_step
    time[:,5] = (valeur6[:,0] - valeur6[0,0])*time_step

    # vol matrix computation
    vol[:,0] = valeur1[:,4]*valeur1[:,5]
    vol[:,1] = valeur2[:,4]*valeur2[:,5]
    vol[:,2] = valeur3[:,4]*valeur3[:,5]
    vol[:,3] = valeur4[:,4]*valeur4[:,5]
    vol[:,4] = valeur5[:,4]*valeur5[:,5]
    vol[:,5] = valeur6[:,4]*valeur5[:,5]

    # defo matrix computation
    for i in range(no_valeur):
        defo[:,i] = ((vol[0,i] - vol[:,i]) / (vol[0,i]))

    # Initialisation depending on the number of stacks #
    # Hystersis evolution
    for i in range(no_cycle):
        for j in range(no_valeur):
            if j == 0:
                valeur = valeur1
            elif j == 1 :
                valeur = valeur2
            elif j == 2 :
                valeur = valeur3
            elif j == 3 :
                valeur = valeur4
            elif j == 4 :
                valeur = valeur5
            elif j == 5 :
                valeur = valeur6
            # end if
            cycle[i] = i
            h[i,j] = hysteresis(defo[i,j],valeur[:,9]/vol[:,j],i)
    # end of i for loop

    # Imposed volumetric deformation
    for i in range(no_valeur):
        plot_ela_traitement(time[:,i],defo[:,i],color[i/no_valeur],'','t (s)','$\u03b5_{vol}$',i+1)
    # end of i for loop

    # Mean stress vs volumetric defo
    for i in range(no_valeur):
        plot_ela_traitement(defo[:]/defo[0],abs(valeur[:,9]/vol[:]),color[i/no_valeur],'','$\u03b5_{vol}$/$\u03b5_{vol,0}$','P',i+1)
    # end of i for loop

    # Hysteresis
    for i in range(no_valeur):
        plot_ela_traitement(cycle,h,color[i/no_valeur],'','$N_{cycle}$','h',i+1)
    # end of i for loop
    return

def graph_ela_cis(data1,data2,data3,data4,data5,data6): # plot for the elastic shearing

    # read data
    valeur1,valeur2,valeur3,valeur4,valeur5,valeur6 = data_ela_read(data1,data2,data3,data4,data5,data6)

    # Variables
    len_vec = len(valeur1)
    no_valeur = 6
    no_cycle = 40
    time_step = 1E-6
    gamma_f = 0.3 # final deformation

    # Vector
    cycle = np.zeros(no_cycle)
    colormap = plt.get_cmap('jet')

    # Matrix
    time = np.zeros((len_vec,no_valeur))
    vol = np.zeros((len_vec,no_valeur))
    defo = np.zeros((len_vec,no_valeur))
    h = np.zeros((no_cycle,no_valeur))

    # time matrix computation
    time[:,0] = (valeur1[:,0] - valeur1[0,0])*time_step
    time[:,1] = (valeur2[:,0] - valeur2[0,0])*time_step
    time[:,2] = (valeur3[:,0] - valeur3[0,0])*time_step
    time[:,3] = (valeur4[:,0] - valeur4[0,0])*time_step
    time[:,4] = (valeur5[:,0] - valeur5[0,0])*time_step
    time[:,5] = (valeur6[:,0] - valeur6[0,0])*time_step

    # vol matrix computation
    vol[:,0] = valeur1[:,4]*valeur1[:,5]
    vol[:,1] = valeur2[:,4]*valeur2[:,5]
    vol[:,2] = valeur3[:,4]*valeur3[:,5]
    vol[:,3] = valeur4[:,4]*valeur4[:,5]
    vol[:,4] = valeur5[:,4]*valeur5[:,5]
    vol[:,5] = valeur6[:,4]*valeur5[:,5]

    # deformation matrix computation
    defo[:,0] = np.tan(((90 - valeur1[:,6])*np.pi)/180) # imposed shear strain E_xy
    defo[:,1] = np.tan(((90 - valeur2[:,6])*np.pi)/180) # imposed shear strain E_xy
    defo[:,2] = np.tan(((90 - valeur3[:,6])*np.pi)/180) # imposed shear strain E_xy
    defo[:,3] = np.tan(((90 - valeur4[:,6])*np.pi)/180) # imposed shear strain E_xy
    defo[:,4] = np.tan(((90 - valeur5[:,6])*np.pi)/180) # imposed shear strain E_xy
    defo[:,5] = np.tan(((90 - valeur6[:,6])*np.pi)/180) # imposed shear strain E_xy

    # Initialisation depending on the number of stacks #
    # Hystersis evolution
    for i in range(no_cycle):
        for j in range(no_valeur):
            if j == 0:
                valeur = valeur1
            elif j == 1 :
                valeur = valeur2
            elif j == 2 :
                valeur = valeur3
            elif j == 3 :
                valeur = valeur4
            elif j == 4 :
                valeur = valeur5
            elif j == 5 :
                valeur = valeur6
            # end if
            cycle[i] = i
            h[i,j] = hysteresis(defo[i,j],valeur[:,9]/vol[:],i)
    # end of i for loop

    # Imposed volumetric deformation
    for i in range(no_valeur):
        plot_ela_traitement(time[:,i],defo[:,i],colormap[i/no_valeur],'','t (s)','$\u03b5_{vol}$',i+1)
    # end of i for loop

    # Shear stress vs shear defo
    for i in range(no_valeur):
        plot_ela_traitement((defo[:]/defo[0])/gamma_f,abs(valeur[:,9]/vol[:]),colormap[i/no_valeur],'','(\u03b3 - $\u03b3_{0}$)/ $\u03b3_{f}$','$\u03c4$',i+1)
    # end of i for loop

    # Hysteresis
    for i in range(no_valeur):
        plot_ela_traitement(cycle,h,colormap[i/no_valeur],'','$N_{cycle}$','h',i+1)
    # end of i for loop
    return

def graph_ela_relax(data1,data2,data3,data4,data5,data6): # plot the evolution of stress during the relaxations
    # Function variables #
    # Read the files
    valeur1,valeur2,valeur3,valeur4,valeur5,valeur6 = data_ela_read(data1,data2,data3,data4,data5,data6)

    # Scalar
    dt = 1E-4 # time discretization
    dN = 10000 # increment of step
    no_valeur = 6 # number of relaxation values
    len_val = len(valeur1)

    # Colors
    colormap = plt.get_cmap('gnuplot')

    # Vector
    time = np.zeros(len_val) # vector of the time of the simulation
    tag = ['0 % simulation','5 % simulation','10 % simulation','25 % simulation','50 % simulation','100 % simulation']

    # Matrix
    vol = np.zeros((len_val,no_valeur))
    val = np.zeros((len_val,no_valeur))
    press = np.zeros((len_val,no_valeur))

    # Computation of the datas to plot them
    # Compute volume
    vol[:,0] = valeur1[:,4]*valeur1[:,5]
    vol[:,1] = valeur2[:,4]*valeur2[:,5]
    vol[:,2] = valeur3[:,4]*valeur3[:,5]
    vol[:,3] = valeur4[:,4]*valeur4[:,5]
    vol[:,4] = valeur5[:,4]*valeur5[:,5]
    vol[:,5] = valeur6[:,4]*valeur6[:,5]

    # Compute shear stress
    val[:,0] = valeur1[:,9]/vol[:,0]
    val[:,1] = valeur2[:,9]/vol[:,1]
    val[:,3] = valeur3[:,9]/vol[:,2]
    val[:,4] = valeur4[:,9]/vol[:,3]
    val[:,5] = valeur5[:,9]/vol[:,4]
    val[:,6] = valeur6[:,9]/vol[:,5]

    # Compute mean stress
    press[:,0] = -(((valeur1[:,7]+valeur1[:,8])/2)/vol[:,3])
    press[:,1] = -(((valeur2[:,7]+valeur2[:,8])/2)/vol[:,3])
    press[:,2] = -(((valeur3[:,7]+valeur3[:,8])/2)/vol[:,3])
    press[:,3] = -(((valeur4[:,7]+valeur4[:,8])/2)/vol[:,3])
    press[:,4] = -(((valeur5[:,7]+valeur5[:,8])/2)/vol[:,3])
    press[:,5] = -(((valeur6[:,7]+valeur6[:,8])/2)/vol[:,3])

    # time set
    for i in range(len_val):
        time[i] = i*dt*dN
    # end of for

    # Plot #
    # Measured shear stress relaxation without plateau
    for i in range(no_valeur):
        plot_ela_traitement(time[:],val[:,i],colormap[i/no_valeur],tag[i],'t (s)','$\u03c4$',i+1)
    # end of i for loop

    # Pressure evolution
    for i in range(no_valeur):
        plot_ela_traitement(time[:],press[:,i],colormap[i/no_valeur],tag[i],'t (s)','$\u03c4$',i+1)
    # end of i for loop
    return

def graph_call(compression,relaxation,cisaillement):
    graph_comp(compression)
    graph_relax(relaxation)
    graph_cis(cisaillement)
    return

def graph_call_ela(ela_comp_1,ela_comp_2,ela_comp_3,ela_comp_4,ela_comp_5,ela_comp_6,ela_cis_1,ela_cis_2,ela_cis_3,ela_cis_4,ela_cis_5,ela_cis_6):
    graph_ela_comp(ela_comp_1,ela_comp_2,ela_comp_3,ela_comp_4,ela_comp_5,ela_comp_6)
    graph_ela_cis(ela_cis_1,ela_cis_2,ela_cis_3,ela_cis_4,ela_cis_5,ela_cis_6)
    return