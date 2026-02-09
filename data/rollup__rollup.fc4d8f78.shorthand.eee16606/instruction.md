# Bug Report

### Describe the bug

I'm encountering an issue with object shorthand property notation. When using shorthand properties in object literals, they are not being recognized correctly and the parser seems to be treating them as regular properties instead.

### Reproduction

```js
const name = 'John';
const age = 30;

// Using shorthand property syntax
const person = {
  name,
  age
};

// The properties should be recognized as shorthand
// but they're being treated as if they were written as:
// { name: name, age: age }
```

When I check the AST or try to process code with shorthand properties, the `shorthand` flag appears to always be `false` even when the property is clearly using shorthand syntax.

### Expected behavior

Object properties using shorthand notation should be correctly identified with the `shorthand` flag set to `true`. The parser should distinguish between `{ name }` and `{ name: name }`.

### Additional context

This seems to affect any code that relies on detecting shorthand properties, making it impossible to properly handle or transform ES6 shorthand syntax.

---
Repository: /testbed
