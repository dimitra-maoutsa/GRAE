"""Model arguments for the main.py experiments."""
# Some arg dicts that will be reused by various models
# Default PHATE args
PHATE_DEFAULTS = dict(verbose=0, n_jobs=-1, t='auto')
PHATE_dict = dict(  # Dataset specific arguments
    Faces=dict(knn=5),
    RotatedDigits=dict(knn=5),
    SwissRoll=dict(knn=20),
    Embryoid=dict(knn=5),
    Tracking=dict(knn=5),
    Teapot=dict(knn=5)
)


# UMAP neighbors
UMAP_DEFAULTS = dict()
UMAP_dict = dict(  # Dataset specific arguments
    Faces=dict(n_neighbors=15),
    RotatedDigits=dict(n_neighbors=15),
    SwissRoll=dict(n_neighbors=20),
    Embryoid=dict(n_neighbors=15),
    Tracking=dict(n_neighbors=15),
    Teapot=dict(n_neighbors=15),
)

# TSNE perplexity
TSNE_DEFAULTS = dict()
TSNE_dict = dict(  # Dataset specific arguments
    Faces=dict(perplexity=10),
    RotatedDigits=dict(perplexity=10),
    SwissRoll=dict(perplexity=30),
    Embryoid=dict(perplexity=10),
    Tracking=dict(perplexity=10),
    Teapot=dict(perplexity=10),
)

# Add defaults to dataset specific dicts
for key, d in PHATE_dict.items():
    d.update(PHATE_DEFAULTS)
    PHATE_dict[key] = dict(embedder_args=d)  # Wrap under embedder argument

for key, d in UMAP_dict.items():
    d.update(UMAP_DEFAULTS)
    UMAP_dict[key] = dict(embedder_args=d)  # Wrap under embedder argument

for key, d in TSNE_dict.items():
    d.update(TSNE_DEFAULTS)
    TSNE_dict[key] = dict(embedder_args=d)  # Wrap under embedder argument

# Model parameters to use for experiments
# Make sure the dict key matches the class name
# Those arguments will be used every time the model is initialized
DEFAULTS = {
    'AE': dict(),
    'GRAE': dict(),
    'SGRAE': dict(),
    'UMAP': dict()
}

DATASET_PARAMS = {
    'AE': dict(),
    'GRAE': PHATE_dict,
    'SGRAE': PHATE_dict,
    'UMAP': UMAP_dict
}

