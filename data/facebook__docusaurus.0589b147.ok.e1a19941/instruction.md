# Bug Report

### Describe the bug

After a recent update, I'm getting an unexpected error when processing GitHub Flavored Markdown (GFM) content. The parser is throwing an error that shouldn't be happening during normal operation.

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

This is a simple test with GFM features.
`;

// This throws an error
processor.processSync(markdown);
```

### Expected behavior

The markdown should be parsed successfully without throwing any errors. The processor should handle the GFM content normally.

### Actual behavior

Getting the following error:
```
Error: Unexpected error
```

This seems to be triggered during the parsing phase. The error appears to come from somewhere deep in the remark-gfm vendor code.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
