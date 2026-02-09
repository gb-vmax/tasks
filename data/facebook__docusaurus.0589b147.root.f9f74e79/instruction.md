# Bug Report

### Describe the bug

When converting HAST (HTML Abstract Syntax Tree) to HTML string using rehype-stringify, the output is duplicated. The HTML content appears twice in the final string output.

### Reproduction

```js
import { unified } from 'unified';
import rehypeParse from 'rehype-parse';
import rehypeStringify from 'rehype-stringify';

const processor = unified()
  .use(rehypeParse)
  .use(rehypeStringify);

const html = '<div>Hello World</div>';
const result = processor.processSync(html);

console.log(result.toString());
// Expected: <div>Hello World</div>
// Actual: <div>Hello World</div><div>Hello World</div>
```

### Expected behavior

The HTML should be serialized once, not duplicated. The output should match the input structure without any repetition.

### System Info

- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
