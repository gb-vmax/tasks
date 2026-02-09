# Bug Report

### Describe the bug

I'm experiencing an issue with JSX identifier renaming in bundled output. When using variable renaming (e.g., through minification or scope hoisting), JSX identifiers that should be renamed are not being updated in the output code, while identifiers that should remain unchanged are being overwritten.

### Reproduction

```jsx
import { Component } from 'library';

function MyComponent() {
  return <Component />;
}
```

When bundling with variable renaming enabled, the imported `Component` identifier should be renamed in the JSX if the variable itself gets renamed (e.g., to `Component$1`). However, the JSX tag still references the original name, causing runtime errors.

Similarly, for native elements:

```jsx
function NativeExample() {
  return <div className="test" />;
}
```

When JSX mode is set to something other than 'preserve', native element names like `div` should be converted to string literals, but they're being left as-is.

### Expected behavior

- JSX identifiers should be renamed when the corresponding variable is renamed
- Native HTML elements should be stringified when JSX mode is not 'preserve'
- Identifiers that don't need renaming should remain untouched

### System Info
- Rollup version: latest
- JSX mode: automatic/classic

---
Repository: /testbed
