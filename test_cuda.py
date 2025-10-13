name: test cuda
description: hhhdhd


implementation:
  container:
    image: nikhilv215/nesy-factory:v22
    command:
      - python3
      - -u
      - -c
      - |-
        import torch
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
