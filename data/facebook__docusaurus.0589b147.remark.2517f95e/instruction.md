# Bug Report

### Describe the bug

After a recent update, markdown processing is behaving incorrectly. When processing markdown content, paragraph nodes are being removed unexpectedly, leaving only headings in the output.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Title

This is a paragraph that should be preserved.

## Subtitle

Another paragraph here.
`;

const result = remark(markdown, { transform: true });
console.log(result);
```

### Expected behavior

The processor should preserve all markdown content including paragraphs. The output should contain both headings and paragraph text. Instead, only the headings are being returned and all paragraph content is stripped out.

This is breaking our documentation generation pipeline where we need to process markdown files while keeping all content intact.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
