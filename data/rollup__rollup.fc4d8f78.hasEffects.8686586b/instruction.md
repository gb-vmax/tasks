# Bug Report

### Describe the bug

Tagged template expressions are not being evaluated correctly for side effects. When a tagged template contains expressions with side effects, the bundler is not properly detecting them, leading to incorrect tree-shaking behavior.

### Reproduction

```js
let counter = 0;

function tag(strings, ...values) {
  return strings[0] + values[0];
}

const result = tag`Value: ${++counter}`;
console.log(counter); // Should be 1
```

When bundling code that uses tagged templates with expressions that have side effects (like `++counter` or function calls), the side effects are not being properly tracked. This can cause the bundler to incorrectly remove code that should be kept.

### Expected behavior

The bundler should correctly identify that the expressions inside the template literal have side effects and preserve them during tree-shaking. All side effects in tagged template expressions should be detected and the code should be retained when necessary.

### Additional context

This appears to affect tagged templates specifically - regular template literals work as expected. The issue manifests when the tag function has side effects AND the template expressions also have side effects.

---
Repository: /testbed
