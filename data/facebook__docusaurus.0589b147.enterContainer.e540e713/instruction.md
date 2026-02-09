# Bug Report

### Describe the bug

I'm experiencing a crash when using container directives in markdown parsing. The parser throws a `TypeError` about `enter.call` receiving arguments in the wrong order, which causes the entire parsing operation to fail.

### Reproduction

```js
import remarkDirective from 'remark-directive';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkStringify from 'remark-stringify';

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)
  .use(remarkStringify);

const markdown = `
:::note
This is a container directive
:::
`;

// This crashes with TypeError
processor.processSync(markdown);
```

### Expected behavior

The container directive should be parsed correctly without throwing errors. The markdown should be processed successfully and the directive node should be created properly.

### Additional context

This seems to happen specifically with container directives (the `:::` syntax). Regular text directives and leaf directives might not be affected, but I haven't tested all cases thoroughly.

The error message suggests that the function call is receiving the wrong context or arguments in an unexpected order.

---
Repository: /testbed
