# Visualization Scripts

This directory collects useful visualization utilities extracted from the project so that they can be reused in papers or other projects. Each script has a simple demo under `demo/`.

## Contents

- `analyze_logs.py` – plot training curves from json logs.
- `confusion_matrix.py` – generate and plot a confusion matrix.
- `demo.py` – visualize segmentation results on an image.
- `test_torchserve.py` – compare TorchServe predictions with local inference.
- `onnx2tensorrt.py` – convert ONNX models to TensorRT and visualize results.

## Demos

Run the demo scripts to produce example figures:

```bash
python demo/demo_analyze_logs.py      # outputs demo_curve.png
python demo/demo_confusion_matrix.py  # outputs confusion_matrix.png
python demo/demo_show_result.py       # displays a segmentation overlay
```

The demo scripts use dummy data so they can run without training.
