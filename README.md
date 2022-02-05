# FAST-VQA

The official open source training and inference code for future paper 'FAST-VQA: FAST-VQA: Efficient End-to-end Video Quality Assessment with Fragment Sub-sampling'.

## Results


See in [demos](./demos/) for more examples.

## Abstract

Video quality assessment (VQA) on high resolution videos is limited by high computational cost: existing methods often require tens of seconds for inference on them and unable to be trained directly. Therefore, an efficient sub-sampling approach that preserves quality-related information on these videos will be significantly helpful. Based on the observation that randomly sampled mini-patches of videos can effectively represent the video's regional quality around them, we design the fragment sub-sampling strategy, including grid mini-patches sub-sampling (GMS) and temporal fragment alignment (TFA) constraint to sub-sample videos in diverse resolutions. We further build the fragment attention network (FANet), an end-to-end transformer model with gated relative position bias (GRPB) to learn self-attention both within and across fragments. With fragment sub-sampling and FANet, the proposed **Fragment Sub-sample Transformer for VQA (FAST-VQA)** enables efficient and effective end-to-end deep video quality assessment (VQA) regardless of its original resolution. With **97.6%** reduced FLOPs, the proposed method has outperformed state-of-the-art methods by **10%** on high-resolution videos. FAST-VQA also provides effective VQA-oriented deep features which transfers well on smaller VQA datasets. We have also done complete ablation study to prove the effectiveness of both fragment sub-sampling and FANet, and also provide analysis on the prediction stability of FAST-VQA and local quality maps generated by it. We believe the FAST-VQA will bring deep VQA methods into practical use with its prediction effectiveness and significantly improved efficiency.



## Build FAST-VQA

### Requirements

The original method is build with

- python=3.8.8
- torch=1.8.1
- torchvision=0.9.1

while using decord module to read original videos (so that you don't need to make any transform on your original .mp4 input).

To get all the requirements, please run

```shell
pip install -r requirements.txt
```

Or directly run 

```shell
pip install .
```

to build the full FAST-VQA.

### Benchmarking 

You can directly benchmark the model with mainstream benchmark VQA datasets.

```shell
python inference.py --dataset $DATASET$
```

Available datasets are LIVE_VQC, KoNViD, CVD2014, LSVQ (or 'all' if you want to infer all of them).

### Fine-tune on Small Labeled VQA Datasets


```shell
python finetune.py --dataset $DATASET$
```

Available datasets are LIVE_VQC, KoNViD, CVD2014.

### Inference on Scripts

You can install this directory by running

```shell
pip install .
```

Then you can embed these lines into your python scripts:

```python
from fastvqa import deep_end_to_end_vqa

video = torch.randn((3,96,224,224))
vq_evaluator = deep_end_to_end_vqa(pretrained=True, pretrained_path='pretrained_weights/fast_vqa_v0_3.pth')
score = vq_evaluator(video)
print(score)
```