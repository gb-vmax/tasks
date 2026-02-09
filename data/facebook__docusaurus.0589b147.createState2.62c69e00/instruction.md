# Bug Report

### Describe the bug

I'm encountering an issue with MDX rendering where SVG elements are being processed with the wrong schema. It appears that when `space` is set to `"svg"`, the HTML schema is being applied instead of the SVG schema, and vice versa.

### Reproduction

```js
const options = {
  space: 'svg'
};

// When processing SVG content with space: 'svg'
// The HTML schema is incorrectly applied
// This causes SVG-specific attributes and elements to be handled improperly
```

### Expected behavior

When `space: 'svg'` is specified in options, the SVG schema should be used for processing. When `space` is not `'svg'` (or defaults to HTML), the HTML schema should be used.

Currently it seems like the schemas are swapped - SVG space gets HTML schema and HTML space gets SVG schema.

### Additional context

This is affecting how SVG elements and attributes are being transformed, particularly with attribute name casing and SVG-specific properties. The rendered output doesn't match what's expected for SVG content.

---
Repository: /testbed
