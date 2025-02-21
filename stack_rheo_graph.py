#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:37:36 2023

@author: rigottia
"""
import numpy as np
import matplotlib.pyplot as plt
import stack_rheo_function as fc
import scipy.optimize as sc
import operator as op

def graph_rheo_param():
    # plot parameters
    glen = 10
    gwid = 6
    ft = 20
    fa = 16
    fl = 12
    lab_s = 0.5
    linew = 3
    linew_f = 2.5
    capw = 5
    alpha = 0.1
    return glen,gwid,ft,fa,fl,lab_s,linew,linew_f,capw,alpha

def graph_color(colormap):
    return [colormap(0.9),colormap(0.5),colormap(0.3),colormap(0.2),colormap(0.1)]

def graph_cis(line,col):
    # Function variable
    # Matrix
    cis1 = np.zeros((line,col))
    cis2 = np.zeros((line,col))
    cis3 = np.zeros((line,col))
    cis4 = np.zeros((line,col))

    for i in range(line):
        for j in range(col):
            if j == 0 :
                cis1[i,j] = 5E-4
                cis2[i,j] = 3.75E-4
                cis3[i,j] = 1.2E-4
                cis4[i,j] = 3.75E-4
            elif j == 1 :
                cis1[i,j] = 1E-4
                cis2[i,j] = 7.5E-5
                cis3[i,j] = 2.5E-5
                cis4[i,j] = 7.5E-5
            elif j == 2 :
                cis1[i,j] = 5E-5
                cis2[i,j] = 3.75E-5
                cis3[i,j] = 1.2E-5
                cis4[i,j] = 3.75E-5
            elif j == 3 :
                cis1[i,j] = 1E-5
                cis2[i,j] = 7.5E-6
                cis3[i,j] = 2.5E-6
                cis4[i,j] = 7.5E-6
            elif j == 4 :
                cis1[i,j] = 5E-6
                cis2[i,j] = 3.75E-6
                cis3[i,j] = 1.2E-6
                cis4[i,j] = 3.75E-6
            # end if
        # end i for loop
    # end of j for loop
    return cis1, cis2, cis3, cis4

def sort_mat(xval,yval,yerr,rev): # sort yval and xval as function of xval
    # Function variables
    col = 5 # number of simulation stacks computed / pressure imposed

    # Sort xval and yval
    for k in range(col):
        mod_valx, mod_valy, mod_err = xval[:,k],yval[:,k],yerr[:,k]
        sort = sorted(zip(mod_valx,mod_valy,mod_err), key=op.itemgetter(0),reverse=rev)
        xval[:,k], yval[:,k], yerr[:,k] = zip(*sort)
    # end of k for loop

    xval = np.ma.masked_equal(xval,0)
    yval = np.ma.masked_equal(yval,0)
    yerr = np.ma.masked_equal(yerr,0)
    # end of i for loop
    return xval, yval, yerr

# Plot function
def rheo_plot(len_global_rheo,x_val,y_val,y_val_err,tag,colormap,x_tag,y_tag,stack):
    # Function variable
    # Colors
    col_g = graph_color(colormap)

    # size of the graphs
    graph_len,graph_wid,font_title,font_axes,font_legend,label_space,linew,linew_fit,capsize,set_a = graph_rheo_param()

    # size of the graphs
    graph_len = 10
    graph_wid = 6
    font_title = 20
    font_axes = 16
    font_legend = 12
    label_space = 0.5
    linew = 1
    capw = 5

    # Plot
    plt.figure(figsize= (graph_len,graph_wid))
    for i in range(len_global_rheo):
        if y_val[i] != 0 :
            if stack >= 1 :
                if i <= 4 :
                    if i == 0 :
                        plt.scatter(x_val[i], y_val[i], color = col_g[0], marker = 'o', label = tag[0])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[0], label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col_g[0], marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[0], label = '', barsabove =True, elinewidth = linew, capsize = capw)
            if stack >= 2 :
                if i > 4 and i <= 9:
                    if i == 5 :
                        plt.scatter(x_val[i], y_val[i], color = col_g[1], marker = 'o', label = tag[1])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[1], label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col_g[1], marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[1], label = '', barsabove =True, elinewidth = linew, capsize = capw)
            if stack >= 3 :
                if i > 9 and i <= 14:
                    if i == 10  :
                        plt.scatter(x_val[i], y_val[i], color = col_g[2], marker = 'o', label = tag[2])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[2], label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col_g[2], marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[2], label = '', barsabove =True, elinewidth = linew, capsize = capw)
            if stack >= 4 :
                if i > 14 and i <= 19:
                    if i == 15 :
                        plt.scatter(x_val[i], y_val[i], color = col_g[3], marker = 'o', label = tag[3])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[3], label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col_g[3], marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col_g[3], label = '', barsabove =True, elinewidth = linew, capsize = capw)
    # end of for loop

    plt.axvline(10**(-1), color = 'silver')
    plt.axvline(10**(-3), color = 'silver')

    # Title
    ##plt.title('Final packing fraction \u03d5 versus inertial number I ', fontsize = font_title)
    plt.xlabel(x_tag, fontsize = font_title)
    plt.ylabel(y_tag, fontsize = font_title)

    plt.xscale('log')
    plt.yscale('log')

    #plt.xlim(xmin = 5E-5, xmax = 2E-1)
    #plt.ylim(ymin = 0.7, ymax = 1.0)

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, loc = 'upper left', labelspacing = label_space)
    #plt.savefig('rheo_phi_vs_I.png')
    plt.show()
    return

def rheo_fit(len_global_rheo,x_val,y_val,y_val_err,x_fit,y_fit,tag,colormap_g,x_tag,y_tag,tag_fit,stack):
    # Function variable
    # Colors
    col1_g = colormap_g(0)
    col2_g = colormap_g(0.3)
    col3_g = colormap_g(0.6)
    col4_g = colormap_g(0.9)

    # size of the graphs
    graph_len = 10
    graph_wid = 6
    font_title = 20
    font_axes = 16
    font_legend = 12
    label_space = 0.5
    linew = 1
    capw = 5

    # Plot
    plt.figure(figsize= (graph_len,graph_wid))
    for i in range(len_global_rheo):
        if y_val[i] != 0 :
            if stack >= 1 :
                if i <= 4 :
                    if i == 0 :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = tag[0])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
            if stack >= 2 :
                if i > 6 and i <= 7:
                    if i == 5 :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = tag[1])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
            if stack >= 3 :
                if i > 9 and i <= 14:
                    if i == 10  :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = tag[2])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
            if stack >= 4 :
                if i > 14 and i <= 19:
                    if i == 15 :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = tag[3])
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
                    else :
                        plt.scatter(x_val[i], y_val[i], color = col1_g, marker = 'o', label = '')
                        plt.errorbar(x_val[i], y_val[i], yerr = y_val_err[i], color = col1_g, label = '', barsabove =True, elinewidth = linew, capsize = capw)
    # end of for loop
    plt.plot(x_fit[:],y_fit[:],color='black')

    plt.axvline(10**(-1), color = 'silver')
    plt.axvline(10**(-3), color = 'silver')

    # Title
    ##plt.title('Final packing fraction \u03d5 versus inertial number I ', fontsize = font_title)
    plt.xlabel(x_tag, fontsize = font_title)
    plt.ylabel(y_tag, fontsize = font_title)

    plt.xscale('log')
    #plt.yscale('log')

    plt.xlim(xmin = 3E-5, xmax = 1.2*x_val[:].max())
    if y_tag == 'µ': plt.ylim(ymin = 0.99*y_val[:].min(), ymax = 1.15*y_val[:].max())
    elif y_tag == '\u03d5': plt.ylim(ymin = 0.99*y_val[:].min(), ymax = 1.01*y_val[:].max())

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, loc = 'upper left', labelspacing = label_space)
    #plt.savefig('rheo_phi_vs_I.png')
    plt.show()
    return

def visc_plot(x_1,x_2,x_3,x_4,y1,y2,y3,y4,dy1,dy2,dy3,dy4,tag,colorm,xtag,ytag,no_line,stack,max_stack):
    # Function variables
    # Colors
    #col_g = [colormap(0.01),colormap(0.05),colormap(0.1),colormap(0.15),colormap(0.2),colormap(0.25),colormap(0.3),colormap(0.35),colormap(0.4),colormap(0.45),colormap(0.5),colormap(0.55),colormap(0.6),colormap(0.65),colormap(0.7),colormap(0.75),colormap(0.8),colormap(0.85),colormap(0.9)]
    graph_len,graph_wid,font_title,font_axes,font_legend,label_space,linew,linew_fit,cap,set_a = graph_rheo_param()

    col_g = [colorm(0.9),colorm(0.5),colorm(0.3),colorm(0.2),colorm(0.1)]
    mark = ['^','>','<','s']

    if xtag == '$I$':
        d_1, d_2, d_3, d_4 = x_1, x_2, x_3, x_4
        x_1, x_2, x_3, x_4 = fc.iner_mat(no_line, max_stack, 'yes')
    if xtag == '$d \u03b3 / dt$':
        d_1, d_2, d_3, d_4 = x_1, x_2, x_3, x_4
        x_1, x_2, x_3, x_4 = graph_cis(no_line, max_stack)
    # end if

    # sort the matrix
    if stack >= 1 : x_1, y1, dy1 = sort_mat(x_1,y1,dy1,False)
    if stack >= 2 : x_2, y2, dy2 = sort_mat(x_2,y2,dy2,False)
    if stack >= 3 : x_3, y3, dy3 = sort_mat(x_3,y3,dy3,False)
    if stack >= 4 : x_4, y4, dy4 = sort_mat(x_4,y4,dy4,False)

    left, bottom, width, height = [0.59, 0.56, 0.3, 0.3]

    # plot fit
    x_fit_i1 = np.array([1E-4,1.25E-4,1.5E-4,2E-4,2.5E-4,3E-4,3.5E-4,4E-4,4.5E-4,5E-4,5.5E-4,6E-4,6.5E-4,7E-4,7.5E-4,8E-4,8.5E-4,9E-4,9.5E-4,1E-3,2E-3,3E-3,4E-3,5E-3])
    x_fit_i2 = np.array([1E-4,1.25E-4,1.5E-4,2E-4,2.5E-4,3E-4,3.5E-4,4E-4,4.5E-4,5E-4,5.5E-4,6E-4,6.5E-4,7E-4,7.5E-4,8E-4,8.5E-4,9E-4,9.5E-4,1E-3,2E-3,3E-3,4E-3,5E-3])
    x_fit_i3 = np.array([1E-4,1.25E-4,1.5E-4,2E-4,2.5E-4,3E-4,3.5E-4,4E-4,4.5E-4,5E-4,5.5E-4,6E-4,6.5E-4,7E-4,7.5E-4,8E-4,8.5E-4,9E-4,9.5E-4,1E-3,2E-3,3E-3,4E-3,5E-3])


    x_fit = np.array([0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34])
    # fit param

    if ytag == '$\u03b7 / (E_{g} \u00b7 t_{N})$': # eta
        n1, n2, n3 = -1, -1, -1
        m1, m2, m3 = 0.008, 0.006, 0.002

        alpha_1, power_1 = 1E-6, -13.5
        alpha_2, power_2 = 1E-6, -11
        a = -1E5
        b = 1E3

    elif ytag == '$\u03b6 / (E_{g} \u00b7 t_{N})$': # zeta
        n1, n2, n3 = -1, -1, -1
        m1, m2, m3 = 0.026, 0.019, 0.006

        alpha_1, power_1 = 5E-6, -11.5
        alpha_2, power_2 = 5E-6, -10
        a = -1E5
        b = 1E3

    if ytag == '$\u03b7 / (E_{g} \u00b7 t_{N})$' or ytag == '$\u03b6 / (E_{g} \u00b7 t_{N})$':
        y_fit_i1 = fc.power_fit(x_fit_i1, m1, n1)
        y_fit_i2 = fc.power_fit(x_fit_i2, m2, n2)
        y_fit_i3 = fc.power_fit(x_fit_i3, m3, n3)

    y_fit_1 = fc.power_fit(x_fit, alpha_1, power_1)
    y_fit_2 = fc.power_fit(x_fit, alpha_2, power_2)
    # end if

    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(max_stack):
        for j in range(no_line):
            if stack >= 1:
                ax1.scatter(x_1[j,i],y1[j,i],color=col_g[i],marker=mark[0],linewidth=linew,label=tag[0])
                ax1.fill_between(x_1[:,i],y1[:,i]-dy1[:,i],y1[:,i]+dy1[:,i], color = col_g[i], alpha = 0.1*set_a)
            if stack >= 2:
                ax1.scatter(x_2[j,i],y2[j,i],color=col_g[i],marker=mark[1],linewidth=linew,label=tag[1])
                ax1.fill_between(x_2[:,i],y2[:,i]-dy2[:,i],y2[:,i]+dy2[:,i], color = col_g[i], alpha = 0.1*set_a)
            if stack >= 3:
                ax1.scatter(x_3[j,i],y3[j,i],color=col_g[i],marker=mark[2],linewidth=linew,label=tag[2])
                ax1.fill_between(x_3[:,i],y3[:,i]-dy3[:,i],y3[:,i]+dy3[:,i], color = col_g[i], alpha = 0.1*set_a)
            if stack >= 4:
                ax1.scatter(x_4[j,i],y4[j,i],color=col_g[i],marker=mark[3],linewidth=linew,label=tag[3])
                ax1.fill_between(x_4[:,i],y4[:,i]-dy4[:,i],y4[:,i]+dy4[:,i], color = col_g[i], alpha = 0.1*set_a)
            # end if
        # end of j for loop
    # end of i for loop

    if xtag == '$d_{G}$' or xtag == '$d_{K}$':
        if ytag == '$\u03b7 / (E_{g} \u00b7 t_{N})$' or ytag == '$\u03b6 / (E_{g} \u00b7 t_{N})$':
            if xtag == '$d_{G}$' :
                ax1.set_xlim(xmin = 0.17, xmax = 0.35)
                ax1.set_ylim(ymin = 0, ymax = 1E2)
            if xtag == '$d_{K}$' :
                ax1.set_xlim(xmin = 0.18, xmax = 0.32)
                ax1.set_ylim(ymin = 0, ymax = 3E2)

            ax1.plot(x_fit,y_fit_1,ls='-.',color = 'black',linewidth = linew)
            ax1.plot(x_fit,y_fit_2,ls='--',color = 'black',linewidth = linew)
            #ax1.plot(x_fit,y_fit_1,ls='--',color = 'black',linewidth = linew)
            #ax1.plot(x_fit,0.2*y_fit,ls='--',color = 'black',linewidth = linew)
            #ax1.plot(x_fit,y_fit_1,ls='--',color = 'black',linewidth = linew)
            #ax1.plot(x_fit,y_fit_2,ls='-.',color = 'black',linewidth = linew)
    # end if

    ax1.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0))
    #ax1.set_xscale('log')
    #ax1.set_yscale('log')
    #if xtag == '$P/E_{g}$' or xtag == '$P/E_{g}$': ax1.set_yscale('log')
    if xtag == '$I$':
        if ytag == '$\u03b7 / (E_{g} \u00b7 t_{N})$' or ytag == '$\u03b6 / (E_{g} \u00b7 t_{N})$':
            ax1.set_xscale('log')
            #ax1.set_yscale('log')
            plt.plot(x_fit_i1,y_fit_i1,color='black',linewidth=linew,ls='-.')
            plt.plot(x_fit_i2,y_fit_i2,color='black',linewidth=linew,ls='--')
            plt.plot(x_fit_i3,y_fit_i3,color='black',linewidth=linew,ls=':')
        # end if
    # end if
    ax1.set_xlabel(xtag, fontsize = font_title)
    ax1.set_ylabel(ytag, fontsize = font_title)

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, labelspacing = label_space)
    #plt.savefig('ela_relax_t*_vs_G.png')
    plt.show()
    return

def param_plot(x_val1,x_val2,x_val3,x_val4,y_val1,y_val2,y_val3,y_val4,dmod1,dmod2,dmod3,dmod4,fit_coeff,tag,colormap,x_tag,y_tag,fit_print,no_ela,stacks,max_stack):
    # Function variables
    # Scalar
    if x_tag == '$P/E_{g}$': no_ela_cut = 1
    else : no_ela_cut = no_ela
    cut_g = 0 # graph cut column

    # insert position
    if y_tag == '$G/E_{g}$' : left, bottom, width, height = [0.23, 0.54, 0.30, 0.30]
    if y_tag == '$K/E_{g}$' : left, bottom, width, height = [0.59, 0.24, 0.30, 0.30]

    # Graph variables
    col_g = graph_color(colormap)
    #col_fit = [colormap(0),colormap(0.3),colormap(0.6),colormap(1)]
    #mark = ['o','>','<','s']
    mark = ['^','>','<','s']
    #mark = ['^','>','<','']
    #mark = ['>','s','','']

    # define the reverse argument
    if x_tag =='\u03d5':
        rev=True
    else :
        rev=False
    # end if

    # size of the graphs
    graph_len,graph_wid,font_title,font_axes,font_legend,label_space,linew,linew_fit,capsize,set_a = graph_rheo_param()

    x_v1,x_v2,x_v3,x_v4 = x_val1,x_val2,x_val3,x_val4

    if x_tag != '$P/E_{g}$':
        x_v1[0,:] = np.zeros(max_stack)
        x_v2[0,:] = np.zeros(max_stack)
        x_v3[0,:] = np.zeros(max_stack)
        x_v4[0,:] = np.zeros(max_stack)
    # end if
    if stacks >= 1 : xval1, yval1, dmod1 = sort_mat(x_v1,y_val1,dmod1,rev)
    if stacks >= 2 : xval2, yval2, dmod2 = sort_mat(x_v2,y_val2,dmod2,rev)
    if stacks >= 3 : xval3, yval3, dmod3 = sort_mat(x_v3,y_val3,dmod3,rev)
    if stacks >= 4 : xval4, yval4, dmod4 = sort_mat(x_v4,y_val4,dmod4,rev)

    # create the y_fit variable # temp
    if y_tag == '$\u03c4_{c}/\u03c3_{yy}$' or y_tag == '$P_{c}/\u03c3_{yy}$' or y_tag == '$s_{c}/\u03c3_{yy}$' or y_tag == '$t_{\u03c4}^{*} / t_{N}$' or y_tag =='$t_{s}^{*} / t_{N}$' or y_tag == '$t_{P}^{*} / t_{N}$' or y_tag == '$\u03b6 / (E_{g} \u00b7 t_{N})$' or y_tag == '$\u03b7 / (E_{g} \u00b7 t_{N})$':
        if y_tag == '$\u03c4_{c}/\u03c3_{yy}$':
            d_c_1, d_c_2 = 0.2, 0.25
            power_a_1, power_a_2 = 0.54, 0.54
            a_1, a_1 = 1, 1

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit_1 = fc.state_function(xval, d_c_1, power_a_1)

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit_2 = fc.state_function(xval, d_c_2, power_a_2)

        if y_tag == '$s_{c}/\u03c3_{yy}$':
            # value from fit : d_c = 0.25, a = 0.521, b = 0.698
            d_c, d_c_min, d_c_max = 0.24, 0.21, 0.27
            a, a_min, a_max = 0.622, 0.820, 0.424
            power_a, power_a_min, power_a_max = 0.591, 0.494, 0.688

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit = fc.state_function(xval, d_c, a, power_a)

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit_min = fc.state_function(xval, d_c_min, a_min, power_a_min)

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit_max = fc.state_function(xval, d_c_max, a_max, power_a_max)

        if y_tag == '$P_{c}/\u03c3_{yy}$':
            # value from fit : d_c = 0.225, a = 0.246, b = 0.523
            d_c, d_c_min, d_c_max = 0.225, 0.205, 0.245
            a, a_min, a_max = 0.246, 0.303, 0.189
            power_a, power_a_min, power_a_max = 0.523, 0.459, 0.587

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit = fc.state_function(xval, d_c, a, power_a)

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit_min = fc.state_function(xval, d_c_min, a_min, power_a_min)

            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            y_fit_max = fc.state_function(xval, d_c_max, a_max, power_a_max)
    # end if

    #max_stack = 2
    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(no_ela_cut):
        for j in range(cut_g,max_stack):
            if i == no_ela-1 and j == max_stack-1 :
                ax1.scatter(xval1[i,j],yval1[i,j],color=col_g[j],marker=mark[0],linewidth=linew,label=tag[0])
                ax1.scatter(xval2[i,j],yval2[i,j],color=col_g[j],marker=mark[1],linewidth=linew,label=tag[1])
                ax1.scatter(xval3[i,j],yval3[i,j],color=col_g[j],marker=mark[2],linewidth=linew,label=tag[2])
                ax1.scatter(xval4[i,j],yval4[i,j],color=col_g[j],marker=mark[3],linewidth=linew,label=tag[3])
            else :
                ax1.scatter(x_val1[i,j],y_val1[i,j],color=col_g[j],marker=mark[0],linewidth=linew)
                ax1.scatter(x_val2[i,j],y_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew)
                ax1.scatter(x_val3[i,j],y_val3[i,j],color=col_g[j],marker=mark[2],linewidth=linew)
                ax1.scatter(x_val4[i,j],y_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew)
            # end if
        # end of j for loop
    # end of i for loop

    for j in range(cut_g,max_stack):
        if x_tag == '$P/E_{g}$':
            ax1.errorbar(xval1[0,j],y_val1[0,j],yerr=dmod1[0,j],color=col_g[j],marker=mark[0],elinewidth=0.5*linew,barsabove=True)
            ax1.errorbar(xval2[0,j],y_val2[0,j],yerr=dmod2[0,j],color=col_g[j],marker=mark[0],elinewidth=0.5*linew,barsabove=True)
            ax1.errorbar(xval3[0,j],y_val3[0,j],yerr=dmod3[0,j],color=col_g[j],marker=mark[0],elinewidth=0.5*linew,barsabove=True)
            ax1.errorbar(xval4[0,j],y_val4[0,j],yerr=dmod4[0,j],color=col_g[j],marker=mark[0],elinewidth=0.5*linew,barsabove=True)
        else :
            ax1.fill_between(xval1[:no_ela_cut,j],yval1[:no_ela_cut,j]-dmod1[:no_ela_cut,j],yval1[:no_ela_cut,j]+dmod1[:no_ela_cut,j], color = col_g[j], alpha = set_a)
            ax1.fill_between(xval2[:no_ela_cut,j],yval2[:no_ela_cut,j]-dmod2[:no_ela_cut,j],yval2[:no_ela_cut,j]+dmod2[:no_ela_cut,j], color = col_g[j], alpha = set_a)
            ax1.fill_between(xval3[:no_ela_cut,j],yval3[:no_ela_cut,j]-dmod3[:no_ela_cut,j],yval3[:no_ela_cut,j]+dmod3[:no_ela_cut,j], color = col_g[j], alpha = set_a)
            ax1.fill_between(xval4[:no_ela_cut,j],yval4[:no_ela_cut,j]-dmod4[:no_ela_cut,j],yval4[:no_ela_cut,j]+dmod4[:no_ela_cut,j], color = col_g[j], alpha = set_a)
    # end j for loop

    if x_tag == '$d_{G}$' or x_tag == '$d_{K}$':
        if y_tag == '$G/\u03c3_{yy}$' or y_tag == '$K/\u03c3_{yy}$':
            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            #ax1.plot(x_val1,fit_coeff[0,0]*x_val1+fit_coeff[0,1],color='black',ls='--')
            #ax1.plot(x_val2,fit_coeff[1,0]*x_val2+fit_coeff[1,1],color='black',ls='-.')
            #ax1.plot(x_val3,fit_coeff[2,0]*x_val3+fit_coeff[2,1],color='black',ls=':')

        elif y_tag =='$\u03c4_{c}/\u03c3_{yy}$' or y_tag == '$P_{c}/\u03c3_{yy}$' or y_tag == '$s_{c}/\u03c3_{yy}$': # residual stress
            xval = np.array([0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3])
            #ax1.plot(xval,y_fit,color='black',ls='-',linewidth=linew)
            #ax1.plot(xval,y_fit_min,color='black',ls='-.',linewidth=linew)
            #ax1.plot(xval,y_fit_max,color='black',ls='--',linewidth=linew)
        # end if

    elif x_tag == '$P/E_{g}$':
        p_fit = np.array([5E3/5E8,7.5E3/5E8,1E4/5E8,2.5E4/5E8,5E4/5E8,7.5E4/5E8,1E5/5E8, 2.5E5/5E8])
        #ax1.plot(p_fit,fit_coeff[0]*p_fit**fit_coeff[1],color ='black',ls='--',linewidth=linew)

    elif x_tag == '$P_{c}/\u03c3_{yy}$':
        p_c_fit = np.array([1E-4,5E-4,1E-3,5E-3,1E-2,5E-2,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2])
        #ax1.plot(p_c_fit,0.35*p_c_fit,color ='black',ls='--',linewidth=linew)
    # end if

    ax1.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0))
    #ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))

    ax1.set_xlabel(x_tag, fontsize = font_title)
    if x_tag != 'P/E_{g}$': ax1.set_ylabel(y_tag, fontsize = font_title)

    #plt.xlim(xmin = 0.70)
    #plt.ylim(ymin = -0.2)

    if x_tag =='$d_{G}$': ax1.set_xlim(xmin = 0.14) #, xmax = 0.36)
    if x_tag =='$d_{K}$' : ax1.set_xlim(xmin = 0.15) #, xmax = 0.32)
    if x_tag == '$d_{E}$': ax1.set_xlim(xmin = 0.14)
    if x_tag =='\u03d5': ax1.set_xlim(xmin = 0.805, xmax = 0.845)
    if x_tag == '$I$': ax1.set_xscale('log')
    if x_tag =='$P/E_{g}$': # pressure
        ax1.set_xscale('log')
        ax1.set_yscale('log')
    if x_tag == '$K/E_{g}$' :
        x_fit = np.array([0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45])
        y_fit = fc.linear_fit(x_fit, 0.5, 0)
        plt.plot(x_fit,y_fit,color='black',ls = '--', linewidth = linew)
        ax1.set_xlim(xmin = 1E-1, xmax = 4.5E-1)
        ax1.set_ylim(ymin = 5E-2, ymax = 2.5E-1)
        ax1.set_xlabel('$K_{0}/E_{g}$', fontsize = font_title)
    if x_tag =='$P_{c}/\u03c3_{yy}$':
        #plt.xscale('log')
        ax1.set_xlim(xmin = 0)
        ax1.set_ylim(ymin = 0)
    if y_tag == '$G/E_{g}$' :
        ax1.set_ylim(ymin = 7E-2, ymax = 7E-1)
        ax1.set_ylabel('$G_{0}/E_{g}$', fontsize = font_title)
    if y_tag == '$K/E_{g}$' :
        ax1.set_ylim(ymin = 1E-1, ymax = 7E-1)
        ax1.set_ylabel('$K_{0}/E_{g}$', fontsize = font_title)
    if y_tag == '$t_{\u03c4}^{*} / t_{N}$' or y_tag =='$t_{s}^{*} / t_{N}$':
        #ax1.set_xlim(xmin = 0.22, xmax = 0.35) #ax1.set_xlim(xmin = 0.14, xmax = 0.35)
        #ax1.set_ylim(ymin = 1E-3, ymax = 3.2E-2), ax1.set_yscale('log')
        ax1.set_ylim(ymin = 0, ymax = 1000)
    if y_tag == '$t_{P}^{*} / t_{N}$':
        #ax1.set_xlim(xmin = 0.21, xmax = 0.325) #ax1.set_xlim(xmin = 0.14, xmax = 0.325)
        #ax1.set_ylim(ymin = 1E-3, ymax = 3.2E-2), ax1.set_yscale('log')
        ax1.set_ylim(ymin = 0, ymax = 1000)
    if y_tag == '$\u03b7 / (E_{g} \u00b7 t_{N})$':
        ax1.set_ylim(ymin = 2,ymax = 2E2)
        ax1.set_yscale('log')
    if y_tag == '$\u03b6 / (E_{g} \u00b7 t_{N})$':
        ax1.set_ylim(ymin = 0.8,ymax = 3E2)
        ax1.set_yscale('log')
    if y_tag == '$\u03bd_{2D}$': ax1.set_ylim(ymin = 0.3, ymax = 0.44)
    if y_tag == '$\u03c4_{c}/\u03c3_{yy}$' or y_tag == '$s_{c}/\u03c3_{yy}$': plt.ylim(ymin = 0,ymax = 5E-1)
    if y_tag == '$\u03c4_{c}/E_{g}$' or y_tag == '$P_{c}/\u03c3_{yy}$': plt.ylim(ymin = 0, ymax = 1.25)
    if y_tag == '$\u03b2_{\u03c4}$' or y_tag == '$\u03b2_{P}$': # beta
        ax1.set_ylim(ymin = 0)
        ax1.axhline(1, color = 'silver', linewidth=0.3*linew)
    if y_tag == '$\u03bc_{M}$' :
        ax1.set_xlim(xmin = 0.14)
        ax1.set_ylim(ymin = 0, ymax = 0.4)
    # end if

    if x_tag == '$P/E_{g}$' and (y_tag == '$G/E_{g}$' or y_tag == '$K/E_{g}$'):
        ax2 = fig.add_axes([left, bottom, width, height])
        for i in range(no_ela):
            for j in range(cut_g,max_stack):
                ax2.scatter(x_val2[i,j],y_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew)
                if j < 3 : ax2.scatter(x_val4[i,j],y_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew)
            # end of j for loop
        # end of i for loop
        for j in range(cut_g,max_stack):
            ax2.fill_between(xval2[:,j],yval2[:,j]-dmod2[:,j],yval2[:,j]+dmod2[:,j], color = col_g[j], alpha = set_a)
            if j < 3 : ax2.fill_between(xval4[:,j],yval4[:,j]-dmod4[:,j],yval4[:,j]+dmod4[:,j], color = col_g[j], alpha = set_a)
        # end of j for loop

        p_fit = np.array([1E-4,1.025E-4,1.05E-4,1.075E-4,1.1E-4,1.125E-4])
        ax2.plot(p_fit,fit_coeff[0]*p_fit**fit_coeff[1],color ='black',ls='--',linewidth=linew)

        ax2.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0))
        ax2.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))

        ax2.set_xlabel(x_tag, fontsize = font_title)
        ax2.set_ylabel(y_tag, fontsize = font_title)
    # end if

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, labelspacing = label_space)
    #plt.savefig('ela_relax_t*_vs_G.png')
    plt.show()
    return

def param_relax_plot(x_val1,x_val2,x_val3,x_val4,y_val1,y_val2,y_val3,y_val4,dmod1,dmod2,dmod3,dmod4,tag,colormap,x_tag,y_tag,no_ela,stacks,max_stack):
    # Function variables
    # Colors
    #col_g = [colormap(0.01),colormap(0.05),colormap(0.1),colormap(0.15),colormap(0.2),colormap(0.25),colormap(0.3),colormap(0.35),colormap(0.4),colormap(0.45),colormap(0.5),colormap(0.55),colormap(0.6),colormap(0.65),colormap(0.7),colormap(0.75),colormap(0.8),colormap(0.85),colormap(0.9)]
    graph_len,graph_wid,font_title,font_axes,font_legend,label_space,linew,linew_fit,capsize,set_a = graph_rheo_param()
    col_g = [colormap(0.9),colormap(0.5),colormap(0.3),colormap(0.2),colormap(0.1)]
    mark = ['^','>','<','s']

    # define the reverse argument
    if x_tag =='\u03d5': rev=True
    else : rev=False

    # Matrix
    y_fit = np.zeros((no_ela,max_stack))

    # sort xval and yval as function of xval
    if stacks >= 1 :
        x_val1, y_val1, dmod1 = sort_mat(x_val1,y_val1,dmod1,rev)
    if stacks >= 2 :
        x_val2, y_val2, dmod2 = sort_mat(x_val2,y_val2,dmod2,rev)
    if stacks >= 3 :
        x_val3, y_val3, dmod3 = sort_mat(x_val3,y_val3,dmod3,rev)
    if stacks >= 4 :
        x_val4, y_val4, dmod4 = sort_mat(x_val4,y_val4,dmod4,rev)
    # end if

    for i in range(no_ela):
        for j in range(max_stack):
            if y_fit[i,j] == 0 : y_fit[i,j] == np.nan
        # end of j for loop
    # end of i for loop

    plt.figure(figsize= (graph_len,graph_wid))
    for i in range(no_ela):
        for j in range(max_stack):
            if i == no_ela-1 and j == max_stack-1 :
                if stacks >= 1: plt.scatter(x_val1[i,j],y_val1[i,j],color=col_g[j],marker=mark[0],linewidth=linew,label=tag[0])
                if stacks >= 2: plt.scatter(x_val2[i,j],y_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew,label=tag[1])
                if stacks >= 3: plt.scatter(x_val3[i,j],y_val3[i,j],color=col_g[j],marker=mark[2],linewidth=linew,label=tag[2])
                if stacks >= 4: plt.scatter(x_val4[i,j],y_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew,label=tag[3])
            else :
                plt.scatter(x_val1[i,j],y_val1[i,j],color=col_g[j],marker=mark[0],linewidth=linew)
                plt.scatter(x_val2[i,j],y_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew)
                plt.scatter(x_val3[i,j],y_val3[i,j],color=col_g[j],marker=mark[2],linewidth=linew)
                plt.scatter(x_val4[i,j],y_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew)
            # end if
        # end of j for loop
    # end of i for loop

    for i in range(max_stack):
        if stacks >= 1:
            plt.fill_between(x_val1[:,i],y_val1[:,i]-dmod1[:,i],y_val1[:,i]+dmod1[:,i], color = col_g[i], alpha = 0.5*set_a)
        if stacks >= 2:
            plt.fill_between(x_val2[:,i],y_val2[:,i]-dmod2[:,i],y_val2[:,i]+dmod2[:,i], color = col_g[i], alpha = 0.5*set_a)
        if stacks >= 3:
            plt.fill_between(x_val3[:,i],y_val3[:,i]-dmod3[:,i],y_val3[:,i]+dmod3[:,i], color = col_g[i], alpha = 0.5*set_a)
        if stacks >= 4:
            plt.fill_between(x_val4[:,i],y_val4[:,i]-dmod4[:,i],y_val4[:,i]+dmod4[:,i], color = col_g[i], alpha = 0.5*set_a)
        # end if
    # end of i for loop

    if x_tag == '$P_{c}/\u03c3_{yy}$' and y_tag == '$|s_{c}|/\u03c3_{yy}$':
        x_fit = np.array([1E-4,2E-4,3E-4,4E-4,5E-4,6E-4,7E-4,8E-4,9E-4,1E-3,2E-3,3E-3,4E-3,5E-3,6E-3,7E-3,8E-3,9E-3,1E-2,2E-2,3E-2,4E-2,5E-2,6E-2,7E-2,8E-2,9E-2,1E-1,2E-1,3E-1,4E-1,5E-1,6E-1,7E-1,8E-1,9E-1,1,1.1,1.2])

        # concatenate
        x_val_fit = np.concatenate((x_val1,x_val2,x_val3))
        y_val_fit = np.concatenate((y_val1,y_val2,y_val3))

        # reshape
        x_val_fit = np.reshape(x_val_fit, max_stack*no_ela*(stacks-1), order='F')
        y_val_fit = np.reshape(y_val_fit, max_stack*no_ela*(stacks-1), order='F')

        param, cv = sc.curve_fit(fc.linear_fit, x_val_fit, y_val_fit, p0 = (0.4,0), method = 'trf')
        print("param = ", param)
        print("cv = ", cv)
        plt.plot(x_fit, x_fit*0.26, color='black', ls='-.', linewidth=linew)
    else :
        for i in range(max_stack):
            if stacks >= 1 :
                plt.fill_between(x_val1[:,i],y_val1[:,i]-dmod1[:,i],y_val1[:,i]+dmod1[:,i], color = col_g[i], alpha = set_a)
            if stacks >= 2 :
                plt.fill_between(x_val2[:,i],y_val2[:,i]-dmod2[:,i],y_val2[:,i]+dmod2[:,i], color = col_g[i], alpha = set_a)
            if stacks >= 3 :
                plt.fill_between(x_val3[:,i],y_val3[:,i]-dmod3[:,i],y_val3[:,i]+dmod3[:,i], color = col_g[i], alpha = set_a)
            if stacks >= 4 :
                plt.fill_between(x_val4[:,i],y_val4[:,i]-dmod4[:,i],y_val4[:,i]+dmod4[:,i], color = col_g[i], alpha = set_a)
            # end if
        # end of i for loop

    #plt.title('Measured shear stress versus time of simulation t', fontsize = font_title)
    #plt.xscale('log')
    #plt.yscale('log')
    plt.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    plt.xlabel(x_tag, fontsize = font_title)
    plt.ylabel(y_tag, fontsize = font_title)

    #plt.xlim(xmin = 0)
    plt.ylim(ymin = 0)

    if x_tag =='$d_{G}$': plt.xlim(xmin = 0.14, xmax = 0.36)
    if x_tag =='$d_{K}$': plt.xlim(xmin = 0.15, xmax = 0.32)
    if x_tag =='\u03d5': plt.xlim(xmin = 0.808, xmax = 0.845)
    if x_tag =='d\u03b3/dt' or x_tag == 'I': plt.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0)), plt.xscale('log')
    if x_tag =='$P/E_{g}$': plt.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0))
    if y_tag =='$\u27E8 t_{\u03c4}^{*} \u27E9$ / $t_{N}$': plt.ylim(ymin = 0, ymax = 8E2)
    if y_tag =='$\u03c4_{c}/\u03c3_{yy}$': plt.ylim(ymin = 0)
    if y_tag =='$\u03c4_{c}/E_{g}$': plt.ylim(ymin = 0)
    if y_tag =='$P_{c}/\u03c3_{yy}$': plt.ylim(ymin = 0)
    if y_tag =='$\u03b2_{\u03c4}$' or y_tag =='$\u03b2_{P}$': plt.ylim(ymin = 0.8, ymax = 2.2), plt.axhline(1, color = 'silver', linewidth=0.3*linew)

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, labelspacing = label_space)
    #plt.savefig('ela_relax_t*_vs_G.png')
    plt.show()
    return

def stress_stress_plot(x_val1,x_val2,x_val3,x_val4,y_val1,y_val2,y_val3,y_val4,dmod1,dmod2,dmod3,dmod4,d_1,d_2,d_3,d_4,tag,colormap,x_tag,y_tag,no_ela,stacks,max_stack):
    # Function variables
    # Colors
    col_g = [colormap(0.9),colormap(0.5),colormap(0.3),colormap(0.2),colormap(0.1)]
    graph_len,graph_wid,font_title,font_axes,font_legend,label_space,linew,linew_fit,capsize,set_a = graph_rheo_param()
    mark = ['^','>','<','s']
    cut = 1
    cut_col = 4

    d_1_max = d_1.max()
    d_2_max = d_2.max()
    d_3_max = d_3.max()
    d_4_max = d_4.max()

    plt.figure(figsize= (graph_len,graph_wid))
    for i in range(cut,no_ela):
        for j in range(max_stack):
            #col_1, col_2, col_3, col_4 = colormap(d_1[i,j]/d_1_max), colormap(d_2[i,j]/d_2_max), colormap(d_3[i,j]/d_3_max) ,colormap(d_4[i,j]/d_4_max)
            if i == no_ela-1 and j == max_stack-1 :
                if stacks >= 1: plt.scatter(x_val1[i,j],y_val1[i,j],color=col_g[j],marker=mark[0],linewidth=linew,label=tag[0])
                if stacks >= 2: plt.scatter(x_val2[i,j],y_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew,label=tag[1])
                if stacks >= 3: plt.scatter(x_val3[i,j],y_val3[i,j],color=col_g[j],marker=mark[2],linewidth=linew,label=tag[2])
                if stacks >= 4: plt.scatter(x_val4[i,j],y_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew,label=tag[3])
            else :
                plt.scatter(x_val1[i,j],y_val1[i,j],color=col_g[j],marker=mark[0],linewidth=linew)
                plt.scatter(x_val2[i,j],y_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew)
                plt.scatter(x_val3[i,j],y_val3[i,j],color=col_g[j],marker=mark[2],linewidth=linew)
                plt.scatter(x_val4[i,j],y_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew)
            # end if
        # end of j for loop
    # end of i for loop

    for i in range(max_stack):
        if stacks >= 1:
            plt.fill_between(x_val1[cut:,i],y_val1[cut:,i]-dmod1[cut:,i],y_val1[cut:,i]+dmod1[cut:,i], color = col_g[j], alpha = 0.5*set_a)
        if stacks >= 2:
            plt.fill_between(x_val2[cut:,i],y_val2[cut:,i]-dmod2[cut:,i],y_val2[cut:,i]+dmod2[cut:,i], color = col_g[j], alpha = 0.5*set_a)
        if stacks >= 3:
            plt.fill_between(x_val3[cut:,i],y_val3[cut:,i]-dmod3[cut:,i],y_val3[cut:,i]+dmod3[cut:,i], color = col_g[j], alpha = 0.5*set_a)
        if stacks >= 4:
            plt.fill_between(x_val4[cut:,i],y_val4[cut:,i]-dmod4[cut:,i],y_val4[cut:,i]+dmod4[cut:,i], color = col_g[j], alpha = 0.5*set_a)
        # end if
    # end of i for loop

    x_fit = np.array([1E-4,2E-4,3E-4,4E-4,5E-4,6E-4,7E-4,8E-4,9E-4,1E-3,2E-3,3E-3,4E-3,5E-3,6E-3,7E-3,8E-3,9E-3,1E-2,2E-2,3E-2,4E-2,5E-2,6E-2,7E-2,8E-2,9E-2,1E-1,2E-1,3E-1,4E-1,5E-1,6E-1,7E-1,8E-1,9E-1,1,1.1,1.2])

    # reshape
    if x_tag == '$P_{c}/\u03c3_{yy}$':
        # concatenate
        x_val_fit = np.concatenate((x_val1,x_val2,x_val3))
        y_val_fit = np.concatenate((y_val1,y_val2,y_val3))

        # reshape
        x_val_fit = np.reshape(x_val_fit, max_stack*no_ela*(stacks-1), order='F')
        y_val_fit = np.reshape(y_val_fit, max_stack*no_ela*(stacks-1), order='F')

        # plot
        param, cv = sc.curve_fit(fc.power_fit, x_val_fit, y_val_fit, p0 = (0.4,0), method = 'trf')
        print("param = ", param), print("cv = ", cv)
        plt.plot(x_fit, x_fit*0.3, color='black', ls='-.', linewidth=linew)

    elif y_tag == '$G/\u03c3_{yy}$' or y_tag == '$K/\u03c3_{yy}$':
        # stack 1
        x_val_fit_1 = np.reshape(x_val1, max_stack*no_ela, order='F')
        y_val_fit_1 = np.reshape(y_val1, max_stack*no_ela, order='F')
        param1, cv1 = sc.curve_fit(fc.linear_fit, x_val_fit_1, y_val_fit_1) #, p0 = (-0.1,1E3), method = 'trf')
        print("param1 = ", param1), print("cv1 = ", cv1**0.5, "\n")

        x_fit = np.array([1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2])
        plt.plot(x_fit[:], param1[1]+x_fit[:]*param1[0], color='black', ls='-.', linewidth=linew)

        # stack 2
        x_val_fit_2 = np.reshape(x_val2, max_stack*no_ela, order='F')
        y_val_fit_2 = np.reshape(y_val2, max_stack*no_ela, order='F')
        param2, cv2 = sc.curve_fit(fc.linear_fit, x_val_fit_2, y_val_fit_2) #, p0 = (-0.05,1E3), method = 'trf')
        print("param2 = ", param2), print("cv2 = ", cv2**0.5, "\n")

        x_fit = np.array([1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2])
        plt.plot(x_fit[:], param2[1]+x_fit[:]*param2[0], color='black', ls='-.', linewidth=linew)

        # stack 3
        x_val_fit_3 = np.reshape(x_val3[:,:cut_col], (max_stack-1)*no_ela, order='F')
        y_val_fit_3 = np.reshape(y_val3[:,:cut_col], (max_stack-1)*no_ela, order='F')
        param3, cv3 = sc.curve_fit(fc.linear_fit, x_val_fit_3, y_val_fit_3) #, p0 = (-0.01,1E3), method = 'trf')
        print("param3 = ", param3), print("cv3 = ", cv3**0.5, "\n")

        x_fit = np.array([1E-3,2.5E-3,5E-3,7.5E-3,1E-2,2.5E-2])
        plt.plot(x_fit[:], param3[1]+x_fit[:]*param3[0], color='black', ls='-.', linewidth=linew)
    # end if

    #plt.title('Measured shear stress versus time of simulation t', fontsize = font_title)
    #if y_tag == '$G/\u03c3_{yy}$' or y_tag == '$K/\u03c3_{yy}$':
        #plt.xscale('log')
        #plt.yscale('log')
    # end if

    #plt.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    plt.xlabel(x_tag, fontsize = font_title), plt.ylabel(y_tag, fontsize = font_title)

    #plt.xlim(xmin = 0)
    plt.ylim(ymin = 8E2)

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, labelspacing = label_space)
    #plt.savefig('ela_relax_t*_vs_G.png')
    plt.show()
    return

def param_3D_plot(z_val1,z_val2,z_val3,z_val4,x_val1,x_val2,x_val3,x_val4,y_val1,y_val2,y_val3,y_val4,dmod1,dmod2,dmod3,dmod4,fit_coeff,tag,colormap,z_tag,x_tag,y_tag,fit_type,fit_print,no_ela,stacks,max_stack):
    # Function variables
    # Scalar
    cut = 1
    cut_g = 0 # graph cut column

    # Graph variables
    col_g = graph_color(colormap)
    #col_fit = [colormap(0),colormap(0.3),colormap(0.6),colormap(1)]
    mark = ['^','>','<','s']
    #mark = ['>','s','','']

    # define the reverse argument
    rev=False

    # size of the graphs
    graph_len,graph_wid,font_title,font_axes,font_legend,label_space,linew,linew_fit,capsize,set_a = graph_rheo_param()

    fig = plt.figure(figsize= (1.5*graph_len,1.5*graph_wid))
    ax = plt.axes(projection ="3d")

    for i in range(no_ela):
        for j in range(cut_g,max_stack):
            if i == no_ela-1 and j == max_stack-1 :
                if stacks >= 1:
                    ax.scatter3D(x_val1[i,j],y_val1[i,j],z_val1[i,j],color=col_g[j],marker=mark[0],linewidth=linew,label=tag[0])
                if stacks >= 2:
                    ax.scatter3D(x_val2[i,j],y_val2[i,j],z_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew,label=tag[1])
                if stacks >= 3:
                    ax.scatter3D(x_val3[i,j],y_val3[i,j],z_val3[i,j],color=col_g[j],marker=mark[2],linewidth=linew,label=tag[2])
                if stacks >= 4:
                    ax.scatter3D(x_val4[i,j],y_val4[i,j],z_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew,label=tag[3])
            else :
                ax.scatter3D(x_val1[i,j],y_val1[i,j],z_val1[i,j],color=col_g[j],marker=mark[0],linewidth=linew)
                ax.scatter3D(x_val2[i,j],y_val2[i,j],z_val2[i,j],color=col_g[j],marker=mark[1],linewidth=linew)
                ax.scatter3D(x_val3[i,j],y_val3[i,j],z_val3[i,j],color=col_g[j],marker=mark[2],linewidth=linew)
                ax.scatter3D(x_val4[i,j],y_val4[i,j],z_val4[i,j],color=col_g[j],marker=mark[3],linewidth=linew)
                # end if
            # end if
        # end of j for loop
    # end of i for loop

    #if z_tag == '$\u03d5$': ax.set_zlim(zmin = 0.75)

    ax.set_xlabel(x_tag,labelpad = 20*label_space,fontweight ='bold')
    ax.set_ylabel(y_tag,labelpad = 20*label_space,fontweight ='bold')
    ax.set_zlabel(z_tag,labelpad = 20*label_space,fontweight ='bold')

    plt.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0)), plt.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0)), plt.ticklabel_format(axis='z', style = 'sci', scilimits = (0,0))

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, labelspacing = label_space)
    #plt.savefig('ela_relax_t*_vs_G.png')
    plt.show()
    return

def graph_rheo(plateau1,plateau2,plateau3,plateau4,E,t,d,no_data,tag1,tag2,tag3,tag4,colormap_g,colormap_ela,fit,no_stack):
    # Variable
    # Scalar
    rheo_line = len(plateau1) # number of line of the plateau_N file
    rheo_col = 16 # number of column of the plateau_N file
    mu_eq = '' # equation of the mu(I) rheology

    txt_mu1 = '$µ_{c}$'
    txt_mu2 = '$µ_{2}$'
    txt_phi1 = '$\u03d5_{c}$'
    txt_phi2 = '$\u03d5_{min}$'

    data_len = 500 # number of value to compute rheology µ(I)

    iner_min = float(5*10**-5) # minimum inertial number for µ(I)
    iner_max = float(1*10**-1) # maximum inertial number for µ(I)

    d_iner = (iner_max-iner_min)/data_len
    len_global_rheo = 10

    # Vector
    tag_name = [tag1,tag2,tag3,tag4]

    # global vectors
    mu = np.zeros(len_global_rheo)
    phi = np.zeros(len_global_rheo)
    error = np.zeros(len_global_rheo)
    iner = np.array([1E-1,5.03E-2,1E-2,5.03E-3,1E-3,5E-3,1E-3,5E-4,1E-4,5E-5])

    cis_rheo = np.array([5E-4,1E-4,5E-5,1E-5,5E-6,3.75E-4,7.5E-5,3.75E-5,7.50E-6,3.75E-6,1.2E-4,2.5E-5,1.2E-5,2.5E-5,7.45E-5,3.75E-4,7.5E-5,3.75E-5,7.50E-6,3.75E-6])

    # Matrix
    plateau = np.zeros((len_global_rheo,rheo_col))

    # ref rheo
    mu_mui = np.zeros(data_len) # effective friction value for rheology µ(I)
    phi_mui = np.zeros(data_len) # packing fraction value for rheology µ(I)
    iner_mui = np.zeros(data_len) # effective friction value for rheology µ(I)
    error_mui = np.zeros(data_len)
    coeff_mu_i = np.zeros(3) # coeff of rheology mu_I

    plateau = fc.global_rheo_vec(plateau, plateau1, plateau2, plateau3, plateau4, rheo_line, no_data)
    print('τ std(τ) \u03a3_yy std(\u03a3_yy) φ std(φ) Z std(Z) Z_min std(Z_min) τ_max std(τ_max) d std(d)')
    print(plateau, '\n')

    for i in range(len_global_rheo):
        if plateau[i,2] != 0 :
            mu[i] = plateau[i,0] / plateau[i,2] # effective friction computation
            phi[i] = plateau[i,4]

            error_mui[i] = ((plateau[i,1]/plateau[i,0]) + (plateau[i,3]/plateau[i,2]))*mu[i]
            error[i] = plateau[i,5]
        if i == len_global_rheo-1 or i == len_global_rheo-2:
            mu[i] = mu[i-3]
            phi[i] = phi[i-3]
        # end if
    # end of i for loop
    print(mu), print(phi)

    if fit == 'yes':
        # Rheology parametes
        coeff_mu_i, error_mu_i = fc.mu_I_fit(iner[:], mu[:])
        coeff_phi, error_phi = fc.phi_fit(iner[:],phi[:])
        mu1 = round(coeff_mu_i[0],2)
        mu2 = round(coeff_mu_i[1],2)
        I0 = format(coeff_mu_i[2],'E')
        phi_c = round(coeff_phi[0],2)
        phi_min = round(coeff_phi[1],2)

        # create the legend for the mu_I fit
        mu_eq, phi_eq = f'{txt_mu1} = {mu1}, {txt_mu2} = {mu2}, $I_{0}$ = {I0}', f'{txt_phi1} = {phi_c}, {txt_phi2} = {phi_min}'

        for i in range(data_len):
            iner_mui[i] = iner_mui[i-1] + d_iner
            if i == 0 : iner_mui[i] = iner_min
            mu_mui[i] = coeff_mu_i[0] + ((coeff_mu_i[1] - coeff_mu_i[0])/((coeff_mu_i[2]/iner_mui[i])+1))
            phi_mui[i] = coeff_phi[0] - (coeff_phi[0] - coeff_phi[1])*iner_mui[i]
        # end of i for loop
    # end of if

    ## Plot begining##
    # Residual packing fraction versus imposed shear rate
    #rheo_fit(len_global_rheo, iner, phi, error, iner_mui, phi_mui, tag_name, colormap_g, 'I', '\u03d5', phi_eq, no_stack)

    # Effective friction rheology
    #rheo_fit(len_global_rheo, iner, mu, error_mui, iner_mui, mu_mui, tag_name, colormap_g, 'I', 'µ', mu_eq, no_stack)

    # Residual shear modulus damage versus imposed shear rate
    #rheo_plot(len_global_rheo,iner,plateau[:,12],plateau[:,13],tag_name,colormap_g,'I','$d_{G}',no_stack)

    # Residual shear modulus damage versus imposed shear rate
    #rheo_plot(len_global_rheo, iner, plateau[:,14], plateau[:,15], tag_name, colormap_g, 'I', '$d_{K}$', no_stack)

    # Coordination number versus imposed shear rate
    #rheo_plot(len_global_rheo, iner, plateau[:,6], plateau[:,7], tag_name, colormap_g, 'I', 'Z', no_stack)

    # Min of coordination number
    #rheo_plot(len_global_rheo, iner, plateau[:,8], plateau[:,9], tag_name, colormap_g, 'I', '$Z_{min}', no_stack)

    # Stress versus inertial number I
    #rheo_plot(len_global_rheo, iner, plateau[:,0], plateau[:,1], tag_name, colormap_g, 'I', '\u03c4 (Pa)', no_stack)

    # Maximum of shear stress
    #rheo_plot(len_global_rheo, iner, plateau[:,10], plateau[:,11], tag_name, colormap_g, 'I', '$\u03c4_{max}$ (Pa)', no_stack)
    return

def param_ela_graph(x1,x2,x3,x4,y_1_1,y_1_2,y_1_3,y_1_4,y_2_1,y_2_2,y_2_3,y_2_4,dy_1_1,dy_1_2,dy_1_3,dy_1_4,dy_2_1,dy_2_2,dy_2_3,dy_2_4,fit_1,fit_2,no_data,tag1,tag2,tag3,tag4,colormap,no_ela,stacks,max_stacks,type_plot):
    # Function variables
    # Vector
    tag_name = [tag1,tag2,tag3,tag4]

    if type_plot == 'phi_ela' or type_plot == 'z_ela' or type_plot == 'P_ela':
        label_y1 = '$G/\u03c3_{yy}$'
        label_y2 = '$K/\u03c3_{yy}$'
        if type_plot == 'phi_ela': label_x = '\u03d5'
        elif type_plot == 'z_ela': label_x = 'Z'
        elif type_plot == 'P_ela':
            label_x, label_y1, label_y2 = '$P/E_{g}$', '$G/E_{g}$', '$K/E_{g}$'
    if type_plot == 'ela_ela':
        label_x, label_y1, label_y2 = '$K/E_{g}$', '$G/E_{g}$', '$K/E_{g}$'
        # end if
    elif type_plot == 'phi_dam' or type_plot == 'z_dam':
        if type_plot == 'phi_dam': label_x = '\u03d5'
        if type_plot == 'z_dam': label_x = 'Z'
        label_y1, label_y2 = '$d_{G}$', '$d_{K}$'
    # end if

    if type_plot == 'ela_ela': param_plot(x1,x2,x3,x4,y_1_1,y_1_2,y_1_3,y_1_4,dy_1_1,dy_1_2,dy_1_3,dy_1_4,fit_1,tag_name,colormap,label_x,label_y1,'yes',no_ela,stacks,max_stacks)
    else :
        param_plot(x1,x2,x3,x4,y_1_1,y_1_2,y_1_3,y_1_4,dy_1_1,dy_1_2,dy_1_3,dy_1_4,fit_1,tag_name,colormap,label_x,label_y1,'yes',no_ela,stacks,max_stacks)
        param_plot(x1,x2,x3,x4,y_2_1,y_2_2,y_2_3,y_2_4,dy_2_1,dy_2_2,dy_2_3,dy_2_4,fit_2,tag_name,colormap,label_x,label_y2,'yes',no_ela,stacks,max_stacks)
    # end if
    return

def param_relax_graph(type_data,val_1,val_2,val_3,val_4,param1_1,param1_2,param1_3,param1_4,param2_1,param2_2,param2_3,param2_4,dparam1_1,dparam1_2,dparam1_3,dparam1_4,dparam2_1,dparam2_2,dparam2_3,dparam2_4,tag1,tag2,tag3,tag4,colormap,no_ela,stacks,max_stacks):
    # Function variables
    # Vector
    tag_name = [tag1,tag2,tag3,tag4]

    # Matrix
    iner = np.zeros((no_ela,max_stacks))
    val1 = np.zeros((no_ela,max_stacks))
    val2 = np.zeros((no_ela,max_stacks))
    val3 = np.zeros((no_ela,max_stacks))
    val4 = np.zeros((no_ela,max_stacks))

    # ylabel Legend initialisation
    if type_data == 'cis_time':
        val1, val2, val3, val4 = graph_cis(no_ela, max_stacks)
        xlabel, ylabel_sh, ylabel_p = 'd\u03b3/dt', '$t_{\u03c4}^{*} / t_{N}$', '$t_{P}^{*} / t_{N}$'
    else :
        val1, val2, val3, val4 = val_1, val_2, val_3, val_4
        if type_data == 'phi_time' or type_data == 'phi_visc' or type_data == 'phi_stress' or type_data == 'phi_beta': xlabel = '$\u03d5$'
        if type_data == 'P_time' or type_data == 'P_stress' or type_data == 'P_beta': xlabel = '$P/E_{g}$'
        if type_data == 'phi_visc':
           ylabel_sh, ylabel_p = '$\u03b7 / (E_{g} \u00b7 t_{N})$', '$\u03b6 / (E_{g} \u00b7 t_{N})$'
        if type_data == 'P_time' or type_data == 'phi_time':
            ylabel_sh, ylabel_p = '$t_{\u03c4}^{*} / t_{N}$', '$t_{P}^{*} / t_{N}$'
        if type_data == 'P_stress' or type_data == 'phi_stress':
            ylabel_sh, ylabel_p = '$s_{c}/\u03c3_{yy}$', '$P_{c}/\u03c3_{yy}$'
        if type_data == 'P_beta' or type_data == 'phi_beta':
            ylabel_sh, ylabel_p = '$\u03b2_{\u03c4}$', '$\u03b2_{P}$'
        if type_data == 'stress_stress':
            xlabel, ylabel = '$P_{c}/\u03c3_{yy}$', '$|s_{c}|/\u03c3_{yy}$'
        if type_data == 'shear_t_shear':
            xlabel, ylabel = '$t_{N}/t_{\u03c4}^{*}$', '$G/\u03c3_{yy}$'
        if type_data == 'press_t_press':
            xlabel, ylabel = '$t_{N}/t_{P}^{*}$', '$K/\u03c3_{yy}$'
    # end if

    # iner initialisation
    for i in range(no_ela):
        for j in range(max_stacks):
            if j == 0 : iner[i,j] = 5E-3
            elif j == 1 : iner[i,j] = 1E-3
            elif j == 2 : iner[i,j] = 5E-4
            elif j == 3 : iner[i,j] = 1E-4
            elif j == 4 : iner[i,j] = 5E-5
        # end of j for loop
    # end of i for loop

    if type_data == 'shear_t_shear' or type_data == 'press_t_press':
        param2_1_inv = np.zeros((no_ela,max_stacks))
        param2_2_inv = np.zeros((no_ela,max_stacks))
        param2_3_inv = np.zeros((no_ela,max_stacks))
        param2_4_inv = np.zeros((no_ela,max_stacks))
        for i in range(no_ela):
            for j in range(max_stacks):
                if param2_1[i,j] != 0: param2_1_inv[i,j] = 1/param2_1[i,j]
                if param2_2[i,j] != 0: param2_2_inv[i,j] = 1/param2_2[i,j]
                if param2_3[i,j] != 0: param2_3_inv[i,j] = 1/param2_3[i,j]
                if param2_4[i,j] != 0: param2_4_inv[i,j] = 1/param2_4[i,j]
    # end if

    if type_data == 'stress_stress' or type_data == 'shear_t_shear' or type_data == 'press_t_press':
        # param sh vs param p
        #param_relax_plot(param1_1,param1_2,param1_3,param1_4,param2_1,param2_2,param2_3,param2_4,dparam2_1,dparam2_2,dparam2_3,dparam2_4,tag_name,colormap,xlabel,ylabel,no_ela,stacks,max_stacks)
        stress_stress_plot(param2_1_inv,param2_2_inv,param2_3_inv,param2_4_inv,param1_1,param1_2,param1_3,param1_4,dparam1_1,dparam1_2,dparam1_3,dparam1_4,val_1,val_2,val_3,val_4,tag_name,colormap,xlabel,ylabel,no_ela,stacks,max_stacks)
    else :
        # param_sh versus phi
        param_relax_plot(val1,val2,val3,val4,param1_1,param1_2,param1_3,param1_4,dparam1_1,dparam1_2,dparam1_3,dparam1_4,tag_name,colormap,xlabel,ylabel_sh,no_ela,stacks,max_stacks)

        # param_p versus phi
        param_relax_plot(val1,val2,val3,val4,param2_1,param2_2,param2_3,param2_4,dparam2_1,dparam2_2,dparam2_3,dparam2_4,tag_name,colormap,xlabel,ylabel_p,no_ela,stacks,max_stacks)

        # param_sh versus I
        #param_relax_plot(iner,iner,iner,iner,param1_1,param1_2,param1_3,param1_4,dparam1_1,dparam1_2,dparam1_3,dparam1_4,tag_name,colormap,'I',ylabel_sh,no_ela,stacks,max_stacks)

        # param_p versus I
        #param_relax_plot(iner,iner,iner,iner,param2_1,param2_2,param2_3,param2_4,dparam2_1,dparam2_2,dparam2_3,dparam2_4,tag_name,colormap,'I',ylabel_p,no_ela,stacks,max_stacks)
    # end if
    return

def visc_graph(d1,d2,d3,d4,mod_eff1,mod_eff2,mod_eff3,mod_eff4,dmod_eff1,dmod_eff2,dmod_eff3,dmod_eff4,no_data,tag1,tag2,tag3,tag4,data_type,colormap,no_ela,stacks,max_stacks):
    # Function variables
    # Scalar
    tag_name = [tag1,tag2,tag3,tag4]
    #xlabel = 'I'
    if data_type == 'visc_sh':
        xlabel = '$d_{G}$'
        ylabel = '$\u03b7 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_p':
        xlabel = '$d_{K}$'
        ylabel = '$\u03b6 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_sh_I':
        xlabel = '$I$'
        ylabel = '$\u03b7 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_p_I':
        xlabel = '$I$'
        ylabel = '$\u03b6 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_sh_g':
        xlabel = '$d \u03b3 / dt$'
        ylabel = '$\u03b7 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_p_g':
        xlabel = '$d \u03b3 / dt$'
        ylabel = '$\u03b6 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_sh_p':
        xlabel = '$P/E_{g}$'
        ylabel = '$\u03b7 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_p_p':
        xlabel = '$P/E_{g}$'
        ylabel = '$\u03b6 / (E_{g} \u00b7 t_{N})$'
    if data_type == 'visc_visc':
        xlabel = '$\u03b6 / (E_{g} \u00b7 t_{N})$'
        ylabel = '$\u03b7 / (E_{g} \u00b7 t_{N})$'
    # end if

    # Vector
    cut_line = np.array([13,13,13,16,19])

    # Matrix
    d_1 = np.zeros((no_ela,max_stacks))
    d_2 = np.zeros((no_ela,max_stacks))
    d_3 = np.zeros((no_ela,max_stacks))
    d_4 = np.zeros((no_ela,max_stacks))
    for j in range(max_stacks):
        cut_lin = cut_line[j]
        for i in range(no_ela):
            if i >= cut_lin :
                # damage attribution
                d_1[i,j] = d1[i,j]
                d_2[i,j] = d2[i,j]
                d_3[i,j] = d3[i,j]
                d_4[i,j] = d4[i,j]
            else :
                d_1[i,j] = np.nan
                d_2[i,j] = np.nan
                d_3[i,j] = np.nan
                d_4[i,j] = np.nan
        # end of i for loop
    # end of j for loop

    if data_type == 'visc_visc': visc_plot(d_1,d_2,d_3,d_4,mod_eff1,mod_eff2,mod_eff3,mod_eff4,dmod_eff1,dmod_eff2,dmod_eff3,dmod_eff4,tag_name,colormap,xlabel,ylabel,no_ela,stacks,max_stacks)
    else :
        # computed viscosity vs damage
        #visc_plot(d_1,d_2,d_3,d_4,mod_eff1,mod_eff2,mod_eff3,mod_eff4,dmod_eff1,dmod_eff2,dmod_eff3,dmod_eff4,tag_name,colormap,xlabel,ylabel,no_ela,stacks,max_stacks)

        # computed viscosity vs I
        visc_plot(d_1,d_2,d_3,d_4,mod_eff1,mod_eff2,mod_eff3,mod_eff4,dmod_eff1,dmod_eff2,dmod_eff3,dmod_eff4,tag_name,colormap,xlabel,ylabel,no_ela,stacks,max_stacks)
    # end if
    return

def param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,param1_1,param1_2,param1_3,param1_4,param2_1,param2_2,param2_3,param2_4,d_1_1,d_1_2,d_1_3,d_1_4,d_2_1,d_2_2,d_2_3,d_2_4,fit_sh,fit_p,no_data,tag1,tag2,tag3,tag4,ylabel,colormap,no_ela,stacks,max_stacks):
    # Function variables
    # Vector
    tag_name = [tag1,tag2,tag3,tag4]
    #tag_name = ['','','','']

    xlabel_sh,  xlabel_p = '$d_{G}$', '$d_{K}$'
    if ylabel == 'ela_mod': ylabel_sh, ylabel_p = '$G/\u03c3_{yy}$', '$K/\u03c3_{yy}$'
    if ylabel == 'time_*':  ylabel_sh, ylabel_p = '$t_{\u03c4}^{*} / t_{N}$', '$t_{P}^{*} / t_{N}$'
    if ylabel == 'time_*_q': ylabel_sh, ylabel_p ='$t_{s}^{*} / t_{N}$', '$t_{P}^{*} / t_{N}$'
    if ylabel == 'sigma_c': ylabel_sh, ylabel_p = '$\u03c4_{c}/\u03c3_{yy}$', '$P_{c}/\u03c3_{yy}$'
    if ylabel == 'nu': xlabel_p, ylabel_sh, ylabel_p = '$d_{E}$', '$\u03c4_{c}/\u03c3_{yy}$', '$\u03bd_{2D}$'
    if ylabel == 'sigma_c_q': ylabel_sh, ylabel_p = '$s_{c}/\u03c3_{yy}$', '$P_{c}/\u03c3_{yy}$'
    if ylabel == 'sigma_c_q': ylabel_sh, ylabel_p = '$s_{c}/\u03c3_{yy}$', '$P_{c}/\u03c3_{yy}$'
    if ylabel == 'mu_c': ylabel_mu = '$\u03bc_{M}$'
    if ylabel == 'beta': ylabel_sh, ylabel_p = '$\u03b2_{\u03c4}$', '$\u03b2_{P}$'
    if ylabel == 'visc':
        ylabel_sh, ylabel_p = '$\u03b7 / (E_{g} \u00b7 t_{N})$', '$\u03b6 / (E_{g} \u00b7 t_{N})$'
    if ylabel == 'iner':
        xlabel_sh, xlabel_p = '$I$', '$I$'
        ylabel_sh, ylabel_p = '$s_{c}/\u03c3_{yy}$', '$P_{c}/\u03c3_{yy}$'
    # end if

    # Matrix
    iner_1 = np.zeros((no_ela,max_stacks))
    iner_2 = np.zeros((no_ela,max_stacks))
    iner_3 = np.zeros((no_ela,max_stacks))
    iner_4 = np.zeros((no_ela,max_stacks))

    for j in range(max_stacks):
        # inertial number attribution
        if j == 0 : iner_1[:,j],iner_2[:,j],iner_3[:,j],iner_4[:,j] = 5E-3, 5E-3, 5E-3, 5E-3
        if j == 1 : iner_1[:,j],iner_2[:,j],iner_3[:,j],iner_4[:,j] = 1E-3, 1E-3, 1E-3, 1E-3
        if j == 2 : iner_1[:,j],iner_2[:,j],iner_3[:,j],iner_4[:,j] = 5E-4, 5E-4, 5E-4, 5E-4
        if j == 3 : iner_1[:,j],iner_2[:,j],iner_3[:,j],iner_4[:,j] = 1E-4, 1E-4, 1E-4, 1E-4
        if j == 4 : iner_1[:,j],iner_2[:,j],iner_3[:,j],iner_4[:,j] = 5E-5, 5E-5, 5E-5, 5E-5
        # end of i for loop
    # end of j for loop

    if ylabel == 'mu_c':
        mu_c_1, dmu_c_1 = fc.eff_res_fric(param1_1, param2_1, d_1_1, d_2_1, no_ela, max_stacks)
        mu_c_2, dmu_c_2 = fc.eff_res_fric(param1_2, param2_2, d_1_2, d_2_2, no_ela, max_stacks)
        mu_c_3, dmu_c_3 = fc.eff_res_fric(param1_3, param2_3, d_1_3, d_2_3, no_ela, max_stacks)
        mu_c_4, dmu_c_4 = fc.eff_res_fric(param1_4, param2_4, d_1_4, d_2_4, no_ela, max_stacks)
    # end if

    if ylabel == 'nu': param_plot(dam_K_1,dam_K_2,dam_K_3,dam_K_4,param2_1,param2_2,param2_3,param2_4,d_2_1,d_2_2,d_2_3,d_2_4,fit_p,tag_name,colormap,xlabel_p,ylabel_p,'yes',no_ela,stacks,max_stacks)
    elif ylabel == 'iner':
        param_plot(iner_1,iner_2,iner_3,iner_4,param1_1,param1_2,param1_3,param1_4,d_1_1,d_1_2,d_1_3,d_1_4,fit_p,tag_name,colormap,xlabel_p,ylabel_p,'yes',no_ela,stacks,max_stacks)
        param_plot(iner_1,iner_2,iner_3,iner_4,param2_1,param2_2,param2_3,param2_4,d_2_1,d_2_2,d_2_3,d_2_4,fit_p,tag_name,colormap,xlabel_p,ylabel_p,'yes',no_ela,stacks,max_stacks)
    elif ylabel == 'mu_c' :
        param_plot(dam_G_1,dam_G_2,dam_G_3,dam_G_4,mu_c_1,mu_c_2,mu_c_3,mu_c_4,dmu_c_1,dmu_c_2,dmu_c_3,dmu_c_4,fit_sh,tag_name,colormap,'$d_{G}$',ylabel_mu,'yes',no_ela,stacks,max_stacks)
        param_plot(dam_K_1,dam_K_2,dam_K_3,dam_K_4,mu_c_1,mu_c_2,mu_c_3,mu_c_4,dmu_c_1,dmu_c_2,dmu_c_3,dmu_c_4,fit_sh,tag_name,colormap,'$d_{K}$',ylabel_mu,'yes',no_ela,stacks,max_stacks)
    else :
        # d_G versus param1
        param_plot(dam_G_1,dam_G_2,dam_G_3,dam_G_4,param1_1,param1_2,param1_3,param1_4,d_1_1,d_1_2,d_1_3,d_1_4,fit_sh,tag_name,colormap,xlabel_sh,ylabel_sh,'yes',no_ela,stacks,max_stacks)

        # d_K versus param2
        param_plot(dam_K_1,dam_K_2,dam_K_3,dam_K_4,param2_1,param2_2,param2_3,param2_4,d_2_1,d_2_2,d_2_3,d_2_4,fit_p,tag_name,colormap,xlabel_p,ylabel_p,'yes',no_ela,stacks,max_stacks)

        # param2 versus param1
        #param_plot(param2_1,param2_2,param2_3,param2_4,param1_1,param1_2,param1_3,param1_4,d_1_1,d_1_2,d_1_3,d_1_4,fit_sh,tag_name,colormap,ylabel_p,ylabel_sh,'yes',no_ela,stacks,max_stacks)
    # end if
    return

def param_dam_3D_graph(press1,press2,press3,press4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,param1_1,param1_2,param1_3,param1_4,param2_1,param2_2,param2_3,param2_4,d_1_1,d_1_2,d_1_3,d_1_4,d_2_1,d_2_2,d_2_3,d_2_4,fit_sh,fit_p,no_data,tag1,tag2,tag3,tag4,ylabel,xlabel,colormap,no_ela,stacks,max_stacks):
    # Function variables
    # Vector
    tag_name = [tag1,tag2,tag3,tag4]
    #tag_name = ['','','','']

    if ylabel == 'ela_mod': ylabel_sh, ylabel_p, fit = '$G/\u03c3_{yy}$','$K/\u03c3_{yy}$', 'linear'
    if ylabel == 'time_*': ylabel_sh, ylabel_p, fit = '$t_{\u03c4}^{*} / t_{N}$', '$t_{P}^{*} / t_{N}$', ''
    if ylabel == 'sigma_c': ylabel_sh, ylabel_p, fit = '$\u03c4_{c}/\u03c3_{yy}$', '$P_{c}/\u03c3_{yy}$', 'sigmoyy'
    if ylabel == 'beta': ylabel_sh, ylabel_p, fit = '$\u03b2_{\u03c4}$', '$\u03b2_{P}$', ''
    if ylabel == 'visc': ylabel_sh, ylabel_p, fit = '$\u03b7 / (\u03c3_{yy} \u00b7 t_{N})$', '$\u03b6 / (\u03c3_{yy} \u00b7 t_{N})$', ''
    if xlabel == 'phi': xlabel = '$\u03d5$'
    if xlabel == 'press': xlabel = '$P/E_{g}$'

    # d_G versus param1
    param_3D_plot(press1,press2,press3,press4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,param1_1,param1_2,param1_3,param1_4,d_1_1,d_1_2,d_1_3,d_1_4,fit_sh,tag_name,colormap,xlabel,'$d_{G}$',ylabel_sh,fit,'yes',no_ela,stacks,max_stacks)

    # d_K versus param2
    param_3D_plot(press1,press2,press3,press4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,param2_1,param2_2,param2_3,param2_4,d_2_1,d_2_2,d_2_3,d_2_4,fit_p,tag_name,colormap,xlabel,'$d_{K}$',ylabel_p,fit,'yes',no_ela,stacks,max_stacks)

    # d_G versus mu_c
    #if ylabel == 'sigma_c': param_plot(dam_G_1,dam_G_2,dam_G_3,dam_G_4,mu_c_1,mu_c_2,mu_c_3,mu_c_4,dmu_c_1,dmu_c_2,dmu_c_3,dmu_c_4,fit_1_dam,tag_name,colormap,'$d_{G}$',ylabel_sh,fit,'yes',no_ela,stacks,max_stacks)
    return