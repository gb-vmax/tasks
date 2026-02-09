# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute normalization in rehype-stringify. When working with HTML properties, it seems like attributes are not being properly mapped to their normalized forms. This is causing properties to not be recognized correctly when processing HTML elements.

### Reproduction

```js
// When trying to process HTML with specific attributes
const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify)

const html = '<div data-custom="value"></div>'
const result = processor.processSync(html)

// Expected: Attributes should be properly normalized and accessible
// Actual: Attribute mapping seems broken
```

The problem appears when dealing with property definitions and their attribute mappings. Properties that should be available through their normalized names aren't being found.

### Expected behavior

HTML attributes should be properly normalized and mapped to their property names. When accessing properties through either their original or normalized forms, they should resolve correctly.

### System Info
- rehype-stringify: 10.0.0
- Node version: Latest

This seems like a regression as it was working in previous versions. The attribute normalization logic might have been inadvertently changed.

---
Repository: /testbed
