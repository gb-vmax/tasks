# Bug Report

### Describe the bug

The `stringify()` method appears to be passing arguments to the compiler in the wrong order. When I try to stringify a markdown AST, I'm getting unexpected errors or the output is not what I expect.

### Reproduction

```js
const processor = remark();
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

const file = { path: 'example.md' };
const result = processor.stringify(tree, file);
// Getting unexpected behavior here
```

### Expected behavior

The stringify method should correctly convert the AST back to markdown format. The compiler should receive the tree as the first argument and the file as the second argument, as documented.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
