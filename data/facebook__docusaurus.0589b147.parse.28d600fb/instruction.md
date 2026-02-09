# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where calling `Parser.parse()` throws an error or produces incorrect results. It seems like the parser instance isn't being properly initialized or the parse method is being called on the wrong context.

### Reproduction

```js
const Parser = require('@mdx-js/mdx').Parser;

const input = `# Hello World

This is a test MDX document.`;

const options = {
  // parser options
};

// This fails or produces unexpected behavior
const result = Parser.parse(input, options);
```

### Expected behavior

The parser should successfully parse the MDX input and return the expected AST. The static `parse` method should create a new parser instance with the provided input and options, then call the parse method on that instance.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
