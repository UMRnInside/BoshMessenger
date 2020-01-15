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

## Note
目前，废话信使 _BoshMessenger_ 一次只能够传递 32767 字节的信息。
