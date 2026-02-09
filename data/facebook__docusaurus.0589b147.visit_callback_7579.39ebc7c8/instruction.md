# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading formatting where headings are being incorrectly formatted as setext-style (underlined with `=` or `-`) when they should be using ATX-style (`#` prefix). This seems to be happening with headings that contain line breaks or certain content.

### Reproduction

```js
const markdown = remark()
  .use(remarkStringify)
  .stringify({
    type: 'heading',
    depth: 2,
    children: [
      { type: 'text', value: 'Normal heading text' }
    ]
  });

// Expected: ## Normal heading text
// Actual: Getting setext format when it shouldn't
```

The issue appears when processing headings - they're being converted to setext style even when the content doesn't actually contain line breaks.

### Expected behavior

Headings should only be formatted as setext-style when they actually contain literal line breaks or break nodes. Regular headings without breaks should use ATX formatting (with `#` symbols) by default.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
