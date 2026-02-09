# Bug Report

### Describe the bug

When using CSS custom properties (CSS variables) in `:root` with multiple declarations of the same property, the wrong declarations are being removed during CSS optimization. When there are `!important` declarations mixed with normal ones, the normal declarations are kept instead of being removed. Similarly, when all declarations have the same priority, the first declaration is kept instead of the last one.

### Reproduction

```css
:root {
  --color: red;
  --color: blue;
  --color: green;
}
```

After optimization, `--color: red` is kept, but it should keep `--color: green` (the last declaration).

Also with `!important`:

```css
:root {
  --background: white;
  --background: black !important;
}
```

After optimization, `--background: black !important` is kept, but it should keep `--background: white` and remove the `!important` declaration.

### Expected behavior

According to CSS cascade rules:
- When multiple declarations of the same property exist, the **last** one should take precedence (not the first)
- When mixing `!important` and normal declarations, the **normal** declarations should be removed (not the `!important` ones)

The CSS optimizer should preserve the declarations that actually apply and remove the ones that are overridden.

### System Info
- Docusaurus version: latest
- CSS optimization is enabled with cssnano preset

---
Repository: /testbed
