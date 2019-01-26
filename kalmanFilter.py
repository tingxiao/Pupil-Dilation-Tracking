import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
from filterpy.kalman import FixedLagSmoother, KalmanFilter
import numpy.random as random

def applyKalmanFilter(csv_file, kalman_file):

    # Read in csv file into a seperate dataframe
    csvFile = pd.read_csv(csv_file, header=None, dtype=np.float64)
    d = csvFile[1].values

    
    fls = FixedLagSmoother(dim_x=2, dim_z=1, N=8)
    
    fls.x = np.array([0., .5])
    fls.F = np.array([[1.,1.],
                      [0.,1.]])
    
    fls.H = np.array([[1.,0.]])
    fls.P *= 200
    fls.R *= 5.
    fls.Q *= 0.001
    
    kf = KalmanFilter(dim_x=2, dim_z=1)
    kf.x = np.array([0., .5])
    kf.F = np.array([[1.,1.],
                     [0.,1.]])
    kf.H = np.array([[1.,0.]])
    kf.P *= 200
    kf.R *= 1
    kf.Q *= 0.0002
    
    N = 4 # size of lag
    
    #set zs equal to dataframe variable
    zs = d
    
    nom =  np.array([t/2. for t in range (0, len(zs))])
    
    for z in zs:
        fls.smooth(z)
        
    kf_x, _, _, _ = kf.batch_filter(zs)
    x_smooth = np.array(fls.xSmooth)[:, 0]
    
    fls_res = abs(x_smooth - nom)
    kf_res = abs(kf_x[:, 0] - nom)
    
    plt.plot(zs,'o', alpha=0.5, marker='o', label='zs')
    plt.plot(x_smooth, label='FLS')
    plt.plot(kf_x[:, 0], label='KF', ls='--')
    plt.legend(loc=4)
    
   # print('standard deviation fixed-lag: {:.3f}'.format(np.mean(fls_res)))
   # print('standard deviation kalman: {:.3f}'.format(np.mean(kf_res)))
   # print(x_smooth[:])#input frame value to print smoothed x val at that point
    
    
    #----
    
    zs = zs.reshape((len(zs), 1))
    zs = pd.DataFrame(zs, columns = ['Original'])
    
    #putting smoothed values (array x_smooth) into a DF
    smoothedVals = pd.DataFrame(x_smooth[:], columns = ['Smoothed'])
    
    #---
    
    
    with open (kalman_file, 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator = '\n', delimiter=' ')
        for num in x_smooth:
            writer.writerow([num])
