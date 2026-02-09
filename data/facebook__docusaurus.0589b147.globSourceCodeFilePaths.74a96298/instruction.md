# Bug Report

### Describe the bug

After a recent update, the translation extraction process seems to be filtering directory paths before globbing instead of filtering the resulting file paths. This causes issues when trying to extract translations from source code files.

### Reproduction

When running the translation extraction with directory paths that contain patterns or special characters, the extraction fails to find translatable source files.

For example, if you have a structure like:
```
src/
  components/
    MyComponent.tsx
  pages/
    index.tsx
```

And you try to extract translations from these directories, the extractor won't properly process the files because it's now filtering the directory paths themselves rather than the globbed file results.

### Expected behavior

The translation extractor should:
1. Glob all files from the provided directory paths
2. Filter the resulting file paths to find translatable source code files
3. Extract translations from those filtered files

Instead, it appears to be filtering the input directory paths first, which prevents proper file discovery.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
