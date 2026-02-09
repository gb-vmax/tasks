# Bug Report

### Describe the bug

When using CSS custom properties (CSS variables) in `:root` with duplicate declarations, the wrong properties are being removed. Specifically, when there are multiple declarations of the same custom property, the first declaration is being kept instead of the last one, which goes against the CSS cascade rules.

### Reproduction

```css
:root {
  --primary-color: red;
  --primary-color: blue;
  --primary-color: green;
}
```

After processing, the output keeps `red` instead of `green`. According to CSS cascade rules, the last declaration should win and earlier ones should be removed.

### Expected behavior

The CSS output should keep only the last declaration of duplicate custom properties:

```css
:root {
  --primary-color: green;
}
```

The earlier declarations (`red` and `blue`) should be removed as they are overridden by the final `green` value.

### Additional context

This affects the CSS optimization process and can lead to incorrect styles being applied when custom properties are redefined multiple times in the `:root` selector.

---
Repository: /testbed
