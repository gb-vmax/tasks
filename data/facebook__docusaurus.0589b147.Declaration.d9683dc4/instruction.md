# Bug Report

### Describe the bug

I'm experiencing an issue with CSS custom property (CSS variable) handling in `:root` declarations. When I have duplicate custom properties defined in `:root`, the wrong property is being removed during CSS optimization.

### Reproduction

```css
:root {
  --color-primary: red;
  --color-primary: blue;
}
```

After processing, the CSS becomes:

```css
:root {
  --color-primary: red;
}
```

### Expected behavior

The expected output should keep the **last** declaration (as per CSS cascade rules), not the first one:

```css
:root {
  --color-primary: blue;
}
```

In CSS, when you have duplicate properties, the last one should win (unless `!important` is involved). The current behavior is keeping the first declaration and removing the second one, which is backwards.

### Additional context

This is affecting our theming system where we override default CSS variables. The overrides are being removed instead of the defaults, causing the wrong colors/values to be applied.

---
Repository: /testbed
