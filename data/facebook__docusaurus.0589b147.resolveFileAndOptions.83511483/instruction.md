# Bug Report

### Describe the bug

I'm experiencing an issue with MDX file format detection. When I explicitly specify `format: "md"` or `format: "mdx"` in the options, the format is not being respected and instead gets overridden based on the file extension logic.

### Reproduction

```js
// When explicitly setting format to "md"
const result = compile(source, { format: "md" });
// Expected: format should be "md"
// Actual: format gets overridden to "mdx" if file extension doesn't match

// Same issue with "mdx"
const result2 = compile(source, { format: "mdx" });
// Expected: format should be "mdx"  
// Actual: format gets overridden based on extension checking
```

The problem seems to be that when I explicitly pass a format option, it's being ignored and the system falls back to checking file extensions instead of honoring my explicit choice.

### Expected behavior

When I explicitly specify `format: "md"` or `format: "mdx"` in the options, that format should be used regardless of file extension or other heuristics. The explicit option should take precedence over automatic detection.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
