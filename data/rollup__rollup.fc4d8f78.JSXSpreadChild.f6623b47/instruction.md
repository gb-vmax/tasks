# Bug Report

### Describe the bug

When using JSX spread children with `jsx.mode: 'preserve'`, the spread operator (`...`) is appearing in the wrong position in the rendered output. Instead of preserving the original JSX syntax `{...children}`, it's being transformed incorrectly.

### Reproduction

```jsx
// Input JSX
<Component>
  {...items}
</Component>

// With jsx.mode: 'preserve'
// Expected output: {...items}
// Actual output: {items...}
```

The spread operator is being moved to after the expression instead of before it when preserve mode is enabled.

### Expected behavior

When `jsx.mode` is set to `'preserve'`, JSX spread children should maintain their original syntax with the spread operator before the expression: `{...expression}`, not after it.

### Configuration

```js
{
  jsx: {
    mode: 'preserve'
  }
}
```

---
Repository: /testbed
