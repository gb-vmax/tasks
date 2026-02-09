# Bug Report

### Describe the bug

I'm experiencing an issue with theme generation where the CSS output appears to be incomplete or corrupted. When applying custom themes, some color variables are missing or cut off, causing the theme styling to break partially.

### Reproduction

Steps to reproduce:
1. Configure a custom theme with foreground colors (success, notice, warning, danger, surprise, info)
2. Apply the theme to the application
3. Inspect the generated CSS variables

The theme CSS generation seems to stop abruptly and some foreground color variables are not properly generated. Specifically, the info foreground color variable appears to be incomplete.

### Expected behavior

All theme color variables should be properly generated with their complete values, including:
- Base color values (RGB, HSL formats)
- Color variants (lighter/darker)
- All foreground and background colors

The generated CSS should be complete and valid.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
