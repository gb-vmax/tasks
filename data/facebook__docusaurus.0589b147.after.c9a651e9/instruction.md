# Bug Report

### Describe the bug

The markdown parser is completely broken after a recent change. When trying to parse any markdown content with links, the parser crashes immediately.

### Reproduction

```js
import { remark } from 'remark';

const markdown = `
This is a [link](https://example.com) in markdown.
`;

const result = remark().parse(markdown);
console.log(result);
```

Running this code results in a parser error. The issue seems to affect all markdown content that contains link syntax.

### Expected behavior

The parser should successfully parse markdown links and return a proper AST without errors.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is blocking our documentation build pipeline. Any help would be appreciated!

---
Repository: /testbed
