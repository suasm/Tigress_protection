#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_264 = SymVar_0
ref_279 = ref_264 # MOV operation
ref_999818 = ref_279 # MOV operation
ref_1132502 = ref_999818 # MOV operation
ref_1132510 = ((ref_1132502 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1132517 = ref_1132510 # MOV operation
ref_1663259 = ref_279 # MOV operation
ref_1795898 = ref_1663259 # MOV operation
ref_1795906 = (ref_1795898 >> (0x7 & 0x3F)) # SHR operation
ref_1795913 = ref_1795906 # MOV operation
ref_1862242 = ref_1795913 # MOV operation
ref_1862254 = ref_1132517 # MOV operation
ref_1862256 = (ref_1862254 | ref_1862242) # OR operation
ref_1928580 = ref_1862256 # MOV operation
ref_2990128 = ref_1928580 # MOV operation
ref_3122807 = ref_2990128 # MOV operation
ref_3122809 = ((ref_3122807 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_3189138 = ref_3122809 # MOV operation
ref_3189140 = (ref_3189138 & 0x1D5ABF66) # AND operation
ref_3719887 = ref_279 # MOV operation
ref_3852571 = ref_3719887 # MOV operation
ref_3852579 = ((ref_3852571 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_3852586 = ref_3852579 # MOV operation
ref_4383328 = ref_279 # MOV operation
ref_4515967 = ref_4383328 # MOV operation
ref_4515975 = (ref_4515967 >> (0xB & 0x3F)) # SHR operation
ref_4515982 = ref_4515975 # MOV operation
ref_4582311 = ref_4515982 # MOV operation
ref_4582323 = ref_3852586 # MOV operation
ref_4582325 = (ref_4582323 | ref_4582311) # OR operation
ref_4648659 = ref_4582325 # MOV operation
ref_4648671 = ref_3189140 # MOV operation
ref_4648673 = ((ref_4648659 - ref_4648671) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_4648681 = ref_4648673 # MOV operation
ref_4715000 = ref_4648681 # MOV operation
ref_5776526 = ref_279 # MOV operation
ref_5842835 = ref_5776526 # MOV operation
ref_5842849 = ((ref_5842835 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_5842857 = ref_5842849 # MOV operation
ref_5909176 = ref_5842857 # MOV operation
ref_6970724 = ref_1928580 # MOV operation
ref_7037033 = ref_6970724 # MOV operation
ref_7037047 = ((0x20453EE3 + ref_7037033) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7567795 = ref_279 # MOV operation
ref_7634104 = ref_7567795 # MOV operation
ref_7634116 = ref_7037047 # MOV operation
ref_7634118 = ((ref_7634104 - ref_7634116) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7634126 = ref_7634118 # MOV operation
ref_7700445 = ref_7634126 # MOV operation
ref_9425332 = ref_1928580 # MOV operation
ref_10155113 = ref_5909176 # MOV operation
ref_10221422 = ref_10155113 # MOV operation
ref_10221434 = ref_9425332 # MOV operation
ref_10221436 = (ref_10221434 | ref_10221422) # OR operation
ref_10354118 = ref_10221436 # MOV operation
ref_10354124 = (0x3F & ref_10354118) # AND operation
ref_10486833 = ref_10354124 # MOV operation
ref_10486841 = ((ref_10486833 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10486848 = ref_10486841 # MOV operation
ref_11083942 = ref_1928580 # MOV operation
ref_11150251 = ref_11083942 # MOV operation
ref_11150263 = ref_10486848 # MOV operation
ref_11150265 = (ref_11150263 | ref_11150251) # OR operation
ref_11216589 = ref_11150265 # MOV operation
ref_12410816 = ref_4715000 # MOV operation
ref_13074248 = ref_11216589 # MOV operation
ref_13206887 = ref_13074248 # MOV operation
ref_13206895 = (ref_13206887 >> (0x1 & 0x3F)) # SHR operation
ref_13206902 = ref_13206895 # MOV operation
ref_13339579 = ref_13206902 # MOV operation
ref_13339585 = (0xF & ref_13339579) # AND operation
ref_13405919 = ref_13339585 # MOV operation
ref_13405933 = (0x1 | ref_13405919) # OR operation
ref_13538637 = ref_13405933 # MOV operation
ref_13538639 = ((0x40 - ref_13538637) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_13538647 = ref_13538639 # MOV operation
ref_13604993 = ref_12410816 # MOV operation
ref_13604997 = ref_13538647 # MOV operation
ref_13604999 = (ref_13604997 & 0xFFFFFFFF) # MOV operation
ref_13605001 = ((ref_13604993 << ((ref_13604999 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13605008 = ref_13605001 # MOV operation
ref_14135772 = ref_4715000 # MOV operation
ref_14799204 = ref_11216589 # MOV operation
ref_14931843 = ref_14799204 # MOV operation
ref_14931851 = (ref_14931843 >> (0x1 & 0x3F)) # SHR operation
ref_14931858 = ref_14931851 # MOV operation
ref_15064535 = ref_14931858 # MOV operation
ref_15064541 = (0xF & ref_15064535) # AND operation
ref_15130875 = ref_15064541 # MOV operation
ref_15130889 = (0x1 | ref_15130875) # OR operation
ref_15197195 = ref_14135772 # MOV operation
ref_15197199 = ref_15130889 # MOV operation
ref_15197201 = (ref_15197199 & 0xFFFFFFFF) # MOV operation
ref_15197203 = (ref_15197195 >> ((ref_15197201 & 0xFF) & 0x3F)) # SHR operation
ref_15197210 = ref_15197203 # MOV operation
ref_15263539 = ref_15197210 # MOV operation
ref_15263551 = ref_13605008 # MOV operation
ref_15263553 = (ref_15263551 | ref_15263539) # OR operation
ref_15329877 = ref_15263553 # MOV operation
ref_16325067 = ref_7700445 # MOV operation
ref_17054848 = ref_15329877 # MOV operation
ref_17121157 = ref_17054848 # MOV operation
ref_17121169 = ref_16325067 # MOV operation
ref_17121171 = ((ref_17121157 - ref_17121169) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17121179 = ref_17121171 # MOV operation
ref_17187498 = ref_17121179 # MOV operation
ref_19111268 = ref_11216589 # MOV operation
ref_19708370 = ref_4715000 # MOV operation
ref_19841027 = ref_19708370 # MOV operation
ref_19841033 = (0xF & ref_19841027) # AND operation
ref_19907367 = ref_19841033 # MOV operation
ref_19907381 = (0x1 | ref_19907367) # OR operation
ref_20040085 = ref_19907381 # MOV operation
ref_20040087 = ((0x40 - ref_20040085) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_20040095 = ref_20040087 # MOV operation
ref_20106441 = ref_19111268 # MOV operation
ref_20106445 = ref_20040095 # MOV operation
ref_20106447 = (ref_20106445 & 0xFFFFFFFF) # MOV operation
ref_20106449 = ((ref_20106441 << ((ref_20106447 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20106456 = ref_20106449 # MOV operation
ref_20637220 = ref_11216589 # MOV operation
ref_21234322 = ref_4715000 # MOV operation
ref_21366979 = ref_21234322 # MOV operation
ref_21366985 = (0xF & ref_21366979) # AND operation
ref_21433319 = ref_21366985 # MOV operation
ref_21433333 = (0x1 | ref_21433319) # OR operation
ref_21499639 = ref_20637220 # MOV operation
ref_21499643 = ref_21433333 # MOV operation
ref_21499645 = (ref_21499643 & 0xFFFFFFFF) # MOV operation
ref_21499647 = (ref_21499639 >> ((ref_21499645 & 0xFF) & 0x3F)) # SHR operation
ref_21499654 = ref_21499647 # MOV operation
ref_21565983 = ref_21499654 # MOV operation
ref_21565995 = ref_20106456 # MOV operation
ref_21565997 = (ref_21565995 | ref_21565983) # OR operation
ref_22163124 = ref_7700445 # MOV operation
ref_22693868 = ref_17187498 # MOV operation
ref_22760177 = ref_22693868 # MOV operation
ref_22760189 = ref_22163124 # MOV operation
ref_22760191 = (ref_22760189 | ref_22760177) # OR operation
ref_22892855 = ref_22760191 # MOV operation
ref_22892863 = (ref_22892855 >> (0x1 & 0x3F)) # SHR operation
ref_22892870 = ref_22892863 # MOV operation
ref_23025547 = ref_22892870 # MOV operation
ref_23025553 = (0x7 & ref_23025547) # AND operation
ref_23091887 = ref_23025553 # MOV operation
ref_23091901 = (0x1 | ref_23091887) # OR operation
ref_23158252 = ref_21565997 # MOV operation
ref_23158256 = ref_23091901 # MOV operation
ref_23158258 = (ref_23158256 & 0xFFFFFFFF) # MOV operation
ref_23158260 = ((ref_23158252 << ((ref_23158258 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_23158267 = ref_23158260 # MOV operation
ref_23224586 = ref_23158267 # MOV operation
ref_23357218 = ref_23224586 # MOV operation
ref_23357220 = ref_23357218 # MOV operation

print ref_23357220 & 0xffffffffffffffff