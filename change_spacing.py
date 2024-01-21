#!/usr/bin/env fontforge
import fontforge

src_name_template = "src-font/FantasqueSansMono-Regular.ttf"

out_family_name = "Fantasque Compact"
author = "Jakub Arnold"

for variant in ["Bold", "BoldItalic", "Italic", "Regular"]:
    src_name = src_name_template.replace("Regular", variant)
    out_short_family_name = out_family_name.replace(" ", "")

    print(f"Processing {src_name}")

    font = fontforge.open(src_name)

    font.fontname = f"{out_short_family_name}-{variant}"
    font.familyname = out_family_name
    font.fullname = out_family_name + " " + variant

    new_unique_id = f"{out_short_family_name}; 2024; {author}"

    font.appendSFNTName('English (US)', 'UniqueID', new_unique_id)
    font.version = "0.1.0"

    # Reduce the letter spacing by 10%
    for glyph in font.glyphs():
        if glyph.isWorthOutputting():
            glyph.width = int(glyph.width * 0.9)

    result_path = f"out/{out_short_family_name}-{variant}.ttf"

    print(f"Generating {result_path}")

    font.generate(result_path)
    font.close()