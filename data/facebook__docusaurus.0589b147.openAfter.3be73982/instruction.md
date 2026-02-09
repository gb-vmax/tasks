# Bug Report

### Describe the bug

When using directive containers with interrupts, the parsing behavior seems incorrect. The container fence handling appears to be checking conditions in the wrong order, which causes issues with how line endings and null codes are processed in interrupt contexts.

### Reproduction

```markdown
:::note
Some content here
:::
```

When this is parsed in an interrupt context (e.g., inside a list or other block element), the directive container doesn't close properly or the content isn't recognized as expected.

Example that triggers the issue:
```js
const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)
  
const result = processor.processSync('- List item\n  :::warning\n  Content\n  :::')
```

### Expected behavior

Directive containers should be properly parsed and closed even when used within interrupt contexts. The fence should correctly handle line endings and EOF markers regardless of whether `self.interrupt` is true or false.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
