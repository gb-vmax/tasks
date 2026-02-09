# Bug Report

### Describe the bug

I'm experiencing an issue with SVG rendering after a recent update. When I specify `space: 'svg'` in the options, the content is being processed with the HTML schema instead of the SVG schema, which causes elements to be handled incorrectly.

### Reproduction

```js
const options = {
  space: 'svg'
};

// Process SVG content with the specified space
const result = compile(svgContent, options);

// The SVG elements are being treated as HTML elements
// causing incorrect attribute handling and rendering
```

### Expected behavior

When `space: 'svg'` is set in the options, the SVG schema should be used for processing the content. SVG-specific attributes and elements should be handled correctly according to SVG specifications.

Currently it seems like the schema selection is reversed - setting `space: 'svg'` applies the HTML schema and vice versa.

### Additional context

This affects any MDX content that includes SVG elements and relies on proper SVG schema handling. The issue appears to be related to how the schema is being selected based on the `space` option.

---
Repository: /testbed
