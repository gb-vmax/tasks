# Bug Report

### Describe the bug

CSS custom properties (CSS variables) are being removed incorrectly when multiple properties are defined in `:root`. The plugin seems to be removing the wrong properties instead of the overridden ones.

### Reproduction

```css
:root {
  --primary-color: red;
  --primary-color: blue;
  --secondary-color: green;
}
```

After processing, the wrong properties get removed. Expected behavior is that the first `--primary-color: red` should be removed (as it's overridden by the second declaration), but instead other properties are being affected.

### Expected behavior

When there are duplicate CSS custom properties in `:root`, only the earlier declarations should be removed, keeping the last one. Properties with `!important` should take precedence over non-important ones.

For example:
```css
:root {
  --color: red;
  --color: blue;
}
```
Should become:
```css
:root {
  --color: blue;
}
```

### Additional context

This appears to be affecting the cssnano preset for Docusaurus. The custom properties removal logic doesn't seem to be identifying duplicate properties correctly.

---
Repository: /testbed
