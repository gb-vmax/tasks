# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when using the remark-gfm plugin. The application crashes with a "Maximum call stack size exceeded" error during markdown processing.

### Reproduction

```js
import remarkGfm from 'remark-gfm';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm);

const markdown = `
# Test

This is a **test** with GFM features.
`;

// This causes a stack overflow
processor.processSync(markdown);
```

### Expected behavior

The markdown should be processed successfully without any stack overflow errors. The plugin should handle the markdown content and return the processed result.

### System Info

- Node version: 18.x
- remark-gfm: 4.0.0

This seems to have started happening recently. The same code was working fine before. Any help would be appreciated!

---
Repository: /testbed
