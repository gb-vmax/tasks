# Bug Report

### Describe the bug

I'm encountering an issue with parsing named function expressions. When I use a function expression with a name (not an anonymous function), the parser seems to crash or behave incorrectly.

### Reproduction

```js
const myFunc = function namedFunction() {
  return 'test';
};
```

When trying to parse code like this, the parser throws an error or produces unexpected results. It seems like the issue is specifically with function expressions that have an identifier/name.

### Expected behavior

Named function expressions should be parsed correctly without errors. The function name should be available in the function's scope but not in the outer scope (as per JavaScript semantics).

### Additional context

Anonymous function expressions (without a name) seem to work fine:
```js
const myFunc = function() {
  return 'test';
};
```

This only affects named function expressions. Arrow functions and regular function declarations are not impacted.

---
Repository: /testbed
