# Bug Report

### Describe the bug

I'm experiencing an issue with leaf directives in remark-directive. When parsing markdown content that contains leaf directives (like `::directive`), the parser seems to crash or produce malformed output.

### Reproduction

```js
import remarkDirective from 'remark-directive';
import remarkParse from 'remark-parse';
import { unified } from 'unified';

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective);

const markdown = `
::my-leaf-directive
`;

const result = processor.parse(markdown);
// Parser fails or produces unexpected output
```

### Expected behavior

The leaf directive should be parsed correctly and produce a valid AST node with type `leafDirective`. The parser should handle leaf directives the same way it handles container and text directives.

### System Info
- remark-directive version: 3.0.0
- Node.js version: 18.x

---
Repository: /testbed
