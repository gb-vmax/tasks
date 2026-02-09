# Bug Report

### Describe the bug

I'm encountering an issue with object type checking in mdast-util-to-string. It seems like the type validation logic is broken and causing unexpected behavior when processing markdown AST nodes.

### Reproduction

```js
const mdast = require('mdast-util-to-string');

// Simple text node
const textNode = {
  type: 'text',
  value: 'Hello world'
};

// This should work but doesn't
const result = mdast.toString(textNode);
console.log(result); // Expected: 'Hello world', but getting unexpected behavior
```

When I try to convert basic markdown nodes to strings, the library doesn't seem to recognize valid node objects anymore. It's like the internal type checking is rejecting legitimate nodes.

### Expected behavior

The library should correctly identify valid mdast nodes and convert them to strings. Basic text nodes and other standard mdast node types should be processed without issues.

### Additional context

This seems to have started recently. The type checking logic might have been changed in a way that breaks compatibility with standard JavaScript objects. Not sure if this is related to how the `node()` helper function validates objects internally.

---
Repository: /testbed
