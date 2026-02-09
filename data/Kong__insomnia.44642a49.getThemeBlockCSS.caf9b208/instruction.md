# Bug Report

### Describe the bug

I'm experiencing an issue with theme CSS generation where the code appears to be duplicated, causing the generated CSS to have redundant variable definitions. The theme block processing logic seems to be defined twice in the same function, which results in unexpected behavior when applying custom themes.

### Reproduction

When generating theme CSS with color variables, the output contains duplicate CSS variable definitions. This happens when processing theme blocks that include background, foreground, or highlight properties.

```js
// Example theme block
const themeBlock = {
  background: {
    default: '#ffffff',
    success: '#00ff00'
  },
  foreground: {
    default: '#000000'
  }
}

// The generated CSS contains duplicate variable definitions
// Expected: each variable defined once
// Actual: variables and helper functions appear to be defined multiple times
```

### Expected behavior

The theme CSS should be generated cleanly with each CSS variable defined only once. Helper functions like `addVar`, `addComment`, and `addNewLine` should not be duplicated within the same scope, and the theme block processing should happen in a single, coherent flow.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
