# Bug Report

### Describe the bug
After a recent update, the rehype-stringify compiler is returning an object with an `html` property instead of returning the HTML string directly. This breaks existing code that expects the compiler to return a plain string.

### Reproduction
```js
import rehypeStringify from 'rehype-stringify';
import { unified } from 'unified';

const processor = unified()
  .use(rehypeStringify);

const tree = {
  type: 'root',
  children: [
    {
      type: 'element',
      tagName: 'div',
      properties: {},
      children: [{ type: 'text', value: 'Hello' }]
    }
  ]
};

const result = processor.stringify(tree);
console.log(result); // Expected: '<div>Hello</div>'
                     // Actual: { html: '<div>Hello</div>' }
```

### Expected behavior
The compiler should return the HTML string directly, not wrapped in an object. Code that previously worked like `const html = processor.stringify(tree)` now breaks because `html` is an object instead of a string.

### Additional context
This appears to have changed recently and is causing issues with existing pipelines that expect a string return value from the compiler.

---
Repository: /testbed
