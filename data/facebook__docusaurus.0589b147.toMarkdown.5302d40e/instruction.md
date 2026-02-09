# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown serialization where the output is getting extra newlines appended incorrectly. It seems like the logic for determining when to add a trailing newline is inverted.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'Hello world' }]
    }
  ]
};

const result = toMarkdown(tree);
// Result has double newlines when it shouldn't
```

When converting markdown AST to string, documents that already end with a newline are getting an additional newline appended, while documents that don't end with a newline are not getting one added.

### Expected behavior

- Documents ending with a newline should not get an extra newline
- Documents not ending with a newline should get one added
- The final output should consistently have exactly one trailing newline

### Additional context

This appears to be affecting the formatting of generated markdown files. Also noticing some strange behavior with nested structures where the state stack isn't being managed correctly - elements seem to be removed in the wrong order (FIFO instead of LIFO).

---
Repository: /testbed
