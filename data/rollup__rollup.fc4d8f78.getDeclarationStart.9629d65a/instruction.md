# Bug Report

### Describe the bug

I'm experiencing an issue with export default declarations in my code. It seems like the parser is not correctly identifying the start position of the declaration after the `default` keyword.

### Reproduction

When I have an export default statement like this:

```js
export default function myFunction() {
  return 'hello';
}
```

Or with classes:

```js
export default class MyClass {
  constructor() {
    this.value = 42;
  }
}
```

The bundler seems to be parsing the declaration incorrectly. The position where it thinks the declaration starts appears to be off by one character.

### Expected behavior

The parser should correctly identify where the actual declaration starts after the `default` keyword (accounting for any whitespace). This affects code generation and source maps.

### Additional context

This seems to affect any code using `export default` syntax. The issue manifests when the bundler processes these exports - the generated output or source mappings may be incorrect.

---
Repository: /testbed
