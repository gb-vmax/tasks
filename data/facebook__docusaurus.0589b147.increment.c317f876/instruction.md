# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute serialization when using rehype-stringify. It seems like attributes that should be space-separated or comma-separated are not being handled correctly. The serialization output is malformed for certain HTML attributes.

### Reproduction

```js
const unified = require('unified')
const rehypeParse = require('rehype-parse')
const rehypeStringify = require('rehype-stringify')

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify)

const html = '<div class="foo bar baz"></div>'
const result = processor.processSync(html)

console.log(result.toString())
// Output is incorrect - class attribute values are not properly separated
```

When processing HTML with attributes that use space or comma separation (like `class`, `rel`, `accept`, etc.), the output doesn't match the expected format. The attribute values seem to be concatenated or improperly formatted.

### Expected behavior

Attributes should be serialized correctly with proper separators. Space-separated attributes (like `class`) should maintain spaces between values, and comma-separated attributes should maintain commas.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
