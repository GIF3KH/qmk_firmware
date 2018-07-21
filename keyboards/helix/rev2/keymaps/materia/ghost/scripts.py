#! /usr/bin/python
# -*- coding: utf-8 -*-

# Script.txt to Hex Converter
# MIT License

import sys
import codecs
import re

command = {
'0':'0x00', '1':'0x01', '2':'0x02', '3':'0x03', '4':'0x04', '5':'0x05', '6':'0x06', '7':'0x07',
'8':'0x08', '9':'0x09', 'a':'0x0A', 'b':'0x0B', 'w':'0x0C', 'e':'0x0D'
}

convert = {
'　':'0x10', '、':'0x11', '。':'0x12', '？':'0x13', '！':'0x14', 'ー':'0x15', '・':'0x16',
'ぁ':'0x20', 'あ':'0x21', 'ぃ':'0x22', 'い':'0x23', 'ぅ':'0x24', 'う':'0x25', 'ぇ':'0x26', 'え':'0x27',
'ぉ':'0x28', 'お':'0x29', 'か':'0x2A', 'が':'0x2B', 'き':'0x2C', 'ぎ':'0x2D', 'く':'0x2E', 'ぐ':'0x2F',
'け':'0x30', 'げ':'0x31', 'こ':'0x32', 'ご':'0x33', 'さ':'0x34', 'ざ':'0x35', 'し':'0x36', 'じ':'0x37',
'す':'0x38', 'ず':'0x39', 'せ':'0x3A', 'ぜ':'0x3B', 'そ':'0x3C', 'ぞ':'0x3D', 'た':'0x3E', 'だ':'0x3F',
'ち':'0x40', 'ぢ':'0x41', 'っ':'0x42', 'つ':'0x43', 'づ':'0x44', 'て':'0x45', 'で':'0x46', 'と':'0x47',
'ど':'0x48', 'な':'0x49', 'に':'0x4A', 'ぬ':'0x4B', 'ね':'0x4C', 'の':'0x4D', 'は':'0x4E', 'ば':'0x4F',
'ぱ':'0x50', 'ひ':'0x51', 'び':'0x52', 'ぴ':'0x53', 'ふ':'0x54', 'ぶ':'0x55', 'ぷ':'0x56', 'へ':'0x57',
'べ':'0x58', 'ぺ':'0x59', 'ほ':'0x5A', 'ぼ':'0x5B', 'ぽ':'0x5C', 'ま':'0x5D', 'み':'0x5E', 'む':'0x5F',
'め':'0x60', 'も':'0x61', 'ゃ':'0x62', 'や':'0x63', 'ゅ':'0x64', 'ゆ':'0x65', 'ょ':'0x66', 'よ':'0x67',
'ら':'0x68', 'り':'0x69', 'る':'0x6A', 'れ':'0x6B', 'ろ':'0x6C', 'ゎ':'0x6D', 'わ':'0x6E', 'ゐ':'0x6F',
'ゑ':'0x70', 'を':'0x71', 'ん':'0x72'
}

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
	print ('Usage: $ python %s filename' % argvs[0])
	quit()

fs = codecs.open(argvs[1], 'r', 'utf-8')

count = 0
for line in fs:
  if (line.startswith('#') == True):
    continue

  sys.stdout.write('// ' + line)

  line = line.replace('\\0', '\\a')
  line = line.replace('\\1', '\\b')
  line = line.replace('\\s0', '\\0')
  line = line.replace('\\s1', '\\1')
  line = line.replace('\\s2', '\\2')
  line = line.replace('\\s3', '\\3')
  line = line.replace('\\s4', '\\4')
  line = line.replace('\\s5', '\\5')
  line = line.replace('\\s6', '\\6')
  line = line.replace('\\s7', '\\7')
  line = line.replace('\\s8', '\\8')
  line = line.replace('\\s9', '\\9')

  sys.stdout.write('static uint8_t talk' + "{0:02d}".format(count) + '[] = {\n\t')
  count += 1
  is_command = False
  for char in line:
    if (char == '\r' or char == '\n'):
      sys.stdout.write(char)
    elif (char == '\\'):
      is_command = True
    else:
      if (is_command):
        sys.stdout.write(command[char] + ', ')
        is_command = False
      else:
        sys.stdout.write(convert[char] + ', ')

  sys.stdout.write('};\n')

fs.close()
