# Bug Report

### Describe the bug

I'm experiencing an issue with schema selection when processing MDX content. It appears that the wrong schema (HTML vs SVG) is being applied based on the `space` option.

### Reproduction

When setting `space: "svg"` in the MDX processor options, the content is being processed with the HTML schema instead of the SVG schema, and vice versa. This causes elements to be handled incorrectly.

```js
// When using SVG space
const processor = createProcessor({ space: 'svg' })
// Expected: SVG schema should be used
// Actual: HTML schema is being applied

// When using HTML space (or default)
const processor = createProcessor({ space: 'html' })
// Expected: HTML schema should be used  
// Actual: SVG schema is being applied
```

### Expected behavior

When `space` is set to `"svg"`, the SVG schema should be used for processing. When `space` is not set to `"svg"` (defaults to HTML), the HTML schema should be used.

### Additional context

This seems to have started happening recently and is causing SVG elements to be processed with incorrect attributes and HTML elements to be treated as SVG elements. The schemas appear to be swapped.

---
Repository: /testbed
