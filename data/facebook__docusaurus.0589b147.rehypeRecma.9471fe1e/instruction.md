# Bug Report

### Describe the bug

I'm encountering an issue where MDX files are not being properly transformed/compiled. The output appears to be returning the raw rehype tree instead of the expected ESTree structure that should be generated.

### Reproduction

When processing an MDX file through the compilation pipeline, the `rehypeRecma` plugin seems to be returning the wrong value. Instead of getting a properly transformed ESTree that can be evaluated, I'm getting back what looks like the original rehype tree structure.

```js
// Processing an MDX file
const result = await compile('# Hello\n\nSome content');
// Expected: ESTree structure
// Actual: rehype tree structure
```

This makes it impossible to properly evaluate or render the MDX content since the tree isn't in the correct format for the next stage of processing.

### Expected behavior

The `rehypeRecma` plugin should transform the rehype tree into an ESTree (JavaScript AST) that can be used by the recma plugins and eventually compiled into executable code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
