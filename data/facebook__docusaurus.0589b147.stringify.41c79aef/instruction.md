# Bug Report

### Describe the bug

I'm experiencing an issue with the `stringify()` method where it seems to be passing arguments to the compiler in the wrong order. The compiler is receiving the file object as the first argument and the tree as the second argument, but based on the expected behavior, it should be the other way around.

### Reproduction

```js
const processor = unified()
  .use(somePlugin)
  .use(remarkStringify);

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'Hello world' }]
    }
  ]
};

const result = processor.stringify(tree);
// Compiler receives arguments in wrong order
```

### Expected behavior

The compiler should receive the tree as the first argument and the file as the second argument. Currently it appears to be reversed, which causes the compiler to process the wrong data structure.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
