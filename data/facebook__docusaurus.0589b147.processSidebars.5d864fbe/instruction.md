# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category metadata in my Docusaurus site. When I have multiple `_category_.json` files in different directories, only the first one seems to be processed correctly. The other category metadata files are being ignored, which causes the sidebar to not display the correct category labels, descriptions, or positions for most of my documentation sections.

### Reproduction

1. Create a docs structure with multiple folders, each containing a `_category_.json` file:
```
docs/
  ├── guide/
  │   ├── _category_.json (label: "Guide", position: 1)
  │   └── intro.md
  ├── api/
  │   ├── _category_.json (label: "API Reference", position: 2)
  │   └── overview.md
  └── tutorials/
      ├── _category_.json (label: "Tutorials", position: 3)
      └── getting-started.md
```

2. Build or run the dev server
3. Check the generated sidebar

### Expected behavior

All category metadata files should be processed and applied to their respective sidebar categories. Each folder should display with its configured label, position, and other metadata.

### Actual behavior

Only the first category metadata file is being used. The other categories either show default labels or are missing their custom metadata entirely.

This seems like a regression - it was working fine before but broke recently.

---
Repository: /testbed
