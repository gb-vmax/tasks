# Bug Report

### Describe the bug

I'm experiencing an issue with HTML entity encoding when using `rehype-stringify`. The output is producing unnecessarily long numeric character references instead of using the shorter named entities, even when named entities are available and shorter.

### Reproduction

```js
const rehype = require('rehype');
const html = require('rehype-stringify');

const processor = rehype()
  .use(html, {
    entities: {
      useNamedReferences: true,
      useShortestReferences: true
    }
  });

// Process HTML with special characters
const result = processor.processSync('<p>&nbsp;</p>');
console.log(result.toString());

// Expected: <p>&nbsp;</p>
// Actual: <p>&#160;</p> (or similar numeric reference)
```

### Expected behavior

When `useShortestReferences` is enabled, the library should choose the shortest representation between named entities and numeric references. Named entities like `&nbsp;` should be preferred over their numeric equivalents `&#160;` when they're shorter.

### Additional context

This seems to affect various HTML entities where the named version is actually shorter than the numeric version. The logic for selecting between named and numeric references appears to be inverted or incorrect.

---
Repository: /testbed
