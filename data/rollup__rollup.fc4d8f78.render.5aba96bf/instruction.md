# Bug Report

### Describe the bug

When using JSX spread attributes with a non-preserve JSX mode, the spread syntax is not being removed correctly from the output. The opening `{...` part of the spread attribute remains in the compiled code instead of being stripped out.

### Reproduction

```jsx
const Component = <div {...props} />;
```

When compiled with JSX mode set to something other than 'preserve' (e.g., 'automatic' or 'classic'), the output incorrectly retains the opening spread syntax:

```js
// Actual output (incorrect)
const Component = <div {...props />;

// Expected output
const Component = <div props />;
```

### Expected behavior

The entire JSX spread attribute syntax (both `{...` and `}`) should be removed when transforming JSX in non-preserve mode, leaving only the argument expression.

### System Info
- Rollup version: latest
- JSX mode: automatic/classic (any non-preserve mode)

---
Repository: /testbed
