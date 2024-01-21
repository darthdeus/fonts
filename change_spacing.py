#!/usr/bin/env fontforge
import fontforge
font = fontforge.open('FantasqueCompact-Regular.ttf')

font.fontname = "FantasqueCompact-Regular"
font.familyname = "Fantasque Compact"
font.fullname = "Fantasque Compact Regular"

new_unique_id = "Fantasquecompact; 2024; Jakub Arnold"

font.appendSFNTName('English (US)', 'UniqueID', new_unique_id)
font.version = "0.1.0"

ratio = 0.9

for glyph in font.glyphs():
    glyph.left_side_bearing = int(ratio * float(glyph.left_side_bearing))
    glyph.right_side_bearing = int(ratio * float(glyph.right_side_bearing))


font.generate('out/FantasqueCompact-Regular.ttf')
font.close()