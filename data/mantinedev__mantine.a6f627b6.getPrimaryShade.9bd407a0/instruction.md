# Bug Report

### Describe the bug

When using `getPrimaryShade` with the theme's color scheme, the function returns the wrong shade value. It appears that light and dark shades are being swapped - when the color scheme is set to 'dark', I'm getting the light shade value instead, and vice versa.

### Reproduction

```js
const theme = {
  primaryShade: {
    light: 6,
    dark: 8
  }
}

// Returns 6 instead of 8
const darkShade = getPrimaryShade(theme, 'dark')

// Returns 8 instead of 6  
const lightShade = getPrimaryShade(theme, 'light')
```

### Expected behavior

When `colorScheme` is 'dark', the function should return `theme.primaryShade.dark`.
When `colorScheme` is 'light', the function should return `theme.primaryShade.light`.

Currently it's doing the opposite - returning light shade for dark mode and dark shade for light mode.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
