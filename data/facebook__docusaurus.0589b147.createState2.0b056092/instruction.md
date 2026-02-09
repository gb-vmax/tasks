# Bug Report

### Describe the bug

I'm encountering an issue with MDX rendering where SVG elements are being processed with the wrong schema. When I specify `space: "svg"` in the options, it seems like the HTML schema is being applied instead, and vice versa.

### Reproduction

```js
const options = {
  space: 'svg'
}

// When processing SVG content with these options,
// elements are treated as HTML instead of SVG
```

When I try to render SVG content in MDX, the attributes and element handling don't match what's expected for SVG. For example, SVG-specific attributes might not be recognized correctly, or the casing of attributes is wrong.

### Expected behavior

When `space: "svg"` is specified, the SVG schema should be used for processing elements. Similarly, when no space is specified or when `space: "html"` is used, the HTML schema should be applied.

The schemas appear to be swapped - SVG space is getting HTML schema and HTML space is getting SVG schema.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
