# Bug Report

### Describe the bug

When parsing HTML tags in markdown, self-closing tags (like `<br/>` or `<img/>`) are not being handled correctly. The parser seems to get stuck in an infinite loop or doesn't properly recognize the closing slash in self-closing tags.

### Reproduction

```markdown
This is some text with a self-closing tag <br/> in the middle.

Or an image: <img src="test.jpg"/>
```

When processing markdown content with self-closing HTML tags, the parser doesn't complete successfully. Tags that should be recognized as valid HTML are not being parsed as expected.

### Expected behavior

Self-closing HTML tags should be properly recognized and parsed. The markdown processor should handle `<br/>`, `<img/>`, and other self-closing tags without issues, just like it handles regular opening and closing tags like `<div></div>`.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
