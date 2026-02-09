# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where it seems to be throwing errors about accessing properties beyond array bounds. The parser appears to be iterating past the end of an array when processing exports, which is causing unexpected behavior.

### Reproduction

```js
// When parsing MDX content with exports
const mdxContent = `
export const foo = 'bar';
export const baz = 'qux';

# Hello World
`;

// Parser attempts to access array elements beyond the valid range
// This causes issues during the parsing phase
```

### Expected behavior

The parser should correctly iterate through the exports without attempting to access indices beyond the array length. It should only process valid array elements.

### Additional context

This seems to happen specifically when the parser is processing module exports. The iteration logic appears to be going one element too far, which could lead to undefined behavior or errors depending on the runtime environment.

---
Repository: /testbed
