# Bug Report

### Describe the bug

I'm encountering an issue with how unknown nodes are being handled in the remark-rehype conversion. It seems like nodes with `value` properties are being converted incorrectly depending on whether they have `hProperties` or `hChildren` data.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkRehype = require('remark-rehype');

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype);

// Create a custom node with value and hProperties
const customNode = {
  type: 'custom',
  value: 'test content',
  data: {
    hProperties: { className: 'custom-class' }
  }
};

// Process the node
const result = processor.runSync({
  type: 'root',
  children: [customNode]
});

console.log(result);
```

### Expected behavior

When a node has a `value` property AND custom `hProperties` or `hChildren` in its data, it should be treated as a text node and preserve the value. Currently, it's being converted to a div element instead, which loses the text content.

### Actual behavior

The node gets converted to a div element wrapper even when it should be converted to a text node based on the presence of hProperties/hChildren.

### Additional context

This affects custom node types that need to pass through as text nodes while still having HTML properties attached. The logic for determining when to create a text node vs an element seems inverted.

---
Repository: /testbed
