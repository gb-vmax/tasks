# Bug Report

### Describe the bug

After a recent update, HTML parsing in markdown appears to be stuck in an infinite loop. The parser seems to hang indefinitely when encountering HTML tags in the markdown content.

### Reproduction

```js
const markdown = '<div>Hello World</div>';
const result = remark().parse(markdown);
// Process hangs here and never completes
```

This also happens with any inline HTML:

```js
const markdown = 'Some text with <span>inline HTML</span> content';
// Parser becomes unresponsive
```

### Expected behavior

The parser should successfully process HTML content embedded in markdown and return the parsed result without hanging.

### System Info
- remark version: 15.0.1
- Node version: Latest

The parsing was working fine before, but now any markdown content containing HTML tags causes the parser to become unresponsive. This is blocking our entire documentation pipeline.

---
Repository: /testbed
