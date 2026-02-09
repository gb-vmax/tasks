# Bug Report

### Describe the bug

I'm encountering a stack overflow error when processing markdown content that contains directives. The parser seems to get stuck in an infinite recursion loop and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
import remarkDirective from 'remark-directive';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective);

const markdown = `
::note
This is a note directive
::
`;

// This causes a stack overflow
processor.processSync(markdown);
```

### Expected behavior

The markdown with directives should be parsed successfully without crashing. The processor should handle the directive syntax and return a valid AST.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

This is blocking our documentation pipeline. Any help would be appreciated!

---
Repository: /testbed
