# Bug Report

### Describe the bug

I'm seeing incorrect logging behavior in the translation extraction system. When processing translation files, the warning messages are displaying the wrong information - instead of showing the individual source file path, it's showing the entire array of all source code file translations.

### Reproduction

When extracting translations from source code files and warnings are generated, the log output shows something like:

```
Translation extraction warnings for file path=[object Array]: [warning messages]
```

Instead of the expected:

```
Translation extraction warnings for file path=src/components/MyComponent.tsx: [warning messages]
```

This makes it very difficult to identify which specific file has translation extraction issues, especially when processing multiple files.

### Expected behavior

The warning log should display the individual source file path that has the translation warnings, not the entire array of all files being processed.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
