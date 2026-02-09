# Bug Report

### Describe the bug

After a recent update, I'm seeing incorrect output when bundling code that contains `undefined` and boolean literals. The generated code is using the wrong representation for these values.

### Reproduction

When I have source code like this:

```js
const x = undefined;
const y = true;
const z = false;
```

The bundled output is generating:

```js
const x = undefined;
const y = true;
const z = false;
```

But I expected it to output the more compatible forms like `void 0` for undefined and string representations for booleans.

### Expected behavior

- `undefined` should be rendered as `void 0` (safer for minification and avoids issues with `undefined` being redefinable in older environments)
- Booleans should be rendered as their string representations for consistency

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with our build pipeline where we rely on the previous behavior for compatibility with older JavaScript environments.

---
Repository: /testbed
