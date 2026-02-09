# Bug Report

### Describe the bug

I'm experiencing an issue with theme translations where the package path resolution seems to be broken. When trying to use translated theme components, I'm getting errors that the translation files or theme components cannot be found.

### Reproduction

The issue appears when the translation system tries to resolve the path to theme packages. It seems like the path calculation is incorrect and points to the wrong directory.

Steps to reproduce:
1. Set up a Docusaurus project with theme translations
2. Try to load translations from a theme package
3. The system fails to locate the correct package directory

I noticed this started happening recently and it's preventing the translation system from working properly. The paths being generated don't seem to match the actual package structure.

### Expected behavior

The translation utilities should correctly resolve the path to theme packages and their source directories, allowing translations to be loaded without errors.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
