# Bug Report

### Describe the bug

I'm experiencing an issue with JSX parsing where namespace handling seems to be inverted. When I don't pass any options (or pass an empty object), namespaces are being disallowed when they should be allowed by default.

### Reproduction

```js
// This should allow namespaces by default
const parser = acornJsx();

// Trying to parse JSX with namespaces
const code = `<svg:circle />`;
parser.parse(code);
// Error: Namespaces are not allowed
```

Also, when I explicitly try to disable namespaces:

```js
const parser = acornJsx({ allowNamespaces: false });
// Namespaces are actually allowed instead of being disabled
```

### Expected behavior

- When no options are passed, `allowNamespaces` should default to `true` (namespaces allowed)
- When `allowNamespaces: false` is explicitly set, namespaces should be disallowed
- The options object should be properly initialized when not provided

### System Info
- acorn-jsx version: 3.0.0
- Node version: 18.x

This seems like it might be a regression as it was working correctly in previous versions. The behavior is completely opposite of what's documented.

---
Repository: /testbed
