# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when processing markdown directives. The parser seems to enter an endless loop and eventually crashes with a stack overflow error.

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
This is a directive
::
`;

// This causes infinite recursion
processor.process(markdown);
```

### Expected behavior

The markdown should be parsed successfully without any recursion errors. The directive should be processed and the parser should complete normally.

### Additional context

This seems to happen specifically when exiting directive nodes during parsing. The process hangs and eventually throws a "Maximum call stack size exceeded" error.

---
Repository: /testbed
