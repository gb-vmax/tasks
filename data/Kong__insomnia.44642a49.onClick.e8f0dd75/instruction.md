# Bug Report

### Describe the bug

I'm experiencing a syntax error in the `async-button.tsx` component after a recent update. The application fails to compile and I'm getting errors about unexpected tokens in the AsyncButton component file.

### Reproduction

The issue occurs when trying to use the AsyncButton component in any part of the application. The compilation fails before the app can even start.

Steps to reproduce:
1. Import AsyncButton component in any file
2. Try to compile/build the application
3. Build fails with syntax errors

### Expected behavior

The AsyncButton component should compile successfully and the application should build without errors. The component should be usable as before.

### System Info
- Insomnia version: latest
- Node version: 18.x
- OS: macOS

The build was working fine before the recent changes to the async-button component. It seems like there might be an issue with the TypeScript/JSX syntax in the component file itself.

---
Repository: /testbed
