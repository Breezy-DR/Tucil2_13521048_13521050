from matplotlib import pyplot as plt

def plot3D(xClosest, yClosest, zClosest, xOthers, yOthers, zOthers):
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    axis = fig.add_subplot(projection="3d")
    axis.scatter(xOthers, yOthers,zOthers, c='black')
    axis.scatter(xClosest,yClosest,zClosest, c='red')