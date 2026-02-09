# Bug Report

### Describe the bug

Anchor links on documentation pages are being incorrectly validated. When navigating to a page with an anchor (like `/docs/intro#getting-started`), the link checker seems to be treating valid anchors as broken links or not validating them properly.

### Reproduction

Create a documentation page with anchors:

```md
# Introduction

## Getting Started

Some content here...

## Installation

More content...
```

Then link to these sections from another page:

```md
Check out the [getting started guide](/docs/intro#getting-started)
```

The anchor links don't seem to be validated correctly - either they're being flagged as broken when they exist, or valid anchors aren't being checked at all.

### Expected behavior

Anchor links should be properly validated:
- Links with valid anchors (like `#getting-started` that exists on the target page) should pass validation
- Links with invalid anchors (like `#nonexistent` that doesn't exist) should be flagged as broken
- Links with empty anchors (like `#`) should be handled appropriately

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
