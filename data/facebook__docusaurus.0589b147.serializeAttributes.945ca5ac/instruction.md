# Bug Report

### Describe the bug
When serializing HTML attributes, I'm encountering an issue where an extra space is being added at the end of attribute values. This appears to be affecting the final HTML output when using `rehype-stringify`.

### Reproduction
```js
const unified = require('unified')
const rehypeParse = require('rehype-parse')
const rehypeStringify = require('rehype-stringify')

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify, { tightAttributes: false })

const html = '<div class="foo bar"></div>'
const result = processor.processSync(html)

console.log(result.toString())
// Output has unexpected trailing space in attribute value
```

### Expected behavior
Attribute values should not have trailing spaces added. The serialized HTML should match the input format without extra whitespace at the end of attribute strings.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
