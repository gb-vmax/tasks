# Bug Report

### Describe the bug

CSS custom properties with `!important` declarations are being removed incorrectly in `:root` selectors. When multiple declarations of the same custom property exist, the plugin is keeping the wrong ones based on the `!important` flag.

### Reproduction

```css
:root {
  --color-primary: blue;
  --color-primary: red !important;
}
```

After processing, the `!important` declaration is being removed when it should be kept, or vice versa. The logic for determining which properties to keep/remove seems inverted.

Also seeing issues when there are multiple declarations without `!important`:

```css
:root {
  --spacing: 10px;
  --spacing: 20px;
  --spacing: 30px;
}
```

The wrong declaration is being preserved - it's keeping the first one instead of the last one.

### Expected behavior

- When `!important` declarations exist, non-important ones should be removed
- When no `!important` declarations exist, all but the last declaration should be removed (following CSS cascade rules)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
