'''
Computes Eigen images of a given dataset of images. (Generally used for face images)
Reconstruct original image from eigen images.
'''

# Imports
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report

# Main Functions
# PCA
def PCA(X, n_pc):
    n_samples, n_features = X.shape
    mean = np.mean(X, axis=0)
    centered_data = X-mean
    U, S, V = np.linalg.svd(centered_data)
    components = V[:n_pc]
    projected = U[:,:n_pc]*S[:n_pc]
    
    return projected, components, mean, centered_data


def ReconstructImage(Y, C, M, h, w, image_index):
    n_samples, n_features = Y.shape
    weights = np.dot(Y, C.T)
    centered_vector = np.dot(weights[image_index, :], C)
    recovered_image = (M + centered_vector).reshape(h, w)
    return recovered_image

# Plot Functions
def PlotPotraits(images, titles, h, w, n_row, n_col):
    plt.figure(figsize=(2.2 * n_col, 2.2 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.20)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.xticks(())
        plt.yticks(())
    plt.show()

# Generate Functions
def GenerateRandomImage(N_IMAGES, IMAGE_SIZE):
    '''
    Generates N_IMAGES random images of size IMAGE_SIZE
    '''
    # Generate random images
    GenSize = tuple([N_IMAGES] + list(IMAGE_SIZE))
    Images = np.random.rand(*GenSize)
    return Images


# Driver Code
# Params
dataset_dir = 'Codes/Datasets/lfwcrop_grey/faces'

N_IMAGES = 1000

n_components = 50
# Params

# RunCode
# Load Images
print(f"Loading {N_IMAGES} Images...")
ImagesNames = os.listdir(dataset_dir)[:N_IMAGES]
ImagesPaths = [dataset_dir + '/' + photo for photo in ImagesNames]
Images = np.array([plt.imread(image) for image in ImagesPaths], dtype=np.float64)
ImageTitles = [name[:name.find('0')-1].replace("_", " ") for name in ImagesNames]
n_samples, h, w = Images.shape
print("Loaded Images.")

# Plot Images
PlotPotraits(Images, ImageTitles, h, w, n_row=4, n_col=4)

# PCA
print("Performing PCA...")
X = Images.reshape(n_samples, h*w)
P, C, M, Y = PCA(X, n_pc=n_components)
eigenfaces = C.reshape((n_components, h, w))
eigenface_titles = ["Eigenface %d" % i for i in range(eigenfaces.shape[0])]
print("PCA Cpmpleted.")

# Plot EigenFaces
PlotPotraits(eigenfaces, eigenface_titles, h, w, 4, 4)

# Reconstruct Images
print("Reconstructing Images...")
Images_Reconstructed = [ReconstructImage(Y, C, M, h, w, i) for i in range(len(Images))]
PlotPotraits(Images_Reconstructed, ImageTitles, h, w, n_row=4, n_col=4)
print("Reconstruction Completed.")

# Comparison Plot
ComparisonImages = []
ComparisonTitles = []
for i in tqdm(range(len(Images))):
    ComparisonImages.append(Images[i])
    ComparisonTitles.append(ImageTitles[i] + " - Original")
    ComparisonImages.append(Images_Reconstructed[i])
    ComparisonTitles.append(ImageTitles[i] + " - Reconstructed")
    ComparisonImages.append(np.abs(Images[i] - Images_Reconstructed[i]))
    ComparisonTitles.append(ImageTitles[i] + " - Error")
PlotPotraits(ComparisonImages, ComparisonTitles, h, w, n_row=4, n_col=3)