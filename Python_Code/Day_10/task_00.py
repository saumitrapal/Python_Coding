from networkit.generators import HyperbolicGenerator
from networkit.community import detectCommunities

# Generate a random hyperbolic graph
g = (
    HyperbolicGenerator(1e5)
    .generate()
)

# Detect communities
detectCommunities(g, inspect=True)