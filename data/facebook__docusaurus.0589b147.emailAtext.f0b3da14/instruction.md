# Bug Report

### Describe the bug
When parsing autolinks with email addresses, the parser enters an infinite loop and hangs indefinitely. This happens specifically when processing the `@` symbol in email autolinks.

### Reproduction
```js
const markdown = '<user@example.com>'

// Parser hangs here and never returns
const result = remark().parse(markdown)
```

### Expected behavior
The parser should successfully parse email autolinks and return the AST without hanging. The `@` symbol should be consumed and processing should continue to parse the rest of the email address.

### Additional context
This appears to affect any markdown content containing email autolinks in the `<email@domain.com>` format. The parser gets stuck and becomes unresponsive, requiring the process to be killed.

---
Repository: /testbed
