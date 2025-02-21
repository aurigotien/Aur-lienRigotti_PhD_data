import matplotlib.pyplot as plt
import numpy as np
import operator as op
import scipy.optimize as sc

# fit function
def linear_fit(x_val,A,B):
    return A*x_val + B

# Treatement functions
def root_mean_square(ref,val): # compute the rms between value and ref
    # Variable
    # Scalar
    val_sum = 0 # sum of (ref - val)^2

    for i in range(len(ref)):
        val_sum = val_sum + (val[i] - ref[i])**2
    # end of i for loop
    rms = val_sum**0.5
    return rms

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

    for j in range((i*it_cycle),(i*it_cycle)+(it_cycle),1):
        ar_cycle = ar_cycle + (min(yval[j+1],yval[j])*(xval[j]-xval[j+1]) + 0.5*(max(yval[j+1],yval[j])-min(yval[j],yval[j+1]))*(xval[j+1]-xval[j]))
    # end of j for lop

    ar_norm = min(T_min,T_max)*(g_max-g_min) + (0.5*max(T_min,T_max)*(g_max-g_min))
    #ar_cycle = abs(h_1 - h_2)

    h = ar_cycle / ar_norm

    # value of hysteresis
    return h

def sort_mat(xval,yval,yerr,stack): # sort yval and xval as function of xval
    # Sort xval and yval
    for k in range(stack):
        mod_valx,mod_valy,mod_err = xval[:,k],yval[:,k],yerr[:,k]
        sort = sorted(zip(mod_valx,mod_valy,mod_err), key=op.itemgetter(0))
        xval[:,k], yval[:,k], yerr[:,k] = zip(*sort)
    # end of k for loop
    return xval, yval, yerr

# Function for data extraction
def val_var_prep(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,val_var,E,t):
    # Variables
    # Scalar
    no_val = 10 # max number of stacks
    len_val = len(val1)

    if val_var == 'std':
        t_i = 10
        p_i = 1
        sh_i = 9
        phi_i = 3
        z_i = 5
    else :
        t_i = 10
        p_i = 0
        sh_i = 8
        phi_i = 2
        z_i = 4

    # Matrix
    time = np.zeros((len_val,no_val))
    press = np.zeros((len_val,no_val))
    cis = np.zeros((len_val,no_val))
    phi = np.zeros((len_val,no_val))
    Z = np.zeros((len_val,no_val))

    # Value attribution
    if stack >= 1:
        time[:,0] = val1[:,t_i]/t
        press[:,0] = abs(val1[:,p_i]/E)
        cis[:,0] = abs(val1[:,sh_i]/E)
        phi[:,0] = val1[:,phi_i]
        Z[:,0] = val1[:,z_i]
    if stack >= 2:
        time[:,1] = val2[:,t_i]/t
        press[:,1] = abs(val2[:,p_i]/E)
        cis[:,1] = abs(val2[:,sh_i]/E)
        phi[:,1] = val2[:,phi_i]
        Z[:,1] = val2[:,z_i]
    if stack >= 3:
        time[:,2] = val3[:,t_i]/t
        press[:,2] = abs(val3[:,p_i]/E)
        cis[:,2] = abs(val3[:,sh_i]/E)
        phi[:,2] = val3[:,phi_i]
        Z[:,2] = val3[:,z_i]
    if stack >= 4:
        time[:,3] = val4[:,t_i]/t
        press[:,3] = abs(val4[:,p_i]/E)
        cis[:,3] = abs(val4[:,sh_i]/E)
        phi[:,3] = val4[:,phi_i]
        Z[:,3] = val4[:,z_i]
    if stack >= 5:
        time[:,4] = val5[:,t_i]/t
        press[:,4] = abs(val5[:,p_i]/E)
        cis[:,4] = abs(val5[:,sh_i]/E)
        phi[:,4] = val5[:,phi_i]
        Z[:,4] = val5[:,z_i]
    if stack >= 6:
        time[:,5] = val6[:,t_i]/t
        press[:,5] = abs(val6[:,p_i]/E)
        cis[:,5] = abs(val6[:,sh_i]/E)
        phi[:,5] = val6[:,phi_i]
        Z[:,5] = val6[:,z_i]
    if stack >= 7:
        time[:,6] = val7[:,t_i]/t
        press[:,6] = abs(val7[:,p_i]/E)
        cis[:,6] = abs(val7[:,sh_i]/E)
        phi[:,6] = val7[:,phi_i]
        Z[:,6] = val7[:,z_i]
    if stack >= 8:
        time[:,7] = val8[:,t_i]/t
        press[:,7] = abs(val8[:,p_i]/E)
        cis[:,7] = abs(val8[:,sh_i]/E)
        phi[:,7] = val8[:,phi_i]
        Z[:,7] = val8[:,z_i]
    if stack >= 9:
        time[:,8] = val9[:,t_i]/t
        press[:,8] = abs(val9[:,p_i]/E)
        cis[:,8] = abs(val9[:,sh_i]/E)
        phi[:,8] = val9[:,phi_i]
        Z[:,8] = val9[:,z_i]
    if stack >= 10:
        time[:,9] = val10[:,t_i]/t
        press[:,9] = abs(val10[:,p_i]/E)
        cis[:,9] = abs(val10[:,sh_i]/E)
        phi[:,9] = val10[:,phi_i]
        Z[:,9] = val10[:,z_i]
    # end if
    return time,press,cis,phi,Z

def val_var_sh(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,val_var,t):
    # Variables
    # Scalar
    # index
    if val_var != 'std':
        sxy_i = 0
        phi_i = 2
        z_i = 4
        vol_i = 6
        cis_i = 8
        p_i = 10
        sy_i = 12
        sx_i = 14
        eq_i = 16
    else :
        sxy_i = 1
        phi_i = 3
        z_i = 5
        vol_i = 7
        cis_i = 9
        p_i = 11
        sy_i = 13
        sx_i = 15
        eq_i = 17
    # end if

    # dimmension variable
    no_val = 10 # max number of stacks
    len_val = len(val1)

    # Matrix
    press = np.zeros((len_val,no_val))
    S_xx = np.zeros((len_val,no_val))
    S_yy = np.zeros((len_val,no_val))
    S_xy = np.zeros((len_val,no_val))
    cis = np.zeros((len_val,no_val))
    e_vol = np.zeros((len_val,no_val))
    phi = np.zeros((len_val,no_val))
    Z = np.zeros((len_val,no_val))
    e_q = np.zeros((len_val,no_val))

    # Value attribution
    if stack >= 1:
        press[:,0] = abs(val1[:,p_i])
        S_xx[:,0] = val1[:,sx_i]
        S_yy[:,0] = val1[:,sy_i]
        S_xy[:,0] = val1[:,sxy_i]
        cis[:,0] = val1[:,cis_i]
        e_vol[:,0] = ((val1[0,vol_i] - val1[:,vol_i]) / val1[0,vol_i])
        phi[:,0] = val1[:,phi_i]
        Z[:,0] = val1[:,z_i]
        e_q[:,0] = val1[:,eq_i]
    if stack >= 2:
        press[:,1] = abs(val2[:,p_i])
        S_xx[:,1] = val2[:,sx_i]
        S_yy[:,1] = val2[:,sy_i]
        S_xy[:,1] = val2[:,sxy_i]
        cis[:,1] = val2[:,cis_i]
        e_vol[:,1] = ((val2[0,vol_i] - val2[:,vol_i]) / val2[0,vol_i])
        phi[:,1] = val2[:,phi_i]
        Z[:,1] = val2[:,z_i]
        e_q[:,1] = val2[:,eq_i]
    if stack >= 3:
        press[:,2] = abs(val3[:,p_i])
        S_xx[:,2] = val3[:,sx_i]
        S_yy[:,2] = val3[:,sy_i]
        S_xy[:,2] = val3[:,sxy_i]
        cis[:,2] = val3[:,cis_i]
        e_vol[:,2] = ((val3[0,vol_i] - val3[:,vol_i]) / val3[0,vol_i])
        phi[:,2] = val3[:,phi_i]
        Z[:,2] = val3[:,z_i]
        e_q[:,2] = val3[:,eq_i]
    if stack >= 4:
        press[:,3] = abs(val4[:,p_i])
        S_xx[:,3] = val4[:,sx_i]
        S_yy[:,3] = val4[:,sy_i]
        S_xy[:,3] = val4[:,sxy_i]
        cis[:,3] = val4[:,cis_i]
        e_vol[:,3] = ((val4[0,vol_i] - val4[:,vol_i]) / val4[0,vol_i])
        phi[:,3] = val4[:,phi_i]
        Z[:,3] = val4[:,z_i]
        e_q[:,3] = val4[:,eq_i]
    if stack >= 5:
        press[:,4] = abs(val5[:,p_i])
        S_xx[:,4] = val5[:,sx_i]
        S_yy[:,4] = val5[:,sy_i]
        S_xy[:,4] = val5[:,sxy_i]
        cis[:,4] = val5[:,cis_i]
        e_vol[:,4] = ((val5[0,vol_i] - val5[:,vol_i]) / val5[0,vol_i])
        phi[:,4] = val5[:,phi_i]
        Z[:,4] = val5[:,z_i]
        e_q[:,4] = val5[:,eq_i]
    if stack >= 6:
        press[:,5] = abs(val6[:,p_i])
        S_xx[:,5] = val6[:,sx_i]
        S_yy[:,5] = val6[:,sy_i]
        S_xy[:,5] = val6[:,sxy_i]
        cis[:,5] = val6[:,cis_i]
        e_vol[:,5] = ((val6[0,vol_i] - val6[:,vol_i]) / val6[0,vol_i])
        phi[:,5] = val6[:,phi_i]
        Z[:,5] = val6[:,z_i]
        e_q[:,5] = val6[:,eq_i]
    if stack >= 7:
        press[:,6] = abs(val7[:,p_i])
        S_xx[:,6] = val7[:,sx_i]
        S_yy[:,6] = val7[:,sy_i]
        S_xy[:,6] = val7[:,sxy_i]
        cis[:,6] = val7[:,cis_i]
        e_vol[:,6] = ((val7[0,vol_i] - val7[:,vol_i]) / val7[0,vol_i])
        phi[:,6] = val7[:,phi_i]
        Z[:,6] = val7[:,z_i]
        e_q[:,6] = val7[:,eq_i]
    if stack >= 8:
        press[:,7] = abs(val8[:,p_i])
        S_xx[:,7] = val8[:,sx_i]
        S_yy[:,7] = val8[:,sy_i]
        S_xy[:,7] = val8[:,sxy_i]
        cis[:,7] = val8[:,cis_i]
        e_vol[:,7] = ((val8[0,vol_i] - val8[:,vol_i]) / val8[0,vol_i])
        phi[:,7] = val8[:,phi_i]
        Z[:,7] = val8[:,z_i]
        e_q[:,7] = val8[:,eq_i]
    if stack >= 9:
        press[:,8] = abs(val9[:,p_i])
        S_xx[:,8] = val9[:,sx_i]
        S_yy[:,8] = val9[:,sy_i]
        S_xy[:,8] = val9[:,sxy_i]
        cis[:,8] = val9[:,cis_i]
        e_vol[:,8] = ((val9[0,vol_i] - val9[:,vol_i]) / val9[0,vol_i])
        phi[:,8] = val9[:,phi_i]
        Z[:,8] = val9[:,z_i]
        e_q[:,8] = val9[:,eq_i]
    if stack >= 10:
        press[:,9] = abs(val10[:,p_i])
        S_xx[:,9] = val10[:,sx_i]
        S_yy[:,9] = val10[:,sy_i]
        S_xy[:,9] = val10[:,sxy_i]
        cis[:,9] = val10[:,cis_i]
        e_vol[:,9] = ((val10[0,vol_i] - val10[:,vol_i]) / val10[0,vol_i])
        phi[:,9] = val10[:,phi_i]
        Z[:,9] = val10[:,z_i]
        e_q[:,9] = val10[:,eq_i]
    # end if
    return press,S_xx,S_yy,S_xy,cis,e_vol,phi,Z,e_q

def val_var_ela(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,E,t):
    # Variables
    # Scalar
    # index
    stress_i = 0
    def_i = 4
    z_i = 6
    # end if

    # dimmension variable
    no_val = 5 # max number of stacks
    len_val = len(val1)

    # time step
    dt = 1E-6
    N_step = 2E3
    dN = 400

    # Matrix
    time = np.zeros((len_val,no_val))
    stress = np.zeros((len_val,no_val))
    defo = np.zeros((len_val,no_val))
    Z = np.zeros((len_val,no_val))

    for i in range(no_val):
        for j in range(len_val):
            time[j,i] = (j*dt*(N_step/dN))/t
        # end of j for loop
    # end of i for loop

    # Value attribution
    if stack >= 1:
        stress[:,0] = abs(val1[:,stress_i]/E)
        defo[:,0] = val1[:,def_i]
        Z[:,0] = val1[:,z_i]
    if stack >= 2:
        stress[:,1] = abs(val2[:,stress_i]/E)
        defo[:,1] = val2[:,def_i]
        Z[:,1] = val2[:,z_i]
    if stack >= 3:
        stress[:,2] = abs(val3[:,stress_i]/E)
        defo[:,2] = val3[:,def_i]
        Z[:,2] = val3[:,z_i]
    if stack >= 4:
        stress[:,3] = abs(val4[:,stress_i]/E)
        defo[:,3] = val4[:,def_i]
        Z[:,3] = val4[:,z_i]
    if stack >= 5:
        stress[:,4] = abs(val5[:,stress_i]/E)
        defo[:,4] = val5[:,def_i]
        Z[:,4] = val5[:,z_i]
    if stack >= 6:
        stress[:,5] = abs(val6[:,stress_i]/E)
        defo[:,5] = val6[:,def_i]
        Z[:,5] = val6[:,z_i]
    if stack >= 7:
        stress[:,6] = abs(val7[:,stress_i]/E)
        defo[:,6] = val7[:,def_i]
        Z[:,6] = val7[:,z_i]
    if stack >= 8:
        stress[:,7] = abs(val8[:,stress_i]/E)
        defo[:,7] = val8[:,def_i]
        Z[:,7] = val8[:,z_i]
    if stack >= 9:
        stress[:,8] = abs(val9[:,stress_i]/E)
        defo[:,8] = val9[:,def_i]
        Z[:,8] = val9[:,z_i]
    if stack >= 10:
        stress[:,9] = abs(val10[:,stress_i]/E)
        defo[:,9] = val10[:,def_i]
        Z[:,9] = val10[:,z_i]
    return time, stress, defo, Z

# Load graphical parameters
def graph_param(graph_type):
    glen = 10
    gwid = 6
    lab_s = 0.5
    a = 0.2
    if graph_type == 'simple':
        ftitle = 20
        faxes = 18
        flegend = 16
        lw = 2
    elif graph_type == 'zoom':
        ftitle = 30
        faxes = 30
        flegend = 30
        lw = 4
    # end if
    return glen, gwid, ftitle, faxes, flegend, lab_s, lw, a

def graph_ls_mk_color(color1,color2):
    #""" # size effects
    col_g = ['red','darkorange','green','dodgerblue','black','black','black','black','black','black']
    line = ['-','--','-.',':','-.','-.','-.','-.','--','--']
    mk_vec = ['o','s','s','s','o','s','s','s','s','s'] #"""

    """ # basic datas with 1 x 5 stacks
    col_g = [color1(0.75),color1(0.40),color1(0.25),color1(0.15),color1(0.05),color2(0.6),color2(0.4),color2(0.2),color2(0.1),color2(0.05)]
    line = ['-','--','-.',':','-.','-.','-.','-.','--','--']
    mk_vec = ['o','s','s','s','s','o','s','s','s','s'] #"""

    """ # basic datas with 2 x 5 stacks
    col_g = [color1(0.75),color1(0.40),color1(0.25),color1(0.15),color1(0.05),color1(0.75),color1(0.40),color1(0.25),color1(0.15),color1(0.05)]
    line = ['-','-.','-.','-.','-.','-','-.','-.','-.','-.']
    mk_vec = ['o','s','s','s','s','o','s','s','s','s'] #"""

    """ # mixed datas with 2 x 3 stacks
    col_g = [color1(0.55),color2(0.6),color1(0.45),color2(0.4),color1(0.25),color2(0.2),color1(0.15),color1(0.05),color2(0.1),color2(0.05)]
    line = ['-','-.','-','-.','-','-.','--','--','--','--']
    mk_vec = ['o','o','s','s','s','s','s','s','s','s'] #"""

    """ # mixed datas with 3 x 2 stacks
    col_g = [color1(0.8),color1(0.75),color1(0.7),color1(0.3),color1(0.25),color1(0.2),color2(0),color2(0),color2(0),color2(0)]
    line = ['-','-.','--','-','-.','--','-','-','-','-']
    mk_vec = ['o','o','o','s','s','s','>','>','>','>'] #"""

    """ # mixed datas with 2 x 4 stacks
    col_g = [color1(0.75),color1(0.40),color1(0.25),color1(0.15),color2(0.6),color2(0.4),color2(0.2),color2(0.1),color1(0),color2(0)]
    line = ['-','-','-','-','-.','-.','-.','-.','--','--']
    mk_vec = ['o','s','s','s','o','s','s','s','s','s'] #"""
    return col_g, line, mk_vec

def graph_plot_legend(label,colorm1,colorm2,stack):
    colormap, ls_vec, marker_vec = graph_ls_mk_color(colorm1,colorm2)
    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = graph_param('simple')
    val = np.zeros((1,10))

    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(stack):
        ax1.plot(val[:,i], val[:,i], color = colormap[i], ls = ls_vec[i], label = label[i], linewidth = linew)
    # end of i for loop

    plt.legend(fontsize = font_legend, frameon=False, loc = 'best', labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')plot
    plt.show()
    return

def graph_scatter_legend(label,colorm1,colorm2,stack):
    colormap, ls_vec, marker_vec = graph_ls_mk_color(colorm1,colorm2)
    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = graph_param('simple')
    val = np.zeros((1,10))

    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(stack):
        ax1.plot(val[:,i], val[:,i], color = colormap[i], marker = marker_vec[i], ls = ls_vec[i], label = label[i], linewidth = linew)
    # end of i for loop
    ax1.set_ylim(ymin = 0, ymax = -100)

    plt.legend(fontsize = font_legend, frameon=False, loc = 'best', labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')plot
    plt.show()
    return

# regime index
def regime_scal(reg,aim_idx,no_max):
    idx = np.zeros((10,1))
    # over shoot index
    for i in range(no_max):
        if aim_idx == 'lin' : idx[i] = reg[0,i]
        if aim_idx == 'pst_lin': idx[i] = reg[1,i] # end of post linear regime
        if aim_idx == 'trans': idx[i] = reg[2,i] # end of transitory regim
    # end of i for loop
    return idx

def regime_split_lines(xval,reg,stack,lw,a):
    # Function variables
    ov_sh = regime_scal(reg, 'lin',stack)
    pst_lin = regime_scal(reg, 'pst_lin',stack)
    trs = regime_scal(reg, 'trans',stack)

    #for i in range(stack):
    # format de tes morts
    ov_i = np.int(ov_sh[0])
    pst_i = np.int(pst_lin[0])
    trs_i = np.int(trs[0])

    # plot the regimes vertical lines
    plt.axvline(xval[ov_i,0], color = 'black', ls = ':', linewidth=lw, alpha = 0.6)
    plt.axvline(xval[pst_i,0], color = 'black', ls = '--', linewidth=lw, alpha = 0.6)
    plt.axvline(xval[trs_i,0], color = 'black', ls = '-.', linewidth=lw, alpha = 0.6)
    # end of i for loop
    return

# Graph plot functions
def plot_stacks(stack,reg,xval,yval,dyval,colorm1,colorm2,x_label,y_label,g_label):
   # Function variable
   graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = graph_param('simple')
   colormap, ls_vec, marker_vec = graph_ls_mk_color(colorm1,colorm2)

   # Cut the datas
   #cut_s = np.array([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000])

   # P = 90 kPa
   #cut_s = np.array([1000,1000,1000,950,410])

   # P = 50 kPa (prep no fric / prep_fric)
   cut_s = np.array([1000,1000,1000,620,1000,1000,1000,620,1000])

   # P_50_90_kPa_I
   #cut_s = np.array([1000,1000,1000,1000,1000,410,1,1,1,1])

   # P_50_90_kPa
   #cut_s = np.array([1000,1000,1000,1000,1000,950,620,1,1,1])

   # P_5_50_90_kPa
   #cut_s = np.array([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000])

   # I_cste
   #cut_s = np.array([1000,1000,1000,1000,1000,410,1000,1000,1000,1000])

   # min val
   yval_min = yval[:,:stack].min()
   yval_max = yval[:,:stack].max()

   # Vector
   ov_sh = regime_scal(reg, 'lin',stack)
   if y_label == '$\u03c4/E_{g}$' or  y_label == '$\u03c4/\u03c3_{yy}$':
       left, bottom, width, height = [0.26, 0.25, 0.30, 0.30]
       #left, bottom, width, height = [0.52, 0.25, 0.30, 0.30]

   if y_label == '$P/E_{g}$' or y_label == '$P/\u03c3_{yy}$':
       #left, bottom, width, height = [0.52, 0.52, 0.30, 0.30] # high phi_ini
       left, bottom, width, height = [0.52, 0.53, 0.30, 0.30] # low phi_ini
       cut_val = cut_s.min()

       yval_min = yval[:cut_val,:stack].min()
       yval_max = yval[:cut_val,:stack].max()

   if y_label == '$\u03bc^{*}$':
       left, bottom, width, height = [0.265,0.24, 0.30, 0.30]
   if y_label == '$Z$':
       left, bottom, width, height = [0.565, 0.57, 0.30, 0.30] # high phi_ini
       #left, bottom, width, height = [0.57, 0.34, 0.30, 0.30] # low phi_ini
   if y_label == '$\u03d5$':
       #left, bottom, width, height = [0.23, 0.25, 0.30, 0.30]
       left, bottom, width, height = [0.565, 0.53, 0.30, 0.30]
   # end if

   # Plot the values
   plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
   fig, ax1 = plt.subplots()

   for i in range(stack):
       ax1.plot(xval[:cut_s[i],i], yval[:cut_s[i],i], color = colormap[i], ls = ls_vec[i], label = g_label[i], linewidth = linew)
       ax1.fill_between(xval[:cut_s[i],i],yval[:cut_s[i],i]-dyval[:cut_s[i],i],yval[:cut_s[i],i]+dyval[:cut_s[i],i], color = colormap[i], alpha = 0.5*set_a)

       if i == 0 : ov_idx = np.int(ov_sh[i])
       if i == 5: ov_idx = np.int(ov_sh[i])-1
       else : ov_idx = np.int(ov_sh[i])
       ax1.scatter(xval[ov_idx,i], yval[ov_idx,i], color = colormap[i], label = '', linewidth = 2*linew)
       # end of i for loop

   ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
   #regime_split_lines(xval, reg, stack, linew, set_a)

   ax1.set_ylim(ymin = 0.999*yval_min, ymax = 1.05*yval_max)
   #ax1.set_ylim(ymin = yval_min, ymax = 1.01*yval_max)
   #ax1.set_xscale('log')
   if y_label == '$P/E_{g}$' or y_label == '$P/\u03c3_{yy}$':
       #ax1.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0))
       ax1.set_ylim(ymin = 0.999*yval_min, ymax = 1.01*yval_max)
   if y_label == '$\u03c4/E_{g}$' or y_label == '$\u03c4/\u03c3_{yy}$':
       #ax1.set_ylim(ymin = -5E-6, ymax = 1.05*yval_max) # strain pressure figures
       #ax1.set_ylim(ymin = -5E-2, ymax = 1.05*yval_max) # press pressure figures
       ax1.set_ylim(ymin = 0, ymax = 1.05*yval_max)
   if y_label == '$\u03bc^{*}$':
       ax1.set_ylim(ymin = 0)
   if y_label == '$\u03d5$':
       ax1.set_ylim(ymin = 0.999*yval_min, ymax = 1.005*yval_max) # high phi_ini
       #ax1.set_ylim(ymin = 0.995*yval_min, ymax = 1.001*yval_max) # low phi_ini
   if y_label == '$Z$':
       ax1.set_ylim(ymin = 0.995*yval_min, ymax = 1.005*yval_max)

   # end if

   ax1.set_xlabel(x_label, fontsize = font_title)
   ax1.set_ylabel(y_label, fontsize = font_title)

   #"""
   if y_label == '$\u03c4/\u03c3_{yy}$' or y_label == '$\u03c4/E_{g}$' or y_label == '$P/E_{g}$' or y_label == '$P/\u03c3_{yy}$' or y_label == '$\u03bc^{*}$' or y_label == '$\u03d5$' or y_label == '$Z$':
       ax2 = fig.add_axes([left, bottom, width, height])

       for i in range(stack):
           ax2.plot(xval[:cut_s[i],i], yval[:cut_s[i],i], color = colormap[i], ls = ls_vec[i], label = g_label[i], linewidth = linew)
           ax2.fill_between(xval[:cut_s[i],i],yval[:cut_s[i],i]-dyval[:cut_s[i],i],yval[:cut_s[i],i]+dyval[:cut_s[i],i], color = colormap[i], alpha = 0.5*set_a)

           if i == 0 : ov_idx = np.int(ov_sh[i])
           if i == 5: ov_idx = np.int(ov_sh[i])-1
           else : ov_idx = np.int(ov_sh[i])
           ax2.scatter(xval[ov_idx,i], yval[ov_idx,i], color = colormap[i], label = '', linewidth = 2*linew)
           # end of i for loop

       ax2.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
       regime_split_lines(xval, reg, stack, linew, set_a)

       if y_label == '$\u03c4/E_{g}$' or y_label == '$\u03c4/\u03c3_{yy}$' or y_label == '\u0394 $\u03c4/E_{g}$':
           #ax2.set_ylim(ymin = 0.5*yval_max,ymax = 1.05*yval_max) # prep no fric
           ax2.set_ylim(ymin = 0, ymax = 1.05*yval_max)
       if y_label == '\u0394 $\u03c4/\u03c3_{yy}$':
           #ax2.set_ylim(ymin = 0.5*yval_max,ymax = 1.05*yval_max) # prep no fric
           ax2.set_ylim(ymin = 0.2, ymax = 1.05*yval_max)
       if y_label == '$P/E_{g}$' or y_label == '$P/\u03c3_{yy}$':
           ax2.set_ylim(ymin = 0.99*yval_min, ymax = 1.01*yval_max)
       if y_label == '$\u03bc^{*}$':
           ax2.set_ylim(ymin = 0)
       if y_label == '$\u03d5$':
           ax2.set_ylim(ymin = 0.999*yval_min, ymax = 1.005*yval_max)
       if y_label == '$Z$':
           ax2.set_ylim(ymin = 0.99*yval_min, ymax = 1.01*yval_max)
       # end if

       ax2.set_xlabel(x_label, fontsize = font_title)
       ax2.set_ylabel(y_label, fontsize = font_title)
       ax2.set_xscale('log')
   # end if """

   plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
   plt.rc('xtick', labelsize = font_axes)
   plt.rc('ytick', labelsize = font_axes)

   plt.legend(fontsize = font_legend, frameon=False, loc = 'best', labelspacing = label_space)
   #plt.savefig('relax_p_vs_t.png')plot
   plt.show()
   return

def plot_size(stack,reg,xval,yval,dyval,colorm1,colorm2,x_label,y_label,label1,label2):
   # Function variable
   graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = graph_param('simple')
   colormap, ls_vec, marker_vec = graph_ls_mk_color(colorm1,colorm2)
   len_mat = 4 # len matrix
   len_col = len(yval)

   # Scatter vec
   x = np.array([1E3,5E3,1E4,2E4])
   max_vec = np.zeros(len_mat)
   plt_vec = np.zeros(len_mat)
   # attribution of scatter matrix
   for i in range(len_mat):
       extract = int(reg[0,i])
       max_vec[i] = dyval[extract,i]/yval[extract,i]
       plt_vec[i] = dyval[len_col-1,i]/yval[len_col-1,i]
   # end if

   # Plot the values
   plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
   fig, ax1 = plt.subplots()

   for i in range(stack):
       if i == 0 :
           ax1.scatter(x[i], max_vec[i], color = 'orangered', marker = 's', label = label1, linewidth = 0.5*linew, s = 150)
           ax1.scatter(x[i], plt_vec[i], color = 'darkviolet', marker = 'v', label = label2, linewidth = 0.5*linew, s = 150)
       else :
           ax1.scatter(x[i], max_vec[i], color = 'orangered', marker = 's', label = '', linewidth = 0.5*linew, s = 150)
           ax1.scatter(x[i], plt_vec[i], color = 'darkviolet', marker = 'v', label = '', linewidth = 0.5*linew, s = 150)
   ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
   #regime_split_lines(xval, reg, stack, linew, set_a)

   ax1.set_ylim(ymin = 0)
   #ax1.set_ylim(ymin = yval_min, ymax = 1.01*yval_max)
   #ax1.set_xscale('log')
   # end if

   ax1.set_xlabel(x_label, fontsize = font_title)
   ax1.set_ylabel(y_label, fontsize = font_title)
   #"""

   plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
   plt.rc('xtick', labelsize = font_axes)
   plt.rc('ytick', labelsize = font_axes)

   plt.legend(fontsize = font_legend, frameon=False, loc = 'best', labelspacing = label_space)
   #plt.savefig('relax_p_vs_t.png')plot
   plt.show()
   return

def plot_stacks_prop(stack,reg,xval,yval,yerr,colorm1,colorm2,x_label,y_label,g_label):
    # Function variable
    # Scalar
    # damage fit variable
    val_len = len(yval)
    length = 12
    dl = val_len - length

    # max and vil values for graph output
    yval_min = yval[:,:stack].min()
    yval_max = yval[:,:stack].max()
    yval_min_z = yval[1:,:stack].min()

    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = graph_param('simple')

    # Insert dimensions
    if y_label == '$K/E_{g}$' or y_label == '$G/E_{g}$' or y_label == '$G/\u03c3_{yy}$' or y_label == '$K/\u03c3_{yy}$': left, bottom, width, height = [0.54, 0.53, 0.30, 0.30]
    if y_label == '$\u03bd_{2D}$': left, bottom, width, height = [0.32, 0.52, 0.30, 0.30]
    if y_label == '$d_{K}$' or y_label == '$d_{G}$': left, bottom, width, height = [0.58, 0.25, 0.30, 0.30] #[0.32, 0.25, 0.30, 0.30]
    # end if

    # Vectors
    colormap, ls_vec, marker_vec = graph_ls_mk_color(colorm1,colorm2)

    # fit for damage
    x_lin_dam = np.zeros((length,stack))
    y_lin_dam = np.zeros((length,stack))
    coeff = np.zeros((2,stack))

    print('Linear damage fit coefficient of ', y_label, '\n')
    if y_label == '$d_{K}$' or y_label == '$d_{G}$':
        for i in range(stack):
            coeff[:,i], cv = sc.curve_fit(linear_fit, np.float64(xval[dl:,i]), np.float64(yval[dl:,i]))
            print(coeff[0,i], '+/-', cv[0,0])
            x_lin_dam[:,i] = xval[dl:,i]
            y_lin_dam[:,i] = coeff[0,i]*x_lin_dam[:,i] + coeff[1,i]
        # end of i for loop
    # end if

    # Plot the values
    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(stack):
        ax1.plot(xval[:,i], yval[:,i], color = colormap[i], marker = marker_vec[i], ls = ls_vec[i], label = g_label[i], linewidth = linew)
        ax1.fill_between(xval[:,i],yval[:,i]-yerr[:,i],yval[:,i]+yerr[:,i], color = colormap[i], alpha = 0.5*set_a)

        #if y_label == '$d_{K}$' or y_label == '$d_{G}$':
        #    ax1.plot(x_lin_dam[:,i],y_lin_dam[:,i], ls = '-',color = colormap[i], linewidth = 0.5*linew)
        # end if
    # end of i for loop

    ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    regime_split_lines(xval, reg, stack, linew, set_a)

    #ax1.set_xscale('log')
    #if y_label == '$\u03bd_{2D}$': ax1.set_ylim(ymin = 0.99*yval_min, ymax = 0.37)
    if y_label == '$\u03bd_{2D}$': ax1.set_ylim(ymin = 0.99*yval_min, ymax = 1.05*yval_max)
    elif y_label == '$d_{G}$' or y_label == '$d_{K}$': ax1.set_ylim(ymin = 0.99*yval_min, ymax = 1.05*yval_max)
    elif y_label == '$G/E_{g}$' or y_label == '$G/\u03c3_{yy}$' :
        ax1.set_ylim(ymin = 0.99*yval_min, ymax = 2.5E3)
        #ax1.set_ylim(ymin = 0.99*yval_min, ymax = 1.05*yval_max)
    elif y_label == '$K/E_{g}$' or y_label == '$K/\u03c3_{yy}$' :
        #ax1.set_ylim(ymin = 0.99*yval_min, ymax = 0.34)
        ax1.set_ylim(ymin = 0.99*yval_min, ymax = 1.05*yval_max)
    #else : ax1.set_ylim(ymin = 0.99*yval_min, ymax = 1.25*yval_max)
    # end if

    ax1.set_xlabel(x_label, fontsize = font_title)
    ax1.set_ylabel(y_label, fontsize = font_title)


    ax2 = fig.add_axes([left, bottom, width, height])

    for i in range(stack):
        ax2.plot(xval[:,i], yval[:,i], color = colormap[i], marker = marker_vec[i], ls = ls_vec[i], label = g_label[i], linewidth = linew)
        ax2.fill_between(xval[:,i],yval[:,i]-yerr[:,i],yval[:,i]+yerr[:,i], color = colormap[i], alpha = set_a)
    # end of i for loop

    ax2.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    regime_split_lines(xval, reg, stack, linew, set_a)

    if y_label == '$G/E_{g}$' or y_label == '$K/E_{g}$' or y_label == '$\u03bd_{2D}$': ax2.set_ylim(ymin = 0.99*yval_min, ymax = 1.01*yval_max)
    elif y_label == '$d_{G}$' or y_label == '$d_{K}$': ax2.set_ylim(ymin = 0.99*yval_min_z, ymax = 1.05*yval_max)
    else : ax2.set_ylim(ymin = 0, ymax = 1.01*yval_max)
    # end if

    ax2.set_xlabel(x_label, fontsize = font_title)
    ax2.set_ylabel(y_label, fontsize = font_title)
    ax2.set_xscale('log') #"""

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, loc = 'best', labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')plot
    plt.show()
    return

def scatter_stacks(stack,reg,xval,yval,dxval,dyval,colorm1,colorm2,x_label,y_label,g_label):
   # Function variable
   graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = graph_param('simple')
   colormap, ls_vec, marker_vec = graph_ls_mk_color(colorm1,colorm2)

   # Cut the datas
   #cut_s = np.array([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000])

   # P = 90 kPa
   #cut_s = np.array([1000,1000,1000,950,410])

   # P = 50 kPa (prep no fric / prep_fric)
   #cut_s = np.array([1000,1000,1000,620,1000,1000,1000,620,1000])

   # P_50_90_kPa
   cut_s = np.array([1000,1000,1000,620,1000,1000,1000,1000,950,410])

   # P_5_50_90_kPa
   #cut_s = np.array([1000,1000,1000,1000,620,950,1000,1000,1000,1000])

   # I_cste
   #cut_s = np.array([1000,1000,1000,1000,1000,410,1000,1000,1000,1000])

   # Function vector
   valx_plot = np.zeros(stack)
   valy_plot = np.zeros(stack)
   dx_plot = np.zeros(stack)
   dy_plot = np.zeros(stack)

   valx_plot,valy_plot = xval,yval
   dx_plot, dy_plot = dxval,dyval

   """for i in range(stack):
       id_x, id_y = int(reg[0,i]),int(reg[0,i])
       valx_plot[i],valy_plot[i] = xval[id_x,i],yval[id_y,i]
       dx_plot[i], dy_plot[i] = dxval[id_x,i],dyval[id_y,i]
    # end i for loop """

   # min val
   xval_min = xval[:,:stack].min()
   xval_max = xval[:,:stack].max()
   yval_min = yval[:,:stack].min()
   yval_max = yval[:,:stack].max()

   # Plot the values
   plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
   fig, ax1 = plt.subplots()

   #x_fit = np.array([1E-6,2.5E-6,5E-6,7.5E-6,1E-6,2.5E-5,5E-5,7.5E-5,1E-4,2.5E-4,5E-4,7.5E-4,1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2,5E-2,7.5E-2,1E-1,2.5E-1,5E-1,7.5E-1,1,1.25,1.5])
   #plt.plot(x_fit,x_fit*0.26,color='black',ls='--',linewidth=linew)
   for i in range(stack):
       ax1.scatter(valx_plot[:cut_s[i],i], valy_plot[:cut_s[i],i], color = colormap[i], ls = ls_vec[i], label = g_label[i], linewidth = linew)
       #ax1.errorbar(valx_plot[i], valy_plot[i], yerr = dy_plot[i], xerr = dx_plot[i], color = colormap[i], linewidth = linew, barsabove = 'True', capthick = 0.5*linew)
       #ax1.plot(xval[:cut_s[i],i], yval[:cut_s[i],i], color = colormap[i], ls = ls_vec[i], label = g_label[i], linewidth = linew)
       #ax1.fill_between(xval[:cut_s[i],i],yval[:cut_s[i],i]-dyval[:cut_s[i],i],yval[:cut_s[i],i]+dyval[:cut_s[i],i], color = colormap[i], alpha = 0.5*set_a)
   # end of i for loop
   x_fit = np.array([0,0.5E-5,1E-4,1.5E-4,2E-4,2.5E-4])
   ax1.plot(x_fit,x_fit*0.25,ls='-.',color='black')
   ax1.plot(x_fit,x_fit*0.4,ls='--',color='black')

   ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))

   if x_label == '$P/E_{g}$' or x_label == '$P/\u03c3_{yy}$':
       ax1.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0))
       ax1.set_xlim(xmin = 0.95*xval_min, xmax = 1.05*xval_max)
   if y_label == '$\u03c4/E_{g}$' or y_label == '$\u03c4/\u03c3_{yy}$':
       ax1.set_ylim(ymin = 0, ymax = 1.05*yval_max)
   if y_label == '$q/E_{g}$' or y_label == '$q/\u03c3_{yy}$':
       ax1.set_ylim(ymin = 0, ymax = 1.05*yval_max)
   # end if

   ax1.set_xlabel(x_label, fontsize = font_title)
   ax1.set_ylabel(y_label, fontsize = font_title)

   plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
   plt.rc('xtick', labelsize = font_axes)
   plt.rc('ytick', labelsize = font_axes)

   plt.legend(fontsize = font_legend, frameon=False, loc = 'best', labelspacing = label_space)
   #plt.savefig('relax_p_vs_t.png')plot
   plt.show()
   return

# Graph plot call functions
def graph_relax(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,E,t,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap1,colormap2,analyse): # !!! graph for the shearing phase
    # Variables
    # Vector
    color_g1, color_g2 = colormap1,colormap2
    #tag = ['','','','','']
    tag = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]

    # Matrix
    r = np.nan((3,5))
    time, press, cis, phi, Z = val_var_prep(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, stack,'val', E, t)
    d_time, d_press, d_cis, d_phi, d_Z = val_var_prep(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, stack,'std', E, t)

    # Plot
    # Evolution of mean stress of the system plot
    plot_stacks(stack,r,time,press,d_press,color_g1,color_g2,'$t_{relax}$/$t_{N}$','$P/E_{g}$',tag)

    # Evolution of shear stress of the system plot
    plot_stacks(stack,r,time,cis,d_cis,color_g1,color_g2,'$t_{relax}$/$t_{N}$','$\u03c4/E_{g}$',tag)

    # Evolution of coordination number plot
    plot_stacks(stack,r,time,Z,d_Z,color_g1,color_g2,'$t_{relax}$/$t_{N}$','Z',tag)

    # Packing fraction plot
    plot_stacks(stack,r,time,phi,d_phi,color_g1,color_g2,'$t_{relax}$/$t_{N}$','\u03d5',tag)
    return

def graph_pre_comp(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,E,t,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap1,colormap2,analyse): # !!! graph for the shearing phase
    # Variables
    # Vector
    color_g1, color_g2 = colormap1,colormap2
    #tag = ['','','','','']
    tag = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]

    # Matrix
    r = np.nan((3,5))
    time, press, cis, phi, Z = val_var_prep(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10, stack, 'val', E, t)
    d_time, d_press, d_cis, d_phi, d_Z = val_var_prep(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10, stack,'std', E, t)

    # Plot
    # Evolution of mean stress of the system plot
    plot_stacks(stack,r,time,press,d_press,color_g1,color_g2,'$t_{precomp}$/$t_{N}$','$P/E_{g}$',tag)

    # Evolution of shear stress of the system plot
    plot_stacks(stack,r,time,cis,d_cis,color_g1,color_g2,'$t_{relax}$/$t_{N}$','$\u03c4/E_{g}$',tag)

    # Evolution of coordination number plot
    plot_stacks(stack,r,time,Z,d_Z,color_g1,color_g2,'$t_{precomp}$/$t_{N}$','Z',tag)

    # Packing fraction plot
    plot_stacks(stack,r,time,phi,d_phi,color_g1,color_g2,'$t_{precomp}$/$t_{N}$','\u03d5',tag)
    return

def graph_cis(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,reg,t,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,fin_val,colormap1,colormap2,analysis): # !!! graph for the shearing phase
    # Function variables #
    # Scalar
    simu_monitor = 'no' # monitor S_xx, S_yy, mu, E_vol etc..
    simu_size = 'yes'
    model_var = 'no' # monitor q vs E_q and s_kk vs E_kk
    param_fit = 'no' # monitor tau, p, Z vs phi

    # Graph output vector
    color_g1, color_g2 = colormap1, colormap2
    #color_g = ['red','darkorange','limegreen','royalblue',''] # for size effects

    tag = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]
    #tag = ['','','','','','','','','','']
    tag_sh = ['','','','','','','','','','']

    # Matrix
    press,S_xx,S_yy,S_xy,cis,e_vol,phi,Z,E_q = val_var_sh(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,'',t,)
    d_press,d_S_xx,d_S_yy,d_S_xy,d_cis,d_e_vol,d_phi,d_Z,d_E_q = val_var_sh(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,'std',t,)
    mu = np.zeros((len(S_xy),stack))
    d_mu = np.zeros((len(S_xy),stack))

    # Labels
    if analysis == 'strain':
        p_label = '$P/E_{g}$'
        xy_label = '$\u03c4/E_{g}$'
    elif analysis == 'pressure':
        p_label = '$P/\u03c3_{yy}$'
        xy_label = '$\u03c4/\u03c3_{yy}$'
    # end if

    # compute effective friction_50kPa
    for i in range(len(S_xy)):
        for j in range(stack):
            if S_yy[i,j] != 0 :
                mu[i,j] = S_xy[i,j]/S_yy[i,j]
                d_mu[i,j] = ((d_S_xy[i,j]/S_xy[i,j])+(d_S_yy[i,j]/S_yy[i,j]))*mu[i,j]
            # end if
        # end of j for loop
    # end of i for loop

    # plot legend
    graph_plot_legend(tag, color_g1, color_g2, stack)

    # Mean stress vs shear strain
    plot_stacks(stack,reg,cis,press,d_press,color_g1,color_g2,'\u03b3',p_label,tag_sh)

    # Shear stress vs shear strain
    plot_stacks(stack,reg,cis,S_xy,d_S_xy,color_g1,color_g2,'\u03b3',xy_label,tag_sh)

    # Effective friction
    #plot_stacks(stack,reg,cis,mu,d_mu,color_g1,color_g2,'\u03b3','$\u03bc^{*}$',tag_sh)

    # Packing fraction
    plot_stacks(stack,reg,cis,phi,d_phi,color_g1,color_g2,'\u03b3','$\u03d5$',tag_sh)

    # Coordination number
    plot_stacks(stack,reg,cis,Z,d_Z,color_g1,color_g2,'\u03b3','$Z$',tag_sh)

    if simu_size == 'yes':
        plot_size(stack,reg,cis,S_xy,d_S_xy,color_g1,color_g2,'$N$','$\u03c4 / \u0394 \u03c4$','$\u03c4_{max}$','$\u03c4_{plt}$')

        plot_size(stack,reg,cis,Z,d_Z,color_g1,color_g2,'$N$','$Z / \u0394 Z$','$Z_{max}$','$Z_{plt}$')
    # end if

    # Addition Plot #
    if simu_monitor == 'yes':
        # Volumetric deformation
        plot_stacks(stack,reg,cis,e_vol,d_e_vol,color_g1,color_g2,'\u03b3','$\u03b5_{vol}$',tag_sh)

        # S_yy
        plot_stacks(stack,reg,cis,S_yy,d_S_yy,color_g1,color_g2,'\u03b3','$\u03c3_{yy}$ / $E_{g}$',tag_sh)

        # S_xx
        plot_stacks(stack,reg,cis,S_xx,d_S_xx,color_g1,color_g2,'\u03b3','$\u03c3_{xx}$ / $E_{g}$',tag_sh)

    if model_var == 'yes':
        # s_{ij} (= q) vs E_q
        plot_stacks(stack,reg,cis,S_xx-S_yy,abs(d_S_xx - d_S_yy),color_g1,color_g2,'\u03b3','$q / E_{g}$',tag)

        # P vs E_kk
        #plot_stacks(stack,reg,e_vol,press,d_press,color_g1,color_g2,'$\u03b5_{kk}$','$P / E_{g}$',tag)

    if param_fit == 'yes':
        if analysis == 'strain':
            p_label = '$P/E_{g}$'
            xy_label = '$q/E_{g}$'
        elif analysis == 'pressure':
            p_label = '$P/\u03c3_{yy}$'
            xy_label = '$q/\u03c3_{yy}$'
        # end if

        # defining S_q & d_S_q
        S_q = np.zeros((len(S_xy),stack))
        d_S_q = np.zeros((len(S_xy),stack))
        for i in range(len(S_xy)):
            for j in range(stack):
                S_q[i,j] = np.sqrt((((S_xx[i,j]-S_yy[i,j])/2)**2)+(S_xy[i,j]**2))
                d_S_q[i,j] = d_S_xy[i,j]
            # end of j for loop
        # end of i for loop

        # |s| vs press
        #plot_stacks(stack,reg,press,S_q,d_S_q,color_g1,color_g2,'$P / E_{g}$','$|s| / E_{g}$',tag)

        # Shear stress versus P
        scatter_stacks(stack,reg,press,S_q,d_press,d_S_q,color_g1,color_g2,p_label,xy_label,tag_sh)
    # end if
    return

def ela_prop_graph(mod1,mod2,dmod1,dmod2,reg,gamma,t,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,fin_val,colormap1,colormap2,analysis):
    # Variable
    # Scalar
    vec_len = 18

    # Vector
    color_g1, color_g2 = colormap1,colormap2

    tag_legend = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]
    tag = ['','','','','','','','','','']
    tag_nu = ['','','','','','','','','','']

    # Matrix
    nu = np.zeros((vec_len+1,10))
    std_nu = np.zeros((vec_len+1,10))

    # legends
    if analysis == 'strain':
        k_label = '$K/E_{g}$'
        g_label = '$G/E_{g}$'
    elif analysis == 'pressure':
        k_label = '$K/\u03c3_{yy}$'
        g_label = '$G/\u03c3_{yy}$'
    # end if

    for i in range(vec_len+1):
        for j in range(stack):
            nu[i,j] = ((mod1[i,j]-mod2[i,j])/(mod1[i,j]+mod2[i,j]))
            std_nu[i,j] = ((dmod1[i,j]/mod1[i,j])+(dmod2[i,j]/mod2[i,j]))*((mod1[i,j]-mod2[i,j])/(mod1[i,j]+mod2[i,j]))
        # end of j for loop
    # end of i for loop

    # Plot legend
    graph_scatter_legend(tag_legend, color_g1,color_g2, stack)

    # Bulk modulus K
    plot_stacks_prop(stack,reg,gamma,mod1,dmod1,color_g1,color_g2,'\u03b3',k_label,tag)

    # Shear modulus G
    plot_stacks_prop(stack,reg,gamma,mod2,dmod2,color_g1,color_g2,'\u03b3',g_label,tag)

    # Poisson coefficient nu_2D
    plot_stacks_prop(stack,reg,gamma,nu,std_nu,color_g1,color_g2,'\u03b3','$\u03bd_{2D}$',tag_nu)
    return

def dam(d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9,d_10,reg,gamma,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,fin_val,colormap1,colormap2,mod,analysis): # !!! damage
    # Variable
    # Scalar
    len_val = len(d_1)
    max_stack = 10

    # Vector
    color_g1, color_g2 = colormap1,colormap2

    tag = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]
    tag = ['','','','','','','','','','']

    # Matrix
    damage = np.zeros((len_val,max_stack))
    std_damage = np.zeros((len_val,max_stack))

    # Matrix
    for i in range(len_val):
        damage[i,0] = d_1[i,0]
        damage[i,1] = d_2[i,0]
        damage[i,2] = d_3[i,0]
        damage[i,3] = d_4[i,0]
        damage[i,4] = d_5[i,0]
        damage[i,5] = d_6[i,0]
        damage[i,6] = d_7[i,0]
        damage[i,7] = d_8[i,0]
        damage[i,8] = d_9[i,0]
        damage[i,9] = d_10[i,0]

        std_damage[i,0] = d_1[i,1]
        std_damage[i,1] = d_2[i,1]
        std_damage[i,2] = d_3[i,1]
        std_damage[i,3] = d_4[i,1]
        std_damage[i,4] = d_5[i,1]
        std_damage[i,5] = d_6[i,1]
        std_damage[i,6] = d_7[i,1]
        std_damage[i,7] = d_8[i,1]
        std_damage[i,8] = d_9[i,1]
        std_damage[i,9] = d_10[i,1]
    # end of i for loop

    # Remove the label of d_G
    if mod =='K':
        ylabel_1 = '$d_{K}$'
    if mod =='G':
        ylabel_1 = '$d_{G}$'
        tag = ['','','','','','','','','','']
    # end if

    # Damage curve
    plot_stacks_prop(stack,reg,gamma,damage,std_damage,color_g1, color_g2,'\u03b3',ylabel_1,tag)
    return