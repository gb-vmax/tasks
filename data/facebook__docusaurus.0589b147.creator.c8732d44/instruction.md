# Bug Report

### Describe the bug

I'm experiencing an issue with CSS custom property deduplication where the wrong properties are being removed. When there are multiple declarations of the same custom property without `!important`, the first declaration is kept instead of the last one, which breaks the CSS cascade behavior.

### Reproduction

Given the following CSS:

```css
:root {
  --color: red;
  --color: blue;
  --color: green;
}
```

After processing, the output keeps `red` instead of `green`. According to CSS cascade rules, the last declaration should win when there are no `!important` flags.

### Expected behavior

The CSS processor should remove earlier declarations and keep the last one:

```css
:root {
  --color: green;
}
```

Instead, it's currently keeping the first declaration and removing the later ones.

### System Info
- Package: @docusaurus/cssnano-preset
- Using the remove-overridden-custom-properties plugin

---
Repository: /testbed
