# Bug Report

### Describe the bug

The blog plugin's reading time calculation is broken. When I build my blog, all posts are showing incorrect reading time estimates - they all show the same value regardless of the actual content length.

### Reproduction

1. Create a blog with multiple posts of different lengths
2. Build the site
3. Check the reading time displayed on each post

All posts show identical reading time estimates instead of calculating based on actual word count.

### Expected behavior

Each blog post should display a reading time estimate based on its actual content length. Longer posts should show longer reading times, shorter posts should show shorter reading times.

### Additional context

This seems to have started recently. The reading time feature was working correctly before and properly calculating estimates based on post content.

---
Repository: /testbed
