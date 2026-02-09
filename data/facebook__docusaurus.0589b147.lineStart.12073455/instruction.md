# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where the parser seems to be incorrectly handling non-lazy lines. When processing directives, lines that should be accepted are being rejected, and the parser behavior appears inconsistent.

### Reproduction

```js
const unified = require('unified')
const remarkParse = require('remark-parse')
const remarkDirective = require('remark-directive')

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const markdown = `
:::note
This is a directive with
multiple lines of content
:::
`

const result = processor.parse(markdown)
console.log(result)
```

When parsing directives with multi-line content, the parser doesn't correctly recognize continuation lines. It seems like the lazy line detection logic is inverted - lines that should be part of the directive block are being treated as if they're outside of it.

### Expected behavior

The parser should correctly identify and include all lines within a directive block, properly distinguishing between lazy and non-lazy lines according to the CommonMark spec.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
