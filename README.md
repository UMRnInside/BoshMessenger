# BoshMessenger
废话信使，能够用废话承载二进制数据。
感谢 [menzi11/BullshitGenerator](https://github.com/menzi11/BullshitGenerator)

## Usage
`boshencode.py` 和 `boshdecode.py` 都从标准输入 `stdin` 读取数据、从标准输出 `stdout` 输出结果。

```
# 原文件: original.bin

# 编码
python3 boshencode.py < original.bin > bosh.txt

# 解码
python3 boshdecode.py < bosh.txt > decoded.bin
```

注意：请把编码存入文件。如果您将编码后的内容直接粘贴至 `boshdecode.py` 的标准输入，您可能得到不完整的内容。

从终端启动 `python3` 且不使用管道时，程序似乎一次只读取 4096 字节，解决办法未知。

## Note
目前，废话信使 _BoshMessenger_ 一次只能够传递 32767 字节的信息。

注意，废话信使的放大倍数（编码后文件大小 / 原始文件大小）很大。

| 编码      | 放大倍数 |
| -------- | ------- |
| UTF-8    | 100     |
| GBK      | 65      |

<del>这可是真的废话</del>
