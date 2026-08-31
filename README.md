# 愛姉妹 .M 音乐播放器 / Aishima .M Music Player

浏览器端播放 Silky's 愛姉妹（1994, PC-98）`.M` 音乐文件的单页工具。
纯本地解码 + YM2203（OPN）FM 合成，**不上传任何数据**。

▶ 在线使用：<https://dragonxash.github.io/m-player/>

## 功能 Features

- 上传 `.M` 音乐文件（SILK0.DAT 解包产物）
- 4 通道并行 FM 合成播放（主旋律 + 低音伴奏）
- 播放 / 暂停 / 进度拖动 / 音量
- 导出 WAV / MP3

## 使用方法 Usage

1. 打开页面（或本地双击 `index.html`）
2. 拖入 `silk_out/SILK0/` 下的 `OPEN.M`、`HOME.M` 等文件
3. 播放 / 导出

## 格式逆向进度（TAM 5PLAY5.COM ver1.00 / INT F2H）—— ✅ 完整还原

已从 MUSIC.COM（INT F2H 驻留驱动）反汇编完整还原格式：

```
.M 文件结构:
  u16[0] = 6, u16[1] = X, u16[2] = Y
  [6..X)    音色表：N 个 × 8 字节（N = (X-6)/8）
  [X..Y)    节奏/鼓音色区
  [Y..EOF)  演奏数据：
              +0: 8 字节通道设置
              +8: 14 00 标记
              +A: 4 × u16 通道偏移（指向各通道数据）

通道指令集（0x80+）:
  0x80-0x9F  设置音长索引 [di+7] = 低 5 位
  0xA0-0xAF  设置 [di+8]（SSG 相关）
  0xB0-0xBF  设置音色号 [di+0xB] = 低 4 位
  0xC0-0xCF  设置音量 [di+9] = 低 4 位
  0xD0-0xDF  设置 [di+0xA]
  0xE0-0xEF  延音标记（音长 ×2）
  0xF0       低 4 位 = 0 结束；= 1 循环（跳回通道开头）
  0x00       结束

音符（0x00-0x7F）:
  字节值 = MIDI 半音（0x3C = 60 = C4）
  音长 = 驱动音长表 CS:0x44CA[音长索引]
        [0]=384(四分音符) [3]=192(八分) [6]=96(十六分) ...
  半音频率表 CS:0x4492（12 平均律）
```

> 逆向证据：F2H handler @ CS:0x18F（AL=0 加载曲目到 CS:0x33FE），
> 通道推进器 @ CS:0x5109（音符/指令分派），音色查表 @ CS:0x46C1（音色号×8）。

## 配套工具 Companion tools

- `m_analyze.py` — .M 结构解析器（音色数 / 通道偏移 / 数据区统计）

## 相关工具

- [SILK.DAT 解包器](https://dragonxash.github.io/elf-dat-extra/)
- [MES 剧本预览器](https://dragonxash.github.io/aishima-mes-to-text/)
- [GP4 图片预览器](https://dragonxash.github.io/gp4-viewer/)
- [工具集入口](https://dragonxash.github.io/aishima-tools/)
