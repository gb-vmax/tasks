# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where promise-based processing doesn't handle errors correctly. When an error occurs during transformation, the promise rejects with `undefined` instead of the actual error object, making it impossible to debug what went wrong.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(remarkRehype)
  .use(rehypeStringify);

// When processing fails, the error is lost
processor.process('some invalid mdx content')
  .catch(error => {
    console.log(error); // prints: undefined (should print the actual error)
  });
```

### Expected behavior

When the processor encounters an error, the promise should reject with the actual error object so I can see what went wrong and handle it appropriately.

### Additional context

This seems to affect error handling in async/await scenarios as well. The error information is completely lost which makes debugging really difficult.

---
Repository: /testbed
