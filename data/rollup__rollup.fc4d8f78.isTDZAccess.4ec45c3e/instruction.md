# Bug Report

### Describe the bug

I'm experiencing an issue with temporal dead zone (TDZ) detection for variables. When accessing variables before their declaration in certain block scopes, the TDZ error is not being triggered correctly. It seems like the logic for determining whether an identifier is in the TDZ is inverted.

### Reproduction

```js
// This should throw a ReferenceError but doesn't
{
  console.log(x); // Should error: Cannot access 'x' before initialization
  let x = 5;
}

// Similarly with const
{
  const y = z; // Should error: Cannot access 'z' before initialization
  const z = 10;
}
```

### Expected behavior

Accessing variables before their declaration in the same block scope should throw a ReferenceError due to the temporal dead zone. The bundler should detect these cases and either throw an error during build time or preserve the runtime error behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The TDZ checks were working correctly before.

---
Repository: /testbed
