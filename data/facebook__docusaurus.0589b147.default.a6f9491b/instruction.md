# Bug Report

### Describe the bug

I'm experiencing an issue with the rehype-stringify plugin where it's not being properly exported or initialized. When trying to use the plugin, it seems like the export is returning a function that returns the plugin instead of the plugin itself, which breaks the normal usage pattern.

### Reproduction

```js
import rehypeStringify from 'rehype-stringify';
import { unified } from 'unified';
import rehypeParse from 'rehype-parse';

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify)
  .processSync('<p>test</p>');

console.log(processor);
```

### Expected behavior

The plugin should be directly usable with `.use()` and should properly stringify the HTML tree. Instead, it appears the export is wrapped in an extra function layer that prevents normal operation.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
