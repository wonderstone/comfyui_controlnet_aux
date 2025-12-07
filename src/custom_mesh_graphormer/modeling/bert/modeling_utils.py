from transformers.modeling_utils import *

# These functions moved to pytorch_utils in newer transformers versions
try:
    from transformers.modeling_utils import prune_linear_layer, prune_layer, Conv1D
except ImportError:
    from transformers.pytorch_utils import prune_linear_layer, prune_layer, Conv1D