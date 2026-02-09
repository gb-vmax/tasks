# Bug Report

### Describe the bug

I'm experiencing an issue with chunk name generation in Docusaurus where chunk names are getting suffixed with numbers unexpectedly. All generated chunk names now have a suffix appended (like `1`, `2`, etc.) even when there are no naming conflicts.

### Reproduction

When building a Docusaurus site, the generated chunk names include unnecessary numeric suffixes:

```
Expected: myComponent
Actual: myComponent1

Expected: aboutPage  
Actual: aboutPage1
```

This happens for all chunks, not just ones with duplicate names. The suffix appears to be added to every single chunk name during the build process.

### Expected behavior

Chunk names should only get numeric suffixes when there's an actual naming collision. The first occurrence of a unique chunk name should not have any suffix appended.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Build environment: production

---
Repository: /testbed
