#!/usr/bin/env python

from utils.font_utils.font_details import FontDetails

FONT_NAME_CLASS = [
    ('agency','sans_serif'),
    ('arial','sans_serif'),
    ('baiti','foreign'),
    ('bankgothic','sans_serif'),
    ('baskerville','transitional'),
    ('bauhaus','sans_serif'),
    ('bell','transitional'),
    ('berlin','sans_serif'),
    ('bernard','modern'),
    ('bitstreamvera','sans_serif'),
    ('blackadder','script'),
    ('bodoni','modern'),
    ('book','unknown'),
    ('bookman','transitional'),
    ('bradley','script'),
    ('britannic','sans_serif'),
    ('broadway','sans_serif'),
    ('brush','script'),
    ('buxton','hand_writing'),
    ('caard','unknown'),
    ('calibri','sans_serif'),
    ('californian','old_style'),
    ('calisto','old_style'),
    ('cambria','transitional'),
    ('candara','sans_serif'),
    ('castellar','decorative'),
    ('centaur','old_style'),
    ('century','modern'),
    ('chiller','decorative'),
    ('cityblueprint','hand_writing'),
    ('comic','decorative'),
    ('commercialscript','script'),
    ('complex','unknown'),
    ('consolas','sans_serif'),
    ('constantia','transitional'),
    ('cooper','old_style'),
    ('copperplate','sans_serif'),
    ('corbel','sans_serif'),
    ('countryblueprint','hand_writing'),
    ('courier','monospace'),
    ('creditcard','unknown'),
    ('curlz','decorative'),
    ('dutch801','modern'),
    ('e13b','electronic'),
    ('ebrima','sans_serif'),
    ('edwardian','script'),
    ('elephant','modern'),
    ('english','unknown'),
    ('engravers','modern'),
    ('eras','sans_serif'),
    ('euroroman','transitional'),
    ('felix_titling','old_style'),
    ('footlight','modern'),
    ('forte','script'),
    ('franklin','sans_serif'),
    ('freestyle','script'),
    ('french','script'),
    ('gabriola','script'),
    ('gadugi','sans_serif'),
    ('garamond','old_style'),
    ('georgia','transitional'),
    ('gigi','script'),
    ('gill','sans_serif'),
    ('gloucester','modern'),
    ('gothice','gothic'),
    ('goudy','old_style'),
    ('gunplay','stencil'),
    ('haettenschweiler','sans_serif'),
    ('handprint','hand_writing'),
    ('harlow','script'),
    ('harrington','decorative'),
    ('high_tower','old_style'),
    ('himalaya','script'),
    ('impact','sans_serif'),
    ('imprint','decorative'),
    ('informal','unknown'),
    ('isoc','unknown'),
    ('italic','unknown'),
    ('javanese','unknown'),
    ('jokerman','decorative'),
    ('juice','decorative'),
    ('kristen','script'),
    ('kunstler','script'),
    ('leelawadee','sans_serif'),
    ('lucida','sans_serif'),
    ('magneto','hand_writing'),
    ('maiandra','sans_serif'),
    ('matura','script'),
    ('mingliu','foreign'),
    ('mistral','hand_writing'),
    ('modern','unknown'),
    ('money','decorative'),
    ('monospac821','sans_serif'),
    ('monotxt','monospace'),
    ('monotype','sans_serif'),
    ('mv_boli','script'),
    ('myanmar','foreign'),
    ('niagara','modern'),
    ('nina','unknown'),
    ('nirmala','sans_serif'),
    ('numerics','unknown'),
    ('ocra','sans_serif'),
    ('ocrb','monospace'),
    ('onyx','modern'),
    ('palace','script'),
    ('palatino','old_style'),
    ('panroman','unknown'),
    ('papyrus','hand_writing'),
    ('perpetua','transitional'),
    ('phagspa','foreign'),
    ('playbill','modern'),
    ('pmingliu-extb','foreign'),
    ('pristina','script'),
    ('proxy','decorative'),
    ('quicktype','sans_serif'),
    ('rage','decorative'),
    ('ravie','decorative'),
    ('reference','unknown'),
    ('richard','unknown'),
    ('rockwell','monospace'),
    ('roman','old_style'),
    ('romantic','unknown'),
    ('sansserif','sans_serif'),
    ('scriptb','script'),
    ('script','script'),
    ('segoe','sans_serif'),
    ('serif','unknown'),
    ('showcard','decorative'),
    ('simplex','unknown'),
    ('sitka','unknown'),
    ('sketchflow','hand_writing'),
    ('snap','decorative'),
    ('stencil','stencil'),
    ('stylus','script'),
    ('superfrench','old_style'),
    ('swis721','sans_serif'),
    ('sylfaen','unknown'),
    ('tahoma','sans_serif'),
    ('tai','unknown'),
    ('technic','sans_serif'),
    ('tempus','unknown'),
    ('times','transitional'),
    ('trebuchet','sans_serif'),
    ('tw','sans_serif'),
    ('txt','monospace'),
    ('verdana','sans_serif'),
    ('vin','unknown'),
    ('viner','hand_writing'),
    ('vineta','decorative'),
    ('vivaldi','script'),
    ('vladimir','script'),
    ('wide','unknown'),
    ('yi_baiti','unknown')
]

CLASS_LU = {
    'hw' : 'hand_writing',
    'de' : 'decorative',
    'ms' : 'monospace',
    'os' : 'old_style',
    'tr' : 'transitional',
    'sc' : 'script',
    'ss' : 'sans_serif',
    'go' : 'gothic',
    'uk' : 'unknown',
    'st' : 'stencil',
    'el' : 'electronic',
    'mo' : 'modern',
    'fo' : 'foreign'
}

REV_CLASS_LU = {
    'monospace'    : 'ms',
    'modern'       : 'mo',
    'stencil'      : 'st',
    'decorative'   : 'de',
    'electronic'   : 'el',
    'old_style'    : 'os',
    'sans_serif'   : 'ss',
    'hand_writing' : 'hw',
    'gothic'       : 'go',
    'foreign'      : 'fo',
    'script'       : 'sc',
    'unknown'      : 'uk',
    'transitional' : 'tr'
}

def print_uniq_classes(class_list):
    for s in set(class_list):
        print(f'{s.upper()}')

def print_reverse_lu(class_list):
    uc = set(class_list)
    for c in uc:
        lu_k = next(key for key,value in CLASS_LU.items() if value == c)
        print(f'{c.upper():12s} : {lu_k}')

def print_details(uniq_class):
    for uc in uniq_class:
        f_list = [x[0] for x in FONT_NAME_CLASS if x[1] == uc]
        print(f'Font class {uc.upper()} ({len(f_list)})')
        for f in f_list:
            print(f'  {f.upper()}')
            fd = FontDetails(f)
            fd.print_font_variant()

def print_named_tuple(uniq_class, tuple_tag):
    for uc in uniq_class:
        f_list = [x[0] for x in FONT_NAME_CLASS if x[1] == uc]
        for f in f_list:
            fd = FontDetails(f)
            var_list = fd.get_font_variant()
            for v in var_list:
                print(f"{tuple_tag}('{f}','{v}','{uc}','{REV_CLASS_LU[uc]}'),")

def main():
    class_list = [x[1] for x in FONT_NAME_CLASS]
    #print_named_tuple(set(class_list),'FontSelection')
    print_reverse_lu(class_list)
    #print_uniq_classes(class_list)
    #print_details(set(class_list))

if __name__ == '__main__':
    main()
