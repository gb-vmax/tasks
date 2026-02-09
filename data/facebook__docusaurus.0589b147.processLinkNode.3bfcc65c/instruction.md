# Bug Report

### Describe the bug

Links with protocol schemes (like `pathname://`) are being processed as local assets when they shouldn't be. This causes the MDX loader to attempt to resolve them as file paths, which fails or produces unexpected behavior.

### Reproduction

```md
[Custom Protocol Link](myapp://open/document)
[Another Protocol](vscode://file/path/to/file)
```

When these links are used in MDX files, they get incorrectly processed as local file paths instead of being left as-is for the Link component to handle.

### Expected behavior

Links with custom protocol schemes should be passed through without modification. The MDX loader should only process actual local file references and assets, not protocol-based URLs.

### Additional context

This affects any custom protocol handlers (like deep links for mobile apps, VS Code extensions, etc.) that need to be preserved in the final output.

---
Repository: /testbed
