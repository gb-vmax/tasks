# Bug Report

### Describe the bug

When trying to load site metadata, the build process crashes if the `package.json` file doesn't exist in the expected location. The error occurs because the code attempts to `require()` a file without first checking if it exists.

### Reproduction

1. Create a Docusaurus project
2. Remove or move the `package.json` file from a plugin directory
3. Run the build command
4. The build fails with a module not found error

```
Error: Cannot find module '/path/to/package.json'
```

### Expected behavior

The build should handle missing `package.json` files gracefully and return `undefined` for the version/name instead of crashing. This was working correctly before where it would check if the file exists first.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
