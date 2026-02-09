# Bug Report

### Describe the bug

When using markdown links with hash fragments (anchor links) in MDX files, the hash portion is being stripped from the final URL. Links that should navigate to specific sections on a page are instead just linking to the top of the page.

### Reproduction

Create an MDX file with a link containing a hash fragment:

```md
[Link to section](#my-section)
[Link to another page with anchor](./other-page.md#specific-heading)
```

After processing, the links lose their hash fragments and only point to the base URLs without the anchor.

### Expected behavior

Links with hash fragments should preserve the hash portion in the final output. For example:
- `./other-page.md#specific-heading` should resolve to the correct page with `#specific-heading` intact
- Internal anchor links like `#my-section` should work as expected

This is breaking navigation to specific sections within documentation pages.

### System Info
- Docusaurus version: latest
- MDX loader: @docusaurus/mdx-loader

---
Repository: /testbed
