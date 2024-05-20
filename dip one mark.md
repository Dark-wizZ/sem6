### Unit 1

1. **What is a Digital Image?**
   - A digital image is a representation of a two-dimensional image as a finite set of digital values, called pixels.

2. **List the applications of Gamma-Ray Imaging and Ultraviolet Imaging.**
   - Gamma-Ray Imaging: Medical imaging (e.g., PET scans), industrial inspection.
   - Ultraviolet Imaging: Fluorescence imaging, biological research, forensic analysis.

3. **Define 8 Adjacency of a pixel.**
   - 8 adjacency refers to the 8 surrounding pixels of a given pixel in a 2D grid.

4. **Recall the formula for City-Block Distance.**
   - \( D_4(p, q) = |x - s| + |y - t| \)

5. **Show the MATLAB command to read and write an image.**
   - Read: `img = imread('filename.png');`
   - Write: `imwrite(img, 'newfilename.png');`

6. **What is the formula for calculating the city-block distance between two pixels P and Q with coordinates (x,y) and (s,t) respectively?**
   - \( D_4(p, q) = |x - s| + |y - t| \)

7. **Show the MATLAB command to convert an image from RGB to grayscale.**
   - `gray_img = rgb2gray(rgb_img);`

### Unit 2

1. **What is High pass and Low pass filtering?**
   - High pass filtering emphasizes high-frequency components (edges).
   - Low pass filtering emphasizes low-frequency components (smooth areas).

2. **Define High Boost filtering.**
   - High Boost filtering enhances high-frequency components by adding a scaled version of the original image to a high-pass filtered image.

3. **Recall the formula for Power law and Logarithmic Gray level Transformations.**
   - Power law: \( s = c \cdot r^\gamma \)
   - Logarithmic: \( s = c \cdot \log(1 + r) \)

4. **State the purpose of sharpening.**
   - Sharpening enhances the edges and fine details in an image.

5. **Recall the equation for Discrete Fourier Transform.**
   - \( X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j \frac{2\pi}{N} kn} \)

6. **Define Histogram.**
   - A histogram is a graphical representation of the distribution of pixel intensity values in an image.

7. **List down any two operators used as masks in Image sharpening.**
   - Sobel operator, Laplacian operator.

### Unit 3

1. **Define Image Segmentation.**
   - Image segmentation is the process of partitioning an image into meaningful regions or objects.

2. **List the response of the mask for vertical and -45 degree line.**
   - Vertical: Detects vertical edges.
   - -45 degree: Detects edges at -45 degrees.

3. **Recall Gradient operator for Laplacian for Detecting edges in an image.**
   - Laplacian: \( \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} \)

4. **Define region growing.**
   - Region growing is a technique for segmenting an image by starting with seed points and growing regions by appending neighboring pixels that meet a similarity criterion.

5. **Recall global and local thresholding.**
   - Global thresholding uses a single threshold value for the entire image.
   - Local thresholding uses different threshold values for different regions of the image.

6. **Define Sobel Operator.**
   - The Sobel operator is a gradient-based edge detection operator that uses convolution with a pair of 3x3 kernels.

7. **Define Gradient operator for Laplacian for Detecting edges in an image.**
   - Same as in point 3 above.

8. **What is an edge?**
   - An edge is a boundary between two regions with different intensity levels in an image.

9. **What is global and local thresholding?**
   - Same as in point 5 above.

10. **List the applications of segmentation.**
    - Medical imaging, object detection, image recognition.

11. **List the response of the mask for vertical and -45 degree line.**
    - Same as in point 2 above.

12. **List out the steps involved in splitting and merging.**
    - Split if homogeneity criterion is not met.
    - Merge if neighboring regions meet the homogeneity criterion.

13. **What is the condition to be met by the partitions in region-based segmentation?**
    - Partitions must be homogeneous and cover the entire image without overlap.

14. **What is multilevel thresholding?**
    - Multilevel thresholding divides an image into multiple regions based on multiple threshold values.

### Unit 4

1. **What is Sub-band coding?**
   - Sub-band coding is a method of image compression that divides the image into frequency bands and encodes each band separately.

2. **Lists the type of basic data redundancies present in Digital Image Compression.**
   - Spatial redundancy, spectral redundancy, temporal redundancy.

3. **Define image pyramid.**
   - An image pyramid is a collection of images, each representing a different level of resolution.

4. **What is the purpose of image pyramids?**
   - To provide multi-resolution representations of an image, facilitating efficient processing at different scales.

5. **What are the types of data redundancy?**
   - Same as in point 2 above.

6. **State the expansion for JPEG.**
   - Joint Photographic Experts Group.

7. **Define Image Pyramid.**
   - Same as in point 3 above.

8. **What are the error-free compression techniques used?**
   - Huffman coding, Lempel-Ziv-Welch (LZW) coding.

9. **List the types of Basic Data Redundancies present in Digital Image Compression.**
   - Same as in point 2 above.

10. **What are Topological descriptors?**
    - Topological descriptors describe the spatial relationships and properties of objects within an image.

11. **What is Sub-band coding?**
    - Same as in point 1 above.

12. **What are the applications of compression?**
    - Image storage, image transmission, multimedia applications.

13. **List the Image Compression Standards.**
    - JPEG, JPEG2000, MPEG.

14. **List the two general classes of fidelity criteria.**
    - Objective fidelity, subjective fidelity.

15. **Draw the block diagram of image compression model.**
    - (Not applicable for text response)

16. **Write the goal of transformation process in transform coding.**
    - To concentrate the image energy into a few coefficients, enabling efficient compression.

### Unit 5

1. **Define Image Watermarking.**
   - Image watermarking is the process of embedding information into an image to protect its copyright or authenticity.

2. **Define skeleton in Image Representation Schemes.**
   - A skeleton is a thin version of an object that represents its general shape and structure.

3. **What is skeleton?**
   - Same as in point 2 above.

4. **What is the equation for representing opening and closing operation?**
   - Opening: \( A \circ B = (A \ominus B) \oplus B \)
   - Closing: \( A \bullet B = (A \oplus B) \ominus B \)

5. **State any two applications of digital image processing.**
   - Medical imaging, facial recognition.

6. **What is the Euler number for a cube?**
   - Euler number = \( V - E + F = 8 - 12 + 6 = 2 \) (Note: Usually, for 2D shapes, the Euler number is calculated; for a cube, it might be confusing without proper context.)

7. **Define reflection and translation of a set B.**
   - Reflection: Flipping the set B over a line or point.
   - Translation: Shifting the set B by a certain distance in a given direction.

8. **What is a Signature in Image Representation scheme?**
   - A signature is a one-dimensional representation of a shape's boundary used for shape analysis.

9. **What is Skeleton?**
   - Same as in point 2 above.

10. **What is the equation for representing Opening operation?**
    - Same as in point 4 above.

11. **Define Morphological Image Processing.**
    - Morphological image processing involves applying operations based on the shape of objects within an image.

12. **Define Skeleton in Image Representation Schemes.**
    - Same as in point 2 above.

13. **List the properties of opening operation.**
    - Idempotence, increasing, translation invariance.

14. **Write the equation for thinning process.**
    - Thinning: \( A \odot B = A - (A \ominus B) \)

15. **What is eigenvector and eigenvalue?**
    - Eigenvector: A non-zero vector that changes only in scale when a linear transformation is applied.
    - Eigenvalue: The factor by which the eigenvector is scaled during the transformation.

16. **What is the purpose of principal components for description?**
    - To reduce the dimensionality of data while preserving most of the variance, enabling efficient representation and analysis.
