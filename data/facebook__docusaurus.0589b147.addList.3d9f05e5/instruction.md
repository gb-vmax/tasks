# Bug Report

### Describe the bug

I'm experiencing an issue where plugins are not being properly added when using an array of plugins. It seems like the first plugin in the array is being skipped or not processed correctly.

### Reproduction

```js
const processor = unified()
  .use([
    remarkParse,
    remarkGfm,
    remarkRehype
  ])

// Only the second and third plugins seem to be applied
// The first plugin (remarkParse) is being skipped
```

When I pass an array with multiple plugins, the first one doesn't get applied. If I add them individually with separate `.use()` calls, everything works fine:

```js
// This works correctly
const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(remarkRehype)
```

### Expected behavior

All plugins in the array should be processed and applied, including the first one. The behavior should be the same whether plugins are added as an array or individually.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
