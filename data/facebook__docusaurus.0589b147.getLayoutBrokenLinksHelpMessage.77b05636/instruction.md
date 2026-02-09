# Bug Report

### Broken links detection showing incorrect frequent links

I'm experiencing an issue with the broken links checker where it's not properly identifying which links are frequently broken across multiple pages.

### Reproduction

When I have broken links scattered across my documentation site, the broken links detection message shows the wrong links in the "frequent broken links" section. Instead of showing the actual broken link URLs that appear multiple times, it seems to be showing page paths or something else entirely.

For example, if I have:
- `/docs/page1` with broken link to `/api/missing`
- `/docs/page2` with broken link to `/api/missing`
- `/docs/page3` with broken link to `/api/missing`
- `/docs/page4` with broken link to `/api/missing`
- `/docs/page5` with broken link to `/api/missing`
- `/docs/page6` with broken link to `/api/missing`

The error message about "frequent broken links" doesn't show `/api/missing` as expected. The detection logic seems broken.

### Expected behavior

When a broken link appears on many pages (5 or more), it should be listed in the "Frequent broken links are linking to:" section of the error message, helping identify links that might be in the layout/navbar/footer.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
