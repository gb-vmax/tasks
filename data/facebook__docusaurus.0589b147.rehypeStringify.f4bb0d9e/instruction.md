# Bug Report

### Describe the bug

I'm experiencing an issue with `rehype-stringify` where the HTML output is not being returned from the compiler. After processing, I'm getting `undefined` instead of the expected HTML string.

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

console.log(result.value); // undefined instead of HTML string
```

### Expected behavior

The processor should return the HTML string after compilation. Instead, it's returning `undefined`.

### Additional context

This seems to have broken recently. The compiler function is not returning the output from `toHtml()`, which causes the entire processing pipeline to fail silently.

---
Repository: /testbed
