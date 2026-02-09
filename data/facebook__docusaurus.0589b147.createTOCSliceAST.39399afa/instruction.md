# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation in my Docusaurus project. After a recent update, the TOC is no longer rendering properly and appears to be broken. The page builds without errors, but the TOC navigation is completely missing or malformed in the output.

### Reproduction

1. Create a markdown file with multiple headings
2. Build the project
3. Check the generated TOC in the browser

Example markdown:
```md
# Main Title

## Section 1
Some content here

## Section 2
More content

### Subsection 2.1
Nested content
```

### Expected behavior

The TOC should display a properly structured navigation tree with all the headings from the markdown file. Each heading should be clickable and link to the corresponding section.

### Actual behavior

The TOC either doesn't appear at all or shows up as malformed/broken structure. It seems like the TOC data isn't being properly exported or the AST generation is creating invalid nodes.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

Any help would be appreciated! This is blocking our documentation updates.

---
Repository: /testbed
