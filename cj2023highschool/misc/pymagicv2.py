#!/usr/bin/env python2
import re
import string

del __builtins__.__import__

_wrestricted = 'bytearray|IndexError|all|help|vars|SyntaxError|unicode|UnicodeDecodeError|linecache|memoryview|isinstance|copyright|NameError|BytesWarning|dict|input|oct|bin|SystemExit|StandardError|format|repr|sorted|False|RuntimeWarning|list|iter|reload|Warning|package|round|dir|cmp|set|bytes|reduce|intern|issubclass|Ellipsis|EOFError|locals|BufferError|slice|FloatingPointError|sum|getattr|abs|exit|print|True|FutureWarning|ImportWarning|None|hash|ReferenceError|len|credits|frozenset|ord|super|TypeError|license|KeyboardInterrupt|UserWarning|filter|range|staticmethod|SystemError|BaseException|pow|RuntimeError|float|MemoryError|StopIteration|globals|divmod|enumerate|apply|LookupError|open|quit|basestring|UnicodeError|zip|hex|long|next|ImportError|chr|xrange|type|Exception|tuple|UnicodeTranslateError|reversed|UnicodeEncodeError|IOError|hasattr|delattr|setattr|raw_input|SyntaxWarning|compile|ArithmeticError|str|property|GeneratorExit|int|import|KeyError|coerce|PendingDeprecationWarning|file|EnvironmentError|unichr|id|OSError|DeprecationWarning|min|UnicodeWarning|exec|execfile|any|complex|bool|ValueError|NotImplemented|map|buffer|max|object|TabError|builtin|callable|ZeroDivisionError|eval|debug|IndentationError|AssertionError|del|classmethod|UnboundLocalError|os|NotImplementedError|AttributeError|OverflowError'
_crestricted = '!"#$%&\'+,-/\\;<>?@][^`|}{()0123456789'
code = raw_input()

if not re.match(r'[^%s]' % re.escape(string.printable), code):
    if re.findall(_wrestricted, code, re.I):
        exit()
    if re.findall('[%s]' % re.escape(_crestricted), code):
        exit()

    try:
        exec(code, {'__builtins__': {}})
    except:
        pass
