# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation in MDX files. The TOC export seems to be creating invalid AST nodes that break the build process.

### Reproduction

```js
// In an MDX file with headings
## Heading 1
### Heading 2
#### Heading 3
```

When the MDX loader processes this file and tries to generate the TOC export, it fails to produce valid JavaScript output. The generated AST structure appears to be malformed.

### Expected behavior

The TOC should be properly exported as a flat array of heading objects that can be used for navigation. The AST nodes should be valid and produce working JavaScript code.

### Additional context

This seems to affect files that use TOC slices/imports. The spread element generation might be creating nested structures instead of the expected flat identifier references.

---
Repository: /testbed
