# Bug Report

### Describe the bug

After a recent update, the docs plugin is not displaying any documentation pages in the version data. All docs are being filtered out and not appearing in the global data structure, which causes the entire documentation section to be empty.

### Reproduction

1. Set up a Docusaurus site with the docs plugin
2. Add some documentation files to your docs folder
3. Build the site or start the dev server
4. Check the global data for the version - the `docs` array will be empty even though documentation files exist

Example setup:
```
docs/
  intro.md
  guide.md
  api.md
```

Expected: All three docs should appear in the version's global data
Actual: The `docs` array is empty

### Expected behavior

The `docs` array in the global version data should contain all the documentation pages that were processed, not be empty. The documentation should be visible and accessible in the built site.

### Additional context

This seems to affect all versions of the documentation. The sidebar still renders but clicking on any doc link leads to a 404 since the docs aren't being included in the global data.

---
Repository: /testbed
