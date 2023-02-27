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
~conda install -c anaconda -y 'cupy>=7.7.0,<8.0.0'~
```
conda install -c anaconda -y chainer
```
2/26/2023 3:42:44 PM: cupy  
~pip install cupy==7.8.0~  
2/26/2023 4:18:48 PM: cupy
```
pip install cupy-cuda12x
```
2/26/2023 4:21:19 PM: cupy error
```
(fca) [nsambhu@mhb-open-wired-237-156 src]$ python generated_and_test.py 
/home/nsambhu/anaconda3/envs/fca/lib/python3.7/site-packages/chainer/backends/cuda.py:155: UserWarning: cuDNN is not enabled.
Please reinstall CuPy after you install cudnn
(see https://docs-cupy.chainer.org/en/stable/install.html#install-cudnn).
  'cuDNN is not enabled.\n'
/home/nsambhu/anaconda3/envs/fca/lib/python3.7/site-packages/cupy/_environment.py:399: UserWarning: 
nccl library could not be loaded.

Reason: ImportError (libnccl.so.2: cannot open shared object file: No such file or directory)

You can install the library by:

  $ python -m cupyx.tools.install_library --library nccl --cuda 12.x

  warnings.warn(msg)
Traceback (most recent call last):
  File "generated_and_test.py", line 3, in <module>
    from data_loader import MyDatasetTestAdv
  File "/home/nsambhu/github/Full-coverage-camouflage-adversarial-attack/src/data_loader.py", line 15, in <module>
    import nmr_test as nmr
  File "/home/nsambhu/github/Full-coverage-camouflage-adversarial-attack/src/nmr_test.py", line 13, in <module>
    import neural_renderer
ModuleNotFoundError: No module named 'neural_renderer'
```
2/26/2023 4:25:39 PM: 
```
python -m cupyx.tools.install_library --library nccl --cuda 12.x
```
## delete and create environment
2/26/2023 4:33:30 PM: environment setup
```
pip install -r requirements.txt
```
~pip install cupy~
```
pip install cupy-cuda12x
```
2/26/2023 4:50:24 PM: chainer
```
conda install -c anaconda -y chainer
```
2/26/2023 4:51:25 PM:
```
(fca) [nsambhu@mhb-open-wired-237-156 src]$ python generated_and_test.py 
/home/nsambhu/anaconda3/envs/fca/lib/python3.7/site-packages/chainer/backends/cuda.py:155: UserWarning: cuDNN is not enabled.
Please reinstall CuPy after you install cudnn
(see https://docs-cupy.chainer.org/en/stable/install.html#install-cudnn).
  'cuDNN is not enabled.\n'
Traceback (most recent call last):
  File "generated_and_test.py", line 3, in <module>
    from data_loader import MyDatasetTestAdv
  File "/home/nsambhu/github/Full-coverage-camouflage-adversarial-attack/src/data_loader.py", line 15, in <module>
    import nmr_test as nmr
  File "/home/nsambhu/github/Full-coverage-camouflage-adversarial-attack/src/nmr_test.py", line 13, in <module>
    import neural_renderer
ModuleNotFoundError: No module named 'neural_renderer'
```
2/27/2023 12:13:43 PM: cudnn install: https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html  
2/27/2023 3:09:27 PM: try to install chainer with pip
```
pip install chainer
```
2/27/2023 3:13:54 PM:
```
pip install typing_extensions
```
