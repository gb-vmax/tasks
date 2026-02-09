# Bug Report

### Describe the bug

When processing MDX files, the processor is not handling compilation results correctly. Files that should have their `value` property set are instead getting their `result` property set, and vice versa. This causes downstream issues when trying to access the compiled output.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(remarkRehype)
  .use(rehypeStringify);

const file = await processor.process('# Hello World');

// Expected: file.value should contain the compiled string
// Actual: file.result contains the string instead
console.log(file.value); // undefined
console.log(file.result); // contains the output
```

### Expected behavior

The processor should correctly assign compilation results based on whether the result looks like a value or not. String-like results should be assigned to `file.value`, while other results should be assigned to `file.result`.

### Additional context

This seems to affect the MDX processor's handling of compiled output. The logic for determining whether to use `value` or `result` appears to be inverted from what it should be.

---
Repository: /testbed
