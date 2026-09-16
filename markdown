Markdown

## 📝 Markdown 完全指南

Markdown 是一种**轻量级标记语言**，由 John Gruber 于 2004 年创建。它的核心思想是 **"易于阅读、易于书写"**，让你可以用纯文本格式编写文档，然后转换成结构化的 HTML。

---

## 🎯 为什么用 Markdown？

| 优点 | 说明 |
|------|------|
| **简洁易学** | 语法简单，几分钟就能上手 |
| **纯文本** | 任何编辑器都能打开，不依赖特定软件 |
| **跨平台** | Windows、macOS、Linux 通用 |
| **版本控制友好** | Git 可以清晰地追踪修改历史 |
| **广泛支持** | GitHub、论坛、笔记软件都支持 |
| **可转换** | 可转成 HTML、PDF、Word 等格式 |

---

## 📚 基础语法

### 1. 标题（Headings）

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```
---

### 2. 强调（Emphasis）

```markdown
*斜体* 或 _斜体_
**粗体** 或 __粗体__
***粗斜体*** 或 ___粗斜体___
~~删除线~~
==高亮==（部分平台支持）
---

### 3. 列表（Lists）

#### 无序列表：
```markdown
- 项目 1
- 项目 2
  - 子项目 2.1
  - 子项目 2.2
* 也可以用星号
+ 或者加号
```

**显示效果：**
- 项目 1
- 项目 2
  - 子项目 2.1
  - 子项目 2.2

#### 有序列表：
```markdown
1. 第一项
2. 第二项
3. 第三项
   1. 子项 3.1
   2. 子项 3.2
```


### 4. 链接和图片（Links & Images）

```markdown
[链接文本](https://www.example.com)
[带标题的链接](https://www.example.com "标题")

![图片替代文本](https://example.com/image.jpg)
![本地图片](./images/photo.jpg)
```

**示例：**
- [访问 Google](https://www.google.com)
- ![示例图片](https://via.placeholder.com/150)

---

### 5. 引用（Blockquotes）

```markdown
> 这是一段引用文本。
> 可以多行。
>> 嵌套引用。
```

**显示效果：**
> 这是一段引用文本。
> 可以多行。
>> 嵌套引用。

---

### 6. 代码（Code）

#### 行内代码：
```markdown
使用 `printf("Hello World")` 输出内容。
```

**显示效果：** 使用 `printf("Hello World")` 输出内容。

#### 代码块：
````markdown
```c
#include <stdio.h>
int main() {
    printf("Hello World\n");
    return 0;
}
```
````

**显示效果：**
```c
#include <stdio.h>
int main() {
    printf("Hello World\n");
    return 0;
}
```

#### 支持的语言标识：
```markdown
```python
```javascript
```cpp
```bash
```json
```yaml
```

---

### 7. 分割线（Horizontal Rules）

```markdown
---
***
___
```

**显示效果：**
---

---

### 8. 表格（Tables）

```markdown
| 左对齐 | 居中对齐 | 右对齐 |
|:-------|:--------:|-------:|
| 内容 1 | 内容 2   | 内容 3 |
| 内容 4 | 内容 5   | 内容 6 |
```

**显示效果：**

| 左对齐 | 居中对齐 | 右对齐 |
|:-------|:--------:|-------:|
| 内容 1 | 内容 2   | 内容 3 |
| 内容 4 | 内容 5   | 内容 6 |

---

### 9. 任务列表（Task Lists）

```markdown
- [x] 已完成的任务
- [ ] 未完成的任务
- [ ] 另一个待办事项
```

**显示效果：**
- [x] 已完成的任务
- [ ] 未完成的任务
- [ ] 另一个待办事项

---

### 10. 脚注（Footnotes）

```markdown
这是带脚注的文本[^1]。

[^1]: 这是脚注的内容。
```

---

## 🚀 扩展语法（GFM - GitHub Flavored Markdown）

GitHub 增加了许多扩展功能：

### 1. 自动链接
```markdown
https://github.com
<email@example.com>
```

### 2. Emoji 表情
```markdown
:smile: :rocket: :heart:
```
显示：😄 🚀 ❤️

### 3. 折叠块（Details）
```markdown
<details>
<summary>点击展开详情</summary>
这里是隐藏的内容。
</details>
```

<details>
<summary>点击展开详情</summary>
这里是隐藏的内容。
</details>

### 4. 警告框（Admonitions）
```markdown
> **Note**: 这是一条提示信息
> **Warning**: 这是警告信息
> **Important**: 重要信息
```

---

## 📖 实战示例：完整的 README.md

````markdown
# 项目名称

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

项目简短描述，一两句话说明项目是什么。

## ✨ 特性

- 特性 1
- 特性 2
- 特性 3

## 📦 安装

```bash
git clone https://github.com/username/project.git
cd project
make install
```

## 🚀 使用

```python
import project

project.do_something()
```

## 📚 文档

详细文档请访问 [文档链接](https://docs.example.com)

## 🤝 贡献

欢迎提交 Pull Request！

## 📄 许可证

本项目使用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。
````

---

## 🛠️ 常用 Markdown 编辑器

| 名称 | 平台 | 特点 |
|------|------|------|
| **Typora** | Win/Mac/Linux | 所见即所得，界面简洁 |
| **VS Code** | 全平台 | 插件丰富，功能强大 |
| **Obsidian** | 全平台 | 知识管理，双向链接 |
| **Notion** | 全平台 | 云端协作，功能全面 |
| **HackMD** | 网页 | 在线协作，实时预览 |
| **Mark Text** | 全平台 | 开源，所见即所得 |

---

## 💡 实用技巧

### 1. 转义特殊字符
```markdown
\* 显示星号
\# 显示井号
\_ 显示下划线
```

### 2. HTML 混用
```markdown
<span style="color: red">红色文字</span>
<br> 换行
<p align="center">居中段落</p>
```

### 3. 锚点跳转
```markdown
[跳转到标题](#标题名称)

## 标题名称
```

### 4. 数学公式（部分平台支持）
```markdown
$E = mc^2$
$$\sum_{i=1}^n i = \frac{n(n+1)}{2}$$
```

---

## ✅ Markdown 最佳实践

1. **保持简洁**：不要过度使用格式
2. **适当使用标题层级**：不要跳级（如 h1 → h3）
3. **代码块指定语言**：方便语法高亮
4. **图片使用相对路径**：便于项目迁移
5. **定期预览**：确保格式正确
6. **使用良好的命名**：文件名有意义

---

## 📊 学习资源

| 资源 | 链接 |
|------|------|
| **官方教程** | [Markdown Guide](https://www.markdownguide.org) |
| **语法速查** | [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) |
| **在线编辑器** | [StackEdit](https://stackedit.io) |
| **GitHub 文档** | [GitHub Markdown](https://docs.github.com/zh/get-started/writing-on-github) |

---

## 🎯 总结

Markdown 是**现代技术写作的必备工具**，它用最少的语法让你专注于内容本身。从写 README、做笔记、发帖子到写技术文档，Markdown 无处不在。

**核心原则：**
- 📝 简单易用，5 分钟上手
- 🔧 纯文本，任何场景都适用
- 🚀 生态丰富，工具链完善

开始用 Markdown 吧！你会发现写文档也可以如此优雅 😊
