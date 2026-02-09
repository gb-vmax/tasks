# Bug Report

### Describe the bug

The `stringify` method is producing incorrect output when converting AST trees to strings. It appears that the arguments are being passed to the compiler in the wrong order, causing the file information and tree data to be swapped.

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

const file = { path: 'example.md' };

// This produces unexpected output
const result = processor.stringify(tree, file);
```

### Expected behavior

The `stringify` method should correctly pass the tree and file arguments to the compiler in the proper order. The tree should be compiled with the associated file metadata, producing the expected string output.

### Additional context

This seems to affect any code using the `stringify` API directly. The compiler receives the arguments in reverse order which breaks the compilation process.

---
Repository: /testbed
