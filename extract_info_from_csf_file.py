# https://docs.python.org/3/library/xml.etree.elementtree.html
# 할일 xpath 검토
# https://docs.python.org/ko/3/library/xml.etree.elementtree.html#elementtree-xpath
# https://docs.python.org/ko/3/library/xml.etree.elementtree.html#supported-xpath-syntax

import xml.etree.ElementTree as ET

src_file = './210902.csf'

tree = ET.parse(src_file)
root = tree.getroot()

print(f'-------------')
print(f'modbus memory')
print(f'-------------')
for cMemoryInfo in root.findall('./ModbusMemory//cMemoryInfo'):
    SlaveNum = cMemoryInfo.find('SlaveNum').text
    SlaveUse = cMemoryInfo.find('SlaveUse').text
    if SlaveUse == 'false':
        continue
    SlaveDesc = cMemoryInfo.find('SlaveDesc').text
    print(f'{SlaveNum}, {SlaveUse}, {SlaveDesc}')

print(f'-------------')
print(f'network channel')
print(f'-------------')
for cChannelParameter in root.findall('./NetworkChannel//cChannelParameter'):
    ChannelNum = cChannelParameter.find('ChannelNum').text
    USE = cChannelParameter.find('USE').text
    if USE == 'false':
        continue
    ChannelType = cChannelParameter.find('ChannelType').text
    print(f'{ChannelNum}, {USE}, {ChannelType}')


print(f'-------------')
print(f'process list')
print(f'-------------')
for cCSProcess in root.findall('./ProcessList//cCSProcess'):
    ProcessNum = cCSProcess.find('ProcessNum').text
    ProcessType = cCSProcess.find('ProcessType').text
    if ProcessType == 'IDLE':
        continue
    print(f'{ProcessNum}, {ProcessType}')

print('process end')
