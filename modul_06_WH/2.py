"""test"""
from pathlib import Path


p = Path('/home/alex/Desktop/garbage/Batniki/Eth+Dcr_CT_SN.bat')
pf = Path('/home/alex/Desktop/garbage/Batniki')

print(p.parent)
print(pf.parent)

print('----------------------------')
print(p.parents)
print(pf.parents)

print('----------------------------')
print(p.name)
print(pf.name)

print('----------------------------')
print(p.suffix)
print(pf.suffix)

print('----------------------------')
print(p.exists())
print(pf.sp.is_dir())