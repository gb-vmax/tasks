# Bug Report

### Describe the bug

When using theme colors with the text color resolver, the behavior seems inverted. If I pass a theme color without specifying a shade (like `"blue"`), it falls through to the regular color resolver instead of using the text variant CSS variable. However, if I specify a shade (like `"blue.5"`), it tries to use a shade-specific text variable that doesn't exist in the CSS variables system.

### Reproduction

```jsx
// This doesn't use the text variant as expected
<Text c="blue">Should use --mantine-color-blue-text</Text>

// This tries to use a non-existent variable
<Text c="blue.5">Tries to use --mantine-color-blue-5-text (doesn't exist)</Text>
```

The expected behavior is:
- `c="blue"` should resolve to `var(--mantine-color-blue-text)`
- `c="blue.5"` should fall back to the regular color resolver

But currently it seems to be doing the opposite - colors without shades don't get the text variant, while colors with shades try to use shade-specific text variables that aren't defined.

### Expected behavior

Theme colors without a shade should use the `-text` CSS variable variant (e.g., `--mantine-color-blue-text`), while colors with explicit shades should use the regular color resolver.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
