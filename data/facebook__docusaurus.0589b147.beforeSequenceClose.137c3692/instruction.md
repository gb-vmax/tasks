# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. Code blocks that should be properly closed are not being recognized correctly, and the parser seems to be treating closing fence sequences incorrectly.

### Reproduction

```markdown
```js
const foo = 'bar';
```
```

When parsing the above markdown with fenced code blocks, the closing fence (the three backticks after the code) is not being matched properly. The parser appears to be inverting the logic for checking whether a character matches the fence marker.

### Expected behavior

The parser should correctly identify and match closing fence sequences when they use the same marker character (backticks or tildes) as the opening fence. A code block should be properly closed when it encounters a sequence of the same fence marker.

For example:
- Opening fence: ` ``` `
- Code content: `const foo = 'bar';`
- Closing fence: ` ``` `

This should be parsed as a complete, valid fenced code block.

### System Info
- remark version: 15.0.1
- Environment: Node.js

---
Repository: /testbed
