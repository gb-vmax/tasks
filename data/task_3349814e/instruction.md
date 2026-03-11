Hi, I'm a localization engineer and I need your help restructuring a translation file so it can be imported into our translation management system.

I have a tab-separated file at `/home/user/translations/export.tsv` that was exported from our database. Each line has four columns:

1. `string_id` — the unique key for the string
2. `context` — a developer note about where the string is used (not needed for import)
3. `source_en` — the original English text
4. `translation_fr` — the French translation

Here's the problem: our translation management system expects an import file with only **three columns** in this exact order: `string_id`, `translation_fr`, `source_en` (note that `translation_fr` and `source_en` are **swapped** compared to the export, and the `context` column is **dropped entirely**).

Please transform `/home/user/translations/export.tsv` into a new file at `/home/user/translations/import_fr.tsv` that:

- Has exactly three tab-separated columns per line: `string_id`, `translation_fr`, `source_en`
- Includes all rows from the original file (including the header row, which should also be restructured to match the new column order)
- Has no trailing whitespace on any line
- Uses Unix line endings (LF only)

The output file should be ready to feed directly into our import pipeline. Let me know if you have any questions!
