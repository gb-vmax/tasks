# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute handling in rehype-stringify. When processing HTML elements, the property and attribute mappings appear to be incorrect, causing attributes to be serialized with wrong names.

### Reproduction

```js
const unified = require('unified');
const rehypeParse = require('rehype-parse');
const rehypeStringify = require('rehype-stringify');

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify);

const html = '<div className="test"></div>';
const result = processor.processSync(html);

console.log(result.toString());
// Expected: <div className="test"></div>
// Actual: attribute name is wrong
```

When I create elements with specific property/attribute combinations, the resulting HTML has swapped or incorrect attribute names. It seems like the internal property-to-attribute mapping is broken.

### Expected behavior

The HTML attributes should be correctly mapped and serialized with their proper names. Properties like `className`, `htmlFor`, etc. should map to their corresponding HTML attributes correctly.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

This is blocking my project as all HTML output has corrupted attribute names. Any help would be appreciated!

---
Repository: /testbed
