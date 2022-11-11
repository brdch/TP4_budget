import os

os.system('git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os.system('git bisect good 33827ba712f81ebc7c1fc935e8115e9a49065a9a')
os.system('git bisect good bfdccab909c32635457d41eeb6e7fed322026170')
os.system('git bisect bad 1ca217161f9f3c0485c6c7e983e0b7fb77170910')
os.system('git bisect reset')