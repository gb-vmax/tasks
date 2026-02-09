# Bug Report

### Describe the bug

Theme color variables are not being generated correctly. When loading a custom plugin theme, the CSS variables for colors (including RGB variants) are missing from the generated stylesheet. This causes themes to not apply properly and fall back to default colors.

### Reproduction

```js
const pluginTheme = {
  name: 'My Theme',
  theme: {
    background: {
      default: '#282c34',
      success: '#98c379'
    }
  }
};

const css = generateThemeCSS(pluginTheme);
// CSS variables like --color-bg and --color-bg-rgb are not present
```

### Expected behavior

The generated CSS should include color variables in both regular and RGB format:
```css
--color-bg: rgb(40, 44, 52);
--color-bg-rgb: 40, 44, 52;
```

These variables should be properly parsed from the theme configuration and added to the stylesheet.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
