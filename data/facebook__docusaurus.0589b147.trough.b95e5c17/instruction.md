# Bug Report

### Describe the bug

I'm experiencing an issue with the middleware pipeline execution in remark. When chaining multiple transformers, the pipeline appears to skip the first middleware function and starts execution from the second one instead.

### Reproduction

```js
const unified = require('unified')
const markdown = require('remark-parse')

const processor = unified()
  .use(markdown)
  .use(function firstPlugin() {
    return function transformer(tree) {
      console.log('First plugin executed')
      // Transform the tree
    }
  })
  .use(function secondPlugin() {
    return function transformer(tree) {
      console.log('Second plugin executed')
      // Transform the tree
    }
  })

processor.process('# Test')
```

### Expected behavior

Both plugins should execute in order:
```
First plugin executed
Second plugin executed
```

### Actual behavior

The first plugin is being skipped entirely. Only the second plugin runs.

This seems to have started happening recently and is breaking my plugin chain where I rely on transformations from earlier plugins.

---
Repository: /testbed
