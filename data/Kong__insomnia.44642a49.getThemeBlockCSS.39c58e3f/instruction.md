# Bug Report

### Describe the bug

I'm experiencing an issue with theme generation where color variant CSS variables are not being created correctly. When a theme defines colors, the system should automatically generate lighter and darker variants (e.g., `-lighter-10`, `-darker-20`), but these variants are missing from the generated CSS.

### Reproduction

```js
const theme = {
  background: {
    default: '#ffffff',
    success: '#00ff00'
  },
  foreground: {
    default: '#000000'
  }
};

// After generating theme CSS, expected variants are missing:
// --color-bg-lighter-10
// --color-bg-darker-10
// --color-success-lighter-20
// etc.
```

### Expected behavior

When theme colors are processed, the system should automatically generate color variants with suffixes like `-lighter-10`, `-lighter-20`, `-darker-10`, and `-darker-20` for each defined color. These variant CSS variables should be available for use in the UI.

For example, if `--color-bg` is set to `#ffffff`, the following should also be generated:
- `--color-bg-lighter-10`
- `--color-bg-lighter-20`
- `--color-bg-darker-10`
- `--color-bg-darker-20`

The variants should adjust based on whether the base color is light or dark.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
