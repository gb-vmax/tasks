# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it's not correctly handling the input file content. When I try to parse markdown content, the parser seems to be receiving the wrong type of data instead of the string representation of the file.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkStringify);

const file = vfile('# Hello World\n\nThis is a test.');
const tree = processor.parse(file);
// Parser receives vfile object instead of string content
```

### Expected behavior

The parser should receive the string content of the file (e.g., `'# Hello World\n\nThis is a test.'`) so it can properly tokenize and parse the markdown. Instead, it appears to be getting the vfile object directly, which causes parsing to fail or produce incorrect results.

### Additional context

This seems to have started happening recently. The parser is expecting string input but is receiving a different type, which breaks the markdown parsing functionality. The issue affects any code that uses the `parse()` method with vfile objects.

---
Repository: /testbed
