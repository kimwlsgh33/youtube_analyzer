'''Copyright The Logosevens Logos Team'''


try:
    # This is populated by setup.py
    from .git_version_info import *  # noqa: F401, F403
except ModuleNotFoundError:
    import os
    if os.path.isfile('version.txt'):
        version = open('version.txt', 'r').read().strip()
    else:
        version = '0.0.0'
    git_hash = '[none]'
    git_branch = '[none]'

    from .ops.op_builder.all_ops import ALL_OPS
