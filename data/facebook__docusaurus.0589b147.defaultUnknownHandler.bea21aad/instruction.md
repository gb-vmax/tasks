# Bug Report

### Describe the bug

I'm experiencing an issue with unknown node handling in remark-rehype. When processing markdown with custom/unknown nodes that have a `value` property, they're not being converted to text nodes as expected. Instead, they're being wrapped in `div` elements with empty children arrays.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkRehype = require('remark-rehype');

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype);

// Create a custom node with a value property
const customNode = {
  type: 'customType',
  value: 'some text content'
};

// Process through the pipeline
const result = processor.runSync({
  type: 'root',
  children: [customNode]
});

// Expected: customNode should become a text node with value "some text content"
// Actual: customNode becomes a div element with empty children
console.log(result);
```

### Expected behavior

Unknown nodes that contain a `value` property should be converted to text nodes preserving their text content, not wrapped in div elements with empty children arrays.

### Additional context

This seems to affect any custom or plugin-generated nodes that aren't part of the standard markdown AST but have text content stored in a `value` field. The conversion logic appears to be inverted - nodes WITH values are being treated as elements instead of text.

---
Repository: /testbed
