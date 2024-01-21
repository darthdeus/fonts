#!/usr/bin/env fontforge
import fontforge
font = fontforge.open('FantasqueCompact-Regular.ttf')

font.fontname = "FantasqueCompact-Regular"
font.familyname = "Fantasque Compact"
font.fullname = "Fantasque Compact Regular"

new_unique_id = "Fantasquecompact; 2024; Jakub Arnold"

font.appendSFNTName('English (US)', 'UniqueID', new_unique_id)
font.version = "0.1.0"

# Reduce the letter spacing by 10%
for glyph in font.glyphs():
    if glyph.isWorthOutputting():
        glyph.width = int(glyph.width * 0.9)

font.generate('out/FantasqueCompact-Regular.ttf')
font.close()