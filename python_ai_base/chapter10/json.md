# JSON 数据格式与 Python 数据容器关联笔记

## 一、核心概念
### 1.1 什么是 JSON
JSON（JavaScript Object Notation）是一种**轻量级、文本化、跨语言**的数据交换格式，本质是符合特定语法规则的字符串。它独立于编程语言，广泛用于前后端数据交互、配置文件、数据存储等场景。

### 1.2 与 Python 数据容器的关系
Python 内置的 `json` 标准库可以实现 **Python 数据容器（dict、list 等）与 JSON 字符串/文件** 的双向转换：
- **序列化（Serialization）**：Python 对象 → JSON 格式字符串/文件
- **反序列化（Deserialization）**：JSON 格式字符串/文件 → Python 对象

## 二、JSON 与 Python 数据类型映射表
这是两者转换的核心规则，必须一一对应：

| JSON 数据类型 | 对应 Python 数据类型 | 说明 |
| :--- | :--- | :--- |
| `object`（对象） | `dict`（字典） | 键值对结构，JSON 键必须为字符串 |
| `array`（数组） | `list`（列表） | 有序元素集合 |
| `string`（字符串） | `str`（字符串） | JSON 字符串必须用双引号包裹 |
| `number`（整数） | `int`（整型） | 无小数的数值 |
| `number`（浮点数） | `float`（浮点型） | 带小数/科学计数法的数值 |
| `true` / `false`（布尔值） | `True` / `False`（布尔值） | JSON 布尔值为小写，Python 为首字母大写 |
| `null`（空值） | `None`（空值） | 代表空/不存在 |

## 三、Python `json` 模块核心 API
Python 标准库 `json` 提供 4 个核心函数，分为**内存字符串交互**和**文件交互**两组。

### 3.1 序列化：Python → JSON
#### 1) `json.dumps()`：Python 对象 → JSON 字符串
内存中完成转换，返回 JSON 格式字符串。

常用参数：
- `indent`：设置缩进空格数，美化输出（如 `indent=2`）
- `ensure_ascii`：默认 `True`，非 ASCII 字符（如中文）会被转义；设为 `False` 保留原始字符
- `sort_keys`：默认 `False`，设为 `True` 按键名升序排列输出
- `separators`：自定义分隔符，可用于压缩输出体积

#### 2) `json.dump()`：Python 对象 → 写入 JSON 文件
直接将数据写入文件对象，需配合文件上下文管理器使用。

### 3.2 反序列化：JSON → Python
#### 1) `json.loads()`：JSON 字符串 → Python 对象
传入 JSON 格式字符串，返回对应 Python 数据容器。

#### 2) `json.load()`：读取 JSON 文件 → Python 对象
从文件对象中读取 JSON 内容并转换为 Python 对象。

## 四、代码示例
### 4.1 基础序列化与反序列化（dumps / loads）
```python
import json

# Python 原始数据
python_data = {
    "name": "张三",
    "age": 20,
    "is_student": True,
    "hobbies": ["编程", "阅读"],
    "address": None
}

# 1. 序列化：Python dict → JSON 字符串
json_str = json.dumps(python_data, indent=2, ensure_ascii=False)
print("JSON 字符串：")
print(json_str)

# 2. 反序列化：JSON 字符串 → Python dict
python_obj = json.loads(json_str)
print("\n反序列化后类型：", type(python_obj))
print("反序列化后数据：", python_obj)