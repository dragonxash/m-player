#!/usr/bin/env python3
"""
SILK?.DAT 解包出的 .M 音乐文件结构分析器
格式：TAM 5PLAY5.COM ver1.00 (INT F2H) 播放的 FM 曲目（YM2203/OPN）

结构:
    u16 0x0006                    ; 格式标记
    u16 X                         ; 音色区结束偏移（= 6 + 32×音色数）
    u16 Y = X + 24                ; 数据区起始（24 字节 = 节奏/SSG 音色区）
    [6..X)     FM 音色 × N (32 B/个)
    [X..X+24)  节奏/鼓音色区
    [Y..EOF)   演奏数据
"""
import struct, sys, os

FILES = ['OPEN.M', 'HOME.M', 'DORAMA.M', 'H1.M', 'H2.M', 'H3.M',
         'HARAHARA.M', 'SAGASU.M', 'CREGIT.M', 'CRASH.M']


def analyze(path):
    d = open(path, 'rb').read()
    if len(d) < 6:
        return None
    magic, x, y = struct.unpack('<HHH', d[:6])
    n = (x - 6) // 32
    return dict(magic=magic, x=x, y=y, voices=n,
                rhythm=y - x, data=len(d) - y, size=len(d))


if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f'{"文件":<12} {"大小":>6} {"标记":>5} {"音色":>5} {"节奏区":>6} {"数据区":>7}  {"音色区结束/数据区起"}')
    for fn in FILES:
        p = os.path.join(base, fn)
        if not os.path.exists(p):
            print(f'{fn:<12}  (不存在)'); continue
        r = analyze(p)
        print(f'{fn:<12} {r["size"]:>6} {r["magic"]:04X} {r["voices"]:>5} '
              f'{r["rhythm"]:>6} {r["data"]:>7}  0x{r["x"]:04X} / 0x{r["y"]:04X}')
