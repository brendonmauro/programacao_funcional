#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  my_map.py
#  
#  Copyright 2020 Brendon <Brendon@DESKTOP-IDG37GT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def loop(func, i, old_list):
  new_list = []
  new_list.append(func(old_list[i]))

  if i + 1 < len(old_list):
    new_list += loop(func, i+1, old_list)
  
  return new_list
  

def my_map(func, old_list):
  return loop(func,0, old_list)


def main(args):
	lista = [1,2,3,4,5]
	print(my_map(lambda x: x + 1, lista))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
