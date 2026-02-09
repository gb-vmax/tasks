# Bug Report

### Describe the bug

I'm experiencing an issue with heading parsing in MDX files. When I use headings with explicit IDs in my markdown, the heading text is being extracted incorrectly, and in some cases I'm getting errors about undefined values or the wrong content is being displayed.

### Reproduction

Create an MDX file with headings that have explicit IDs:

```markdown
## My Heading {#custom-id}

## Another **bold** heading {#another-id}

## Simple heading
```

The headings with explicit IDs are not being processed correctly. The text extraction seems to be pulling in the wrong nodes, and when there are multiple child nodes (like when using bold/italic syntax), the ID removal logic fails.

### Expected behavior

- Headings with explicit IDs should have the ID properly extracted and removed from the visible text
- The slug should use the custom ID when provided
- Headings with formatting (bold, italic, etc.) should work correctly with custom IDs
- Regular headings without custom IDs should continue to work as before

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently - headings were working fine before but now the ID parsing is behaving strangely.

---
Repository: /testbed
