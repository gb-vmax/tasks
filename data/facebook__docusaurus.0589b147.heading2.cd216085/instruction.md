# Bug Report

### Describe the bug

After a recent update, MDX heading elements are being generated with incorrect properties. The heading nodes now have `type: "header"` instead of `type: "heading"`, and the `depth` property is set to `undefined` instead of a numeric value.

### Reproduction

```js
// When parsing MDX with headings:
const mdxContent = `
# My Heading
## Subheading
`;

// The generated AST nodes have wrong structure:
// Expected: { type: "heading", depth: 1, children: [...] }
// Actual: { type: "header", depth: undefined, children: [...] }
```

### Expected behavior

Heading nodes in the MDX AST should:
1. Have `type: "heading"` (not `"header"`)
2. Have a numeric `depth` property (1-6) corresponding to the heading level
3. Maintain compatibility with existing MDX processors and plugins

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is breaking existing MDX plugins that rely on the standard heading node structure. Any transformations or visitors looking for `type: "heading"` nodes will no longer work correctly.

---
Repository: /testbed
