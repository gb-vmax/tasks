# Bug Report

### Describe the bug

After a recent update, MDX processing seems to be broken when using `remarkRehype` with a processor destination. The transformed output is incorrect - instead of getting the expected HAST tree, I'm getting the original MDAST tree back.

### Reproduction

```js
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkRehype from 'remark-rehype';
import rehypeStringify from 'rehype-stringify';

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype, unified().use(rehypeStringify))
  .use(rehypeStringify);

const result = await processor.process('# Hello\n\nWorld');
console.log(result.value);
```

### Expected behavior

Should output proper HTML like `<h1>Hello</h1><p>World</p>`, but instead the tree transformation doesn't happen correctly and the output is malformed or the wrong tree type is being passed through the pipeline.

This was working fine before the update. The issue appears when passing a unified processor as the destination argument to `remarkRehype`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
