# Bug Report

### Issue with parse method - arguments passed in wrong order

I've encountered an issue where the `parse` method seems to be passing arguments to the parser in an unexpected order. When trying to parse files, the parser receives the file object and string content in the wrong positions.

### Reproduction

```js
const processor = unified()
  .use(someParser)
  
const file = vfile('# Hello')
const result = processor.parse(file)
// Parser receives arguments in wrong order
```

When the parser function is called, it appears to be receiving:
1. The file object (vfile instance) as the first argument
2. The string content as the second argument

This causes parsing to fail or produce incorrect results since parsers typically expect the string content first, followed by the file object.

### Expected behavior

The parser should receive:
1. String content as the first argument
2. File object (vfile instance) as the second argument

This matches the standard unified/vfile API where parsers process the string content with optional file metadata.

### Additional context

This seems to have broken after a recent change. The argument order matters because parsers rely on the correct positioning to access the content and file metadata properly.

---
Repository: /testbed
