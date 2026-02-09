# Bug Report

### Describe the bug

I'm experiencing an issue where HTML attributes are being set incorrectly when using rehype-stringify. Instead of the attribute being set to its proper value, it's being set to the attribute name itself.

### Reproduction

```js
const unified = require('unified')
const rehypeParse = require('rehype-parse')
const rehypeStringify = require('rehype-stringify')

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify)

const html = '<img src="image.jpg" alt="description">'
const result = processor.processSync(html)

console.log(result.toString())
// Expected: <img src="image.jpg" alt="description">
// Actual: <img src="src" alt="alt">
```

### Expected behavior

Attributes should retain their original values. For example, `src="image.jpg"` should remain `src="image.jpg"`, not become `src="src"`.

### System Info

- rehype-stringify version: 10.0.0
- Node version: 18.x

This seems to have broken recently and is affecting all HTML attributes in my project. Any elements with attributes are now rendering with the attribute name as the value instead of the actual value.

---
Repository: /testbed
