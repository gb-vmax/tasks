# Bug Report

### Describe the bug

CSS custom properties are being removed incorrectly when there are multiple declarations of the same property. The plugin is keeping the wrong declarations and removing the ones that should actually be applied.

### Reproduction

```css
:root {
  --color: red;
  --color: blue;
  --color: green;
}
```

After processing with the cssnano preset, the wrong custom property declaration is being kept. Instead of keeping the last declaration (which should take precedence according to CSS cascade rules), an earlier declaration is being retained.

### Expected behavior

According to CSS specificity rules, when there are multiple declarations of the same property without `!important`, the **last** declaration should be kept and earlier ones should be removed as they are overridden.

So the example above should result in:
```css
:root {
  --color: green;
}
```

But currently it seems like the first declaration is being kept instead.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
