# Bug Report

### Describe the bug

I'm encountering an issue with heading elements when using remark-rehype. It appears that the `state.applyData` function is receiving its arguments in the wrong order, which causes data attributes and properties to be applied incorrectly to heading elements.

### Reproduction

```js
import remarkParse from 'remark-parse';
import remarkRehype from 'remark-rehype';
import { unified } from 'unified';

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype);

const markdown = '# Hello World';
const result = processor.processSync(markdown);

// The heading element properties are not applied correctly
console.log(result);
```

When processing markdown headings with custom data attributes or properties, the resulting HTML element structure doesn't have the expected properties attached to it. The data seems to be getting mixed up during the transformation.

### Expected behavior

Heading elements should properly receive all data attributes and properties from the markdown AST node. The `applyData` function should apply the data to the correct target element with the source node as reference.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
