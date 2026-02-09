# Bug Report

### Describe the bug

I'm experiencing a syntax error in the theme CSS generation code. After a recent update, the application fails to start and throws a parsing error related to the plugin theme system.

### Reproduction

The error occurs when the theme CSS is being generated during application initialization. It seems like there's an issue with the code structure in the theme block CSS generation function.

Steps to reproduce:
1. Start the application with any plugin theme enabled
2. The app fails to load with a syntax error
3. Console shows parsing errors related to theme generation

### Expected behavior

The application should start normally and generate theme CSS without errors. Theme variables should be properly created for both light and dark mode variants, including contrast ratios.

### System Info

- Insomnia version: latest
- OS: Any
- Node version: 18.x

### Additional context

This appears to have been introduced in a recent commit that added dark mode variant generation and contrast ratio calculations to the theme system. The code seems to be incomplete or malformed, causing the parser to fail.

---
Repository: /testbed
