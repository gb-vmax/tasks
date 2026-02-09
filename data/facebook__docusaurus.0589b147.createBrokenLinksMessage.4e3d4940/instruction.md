# Bug Report

### Broken link detection not working properly

I'm experiencing an issue with the broken link checker where it's not correctly identifying broken links and anchors in my documentation.

### Reproduction

When I have a page with broken links, the error messages are showing incorrect information:

1. Links are being labeled as "anchors" and vice versa
2. Single broken links on a page are not being reported at all
3. The error messages only appear when there are multiple broken links on the same page

For example, if I have a markdown file with one broken link like:
```md
[Click here](/non-existent-page)
```

No error is shown during build, even though the link is clearly broken.

But if I have multiple broken links:
```md
[Link 1](/non-existent-page-1)
[Link 2](/non-existent-page-2)
```

Then I get an error, but it says "Broken anchor" instead of "Broken link".

### Expected behavior

- Single broken links should be reported
- The error message should correctly distinguish between broken links and broken anchors
- All broken links should be caught regardless of how many there are on a page

This is making it really hard to catch broken links during the build process since single broken links are silently ignored.

---
Repository: /testbed
