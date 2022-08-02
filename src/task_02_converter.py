from pathlib import Path

import cv2
from PIL import Image

VIDEO_URL = "https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55"


def mp4_to_gif(url: str, filename: str = "default.gif") -> Path:
    """
    Save mp4 data to gif by given URL
    """
    # TODO Handle 403 with proxies and fake user-agent

    cap = cv2.VideoCapture(url)
    is_reading, frame = cap.read()

    frames: list[Image.Image] = []
    while is_reading:
        frames.append(Image.fromarray(frame))
        is_reading, frame = cap.read()  # type: ignore

    # TODO Handle possible giant size of file
    # Possible solution is to use exact amount of frames, e.g. 10

    frames[0].save(
        filename,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0,
    )

    return Path(filename).absolute()


mp4_to_gif(url=VIDEO_URL)
