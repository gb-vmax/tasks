# Bug Report

### Describe the bug

CSS custom properties are being incorrectly removed during optimization. When multiple declarations of the same custom property exist, the wrong ones are being kept/removed, resulting in incorrect final CSS output.

### Reproduction

```css
:root {
  --my-color: red;
  --my-color: blue;
  --my-color: green;
}
```

After running through the CSS optimization, the final value that gets kept is not the expected one. The last declaration should win according to CSS cascade rules, but instead an earlier declaration is being preserved.

### Expected behavior

When there are multiple declarations of the same CSS custom property without `!important`, the **last** declaration should be kept and all previous ones should be removed (following standard CSS cascade behavior).

For example:
```css
:root {
  --my-color: red;   /* should be removed */
  --my-color: blue;  /* should be removed */
  --my-color: green; /* should be kept */
}
```

Should result in:
```css
:root {
  --my-color: green;
}
```

### Additional context

This appears to be affecting the `remove-overridden-custom-properties` optimization in the cssnano preset. The cascade order is not being respected correctly when determining which properties to remove.

---
Repository: /testbed
