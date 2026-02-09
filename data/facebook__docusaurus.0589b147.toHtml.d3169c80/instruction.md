# Bug Report

### Describe the bug

I'm experiencing issues with the HTML/SVG serialization in rehype-stringify. When I try to use the library with specific quote options or SVG namespaces, it's not working as expected.

### Reproduction

```js
const rehype = require('rehype');
const stringify = require('rehype-stringify');

// Case 1: Using single quotes
const processor = rehype()
  .use(stringify, { quote: "'" });

const result = processor.processSync('<div class="test">content</div>');
// Expected: <div class='test'>content</div>
// Getting an error instead

// Case 2: SVG elements
const svgProcessor = rehype()
  .use(stringify, { space: 'svg' });

const svgResult = svgProcessor.processSync('<svg><circle /></svg>');
// SVG elements are not being handled correctly
```

### Expected behavior

1. When setting `quote: "'"`, the output should use single quotes for attributes without throwing errors
2. When setting `space: 'svg'`, SVG elements should be serialized with the correct SVG schema/namespace rules

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

The quote validation seems overly strict and SVG space handling appears to be inverted. This is breaking my workflow for generating both HTML and SVG outputs.

---
Repository: /testbed
