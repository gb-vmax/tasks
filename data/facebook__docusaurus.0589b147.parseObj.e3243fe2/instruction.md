# Bug Report

### Describe the bug

I'm encountering a parsing issue with object literals in MDX files. When trying to parse objects, the parser seems to get stuck in an infinite loop or fails to properly recognize the closing brace of the object.

### Reproduction

```js
const obj = {
  foo: 'bar',
  baz: 'qux'
}
```

When this code is processed through the MDX parser, it doesn't complete successfully. The parser appears to be looking for the wrong token to terminate the object parsing loop.

### Expected behavior

The parser should correctly parse object literals by:
1. Consuming the opening brace
2. Parsing properties separated by commas
3. Recognizing the closing brace to end the object

Instead, it seems like the parser is checking for the wrong token type when determining whether to continue parsing object properties.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: latest

---
Repository: /testbed
