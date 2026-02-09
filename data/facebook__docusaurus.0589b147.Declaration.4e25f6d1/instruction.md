# Bug Report

### Describe the bug

CSS custom properties (CSS variables) defined in `:root` are not being deduplicated correctly. When multiple declarations of the same custom property exist, the wrong ones are being removed, causing styles to break.

### Reproduction

```css
:root {
  --primary-color: blue;
  --primary-color: red;
  --secondary-color: green;
}
```

After processing with the cssnano preset, the expected behavior would be to keep only the last `--primary-color: red` declaration (or the `!important` one if present), but instead the wrong declarations are being kept/removed.

### Expected behavior

When there are duplicate custom property declarations in `:root`:
- The last declaration should be kept (unless there's an `!important` declaration)
- If any declaration has `!important`, only those with `!important` should be kept
- Earlier declarations should be removed as they are overridden

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues with our theming system where we override CSS variables in different files, and the final bundled CSS has the wrong values applied.

---
Repository: /testbed
