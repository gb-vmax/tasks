# Bug Report

### Describe the bug

After a recent update, the HTML serialization is returning the wrong value. Instead of getting the serialized HTML string, I'm getting what appears to be the internal state object.

### Reproduction

```js
import {rehype} from 'rehype'
import rehypeStringify from 'rehype-stringify'

const processor = rehype().use(rehypeStringify)

const result = processor.processSync('<p>Hello world</p>')
console.log(result.toString())
// Expected: '<p>Hello world</p>'
// Actual: '[object Object]'
```

When I try to use the result as a string or call `toString()` on it, I get `[object Object]` instead of the actual HTML content.

### Expected behavior

The processor should return the serialized HTML string that can be used directly or converted to a string with `toString()`.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
