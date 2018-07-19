#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pinyin

# it must be installed pinyin

def to_pinyin(var_str):
    if isinstance(var_str, str):
        if var_str == 'None':
            return ""
        else:
            return pinyin.get(var_str, format='strip', delimiter="")
    else:
        return '类型不对'

