# Bug Report

### Describe the bug

I'm encountering a problem with theme CSS generation where duplicate code is being added to the output. It looks like the function is generating CSS variables twice, which is causing bloated stylesheets and potentially conflicting variable definitions.

### Reproduction

When generating theme CSS with color blocks (background, foreground, highlight), the output contains duplicate CSS variable definitions. The variables are being processed and added multiple times in the same CSS output.

Example of what's happening:
```js
// Theme block with colors
const themeBlock = {
  background: {
    default: '#ffffff',
    success: '#00ff00'
  },
  foreground: {
    default: '#000000'
  }
}

// Generated CSS contains duplicate variable definitions
// --color-bg appears twice
// --color-font appears twice
// etc.
```

### Expected behavior

Each CSS variable should only be defined once in the generated theme CSS. The function should produce clean, non-redundant CSS output.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
