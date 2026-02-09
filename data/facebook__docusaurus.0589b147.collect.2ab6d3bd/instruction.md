# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where source position mappings are being generated incorrectly. When processing MDX content, the position stops that map the serialized output back to the original source locations appear to be in the wrong order.

### Reproduction

```js
// When parsing MDX content with nested elements
const mdxContent = `
# Hello

Some **bold** text here
`;

// After processing, the position stops are reversed
// The start position is being added after the end position
// This causes source maps and error reporting to point to incorrect locations
```

### Expected behavior

The position stops array should maintain the correct order with start positions before end positions. Currently it seems like the start and end positions are being pushed in reverse order, which breaks any tooling that relies on these position mappings for error reporting or source map generation.

### Additional context

This affects error messages and debugging tools that try to map compiled output back to the original MDX source. The positions end up pointing to the wrong locations in the source file.

---
Repository: /testbed
