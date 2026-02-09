# Bug Report

### Describe the bug

I'm experiencing an issue with CSS custom property optimization where duplicate custom property declarations are not being removed correctly. It seems like the wrong properties are being kept/removed when there are multiple declarations of the same custom property in a CSS rule.

### Reproduction

```css
.example {
  --color: red;
  --color: blue;
  --color: green;
}
```

After running the CSS optimization, I would expect only the last declaration (`--color: green;`) to be kept since it overrides the previous ones. However, the behavior seems incorrect - either the wrong declarations are being removed or none are being removed at all.

Similarly, when using `!important`:

```css
.example {
  --color: red;
  --color: blue !important;
  --color: green;
}
```

The important declaration should take precedence, but the optimization doesn't seem to handle this case properly either.

### Expected behavior

- When multiple declarations of the same custom property exist, only the last one should be kept (unless `!important` is involved)
- When `!important` is present, non-important declarations should be removed regardless of order
- The final CSS should have no duplicate custom property declarations

### System Info

- Using the docusaurus-cssnano-preset package
- This appears to affect the remove-overridden-custom-properties plugin specifically

---
Repository: /testbed
