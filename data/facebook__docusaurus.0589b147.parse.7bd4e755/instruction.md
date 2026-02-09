# Bug Report

### Describe the bug

After a recent update, the MDX parser is throwing errors when trying to parse input. It seems like the static `parse` method is not working correctly anymore - getting errors about `this.parse()` not being a function or the parser not being properly initialized.

### Reproduction

```js
const { Parser } = require('@mdx-js/mdx');

const input = '# Hello World';
const options = { /* ... */ };

// This throws an error
const result = Parser.parse(input, options);
```

### Expected behavior

The parser should successfully parse the MDX input and return the parsed result without errors. The static `parse` method should create a new parser instance and return the parsed output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
