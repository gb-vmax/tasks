# Bug Report

### Describe the bug

Magic comments in Python code blocks are not being recognized correctly. When I use highlighting directives like `# highlight-next-line` or `# highlight-start` in Python code blocks, they don't work as expected.

### Reproduction

```python
# highlight-next-line
def my_function():
    pass
```

The highlighting doesn't apply to Python code blocks, but it works fine in JavaScript code blocks.

### Steps to reproduce:
1. Create a markdown file with a Python code block
2. Add a magic comment directive like `# highlight-next-line`
3. The line highlighting doesn't work

This also affects bash code blocks with the same issue.

### Expected behavior

Magic comments should work in Python and bash code blocks just like they do in JavaScript code blocks. The `#` comment syntax should be recognized for these languages.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
