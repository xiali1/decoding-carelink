# ./status-quo.sh /dev/ttyUSB0 047006
## cat ./status-quo.sh
```bash
```
## cat logs/explain.log
OUT
## Observations
Wed Aug 21 19:58:32 EDT 2013

## stick

* stick runs appear to be ok

## pump


## downloaded: 1

```
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][0]:data[1024]:
```


## commands session:finished: 10

```
INFO:session:finished executing:ReadBasalTemp:size[64]:data:{'duration': 0, 'rate': 0.0}
INFO:session:finished executing:ReadBatteryStatus:size[64]:data:{'status': 'normal', 'voltage': 1.34}
INFO:session:finished executing:ReadFirmwareVersion:size[64]:data:'VER 1.3B1.1'
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][0]:data[1024]:
INFO:session:finished executing:ReadPumpID:size[64]:data:'047006'
INFO:session:finished executing:ReadPumpModel:size[64]:data:'512'
INFO:session:finished executing:ReadRadioCtrlACL:size[64]:data:['------', '------', '------']
INFO:session:finished executing:ReadRemainingInsulin:size[64]:data:120.8
INFO:session:finished executing:ReadRTC:size[64]:data:'2013-8-21T20:2:14'
INFO:session:finished executing:ReadTotalsToday:size[64]:data:{'yesterday': 6.9, 'today': 9.1}
```

howdy! pump runs were NOT OK

### Last send command

```
INFO:stick:Stick transmit[TransmitPacket:ReadCurPageNumber:pages:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:error::size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):adding segment
INFO:stick:Stick transmit[TransmitPacket:ReadCurPageNumber:pages:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:error::size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):DONE
INFO:commands:XXX: READ cur page number:
0000   0x08                                       .
```
### stats before traceback

```
155:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 231L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 231L, 'errors.crc': 0}
173:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 36L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 35L, 'errors.crc': 0}
174:INFO:__main__:{'radio': {'errors.crc': 0,
175:           'errors.naks': 0,
176:           'errors.sequence': 0,
177:           'errors.timeouts': 0,
178:           'packets.received': 35L,
179:           'packets.transmit': 36L},
180: 'usb': {'errors.crc': 0,
181:         'errors.naks': 0,
182:         'errors.sequence': 0,
183:         'errors.timeouts': 0,
184:         'packets.received': 231L,
185:         'packets.transmit': 231L}}
1216:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 274L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 274L, 'errors.crc': 0}
1234:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 47L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 46L, 'errors.crc': 0}
1235:INFO:__main__:{'radio': {'errors.crc': 0,
1236:           'errors.naks': 0,
1237:           'errors.sequence': 0,
1238:           'errors.timeouts': 0,
```
### Traceback

```
0020   0x00 0x01 0x00 0xf2 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:PowerControl:data:unknown, bytearray(b'\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00"\x00\x00\x00\x0f\x00\x05\x00\x10\x00\x1a\x00\x03\x00\x02\x00\x00\x00\x00\x01\x00\xf2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:__main__:sleeping 17 before download
INFO:__main__:no download required
INFO:__main__:finished executing:PowerControl:data:unknown
INFO:commands:PowerControl:data:unknown:download:done?:found[0] expected[0]
Traceback (most recent call last):
  File "decocare/session.py", line 127, in <module>
    session.power_control( )
  File "decocare/session.py", line 83, in power_control
    log.info('manually download PowerControl serial' % serial)
NameError: global name 'serial' is not defined
Command exited with non-zero status 1
python decocare/session.py /dev/ttyUSB0 047006
	elapsed 0:17.15
	user 0.09
	system 0.02
	CPU 0% (0text+0data 60032max)k
```
```
INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
INFO:link:Link opened serial port: Serial<id=0x17e7150, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.4, xonxoff=False, rtscts=False, dsrdtr=False)
--
INFO:stick:quit send_force_read, found len: 15 expected 64 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 15 True
INFO:stick:readData; raw[retries] 0
INFO:stick:ReadRadio:size:15:eod:found eod (True)
INFO:stick:found packet len(1), link expects(1)
INFO:stick:Stick transmit[TransmitPacket:ReadSettings:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:error::size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):adding segment
INFO:stick:Stick transmit[TransmitPacket:ReadSettings:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:error::size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):DONE
INFO:__main__:READ pump settings:
0000   0x08                                       .
Traceback (most recent call last):
  File "decocare/commands.py", line 646, in <module>
    do_commands(session)
  File "decocare/commands.py", line 591, in do_commands
    device.execute(comm)
  File "/home/sharon/decoding-carelink/decocare/session.py", line 101, in execute
    return super(type(self), self).execute(command)
  File "/home/sharon/decoding-carelink/decocare/session.py", line 39, in execute
    self.download( )
  File "/home/sharon/decoding-carelink/decocare/session.py", line 54, in download
    self.command.respond(data)
  File "decocare/commands.py", line 55, in respond
    self.getData( )
  File "decocare/commands.py", line 465, in getData
    alarm = self.alarm(data[1])
IndexError: bytearray index out of range
--
INFO:stick:quit send_force_read, found len: 15 expected 64 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 15 True
INFO:stick:readData; raw[retries] 0
INFO:stick:ReadRadio:size:15:eod:found eod (True)
INFO:stick:found packet len(1), link expects(1)
INFO:stick:Stick transmit[TransmitPacket:ReadCurPageNumber:pages:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:error::size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):adding segment
INFO:stick:Stick transmit[TransmitPacket:ReadCurPageNumber:pages:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:error::size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):DONE
INFO:commands:XXX: READ cur page number:
0000   0x08                                       .
Traceback (most recent call last):
  File "decocare/download.py", line 87, in <module>
    downloader.download( )
  File "decocare/download.py", line 56, in download
    self.read_current( )
  File "decocare/download.py", line 40, in read_current
    self.device.execute(comm)
  File "/home/sharon/decoding-carelink/decocare/session.py", line 101, in execute
    return super(type(self), self).execute(command)
  File "/home/sharon/decoding-carelink/decocare/session.py", line 39, in execute
    self.download( )
  File "/home/sharon/decoding-carelink/decocare/session.py", line 54, in download
    self.command.respond(data)
  File "/home/sharon/decoding-carelink/decocare/commands.py", line 266, in respond
    self.pages = self.getData( )
  File "/home/sharon/decoding-carelink/decocare/commands.py", line 271, in getData
```
* NO CRC ERROR FOUND
* no nak found
* NOT A CLEAN RUN
