# Bug Report

### Describe the bug

I'm getting an error when trying to build my Docusaurus site with the docs plugin, even though I have documentation files in my versioned docs folder. The error message says my docs version "has no docs" but the files are definitely there.

### Reproduction

1. Create a Docusaurus site with versioned docs
2. Add documentation files to the version folder (e.g., `versioned_docs/version-1.0.0/`)
3. Try to build the site

The build fails with an error like:
```
Docs version "1.0.0" has no docs! At least one doc should exist at "versioned_docs/version-1.0.0"
```

But when I check the folder, my markdown files are present.

### Expected behavior

The build should succeed when documentation files exist in the versioned docs folder. The plugin should only throw an error when the folder is actually empty.

### Additional context

This seems to have started happening recently. The same setup was working fine before. The error message itself also looks a bit odd - the path shown doesn't match the actual folder structure.

---
Repository: /testbed
