# Bug Report

### Describe the bug

I'm experiencing an issue with markdown serialization where the output is missing trailing content or has incorrect spacing at the end of container elements. It seems like the serialization logic is popping the index stack prematurely, which might be affecting how the final child element in a container is processed.

### Reproduction

```js
// Example markdown structure with nested containers
const ast = {
  type: 'root',
  children: [
    {
      type: 'blockquote',
      children: [
        { type: 'paragraph', children: [/* ... */] },
        { type: 'paragraph', children: [/* ... */] },
        { type: 'paragraph', children: [/* ... */] }
      ]
    }
  ]
}

// Serialize the AST back to markdown
const output = serialize(ast)

// The output appears to be missing proper handling of the last child element
```

### Expected behavior

The serialization should correctly handle all children in a container, including the last one, and maintain proper spacing/formatting between elements. The index stack should only be popped after all children have been fully processed.

### Additional context

This appears to be related to how the containerFlow function manages the index stack and determines when to add spacing between child elements. The condition for adding spacing between children might be off by one, causing the last child to be handled differently than expected.

---
Repository: /testbed
