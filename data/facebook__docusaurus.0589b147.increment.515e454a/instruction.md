# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with HTML attribute serialization in rehype-stringify. When rendering HTML nodes with space-separated or comma-separated attributes (like `class` or `style`), the attribute values are getting corrupted or not properly formatted.

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
// Output is malformed - class attribute not properly serialized
```

The issue seems to affect any attributes that use space or comma separation. I noticed this after a recent update and it's breaking our HTML generation pipeline.

### Expected behavior

The HTML attributes should be properly serialized with correct spacing/comma separation. The output should match the input format for standard HTML attributes like `class`, `rel`, `sizes`, etc.

### System Info
- rehype-stringify: 10.0.0
- Node version: 18.x

---
Repository: /testbed
