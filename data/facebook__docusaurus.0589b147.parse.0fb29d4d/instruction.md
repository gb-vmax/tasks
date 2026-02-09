# Bug Report

### Describe the bug

The `parse()` method is passing arguments to the parser in the wrong order. After a recent change, the parser is receiving the file object first and the string content second, but it should be the other way around.

### Reproduction

```js
const processor = unified()
  .use(someParser)
  
const file = vfile('# Hello world')
const result = processor.parse(file)
// Parser receives arguments in wrong order
```

When calling `parse()` with a file, the parser function is invoked with arguments in an incorrect sequence. The string content should be passed as the first argument and the file object as the second argument, but currently they're reversed.

### Expected behavior

The parser should receive the string content as the first parameter and the file object as the second parameter, consistent with the expected parser signature.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
