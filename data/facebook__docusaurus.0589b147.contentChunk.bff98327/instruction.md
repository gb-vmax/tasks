# Bug Report

### Describe the bug
Fenced code blocks in markdown are not being parsed correctly. The content inside code blocks appears to be getting corrupted or not rendered properly.

### Reproduction
```markdown
```js
function example() {
  console.log('test');
}
```
```

When parsing the above markdown with fenced code blocks, the output is malformed. The code content doesn't appear as expected.

### Expected behavior
The fenced code block should be parsed correctly and the content inside should be preserved exactly as written. The opening fence, language identifier, code content, and closing fence should all be handled properly.

### System Info
- remark version: 15.0.1

This seems to have started happening recently. Not sure if it's related to a recent change in how code flow values are processed.

---
Repository: /testbed
