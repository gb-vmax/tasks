# Bug Report

### Describe the bug

I'm encountering an issue with text directives when using attributes. It seems like the directive attributes are not being parsed correctly, causing unexpected behavior in the resulting AST.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

const input = ':directive[text]{.class #id attr=value}'
const result = processor.parse(input)

// The attributes are not being recognized properly
console.log(result)
```

When I try to use text directives with attributes (especially class and id attributes), they don't seem to be processed as expected. The parser appears to be handling the attributes incorrectly.

### Expected behavior

Text directives with attributes should be parsed correctly and the resulting AST should properly represent the class, id, and other attributes specified in the directive syntax.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
