# Bug Report

### Describe the bug

I'm experiencing an issue with theme CSS generation where duplicate code is being added to the output. It looks like the `getThemeBlockCSS` function has some code that appears twice in the file, causing the CSS variables to be defined multiple times.

### Reproduction

When loading a custom plugin theme, the generated CSS contains duplicate variable definitions. This happens when the theme has background or foreground color definitions.

Steps to reproduce:
1. Create a plugin with a custom theme that includes background colors
2. Load the plugin in Insomnia
3. Inspect the generated CSS variables

You'll notice that variables like `--color-bg`, `--color-success`, etc. are being defined multiple times in the stylesheet.

### Expected behavior

Each CSS variable should only be defined once in the generated theme CSS. The `addVar`, `addComment`, and `addNewLine` helper functions should not be duplicated within the `getThemeBlockCSS` function.

### Additional context

This seems to have been introduced recently when color variation support was added (lighter/darker variations of colors). The helper functions that were already defined at the top of the function are being redefined again at the bottom, which causes parsing issues and potentially incorrect CSS output.

---
Repository: /testbed
