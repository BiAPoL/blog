# Principal Feature Analysis
[Ryan Savill](../readme.md), July 8th 2021

## Background
Principal feature analysis (PFA) is a method for selecting a subset of features that describe most of the variability in the dataset based on [this paper](http://venom.cs.utsa.edu/dmz/techrep/2007/CS-TR-2007-011.pdf) by Y. Lu et al. published in ACM, 2007. Most of the code for the implementation below was provided in a [stackexchange comment section](https://stats.stackexchange.com/questions/108743/methods-in-r-or-python-to-perform-feature-selection-in-unsupervised-learning/203978#203978) and is greatly appreciated! 

This sounds oddly similar to principal component analysis (PCA), which is no coincidence as the methodologies are intertwined. PCA also does a similar thing but instead of choosing features that describe the variability to a certain threshold we choose a subset of principal components. This is not always optimal and there are valid choices for working with the features instead of the principal components as the principal components are always a transformed form of the data.

If you have not heard of PCA before I would advise you to check out [this video](https://www.youtube.com/watch?v=FgakZw6K1QQ). If you (like me just a few days ago) have an understanding of the principle of PCA but don't understand the math behind it I'd advise you to take some time to grasp the concepts. I found a great series of videos that explain all necessary parts of the puzzle that is PCA. Each video is just about 10 minutes long and explained quite well, even if your math lectures have been a few years ago!

- [Vector Projections](https://www.youtube.com/watch?v=X78tLBY3BMk)
- [Eigenvectors and Eigenvalues](https://www.youtube.com/watch?v=glaiP222JWA)
- [Derivative of a Matrix](https://www.youtube.com/watch?v=e73033jZTCI)
- [Lagrange Multipliers](https://www.youtube.com/watch?v=6oZT72-nnyI)
- [Covariance Matrix](https://www.youtube.com/watch?v=152tSYtiQbw)
- [PCA](https://www.youtube.com/watch?v=dhK8nbtii6I) (finally!)

Once you have grasped these concepts this explanation should be a breeze!

Principal feature analysis takes advantage of some of the transformations in PCA to find out which features explain the variance. The first steps in PFA are to create the covariance matrix and find the orthonormal eigenvectors and sort them by their eigenvalues, creating a matrix A. This in effect is what PCA does as well since the principal components are the eigenvectors of the covariance matrix. We can output them in [scikit-learn](https://scikit-learn.org/stable/) with the command '.components_'. 


```python
# importing everything we might need and more:
from sklearn import decomposition
import tribolium_clustering as tc
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from collections import defaultdict
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler

# function for labelling eigenvectors so it is readable:
def pca_comp_inf_dataframe(pca_object,regprops_df,n_components):
    from sklearn.decomposition import PCA
    import pandas as pd
    import numpy as np
    features = regprops_df.keys()
    component_names = ['PC{}'.format(i+1) for i in range(n_components)]
    comps = pca_object.components_
    df_comps = pd.DataFrame(comps,index = component_names, columns = features)
    
    return df_comps

# loading our test dataset
location_prefix = 'data/folder/'

timepoint = 9
regionpropspath = location_prefix + 'Master Thesis//First Coding Tries//regionprops_all_timepoints_lund//regprops t{}.csv'.format(timepoint)
regprops = tc.readcsv_as_cl_input(regionpropspath)

# redefinition of our dataset
X = regprops

# standardscaling the dataset is a prerequisite for PCA
sc = StandardScaler()
X = sc.fit_transform(X)

# fitting our PCA
pca = PCA().fit(X)

# getting our orthonormal eigenvectors:
A = pca.components_.T

# labelling that matrix for ease of use
A_readable = pca_comp_inf_dataframe(pca,regprops,len(regprops.keys())).transpose()

A_readable
```

    No Predictions in Regionprops of data/folder/Master Thesis/First Coding Tries/regionprops_all_timepoints_lund/regprops t9.csv
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PC1</th>
      <th>PC2</th>
      <th>PC3</th>
      <th>PC4</th>
      <th>PC5</th>
      <th>PC6</th>
      <th>PC7</th>
      <th>PC8</th>
      <th>PC9</th>
      <th>PC10</th>
      <th>PC11</th>
      <th>PC12</th>
      <th>PC13</th>
      <th>PC14</th>
      <th>PC15</th>
      <th>PC16</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>area</th>
      <td>0.317564</td>
      <td>0.035871</td>
      <td>0.001643</td>
      <td>-0.060553</td>
      <td>-0.099831</td>
      <td>0.060197</td>
      <td>0.121308</td>
      <td>-0.070996</td>
      <td>-0.059213</td>
      <td>-0.200579</td>
      <td>0.358877</td>
      <td>0.496485</td>
      <td>0.533148</td>
      <td>0.376162</td>
      <td>0.126583</td>
      <td>-0.007435</td>
    </tr>
    <tr>
      <th>centroid-0</th>
      <td>0.031897</td>
      <td>0.394748</td>
      <td>-0.671168</td>
      <td>0.066552</td>
      <td>-0.171701</td>
      <td>-0.245463</td>
      <td>-0.296170</td>
      <td>-0.423315</td>
      <td>-0.143398</td>
      <td>0.086719</td>
      <td>0.030823</td>
      <td>-0.041805</td>
      <td>-0.005947</td>
      <td>0.007349</td>
      <td>0.026808</td>
      <td>0.005131</td>
    </tr>
    <tr>
      <th>centroid-1</th>
      <td>0.008123</td>
      <td>0.382147</td>
      <td>0.488175</td>
      <td>0.230320</td>
      <td>-0.613868</td>
      <td>-0.143166</td>
      <td>-0.356966</td>
      <td>0.192595</td>
      <td>0.011508</td>
      <td>-0.013926</td>
      <td>0.001356</td>
      <td>0.008315</td>
      <td>-0.007246</td>
      <td>0.000669</td>
      <td>-0.015394</td>
      <td>-0.000195</td>
    </tr>
    <tr>
      <th>centroid-2</th>
      <td>0.240592</td>
      <td>-0.076633</td>
      <td>-0.435728</td>
      <td>0.075588</td>
      <td>-0.140601</td>
      <td>-0.327701</td>
      <td>0.114531</td>
      <td>0.634164</td>
      <td>0.393689</td>
      <td>-0.174994</td>
      <td>-0.084351</td>
      <td>0.026689</td>
      <td>-0.018534</td>
      <td>-0.022879</td>
      <td>-0.062223</td>
      <td>-0.007310</td>
    </tr>
    <tr>
      <th>feret_diameter_max</th>
      <td>0.289769</td>
      <td>-0.012282</td>
      <td>-0.032635</td>
      <td>0.181363</td>
      <td>-0.160207</td>
      <td>0.380691</td>
      <td>0.084649</td>
      <td>-0.211788</td>
      <td>0.439432</td>
      <td>0.320636</td>
      <td>-0.163147</td>
      <td>0.056981</td>
      <td>-0.363715</td>
      <td>0.448382</td>
      <td>0.007851</td>
      <td>-0.012093</td>
    </tr>
    <tr>
      <th>major_axis_length</th>
      <td>0.301739</td>
      <td>0.002370</td>
      <td>-0.021720</td>
      <td>0.113154</td>
      <td>-0.135457</td>
      <td>0.346191</td>
      <td>0.039834</td>
      <td>-0.195065</td>
      <td>0.315525</td>
      <td>0.010066</td>
      <td>0.049534</td>
      <td>-0.247254</td>
      <td>0.419644</td>
      <td>-0.608955</td>
      <td>-0.086439</td>
      <td>0.013967</td>
    </tr>
    <tr>
      <th>minor_axis_length</th>
      <td>0.308058</td>
      <td>0.048526</td>
      <td>0.032858</td>
      <td>-0.149205</td>
      <td>-0.075049</td>
      <td>0.130833</td>
      <td>0.027726</td>
      <td>-0.170614</td>
      <td>-0.094954</td>
      <td>-0.740310</td>
      <td>0.122889</td>
      <td>-0.086970</td>
      <td>-0.489703</td>
      <td>-0.077289</td>
      <td>-0.034946</td>
      <td>-0.005721</td>
    </tr>
    <tr>
      <th>solidity</th>
      <td>0.139750</td>
      <td>0.213562</td>
      <td>0.179860</td>
      <td>-0.784037</td>
      <td>0.109756</td>
      <td>-0.245965</td>
      <td>-0.162139</td>
      <td>-0.093897</td>
      <td>0.399242</td>
      <td>0.142184</td>
      <td>-0.016268</td>
      <td>-0.005970</td>
      <td>0.007210</td>
      <td>-0.012330</td>
      <td>0.005534</td>
      <td>-0.001295</td>
    </tr>
    <tr>
      <th>mean_intensity</th>
      <td>-0.298859</td>
      <td>-0.031721</td>
      <td>-0.044582</td>
      <td>-0.053140</td>
      <td>-0.290490</td>
      <td>-0.081776</td>
      <td>0.366782</td>
      <td>-0.070965</td>
      <td>0.147539</td>
      <td>0.210029</td>
      <td>0.577876</td>
      <td>0.280034</td>
      <td>-0.316568</td>
      <td>-0.304428</td>
      <td>0.055622</td>
      <td>0.001809</td>
    </tr>
    <tr>
      <th>max_intensity</th>
      <td>-0.223891</td>
      <td>0.445127</td>
      <td>-0.015072</td>
      <td>-0.078562</td>
      <td>-0.095429</td>
      <td>0.088448</td>
      <td>0.504917</td>
      <td>-0.064260</td>
      <td>-0.004226</td>
      <td>-0.155993</td>
      <td>-0.573306</td>
      <td>0.308846</td>
      <td>0.074610</td>
      <td>-0.118217</td>
      <td>-0.036991</td>
      <td>0.002788</td>
    </tr>
    <tr>
      <th>min_intensity</th>
      <td>-0.248677</td>
      <td>-0.277709</td>
      <td>-0.003527</td>
      <td>-0.151868</td>
      <td>-0.443942</td>
      <td>-0.187537</td>
      <td>0.304523</td>
      <td>-0.223142</td>
      <td>0.067566</td>
      <td>-0.152249</td>
      <td>-0.039673</td>
      <td>-0.525101</td>
      <td>0.223898</td>
      <td>0.328584</td>
      <td>-0.005177</td>
      <td>-0.002429</td>
    </tr>
    <tr>
      <th>image_stdev</th>
      <td>-0.124373</td>
      <td>0.597732</td>
      <td>-0.026935</td>
      <td>0.059831</td>
      <td>0.275986</td>
      <td>0.222842</td>
      <td>0.207255</td>
      <td>0.258350</td>
      <td>0.080221</td>
      <td>-0.016470</td>
      <td>0.376158</td>
      <td>-0.432514</td>
      <td>0.043550</td>
      <td>0.222652</td>
      <td>0.025638</td>
      <td>-0.004268</td>
    </tr>
    <tr>
      <th>avg distance of 2 closest points</th>
      <td>0.312403</td>
      <td>0.040115</td>
      <td>0.025366</td>
      <td>-0.113510</td>
      <td>-0.083929</td>
      <td>-0.065002</td>
      <td>0.223752</td>
      <td>0.060992</td>
      <td>-0.355553</td>
      <td>0.261325</td>
      <td>0.057316</td>
      <td>-0.050857</td>
      <td>-0.037707</td>
      <td>0.038347</td>
      <td>-0.716577</td>
      <td>0.324435</td>
    </tr>
    <tr>
      <th>avg distance of 3 closest points</th>
      <td>0.315714</td>
      <td>0.031638</td>
      <td>0.028109</td>
      <td>-0.084834</td>
      <td>-0.084732</td>
      <td>-0.064296</td>
      <td>0.212046</td>
      <td>0.076844</td>
      <td>-0.308744</td>
      <td>0.228016</td>
      <td>-0.034887</td>
      <td>-0.121603</td>
      <td>-0.049914</td>
      <td>-0.068178</td>
      <td>0.120108</td>
      <td>-0.802665</td>
    </tr>
    <tr>
      <th>avg distance of 4 closest points</th>
      <td>0.316944</td>
      <td>0.023361</td>
      <td>0.033518</td>
      <td>-0.059729</td>
      <td>-0.078356</td>
      <td>-0.068524</td>
      <td>0.204538</td>
      <td>0.092240</td>
      <td>-0.253916</td>
      <td>0.188049</td>
      <td>-0.088972</td>
      <td>-0.156060</td>
      <td>-0.072032</td>
      <td>-0.097133</td>
      <td>0.660690</td>
      <td>0.499889</td>
    </tr>
    <tr>
      <th>touching neighbor count</th>
      <td>-0.190434</td>
      <td>-0.078438</td>
      <td>-0.284396</td>
      <td>-0.437245</td>
      <td>-0.339335</td>
      <td>0.594522</td>
      <td>-0.243295</td>
      <td>0.334427</td>
      <td>-0.201843</td>
      <td>0.052019</td>
      <td>-0.024418</td>
      <td>0.025692</td>
      <td>0.012726</td>
      <td>0.013417</td>
      <td>0.028237</td>
      <td>0.006079</td>
    </tr>
  </tbody>
</table>
</div>



Now we have a massive matrix of our eigenvectors sorted by eigenvalues, but since every feature has equal influence on the eigenvectors we need to take a subset of matrix `A` called `A_q`. `q` represents the number of eigenvectors we take into account and the value of `q` will influence how much variance we can explain with the subset of the principal components. We can turn this question around and set a threshold of how much variance should at least be explained and then find the corresponding subset `A-q` of matrix `A`:


```python
# this shows us how much variance each principal component explains
explained_variance = pca.explained_variance_ratio_
print('Explained Variances')
print(explained_variance)
print('')

# this shows us how much variance the subset up to the i'th index explains
cumulative_expl_var = [sum(explained_variance[:i+1]) for i in range(len(explained_variance))]
print('Cumulative Explained Variance')
print(cumulative_expl_var)
print('')

# now we iterate through the cumulative explained variance until we reach a threshold that we define
q_variance_limit = 0.9

for i,j in enumerate(cumulative_expl_var):
    if j >= q_variance_limit:
        q = i
        break
print('The Subset will include the first {} Eigenvectors'.format(q))
```

    Explained Variances
    [5.89549241e-01 1.24817549e-01 7.44073363e-02 6.06447683e-02
     5.05242728e-02 3.80817718e-02 2.29718719e-02 1.43923774e-02
     1.16341513e-02 5.35585488e-03 2.50361397e-03 1.82220555e-03
     1.48239356e-03 1.06126637e-03 6.85699035e-04 6.56265602e-05]
    
    Cumulative Explained Variance
    [0.5895492409109632, 0.7143667903013323, 0.7887741265865403, 0.8494188949293884, 0.8999431677426732, 0.9380249394988094, 0.9609968114170524, 0.9753891887742816, 0.9870233400706391, 0.992379194950718, 0.9948828089223744, 0.9967050144743802, 0.9981874080386469, 0.9992486744047498, 0.9999343734397964, 0.9999999999999999]
    
    The Subset will include the first 5 Eigenvectors
    

With our q defined we can get the the subset matrix of eigenvectors A_q:


```python
A_q = A[:,:q]

A_q_readable = pd.DataFrame(A_q,index = regprops.keys(), columns = ['PC{}'.format(i+1) for i in range(q)])

A_q_readable
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PC1</th>
      <th>PC2</th>
      <th>PC3</th>
      <th>PC4</th>
      <th>PC5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>area</th>
      <td>0.317564</td>
      <td>0.035871</td>
      <td>0.001643</td>
      <td>-0.060553</td>
      <td>-0.099831</td>
    </tr>
    <tr>
      <th>centroid-0</th>
      <td>0.031897</td>
      <td>0.394748</td>
      <td>-0.671168</td>
      <td>0.066552</td>
      <td>-0.171701</td>
    </tr>
    <tr>
      <th>centroid-1</th>
      <td>0.008123</td>
      <td>0.382147</td>
      <td>0.488175</td>
      <td>0.230320</td>
      <td>-0.613868</td>
    </tr>
    <tr>
      <th>centroid-2</th>
      <td>0.240592</td>
      <td>-0.076633</td>
      <td>-0.435728</td>
      <td>0.075588</td>
      <td>-0.140601</td>
    </tr>
    <tr>
      <th>feret_diameter_max</th>
      <td>0.289769</td>
      <td>-0.012282</td>
      <td>-0.032635</td>
      <td>0.181363</td>
      <td>-0.160207</td>
    </tr>
    <tr>
      <th>major_axis_length</th>
      <td>0.301739</td>
      <td>0.002370</td>
      <td>-0.021720</td>
      <td>0.113154</td>
      <td>-0.135457</td>
    </tr>
    <tr>
      <th>minor_axis_length</th>
      <td>0.308058</td>
      <td>0.048526</td>
      <td>0.032858</td>
      <td>-0.149205</td>
      <td>-0.075049</td>
    </tr>
    <tr>
      <th>solidity</th>
      <td>0.139750</td>
      <td>0.213562</td>
      <td>0.179860</td>
      <td>-0.784037</td>
      <td>0.109756</td>
    </tr>
    <tr>
      <th>mean_intensity</th>
      <td>-0.298859</td>
      <td>-0.031721</td>
      <td>-0.044582</td>
      <td>-0.053140</td>
      <td>-0.290490</td>
    </tr>
    <tr>
      <th>max_intensity</th>
      <td>-0.223891</td>
      <td>0.445127</td>
      <td>-0.015072</td>
      <td>-0.078562</td>
      <td>-0.095429</td>
    </tr>
    <tr>
      <th>min_intensity</th>
      <td>-0.248677</td>
      <td>-0.277709</td>
      <td>-0.003527</td>
      <td>-0.151868</td>
      <td>-0.443942</td>
    </tr>
    <tr>
      <th>image_stdev</th>
      <td>-0.124373</td>
      <td>0.597732</td>
      <td>-0.026935</td>
      <td>0.059831</td>
      <td>0.275986</td>
    </tr>
    <tr>
      <th>avg distance of 2 closest points</th>
      <td>0.312403</td>
      <td>0.040115</td>
      <td>0.025366</td>
      <td>-0.113510</td>
      <td>-0.083929</td>
    </tr>
    <tr>
      <th>avg distance of 3 closest points</th>
      <td>0.315714</td>
      <td>0.031638</td>
      <td>0.028109</td>
      <td>-0.084834</td>
      <td>-0.084732</td>
    </tr>
    <tr>
      <th>avg distance of 4 closest points</th>
      <td>0.316944</td>
      <td>0.023361</td>
      <td>0.033518</td>
      <td>-0.059729</td>
      <td>-0.078356</td>
    </tr>
    <tr>
      <th>touching neighbor count</th>
      <td>-0.190434</td>
      <td>-0.078438</td>
      <td>-0.284396</td>
      <td>-0.437245</td>
      <td>-0.339335</td>
    </tr>
  </tbody>
</table>
</div>



If you have read the paper or are following along with the paper we have just completed step 3 of the explained algorithm. What is done now is that we perform clustering on the matrix A_q with K-means clustering. Essentially, we are trying to find clusters of features as features that are clustered in this matrix have similar influences on the principal components and are thus correlating and not telling us much. This way we can just choose the feature that is closest to the cluster centre and it will be chosen as a principal feature. 

We can see that the choice of the cluster-number will determine how many features we choose. Y. Lu et al. recommend choosing the cluster-number: p, as: `p >= q` because we can't be completely sure that the variance that we chose is explained when `p = q`. We can just opt for a slightly larger `p` (arbitrary choice of 2  larger than `q`) but there is room for improvement in terms of an automated choice here OR it could be a parameter that we can implement later.

Since K-means-clustering is implemented well in [scikit-learn](https://scikit-learn.org/stable/modules/clustering.html) this procedure is just a couple of lines:


```python
kmeans = KMeans(n_clusters= q + 2, random_state= 42).fit(A_q)
clusters = kmeans.predict(A_q)
cluster_centers = kmeans.cluster_centers_

clusters_readable = pd.DataFrame(clusters, index = regprops.keys(), columns = ['Cluster'])
clusters_readable
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>area</th>
      <td>2</td>
    </tr>
    <tr>
      <th>centroid-0</th>
      <td>5</td>
    </tr>
    <tr>
      <th>centroid-1</th>
      <td>6</td>
    </tr>
    <tr>
      <th>centroid-2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>feret_diameter_max</th>
      <td>2</td>
    </tr>
    <tr>
      <th>major_axis_length</th>
      <td>2</td>
    </tr>
    <tr>
      <th>minor_axis_length</th>
      <td>2</td>
    </tr>
    <tr>
      <th>solidity</th>
      <td>4</td>
    </tr>
    <tr>
      <th>mean_intensity</th>
      <td>0</td>
    </tr>
    <tr>
      <th>max_intensity</th>
      <td>3</td>
    </tr>
    <tr>
      <th>min_intensity</th>
      <td>0</td>
    </tr>
    <tr>
      <th>image_stdev</th>
      <td>3</td>
    </tr>
    <tr>
      <th>avg distance of 2 closest points</th>
      <td>2</td>
    </tr>
    <tr>
      <th>avg distance of 3 closest points</th>
      <td>2</td>
    </tr>
    <tr>
      <th>avg distance of 4 closest points</th>
      <td>2</td>
    </tr>
    <tr>
      <th>touching neighbor count</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



What can we see here? Well each feature is now part of a cluster (numbers 0 - 6, since we have chosen 7 clusters). What we can also see is that quite a few features are part of the same cluster( = 2), while some features are only part of a unique cluster without any other features. This means that these features do not correlate (much at least) with any other features and will be chosen by our feature analysis. The clusters which have 2 or more features as part of it are the clusters where a feature has to be chosen. This is decided by the distances the features have from the cluster centres, so let's determine the distances from the cluster centres for each feature:


```python
# initialising a dictionary to keep the distances in:
dists = defaultdict(list)

# iterating through each feature (i) and it's cluster (c)
for i, c in enumerate(clusters):
    
    # measuring the distance of each feature in A_q ([A_q[i, :]])
    # and the cluster centers [cluster_centers[c, :]]
    dist = euclidean_distances([A_q[i, :]], [cluster_centers[c, :]])[0][0]
    
    # each cluster is a key in the dictionary and the distance of each feature
    # belonging to that cluster is saved under this key as a tupule (feature_idx, distance)
    dists[c].append((i, dist))

dists
```




    defaultdict(list,
                {2: [(0, 0.039527541499107074),
                  (4, 0.22202861661398224),
                  (5, 0.1470198671974888),
                  (6, 0.13180725994276707),
                  (12, 0.09346378648078914),
                  (13, 0.06610212866152891),
                  (14, 0.04944098356286365)],
                 5: [(1, 0.0)],
                 6: [(2, 0.0)],
                 1: [(3, 0.0)],
                 4: [(7, 0.0)],
                 0: [(8, 0.217150845350435),
                  (10, 0.2117088702247021),
                  (15, 0.29315857787851873)],
                 3: [(9, 0.21819421392343466), (11, 0.21819421392343452)]})



In our `dists` dictionary each cluster has a list of tuples associated with it. Each tuple contains:
(feature index, distance to cluster center)
We can see that for the clusters with only one tuple associated `(5,6,1,4)`, the features all have distance 0 since the cluster center IS the feature. For all other clusters we still have to determine which feature is closest to the cluster center. Once the features have been determined we can transform our original dataset to only include these features:


```python
# here we are getting the indices of the features with the smallest distances 
# to the cluster centers, essentially choosing which features to keep
indices_ = [sorted(f, key=lambda x: x[1])[0][0] for f in dists.values()]

# transforming the input data to only include the features we just chose
features_ = X[:, indices_]
```

## Implementation
Since data science in python is mainly performed in [scikit-learn](https://scikit-learn.org/stable/) we'll stick to the conventions and create a class instead of a function for PFA. As stated above this is a slightly modified code provided by [Ulf Aslak](https://stats.stackexchange.com/users/76815/ulf-aslak) on [this stackexchange thread](https://stats.stackexchange.com/questions/108743/methods-in-r-or-python-to-perform-feature-selection-in-unsupervised-learning). Thanks for your kind code donation!


```python
class PFA(object):
    def __init__(self, diff_n_features = 2, q=None, explained_var = 0.95):
        self.q = q
        self.diff_n_features = diff_n_features
        self.explained_var = explained_var

    def fit(self, X):
        sc = StandardScaler()
        X = sc.fit_transform(X)

        pca = PCA().fit(X)
        
        if not self.q:
            explained_variance = pca.explained_variance_ratio_
            cumulative_expl_var = [sum(explained_variance[:i+1]) for i in range(len(explained_variance))]
            for i,j in enumerate(cumulative_expl_var):
                if j >= self.explained_var:
                    q = i
                    break
                    
        A_q = pca.components_.T[:,:q]
        
        clusternumber = min([q + self.diff_n_features, X.shape[1]])
        
        kmeans = KMeans(n_clusters= clusternumber).fit(A_q)
        clusters = kmeans.predict(A_q)
        cluster_centers = kmeans.cluster_centers_

        dists = defaultdict(list)
        for i, c in enumerate(clusters):
            dist = euclidean_distances([A_q[i, :]], [cluster_centers[c, :]])[0][0]
            dists[c].append((i, dist))

        self.indices_ = [sorted(f, key=lambda x: x[1])[0][0] for f in dists.values()]
        self.features_ = X[:, self.indices_]
        
    def fit_transform(self,X):    
        sc = StandardScaler()
        X = sc.fit_transform(X)

        pca = PCA().fit(X)
        
        if not self.q:
            explained_variance = pca.explained_variance_ratio_
            cumulative_expl_var = [sum(explained_variance[:i+1]) for i in range(len(explained_variance))]
            for i,j in enumerate(cumulative_expl_var):
                if j >= self.explained_var:
                    q = i
                    break
                    
        A_q = pca.components_.T[:,:q]
        
        clusternumber = min([q + self.diff_n_features, X.shape[1]])
        
        kmeans = KMeans(n_clusters= clusternumber).fit(A_q)
        clusters = kmeans.predict(A_q)
        cluster_centers = kmeans.cluster_centers_

        dists = defaultdict(list)
        for i, c in enumerate(clusters):
            dist = euclidean_distances([A_q[i, :]], [cluster_centers[c, :]])[0][0]
            dists[c].append((i, dist))

        self.indices_ = [sorted(f, key=lambda x: x[1])[0][0] for f in dists.values()]
        self.features_ = X[:, self.indices_]
        
        return X[:, self.indices_]
    
    def transform(self, X):
        return X[:, self.indices_]

# Testing
pfa = PFA(diff_n_features=1, explained_var= 0.95)
pfa.fit_transform(regprops)

featurekeys = [regprops.keys().tolist()[i] for i in pfa.indices_]
featurekeys
```




    ['area',
     'centroid-0',
     'centroid-1',
     'solidity',
     'mean_intensity',
     'image_stdev',
     'touching neighbor count']



This is a modification of the provided code in that it tries to force you to choose a subset. If you don't manually say what the subset is, it will get a subset that explains 95% of the variance or the amount of variance that you determine. As described in the paper, the number of clusters (and with that the number of features) should be larger than the subset of eigenvectors chosen. This is implemented by not determining the number of features but only setting how many more features than the subset should be chosen. Apart from this a transform function was added as well as a fit_transform function, similarly to other scikit learn functions.
