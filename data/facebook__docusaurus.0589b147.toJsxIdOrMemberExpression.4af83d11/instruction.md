# Bug Report

### Describe the bug
JSX member expressions are being constructed incorrectly, resulting in reversed object/property relationships. When using namespaced JSX components (e.g., `Foo.Bar.Baz`), the member expression tree is built in the wrong order.

### Reproduction
```js
// When trying to create a JSX member expression for something like:
// <Foo.Bar.Baz />

const ids = ['Foo', 'Bar', 'Baz'];
const result = toJsxIdOrMemberExpression(ids);

// The resulting structure has object and property swapped
// Expected: Foo.Bar.Baz
// Actual: Baz.Bar.Foo (reversed)
```

### Expected behavior
The JSX member expression should be built left-to-right, with the leftmost identifier as the base object and subsequent identifiers as nested properties. For `Foo.Bar.Baz`, the structure should be:
- `Foo` is the base object
- `Bar` is a property of `Foo`
- `Baz` is a property of `Bar`

Currently, it appears the object and property are being assigned in reverse order during the construction of the member expression tree.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
