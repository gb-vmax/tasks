# Bug Report

### Describe the bug

When bundling code with object expressions that have trailing commas, the output is malformed. The closing brace `}` of the object is being removed from the generated code, resulting in invalid JavaScript syntax.

### Reproduction

```js
// Input code
const obj = {
  foo: 1,
  bar: 2,
};

export { obj };
```

After bundling, the output becomes:

```js
const obj = {
  foo: 1,
  bar: 2,
// Missing closing brace here!

export { obj };
```

This happens specifically when:
1. The object has multiple properties
2. There's a trailing comma after the last property
3. Tree-shaking is enabled

### Expected behavior

The bundled output should maintain valid JavaScript syntax with the closing brace intact:

```js
const obj = {
  foo: 1,
  bar: 2,
};

export { obj };
```

### Additional context

This appears to be a regression as this was working correctly in previous versions. The issue only manifests when object expressions are used in certain contexts where they need to be wrapped in parentheses (like expression statements or arrow functions).

---
Repository: /testbed
