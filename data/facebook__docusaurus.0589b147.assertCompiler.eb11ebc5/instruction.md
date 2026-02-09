# Bug Report

### Describe the bug

I'm encountering an error when trying to use the compiler functionality. The system is throwing a `TypeError` saying it cannot process with a `compiler`, even though I've correctly provided a compiler function.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkStringify)

// This throws an error: "Cannot `stringify` with `compiler`"
const result = processor.processSync('# Hello')
```

The error message doesn't make sense - it's complaining about having a compiler when a compiler is actually required for the operation to work.

### Expected behavior

The processor should accept and use the compiler function without throwing an error. The operation should complete successfully and return the processed result.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
