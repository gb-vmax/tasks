# Bug Report

### Describe the bug

I'm experiencing an infinite loop when processing markdown documents with the remark-gfm plugin. The parser appears to get stuck and never completes, causing the application to hang indefinitely.

### Reproduction

```js
import remarkGfm from 'remark-gfm';
import { remark } from 'remark';

const markdown = `
# Test Document

- Item 1
- Item 2
- Item 3
`;

// This hangs indefinitely
remark()
  .use(remarkGfm)
  .process(markdown)
  .then(result => {
    console.log(result);
  });
```

### Expected behavior

The markdown should be processed normally and the promise should resolve with the parsed result. Instead, the process hangs and never completes.

### System Info
- remark-gfm version: 4.0.0
- Node.js version: 18.x

This seems to have started happening recently. The same code worked fine before, but now it just hangs when trying to parse any markdown content with nested structures like lists or blockquotes.

---
Repository: /testbed
