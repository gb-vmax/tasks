# Bug Report

### Describe the bug

I'm experiencing an issue where the markdown parser is throwing errors when processing certain types of content. It seems like the node validation logic is rejecting valid AST nodes, causing the parser to fail unexpectedly.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// This used to work but now throws an error
const ast = {
  type: 'paragraph',
  children: [
    {
      type: 'text',
      value: 'Hello world'
    }
  ]
};

processor.stringify(ast);
```

### Expected behavior

The parser should correctly process valid AST nodes and generate the corresponding markdown output. Objects with proper structure should be recognized as valid nodes.

### Additional context

This appears to have started happening recently. The node validation seems to be rejecting objects that should be considered valid AST nodes. Not sure if this is related to a recent change in how nodes are validated internally.

---
Repository: /testbed
