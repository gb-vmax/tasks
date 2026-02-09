# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute normalization when using rehype-stringify. It appears that certain HTML attributes are not being properly normalized or merged, particularly when dealing with multiple schema definitions.

### Reproduction

When processing HTML with multiple attribute schemas, the resulting output seems to be missing some normalized attribute mappings. This affects how attributes are serialized in the final HTML output.

```js
// Example scenario where this manifests
const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify)

const result = processor.processSync('<div data-custom="value"></div>')
// Attributes may not be normalized as expected
```

### Expected behavior

All attribute definitions should be properly merged and normalized across all schema definitions. The final schema should include all property and normal mappings from every definition in the array.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
