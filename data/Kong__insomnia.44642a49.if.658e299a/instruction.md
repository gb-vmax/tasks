# Bug Report

### Describe the bug

After a recent update, the themed button component is not rendering correctly. The font color seems to be broken - buttons are displaying with incorrect text colors or the text is not visible at all.

### Reproduction

```tsx
import { Button } from './themed-button/button';

// Button with default theme
<Button theme="default">Click me</Button>

// Button with custom theme
<Button theme="primary">Submit</Button>
```

When rendering buttons with different themes, the font color is not being applied properly. The text appears to be using the wrong color variable or is completely invisible against the button background.

### Expected behavior

Buttons should display text with the appropriate font color based on the theme prop. The `getFontColorVar` function should return the correct CSS variable for the font color corresponding to the button's theme.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
