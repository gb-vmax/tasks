# Bug Report

### Describe the bug

I'm experiencing an issue where variable declarations and references are not being tracked correctly in scope analysis. It seems like the data structures for storing declarations and references got swapped somehow.

### Reproduction

When trying to work with scopes, I'm seeing unexpected behavior:

1. Trying to add a declaration to the scope
2. The declaration gets stored but can't be retrieved properly
3. Similarly, references are not being tracked as expected

For example, when analyzing code like:

```js
const x = 1;
function foo() {
  return x;
}
```

The scope should track `x` as a declaration in the outer scope and as a reference in the function scope, but the lookup operations are failing because the internal storage seems to be using the wrong data structure type.

### Expected behavior

- Declarations should be stored and retrievable by name (key-value pairs)
- References should be stored as a collection of identifiers
- Scope analysis should correctly identify which variables are declared vs referenced

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
