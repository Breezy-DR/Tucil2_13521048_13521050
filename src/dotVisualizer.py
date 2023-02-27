from matplotlib import pyplot as plt

def plot3D(xClosest, yClosest, zClosest, xOthers, yOthers, zOthers):
    # Menggambarkan semua titik dalam bidang 3D
    # Sepasang titik yang jaraknya terdekat ditunjukkan dengan warna merah, 
    # sedangkan titik lainnya ditunjukkan dengan warna hijau
    plt.rcParams["figure.figsize"] = [12, 9]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    axis = fig.add_subplot(projection="3d")
    axis.scatter(xOthers, yOthers,zOthers, c='green')
    axis.scatter(xClosest,yClosest,zClosest, c='red')
    plt.show()

# xClosest = [1,2]
# yClosest = [3,4]
# zClosest = [5,6]
# xOthers = [2,3,4]
# yOthers = [5,6,7]
# zOthers = [8,9,10]

# plot3D(xClosest,yClosest,zClosest,xOthers,yOthers,zOthers)
