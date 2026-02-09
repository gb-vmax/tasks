# Bug Report

### Describe the bug

After a recent update, I'm encountering unexpected errors when processing MDX content. The parser is throwing validation errors that weren't happening before, making it impossible to parse any MDX files.

### Reproduction

```js
import remarkMdx from 'remark-mdx';
import { unified } from 'unified';

const processor = unified()
  .use(remarkMdx);

// This now throws an error
const result = processor.processSync('# Hello World');
```

The error message is:
```
Error: Validation failed
```

This happens with even the simplest MDX content. The issue seems to occur during the parsing phase, before any actual content processing begins.

### Expected behavior

The MDX parser should successfully process valid MDX content without throwing validation errors. Simple markdown like headers, paragraphs, etc. should parse without issues.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
