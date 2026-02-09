# Bug Report

### Describe the bug

I'm experiencing an issue with the sidebar items generator where the document `id` is being replaced with the document `title`. This causes problems when multiple documents have the same title but different IDs, or when the title contains characters that aren't valid for use as an ID.

### Reproduction

```js
// Document with specific ID and title
const doc = {
  id: 'getting-started',
  title: 'Getting Started Guide',
  frontMatter: {},
  source: '@site/docs/intro.md',
  sourceDirName: '.',
  sidebarPosition: 1
}

// After processing, the id becomes the title instead
// Expected: { id: 'getting-started', title: 'Getting Started Guide', ... }
// Actual: { id: 'Getting Started Guide', title: 'Getting Started Guide', ... }
```

### Expected behavior

The `id` field should retain its original value from the document metadata, not be overwritten with the `title` value. Document IDs are meant to be unique identifiers and shouldn't be replaced with titles which may contain spaces, special characters, or be duplicated across different documents.

### Additional context

This breaks sidebar navigation when:
- Multiple docs have the same title
- Titles contain spaces or special characters
- Code references docs by their ID

The ID should remain as the unique identifier separate from the display title.

---
Repository: /testbed
