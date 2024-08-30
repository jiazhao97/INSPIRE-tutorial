Installation 
============

Installation
------------
INSPIRE package is publicly available at https://github.com/jiazhao97/INSPIRE.

INSPIRE can be downloaded from GitHub:

.. code-block:: python

   git clone https://github.com/jiazhao97/INSPIRE.git
   cd INSPIRE
   conda env update --f environment.yml
   conda activate inspire

After installation, the package can be imported in Python by:

.. code-block:: python

   import INSPIRE

Software dependencies
---------------------
.. code-block:: python

   python>=3.7
   pytorch>=1.6.0, <=1.13.1
   scanpy=1.7.2
   anndata=0.7.6
   pandas=1.1.5
   numpy>=1.19.0
   louvain=0.7.0
   leidenalg>=0.7.0
   umap-learn>=0.4.6
   pot>=0.8.0
   numba>=0.49.1
   matplotlib<3.7