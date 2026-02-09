# Bug Report

### Describe the bug

I'm experiencing an issue with markdown serialization where the output is not being generated correctly. When converting an AST tree to markdown using the toMarkdown function, the result appears to be malformed or incomplete.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello world' }
      ]
    }
  ]
};

const result = toMarkdown(tree);
console.log(result); // Expected: "Hello world\n", but getting unexpected output
```

### Expected behavior

The toMarkdown function should properly serialize the AST tree into valid markdown text. The output should be a string with the correct content.

### Additional context

This seems to have started happening recently. The markdown conversion was working fine before, but now the generated output doesn't match what's expected. It's affecting any code that relies on converting AST trees back to markdown format.

---
Repository: /testbed
