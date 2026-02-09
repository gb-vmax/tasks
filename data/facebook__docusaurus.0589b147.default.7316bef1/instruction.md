# Bug Report

### Describe the bug
I'm getting a "rehypeStringify is not a function" error when trying to use the rehype-stringify plugin. It seems like the default export is being called immediately instead of being exported as a function.

### Reproduction
```js
import rehypeStringify from 'rehype-stringify';
import { unified } from 'unified';
import rehypeParse from 'rehype-parse';

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify); // Error: rehypeStringify is not a function

const html = '<div>test</div>';
processor.process(html);
```

### Expected behavior
The plugin should be exported as a function that can be passed to `.use()`. Instead, it appears to be invoked during the export, which breaks the plugin system.

### System Info
- rehype-stringify: 10.0.0
- Node.js: v18.x

---
Repository: /testbed
