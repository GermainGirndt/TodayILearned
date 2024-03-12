# Stable Diffusion

- Use automatic1111 webui for working with stable diffusion
```
https://github.com/AUTOMATIC1111/stable-diffusion-webui
```

Use following mods:

- Models - Download on civai
```
├── ControlNet
│   ├── control_v11f1e_sd15_tile.pth
│   ├── control_v11p_sd15_canny.pth
│   └── control_v11p_sd15_openpose.pth
├── Lora
│   ├── MJ52.safetensors
│   ├── bad-hands-5.pt
├── RealESRGAN
│   ├── RealESRGAN_x4plus.pth
│   └── RealESRGAN_x4plus_anime_6B.pth
├── Stable-diffusion
│   ├── Put Stable Diffusion checkpoints here.txt
│   ├── dreamshaper_8.safetensors
│   ├── realisticVisionV60B1_v51VAE.safetensors
│   ├── v1-5-pruned-emaonly.ckpt
│   └── v1-5-pruned.ckpt
```

- Extensions
```
├── sd-webui-controlnet
└── sd-webui-inpaint-anything
```

- Embeddings
```
baddream
unrealistic dream
```


### Negative Prompts

```
bad photo, bad photography, noisy, wrong anatomy, extra limb, missing limb, floating limbs, disconnected limbs, mutation, mutated, (deformed, distorted, disfigured:1.3), deformed pupils, ((no head)), (extra legs), (low quality:2), (out of frame), (poorly drawn eyes), (worst quality:2), artist name,  bad anatomy, bad hands, bad knees, bad legs, bad neck, bad proportions, black and white, blurry, cloned face, cropped, deformed, dehydrated, disconnected limbs, disfigured, disgusting, duplicate, error, extra arms, extra digit, extra fingers, extra legs, extra limb, extra limbs, feet out of view, fewer digits, floating limbs, fused fingers, grayscale, gross proportions, head out of view, jpeg artifacts, long body, long neck, low quality, lowres, malformed hands, malformed limbs, missing arms, missing fingers, missing legs, missing limb, mole, monochrome, morbid, multiple shoulders, mutated, mutated hands, mutation, mutilated, normal quality, obese, out of focus, out of frame, paintings, poorly drawn eyes, poorly drawn face, poorly drawn hands,  signature, sketches, text, too many fingers, ugly, username, watermark, without hands, worst quality, worst quality, <lora:bad-hands-5:0.5>, 3d, computer generated, artificial
```