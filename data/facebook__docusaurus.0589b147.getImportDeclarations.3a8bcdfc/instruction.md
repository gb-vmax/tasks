# Bug Report

### Describe the bug

I'm encountering an issue with the TOC (Table of Contents) generation in my Docusaurus project. After a recent update, the TOC is not being generated correctly - it appears completely empty even though my MDX files have proper heading structures.

### Reproduction

Create an MDX file with headings and imports:

```mdx
---
title: My Document
---

import SomeComponent from './SomeComponent';

## Section 1
Content here...

## Section 2
More content...

### Subsection 2.1
Nested content...
```

Expected: TOC should display the heading hierarchy
Actual: TOC is empty or not rendered at all

### Additional context

This seems to affect all pages with MDX content. The issue appeared after updating to the latest version. Pages without any imports seem to work fine, but pages with import statements at the top don't generate a TOC properly.

The MDX files parse correctly and the content renders, but the table of contents functionality is broken.

---
Repository: /testbed
