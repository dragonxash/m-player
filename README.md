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

## 格式逆向进度（TAM 5PLAY5.COM ver1.00 / INT F2H）

```
u16 0x0006                 ; 格式标记
u16 X = 6+32×音色数         ; 音色区结束
u16 Y                       ; 数据区起点
[6..X)    FM 音色 × N（32 B/个）
[X..Y)    节奏/鼓音色区
[Y..EOF)  演奏数据：
            seq[8]  = 14 00 标记
            seq[10..18) = 4 × u16 通道偏移
            每通道: bX YY cZ d0 头 + 音符/音长事件流
            音符 0x00-0x7F = MIDI 半音（0x3C = C4）
            音长 0x80+ = 值 & 0x7F（tick）
```

> 当前为**逆向中的实验性实现**：指令集（循环/音量/音色切换）与通道音色分配
> 为近似值，节奏与原版可能有差异。已确认：4 通道并行结构、MIDI 半音映射。

## 配套工具 Companion tools

- `m_analyze.py` — .M 结构解析器（音色数 / 通道偏移 / 数据区统计）

## 相关工具

- [SILK.DAT 解包器](https://dragonxash.github.io/elf-dat-extra/)
- [MES 剧本预览器](https://dragonxash.github.io/aishima-mes-to-text/)
- [GP4 图片预览器](https://dragonxash.github.io/gp4-viewer/)
- [工具集入口](https://dragonxash.github.io/aishima-tools/)
