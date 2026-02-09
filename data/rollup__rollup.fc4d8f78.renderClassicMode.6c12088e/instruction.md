# Bug Report

### Describe the bug

JSX Fragments are not being rendered correctly in classic mode. When using fragment syntax (`<>...</>`), the output includes an extra property access that shouldn't be there, causing runtime errors.

### Reproduction

```jsx
// Input JSX
function Component() {
  return (
    <>
      <div>Hello</div>
      <div>World</div>
    </>
  );
}
```

When compiled with `jsxFactory` set to `React.createElement` in classic mode, the fragment is transformed incorrectly. The factory function call includes the factory name twice in the property chain.

### Expected behavior

The fragment should be compiled to a valid `React.createElement` call with the proper factory reference, not duplicating parts of the factory path.

For example, with factory `React.createElement`, it should generate something like:
```js
React.createElement(React.Fragment, null, ...)
```

But instead it's generating an invalid property access pattern.

### Additional context

This appears to affect JSX fragment compilation specifically when using classic JSX runtime mode with a dotted factory name (e.g., `React.createElement`).

---
Repository: /testbed
