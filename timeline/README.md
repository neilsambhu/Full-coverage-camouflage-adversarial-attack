# FCA Timeline
2/26/2023 2:24:49 PM: TODO: texture_camouflage.npy. Find code that references this file. See file dimensions.  
2/26/2023 3:16:55 PM: 
```
arrayTextureCamouflage.shape: (1, 23145, 6, 6, 6, 3)
```
2/26/2023 3:17:43 PM: code references
```
grep -r --exclude *README.md --exclude outgrep.txt -e "texture_camouflage.npy">outgrep.txt
```
2/26/2023 3:19:32 PM: code references
```
Binary file .git/index matches
src/generated_and_test.py:parser.add_argument("--textures", type=str, default='textures/texture_camouflage.npy')
src/0sandbox.py:arrayTextureCamouflage = np.load('textures/texture_camouflage.npy')
```
2/26/2023 3:27:15 PM: missing installation
```
conda install -c anaconda cupy
conda install -c anaconda -y chainer
```
