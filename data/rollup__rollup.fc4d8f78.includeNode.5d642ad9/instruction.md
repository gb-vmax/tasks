# Bug Report

### Describe the bug

I'm encountering an issue with the `in` operator when used with string literals in binary expressions. It seems like the tree-shaking/inclusion logic isn't working correctly for properties being checked.

### Reproduction

```js
const obj = {
  foo: 1,
  bar: 2
};

// This should work but the property access isn't being included properly
if ('foo' in obj) {
  console.log(obj.foo);
}
```

When bundling code that uses the `in` operator with string literals (checking if a property exists in an object), the left-hand side of the expression doesn't seem to be getting included in the dependency graph correctly. This can lead to incorrect tree-shaking behavior where necessary code paths are removed.

### Expected behavior

When using `'propertyName' in object`, the bundler should properly track the property name being checked and include the necessary code paths in the final bundle.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
