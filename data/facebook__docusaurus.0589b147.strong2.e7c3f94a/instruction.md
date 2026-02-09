# Bug Report

### Describe the bug

After a recent update, bold/strong text formatting is not rendering correctly in markdown. When using `**text**` or `__text__` syntax, the content either doesn't appear or throws errors during processing.

### Reproduction

```js
const markdown = '**This should be bold**';
// Process the markdown
// Expected: renders as bold text
// Actual: content missing or error thrown
```

Try processing any markdown with strong/bold formatting:
- `**bold text**`
- `__also bold__`

The text either disappears completely or the parser fails to handle it properly.

### Expected behavior

Bold/strong markdown syntax should render correctly and produce the expected output with proper text formatting.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
