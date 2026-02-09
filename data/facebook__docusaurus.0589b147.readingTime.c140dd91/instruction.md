# Bug Report

### Describe the bug

The reading time calculation for blog posts seems to be producing incorrect values. I noticed that the estimated reading time shown on my blog posts doesn't match the actual time it takes to read them.

### Reproduction

I have a blog post with approximately 1200 words of content. The reading time displayed is showing a higher value than expected. When I tested with shorter posts (under 1000 words), the reading time also seems off but in a different way.

Here's what I'm seeing:
- For a post with ~1200 words: reading time is inflated by 1 minute
- For a post with ~800 words: reading time seems to be calculated based on less content than actually exists

### Expected behavior

The reading time should accurately reflect the full content of the blog post. A 1200-word article should show the correct reading time based on all 1200 words, not have an arbitrary +1 minute added.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

Has anyone else noticed this? The reading time calculation used to work fine in previous versions.

---
Repository: /testbed
