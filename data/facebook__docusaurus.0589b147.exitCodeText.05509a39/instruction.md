# Bug Report

### Describe the bug

I'm encountering an issue with inline code rendering in GFM (GitHub Flavored Markdown) tables. When using inline code (backticks) inside table cells, the code content is not being captured correctly, resulting in either empty or incorrect output.

### Reproduction

```markdown
| Header 1 | Header 2 |
|----------|----------|
| `code`   | normal   |
| text     | `more`   |
```

When parsing this table, the inline code blocks appear empty or display unexpected content instead of showing "code" and "more" as expected.

### Expected behavior

The inline code within table cells should preserve and display the actual code content between the backticks. For example:
- First cell should contain the text "code" 
- Last cell should contain the text "more"

Currently the code blocks are rendering with missing or corrupted values.

### System Info
- remark-gfm version: 4.0.0
- Parser: markdown-it based

Has anyone else run into this? This seems to have started recently and is breaking our documentation rendering.

---
Repository: /testbed
