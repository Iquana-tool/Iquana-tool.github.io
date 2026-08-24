# GPU and CUDA

An NVIDIA GPU is **optional but strongly recommended**.

The installer asks whether to install with CUDA support. Without a GPU, model
inference and training fall back to the CPU — they still work, but not at a speed
that supports iterating.

| Task | Without a GPU |
|---|---|
| Interactive prompting | usable, but slow enough to interrupt your flow |
| [Batch inference](../guides/batch-inference.md) | feasible for small datasets, painful for large ones |
| [Training](../guides/train-a-model.md) | impractical |

## Requirements

- an NVIDIA GPU with current drivers
- CUDA support selected during installation

To change this later:

```bash
./install.sh --reconfigure
```

## Checking it is being used

If inference is far slower than expected, check the AI service's log:

```bash
./iquana.sh logs ai-service
```

A service that fell back to the CPU says so at startup.

!!! note "uv 0.10 or newer is required for the CUDA wheels"
    Older versions reject the PyTorch wheels the AI service needs. Run
    `uv self update` if the installer complains.
