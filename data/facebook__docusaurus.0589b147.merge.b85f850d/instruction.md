# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute handling in rehype-stringify. It seems like HTML attributes are being processed incorrectly, causing attributes to be rendered with wrong values or in the wrong format.

### Reproduction

```js
const unified = require('unified');
const rehypeParse = require('rehype-parse');
const rehypeStringify = require('rehype-stringify');

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify);

const html = '<div data-custom="value" class="test"></div>';
const result = processor.processSync(html);

console.log(result.toString());
// Expected: attributes should be preserved correctly
// Actual: attributes appear to be swapped or incorrectly formatted
```

### Expected behavior

HTML attributes should be preserved and rendered correctly when processing HTML through rehype-stringify. The attribute names and values should match the input.

### System Info
- rehype-stringify version: 10.0.0
- Node.js version: 16.x

---
Repository: /testbed
