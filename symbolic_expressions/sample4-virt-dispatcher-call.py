#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_1644 = SymVar_0
ref_1655 = ref_1644 # MOV operation
ref_1667 = ref_1655 # MOV operation
ref_1669 = ref_1667 # MOV operation
ref_1703 = ((ref_1669 >> 56) & 0xFF) # Byte reference - MOV operation
ref_1704 = ((ref_1669 >> 48) & 0xFF) # Byte reference - MOV operation
ref_1705 = ((ref_1669 >> 40) & 0xFF) # Byte reference - MOV operation
ref_1706 = ((ref_1669 >> 32) & 0xFF) # Byte reference - MOV operation
ref_1707 = ((ref_1669 >> 24) & 0xFF) # Byte reference - MOV operation
ref_1708 = ((ref_1669 >> 16) & 0xFF) # Byte reference - MOV operation
ref_1709 = ((ref_1669 >> 8) & 0xFF) # Byte reference - MOV operation
ref_1710 = (ref_1669 & 0xFF) # Byte reference - MOV operation
ref_14091 = ref_1710 # MOVZX operation
ref_14279 = (ref_14091 & 0xFF) # MOVZX operation
ref_14281 = (ref_14279 & 0xFF) # MOVZX operation
ref_14929 = (ref_14281 & 0xFFFFFFFF) # MOV operation
ref_14931 = (((ref_14929 & 0xFFFFFFFF) + 0x1) & 0xFFFFFFFF) # ADD operation
ref_15788 = (ref_14931 & 0xFFFFFFFF) # MOV operation
ref_15799 = ((((0x0) << 32 | (ref_15788 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_15801 = (ref_15799 & 0xFFFFFFFF) # MOV operation
ref_16021 = (ref_15801 & 0xFFFFFFFF) # MOV operation
ref_16725 = (ref_16021 & 0xFFFFFFFF) # MOV operation
ref_17373 = (ref_16725 & 0xFFFFFFFF) # MOV operation
ref_17375 = (((ref_17373 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_18232 = (ref_17375 & 0xFFFFFFFF) # MOV operation
ref_18243 = ((((0x0) << 32 | (ref_18232 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_18245 = (ref_18243 & 0xFFFFFFFF) # MOV operation
ref_18465 = (ref_18245 & 0xFFFFFFFF) # MOV operation
ref_23688 = ref_1709 # MOVZX operation
ref_23876 = (ref_23688 & 0xFF) # MOVZX operation
ref_23878 = (ref_23876 & 0xFF) # MOVZX operation
ref_24318 = (ref_16021 & 0xFFFFFFFF) # MOV operation
ref_24512 = (ref_24318 & 0xFFFFFFFF) # MOV operation
ref_24526 = (ref_23878 & 0xFFFFFFFF) # MOV operation
ref_24528 = (((ref_24526 & 0xFFFFFFFF) + (ref_24512 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_25385 = (ref_24528 & 0xFFFFFFFF) # MOV operation
ref_25396 = ((((0x0) << 32 | (ref_25385 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_25398 = (ref_25396 & 0xFFFFFFFF) # MOV operation
ref_25618 = (ref_25398 & 0xFFFFFFFF) # MOV operation
ref_26322 = (ref_25618 & 0xFFFFFFFF) # MOV operation
ref_26762 = (ref_18465 & 0xFFFFFFFF) # MOV operation
ref_26956 = (ref_26762 & 0xFFFFFFFF) # MOV operation
ref_26970 = (ref_26322 & 0xFFFFFFFF) # MOV operation
ref_26972 = (((ref_26970 & 0xFFFFFFFF) + (ref_26956 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_27829 = (ref_26972 & 0xFFFFFFFF) # MOV operation
ref_27840 = ((((0x0) << 32 | (ref_27829 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_27842 = (ref_27840 & 0xFFFFFFFF) # MOV operation
ref_28062 = (ref_27842 & 0xFFFFFFFF) # MOV operation
ref_33285 = ref_1708 # MOVZX operation
ref_33473 = (ref_33285 & 0xFF) # MOVZX operation
ref_33475 = (ref_33473 & 0xFF) # MOVZX operation
ref_33915 = (ref_25618 & 0xFFFFFFFF) # MOV operation
ref_34109 = (ref_33915 & 0xFFFFFFFF) # MOV operation
ref_34123 = (ref_33475 & 0xFFFFFFFF) # MOV operation
ref_34125 = (((ref_34123 & 0xFFFFFFFF) + (ref_34109 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_34982 = (ref_34125 & 0xFFFFFFFF) # MOV operation
ref_34993 = ((((0x0) << 32 | (ref_34982 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_34995 = (ref_34993 & 0xFFFFFFFF) # MOV operation
ref_35215 = (ref_34995 & 0xFFFFFFFF) # MOV operation
ref_35919 = (ref_35215 & 0xFFFFFFFF) # MOV operation
ref_36359 = (ref_28062 & 0xFFFFFFFF) # MOV operation
ref_36553 = (ref_36359 & 0xFFFFFFFF) # MOV operation
ref_36567 = (ref_35919 & 0xFFFFFFFF) # MOV operation
ref_36569 = (((ref_36567 & 0xFFFFFFFF) + (ref_36553 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_37426 = (ref_36569 & 0xFFFFFFFF) # MOV operation
ref_37437 = ((((0x0) << 32 | (ref_37426 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_37439 = (ref_37437 & 0xFFFFFFFF) # MOV operation
ref_37659 = (ref_37439 & 0xFFFFFFFF) # MOV operation
ref_42882 = ref_1707 # MOVZX operation
ref_43070 = (ref_42882 & 0xFF) # MOVZX operation
ref_43072 = (ref_43070 & 0xFF) # MOVZX operation
ref_43512 = (ref_35215 & 0xFFFFFFFF) # MOV operation
ref_43706 = (ref_43512 & 0xFFFFFFFF) # MOV operation
ref_43720 = (ref_43072 & 0xFFFFFFFF) # MOV operation
ref_43722 = (((ref_43720 & 0xFFFFFFFF) + (ref_43706 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_44579 = (ref_43722 & 0xFFFFFFFF) # MOV operation
ref_44590 = ((((0x0) << 32 | (ref_44579 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_44592 = (ref_44590 & 0xFFFFFFFF) # MOV operation
ref_44812 = (ref_44592 & 0xFFFFFFFF) # MOV operation
ref_45516 = (ref_44812 & 0xFFFFFFFF) # MOV operation
ref_45956 = (ref_37659 & 0xFFFFFFFF) # MOV operation
ref_46150 = (ref_45956 & 0xFFFFFFFF) # MOV operation
ref_46164 = (ref_45516 & 0xFFFFFFFF) # MOV operation
ref_46166 = (((ref_46164 & 0xFFFFFFFF) + (ref_46150 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_47023 = (ref_46166 & 0xFFFFFFFF) # MOV operation
ref_47034 = ((((0x0) << 32 | (ref_47023 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_47036 = (ref_47034 & 0xFFFFFFFF) # MOV operation
ref_47256 = (ref_47036 & 0xFFFFFFFF) # MOV operation
ref_52479 = ref_1706 # MOVZX operation
ref_52667 = (ref_52479 & 0xFF) # MOVZX operation
ref_52669 = (ref_52667 & 0xFF) # MOVZX operation
ref_53109 = (ref_44812 & 0xFFFFFFFF) # MOV operation
ref_53303 = (ref_53109 & 0xFFFFFFFF) # MOV operation
ref_53317 = (ref_52669 & 0xFFFFFFFF) # MOV operation
ref_53319 = (((ref_53317 & 0xFFFFFFFF) + (ref_53303 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_54176 = (ref_53319 & 0xFFFFFFFF) # MOV operation
ref_54187 = ((((0x0) << 32 | (ref_54176 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_54189 = (ref_54187 & 0xFFFFFFFF) # MOV operation
ref_54409 = (ref_54189 & 0xFFFFFFFF) # MOV operation
ref_55113 = (ref_54409 & 0xFFFFFFFF) # MOV operation
ref_55553 = (ref_47256 & 0xFFFFFFFF) # MOV operation
ref_55747 = (ref_55553 & 0xFFFFFFFF) # MOV operation
ref_55761 = (ref_55113 & 0xFFFFFFFF) # MOV operation
ref_55763 = (((ref_55761 & 0xFFFFFFFF) + (ref_55747 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_56620 = (ref_55763 & 0xFFFFFFFF) # MOV operation
ref_56631 = ((((0x0) << 32 | (ref_56620 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_56633 = (ref_56631 & 0xFFFFFFFF) # MOV operation
ref_56853 = (ref_56633 & 0xFFFFFFFF) # MOV operation
ref_62076 = ref_1705 # MOVZX operation
ref_62264 = (ref_62076 & 0xFF) # MOVZX operation
ref_62266 = (ref_62264 & 0xFF) # MOVZX operation
ref_62706 = (ref_54409 & 0xFFFFFFFF) # MOV operation
ref_62900 = (ref_62706 & 0xFFFFFFFF) # MOV operation
ref_62914 = (ref_62266 & 0xFFFFFFFF) # MOV operation
ref_62916 = (((ref_62914 & 0xFFFFFFFF) + (ref_62900 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_63773 = (ref_62916 & 0xFFFFFFFF) # MOV operation
ref_63784 = ((((0x0) << 32 | (ref_63773 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_63786 = (ref_63784 & 0xFFFFFFFF) # MOV operation
ref_64006 = (ref_63786 & 0xFFFFFFFF) # MOV operation
ref_64710 = (ref_64006 & 0xFFFFFFFF) # MOV operation
ref_65150 = (ref_56853 & 0xFFFFFFFF) # MOV operation
ref_65344 = (ref_65150 & 0xFFFFFFFF) # MOV operation
ref_65358 = (ref_64710 & 0xFFFFFFFF) # MOV operation
ref_65360 = (((ref_65358 & 0xFFFFFFFF) + (ref_65344 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_66217 = (ref_65360 & 0xFFFFFFFF) # MOV operation
ref_66228 = ((((0x0) << 32 | (ref_66217 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_66230 = (ref_66228 & 0xFFFFFFFF) # MOV operation
ref_66450 = (ref_66230 & 0xFFFFFFFF) # MOV operation
ref_71673 = ref_1704 # MOVZX operation
ref_71861 = (ref_71673 & 0xFF) # MOVZX operation
ref_71863 = (ref_71861 & 0xFF) # MOVZX operation
ref_72303 = (ref_64006 & 0xFFFFFFFF) # MOV operation
ref_72497 = (ref_72303 & 0xFFFFFFFF) # MOV operation
ref_72511 = (ref_71863 & 0xFFFFFFFF) # MOV operation
ref_72513 = (((ref_72511 & 0xFFFFFFFF) + (ref_72497 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_73370 = (ref_72513 & 0xFFFFFFFF) # MOV operation
ref_73381 = ((((0x0) << 32 | (ref_73370 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_73383 = (ref_73381 & 0xFFFFFFFF) # MOV operation
ref_73603 = (ref_73383 & 0xFFFFFFFF) # MOV operation
ref_74307 = (ref_73603 & 0xFFFFFFFF) # MOV operation
ref_74747 = (ref_66450 & 0xFFFFFFFF) # MOV operation
ref_74941 = (ref_74747 & 0xFFFFFFFF) # MOV operation
ref_74955 = (ref_74307 & 0xFFFFFFFF) # MOV operation
ref_74957 = (((ref_74955 & 0xFFFFFFFF) + (ref_74941 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_75814 = (ref_74957 & 0xFFFFFFFF) # MOV operation
ref_75825 = ((((0x0) << 32 | (ref_75814 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_75827 = (ref_75825 & 0xFFFFFFFF) # MOV operation
ref_76047 = (ref_75827 & 0xFFFFFFFF) # MOV operation
ref_81270 = ref_1703 # MOVZX operation
ref_81458 = (ref_81270 & 0xFF) # MOVZX operation
ref_81460 = (ref_81458 & 0xFF) # MOVZX operation
ref_81900 = (ref_73603 & 0xFFFFFFFF) # MOV operation
ref_82094 = (ref_81900 & 0xFFFFFFFF) # MOV operation
ref_82108 = (ref_81460 & 0xFFFFFFFF) # MOV operation
ref_82110 = (((ref_82108 & 0xFFFFFFFF) + (ref_82094 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_82967 = (ref_82110 & 0xFFFFFFFF) # MOV operation
ref_82978 = ((((0x0) << 32 | (ref_82967 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_82980 = (ref_82978 & 0xFFFFFFFF) # MOV operation
ref_83200 = (ref_82980 & 0xFFFFFFFF) # MOV operation
ref_83904 = (ref_83200 & 0xFFFFFFFF) # MOV operation
ref_84344 = (ref_76047 & 0xFFFFFFFF) # MOV operation
ref_84538 = (ref_84344 & 0xFFFFFFFF) # MOV operation
ref_84552 = (ref_83904 & 0xFFFFFFFF) # MOV operation
ref_84554 = (((ref_84552 & 0xFFFFFFFF) + (ref_84538 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_85411 = (ref_84554 & 0xFFFFFFFF) # MOV operation
ref_85422 = ((((0x0) << 32 | (ref_85411 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_85424 = (ref_85422 & 0xFFFFFFFF) # MOV operation
ref_85644 = (ref_85424 & 0xFFFFFFFF) # MOV operation
ref_89731 = (ref_85644 & 0xFFFFFFFF) # MOV operation
ref_90163 = (ref_89731 & 0xFFFFFFFF) # MOV operation
ref_90173 = (((ref_90163 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_90180 = (ref_90173 & 0xFFFFFFFF) # MOV operation
ref_90638 = (ref_83200 & 0xFFFFFFFF) # MOV operation
ref_90840 = (ref_90180 & 0xFFFFFFFF) # MOV operation
ref_90846 = (ref_90638 & 0xFFFFFFFF) # MOV operation
ref_90848 = ((ref_90846 & 0xFFFFFFFF) | (ref_90840 & 0xFFFFFFFF)) # OR operation
ref_91073 = (ref_90848 & 0xFFFFFFFF) # MOV operation
ref_91746 = (ref_91073 & 0xFFFFFFFF) # MOV operation
ref_91934 = (ref_91746 & 0xFFFFFFFF) # MOV operation
ref_91974 = (ref_91934 & 0xFFFFFFFF) # MOV operation
ref_91998 = (ref_91974 & 0xFFFFFFFF) # MOV operation
ref_92006 = (ref_91998 & 0xFFFFFFFF) # MOV operation
ref_92008 = (ref_92006 & 0xFFFFFFFF) # MOV operation

print ref_92008 & 0xffffffffffffffff