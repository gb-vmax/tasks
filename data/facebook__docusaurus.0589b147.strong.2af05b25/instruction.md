# Bug Report

### Describe the bug

I'm experiencing an issue with the `strong` function in remark-rehype where it seems to be referencing an undefined variable. When processing markdown with bold/strong text, the conversion is failing.

### Reproduction

```js
import remarkRehype from 'remark-rehype';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype);

const markdown = '**bold text**';
const result = processor.processSync(markdown);
```

### Expected behavior

The markdown should be successfully converted to HTML with the strong text properly transformed into `<strong>` tags. Instead, it appears to fail during the conversion process.

### Additional context

This seems to be related to how the `strong` function handles the node transformation. The issue occurs specifically when processing any markdown that contains bold/strong syntax (`**text**` or `__text__`).

---
Repository: /testbed
