# Bug Report

### Describe the bug

Images with `@site/` prefix are not being resolved correctly. When using `@site/` aliased paths in markdown image references, the image path resolution appears to be broken and returns incorrect file paths.

### Reproduction

```markdown
![My Image](@site/static/img/example.png)
```

When processing markdown files with `@site/` aliased image paths, the resolved path doesn't point to the actual image file location. The path seems to be getting mangled during the resolution process.

### Expected behavior

Images referenced with `@site/` should resolve to the correct absolute file path and be processed properly. The `@site/` alias should be replaced with the actual site directory path and the resulting path should point to the existing image file.

### Additional context

This seems to affect both `@site/` prefixed paths and relative image paths. The image resolution logic appears to be returning the wrong file path in certain cases, which likely causes downstream processing issues.

---
Repository: /testbed
