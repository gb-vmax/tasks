# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation where depth-1 headings (h1 tags) are now being included in the TOC. According to the documentation and expected behavior, only h2-h6 headings should appear in the TOC, but h1 headings are now showing up.

### Reproduction

Create an MDX file with the following content:

```markdown
# Main Title

This is the main page title and should not be in the TOC.

## Section 1

Content here

## Section 2

More content

### Subsection 2.1

Details
```

The generated TOC now includes "Main Title" which shouldn't be there.

### Expected behavior

The TOC should only include headings with depth 2 and greater (h2, h3, h4, h5, h6). Depth-1 headings (h1) should be excluded as they typically represent the page title.

The TOC should look like:
- Section 1
- Section 2
  - Subsection 2.1

But instead it's showing:
- Main Title
- Section 1
- Section 2
  - Subsection 2.1

### System Info

- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
