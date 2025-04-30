from sklearn.cluster import KMeans as SK_KMeans


class KMeans:
    def __init__(self, n_clusters=8, init="k-means++", n_init="auto", max_iter=300, tol=1e-4,
                 verbose=0, random_state=None, copy_x=True, algorithm="lloyd"):
        ...