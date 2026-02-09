# Bug Report

### Describe the bug

After a recent update, the remark-directive vendor bundle appears to be broken. When trying to use directives in markdown processing, I'm getting errors related to property definitions not working correctly.

### Reproduction

```js
// When processing markdown with directives
const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)
  .use(remarkRehype)

const result = processor.processSync('::directive[content]')
// Throws error about undefined properties
```

### Expected behavior

Directives should be parsed and processed normally without errors. The exports from the remark-directive module should be accessible and functional.

### System Info

- remark-directive version: 3.0.0 (vendored)
- Node version: Latest

### Additional context

This seems to have started after changes to the vendor bundle. The module exports aren't working as expected and trying to access any exported functions results in undefined or property access errors.

---
Repository: /testbed
