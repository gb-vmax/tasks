# Bug Report

### Describe the bug

The sitemap generation is producing empty sitemaps. After building my Docusaurus site, the generated `sitemap.xml` file contains no URLs even though I have multiple pages that should be included.

### Reproduction

1. Set up a Docusaurus site with the sitemap plugin enabled
2. Create several pages/docs that should appear in the sitemap
3. Build the site
4. Check the generated `sitemap.xml` file

The sitemap file is generated but contains no route entries.

### Expected behavior

The sitemap should include all non-excluded routes from the site. For example, if I have pages like `/docs/intro`, `/blog`, etc., they should all appear in the sitemap XML with proper URLs.

### Additional context

This seems to have started recently. The sitemap was working fine before and now it's completely empty. I haven't changed my sitemap plugin configuration.

---
Repository: /testbed
