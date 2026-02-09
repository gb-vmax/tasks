# Bug Report

### Describe the bug

Getting a runtime error when trying to use the remark-rehype plugin. It seems like the default export is being called as a function immediately instead of being exported as a reference.

### Reproduction

```js
import remarkRehype from 'remark-rehype';

// Trying to use the plugin throws an error
const processor = unified()
  .use(remarkRehype)
  .process(content);
```

### Expected behavior

The plugin should be importable and usable without errors. The default export should be a function that can be called when needed, not the result of calling that function.

### System Info
- remark-rehype version: 11.0.0
- Node version: Latest

---
Repository: /testbed
