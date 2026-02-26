def compute_containment(sock_box, dog_box):
    # find where the two boxes overlap, see explain.md for what the numbers mean
    x1, y1 = max(sock_box[0], dog_box[0]), max(sock_box[1], dog_box[1])
    x2, y2 = min(sock_box[2], dog_box[2]), min(sock_box[3], dog_box[3])

    # no overlap or zero-area sock
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    sock_area = (sock_box[2] - sock_box[0]) * (sock_box[3] - sock_box[1])

    # avoid dividing by zero
    return intersection / sock_area if sock_area > 0 else 0.0