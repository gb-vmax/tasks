# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where it throws an error saying "has no docs" even though I have a single documentation file in my version folder. The error message claims that at least one doc should exist, but one doc DOES exist and it still fails.

### Reproduction

1. Create a docs version folder with exactly one markdown file
2. Try to build the site
3. Get an error: `Docs version "X" has no docs! At least one doc should exist at "..."`

This seems wrong - if I have one doc file, that should be enough to satisfy the "at least one doc should exist" requirement mentioned in the error message.

### Expected behavior

The build should succeed when there is at least one documentation file present. The error should only be thrown when there are actually zero docs, not when there's exactly one.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
