# Using custom conda environments on the cluster

In this blog post, we explain how to use custom conda environments on the HPC cluster of TU Dresden. This is very useful for prototyping and developing workflows. If you already have an established workflow, you may want to [use a singularity container instead.](../devbio-devbio-napari_cluster/readme.md)

We are assuming, that you already have [applied for access to the cluster](../devbio-napari_cluster_setup/readme.md).

## Step 1: ssh into the cluster

For this you need to be connected to the TU network. e.g. via the [TUD VPN](https://tu-dresden.de/zih/dienste/service-katalog/arbeitsumgebung/zugang_datennetz/vpn/openvpn)

```bash
ssh <ZIH-username>@taurus.hrsk.
```

## Step 2: install micromamba

```bash
curl micro.mamba.pm/install.sh | bash
echo "alias mamba=micromamba" >> ~/.alias
echo "channels: [conda-forge]" >> ~/.mambarc
```

Now you can use `mamba` instead of `conda` and just start managing your environment.

## Step 3: Create an environment

for example, if you want to create a python 3.9 environment, you type

```bash
mamba create -n my-env python=3.9
mamba activate my-env
mamba install ...
```

however, this creates an environment in your home directory, which has two disadvantages:

1. The home directory can be slow if it is busy (because other users are also using it)
2. The home directory is limited to a total of 50 GB

The proper way around this is to create the environment in a workspace:

```bash
# create a workspace
WSDIR=$( ws_allocate -F beegfs -n my-env -d 30 )
mamba create --prefix="$WSDIR"/env python=3.9
mamba activate "$WSDIR"/env
mamba install ...
```

## Step 3: (optional) Create jupyter kernel file

If you want to use your custom environment with the jupyter hub that is already running on the cluster, you need to create a kernel with your environment.

```bash
# start a compute job with gpu support to make sure we can create the right PATH and LD_LIBRARY_PATH variables
srun --pty --gres=gpu:1 -p alpha bash -l

# activate target environment
mamba activate my-env # or: mamba activate "$WSDIR"/env


# load environment modules to create the right PATH and LD_LIBRARY_PATH variables
ml modenv/hiera  GCCcore/11.3.0

# install ipykernel
mamba install ipykernel
export kernel_name=my-kernel
python -m ipykernel install --user --name "$kernel_name" --display-name="$kernel_name"

# make sure that the right environment variables are set for the jupyter kernel
awk -v "pwd=$CONDA_PREFIX" -v "lib=$LD_LIBRARY_PATH" -v "path=$PATH" '/^ \"display/ && !modif { printf(" \"env\": {\n  \"LD_LIBRARY_PATH\": \""pwd"/lib:"lib"\",\n  \"PATH\": \""pwd"/bin:"path"\",\n  \"CONDA_PREFIX\": \""pwd"\"\n },\n"); modif=1 } {print}' ~/.local/share/jupyter/kernels/"$kernel_name"/kernel.json > /tmp/"$USER"tmp && mv /tmp/"$USER"tmp ~/.local/share/jupyter/kernels/"$kernel_name"/kernel.json
