# https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

src_file = './210902.csf'

tree = ET.parse(src_file)
root = tree.getroot()

print(f'-------------')
print(f'modbus memory')
print(f'-------------')
for ModbusMemory in root.iter('ModbusMemory'):
    for Memory in ModbusMemory.iter('Memory'):
        for cMemoryInfo in Memory.iter('cMemoryInfo'):
            SlaveNum = cMemoryInfo.find('SlaveNum').text
            SlaveUse = cMemoryInfo.find('SlaveUse').text
            if SlaveUse == 'false':
                continue
            SlaveDesc = cMemoryInfo.find('SlaveDesc').text
            print(f'{SlaveNum}, {SlaveUse}, {SlaveDesc}')

print(f'-------------')
print(f'network channel')
print(f'-------------')
for NetworkChannel in root.iter('NetworkChannel'):
    for ChannelParameter in NetworkChannel.iter('ChannelParameter'):
        for cChannelParameter in ChannelParameter.iter('cChannelParameter'):
            ChannelNum = cChannelParameter.find('ChannelNum').text
            USE = cChannelParameter.find('USE').text
            if USE == 'false':
                continue
            ChannelType = cChannelParameter.find('ChannelType').text
            print(f'{ChannelNum}, {USE}, {ChannelType}')


print(f'-------------')
print(f'process list')
print(f'-------------')
for ProcessList in root.iter('ProcessList'):
    for Process in ProcessList.iter('Process'):
        for cCSProcess in Process.iter('cCSProcess'):
            ProcessNum = cCSProcess.find('ProcessNum').text
            ProcessType = cCSProcess.find('ProcessType').text
            if ProcessType == 'IDLE':
                continue
            print(f'{ProcessNum}, {ProcessType}')

print('process end')
