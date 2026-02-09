# Bug Report

### Describe the bug

I'm experiencing an issue with HTML serialization where the output is completely broken. Instead of getting the expected HTML string, I'm getting back either the node object itself or some internal state transforms object.

### Reproduction

```js
const { unified } = require('unified');
const rehypeParse = require('rehype-parse');
const rehypeStringify = require('rehype-stringify');

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify);

const html = '<div><p>Hello world</p></div>';
const result = processor.processSync(html);

console.log(result.toString());
// Expected: '<div><p>Hello world</p></div>'
// Actual: [object Object] or something similar
```

The HTML tree is not being properly serialized to a string. It seems like the root handler is returning the wrong thing entirely.

### Expected behavior

The processor should return a properly stringified HTML document, not an object reference or internal state.

### Additional context

This appears to have started happening recently. The HTML parsing works fine, but the stringify step is completely broken. Any document I try to process just returns object references instead of actual HTML strings.

---
Repository: /testbed
