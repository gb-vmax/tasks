# Bug Report

### Describe the bug

I'm experiencing an issue with JSX property access in MDX files. When using member expressions with certain property names, the generated code is incorrect and causes runtime errors.

### Reproduction

```jsx
// In an MDX file
export const obj = {
  myProperty: 'value',
  'kebab-case': 'test'
}

<div>{obj.myProperty}</div>
<div>{obj['kebab-case']}</div>
```

The generated JavaScript output appears to have the computed property flags inverted - regular identifier properties are being treated as computed (bracket notation) and literal properties are being treated as non-computed (dot notation), which breaks at runtime.

### Expected behavior

- `obj.myProperty` should generate `obj.myProperty` (non-computed member expression)
- `obj['kebab-case']` should generate `obj['kebab-case']` (computed member expression)

The compiler should correctly distinguish between identifier-based property access and literal-based property access.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after a recent update. The transpiled output has the wrong syntax for accessing object properties.

---
Repository: /testbed
