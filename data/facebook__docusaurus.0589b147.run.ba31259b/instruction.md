# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where the `run()` method doesn't properly handle the output tree from transformers. When transformers return a modified tree, the resulting tree appears to be incorrect or undefined in certain cases.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  // ... other plugins

const tree = processor.parse('# Hello\n\nSome content')

processor.run(tree, (err, resultingTree) => {
  // resultingTree is not what's expected
  console.log(resultingTree)
})
```

### Expected behavior

When transformers modify the tree, the `run()` method should return the transformed tree (outputTree) if it exists, otherwise fall back to the original tree. The resulting tree should always be a valid tree object.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The processor runs without errors but the output tree structure is not correct.

---
Repository: /testbed
