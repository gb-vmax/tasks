# Bug Report

### Describe the bug

I'm experiencing an issue with the `visit` function where the visitor callback is receiving incorrect parent node and index information when traversing the AST. The parent parameter passed to the visitor seems to be off by one level in the tree hierarchy.

### Reproduction

```js
import { visit } from 'unist-util-visit';

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'hello' }
      ]
    }
  ]
};

visit(tree, 'text', (node, index, parent) => {
  console.log('Node:', node.value);
  console.log('Parent type:', parent?.type);
  console.log('Index:', index);
  // Expected parent to be 'paragraph', but getting something else
});
```

### Expected behavior

When visiting a text node that's nested inside a paragraph, the `parent` parameter should reference the paragraph node, and `index` should be the position of the text node within that paragraph's children array.

### Additional context

This seems to affect any nested node traversal where you need accurate parent/index information. The visitor callback parameters don't match the actual tree structure, making it difficult to perform operations that depend on knowing the correct parent-child relationships.

---
Repository: /testbed
