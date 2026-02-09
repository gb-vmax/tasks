# Bug Report

### Describe the bug

Links to local assets in MDX files are not resolving correctly. When I reference a local file (like a PDF or image) using a relative path, the link appears broken or points to the wrong location.

### Reproduction

I have the following file structure:
```
docs/
  guide/
    introduction.md
  assets/
    document.pdf
```

In `introduction.md`, I'm trying to link to the PDF:
```md
[Download PDF](../assets/document.pdf)
```

The generated link doesn't work and seems to point to an incorrect path. The asset isn't being loaded properly by webpack.

### Expected behavior

The link should correctly resolve to the asset file relative to the current document's location, and webpack should be able to require/load the asset properly.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
