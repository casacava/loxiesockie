whhen YOLO detects objects in a frame, it draws a rectangle (a **bounding box**) around each one. each box is defined by four numbers: `[x1, y1, x2, y2]`

```
(x1, y1) ─────────────┐
│                      │
│       dog            │
│                      │
│    (x1, y1) ──┐      │
│    │  sock    │      │
│    └──(x2, y2)│      │
│                      │
└──────────────(x2, y2)
```

what i'm looking for is: percentage of the sock box is inside the dog box? if most of the sock is inside the dog, the dog probably has it in its mouth :(

