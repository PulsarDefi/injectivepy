# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/channel/v1/channel.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/core/channel/v1/channel.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto\"\xeb\x01\n\x07\x43hannel\x12)\n\x05state\x18\x01 \x01(\x0e\x32\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e\x32\x1a.ibc.core.channel.v1.Order\x12=\n\x0c\x63ounterparty\x18\x03 \x01(\x0b\x32!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x17\n\x0f\x63onnection_hops\x18\x04 \x03(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x18\n\x10upgrade_sequence\x18\x06 \x01(\x04:\x04\x88\xa0\x1f\x00\"\x9a\x02\n\x11IdentifiedChannel\x12)\n\x05state\x18\x01 \x01(\x0e\x32\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e\x32\x1a.ibc.core.channel.v1.Order\x12=\n\x0c\x63ounterparty\x18\x03 \x01(\x0b\x32!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x17\n\x0f\x63onnection_hops\x18\x04 \x03(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x0f\n\x07port_id\x18\x06 \x01(\t\x12\x12\n\nchannel_id\x18\x07 \x01(\t\x12\x18\n\x10upgrade_sequence\x18\x08 \x01(\x04:\x04\x88\xa0\x1f\x00\"9\n\x0c\x43ounterparty\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t:\x04\x88\xa0\x1f\x00\"\xe7\x01\n\x06Packet\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12\x13\n\x0bsource_port\x18\x02 \x01(\t\x12\x16\n\x0esource_channel\x18\x03 \x01(\t\x12\x18\n\x10\x64\x65stination_port\x18\x04 \x01(\t\x12\x1b\n\x13\x64\x65stination_channel\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x38\n\x0etimeout_height\x18\x07 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12\x19\n\x11timeout_timestamp\x18\x08 \x01(\x04:\x04\x88\xa0\x1f\x00\"X\n\x0bPacketState\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c:\x04\x88\xa0\x1f\x00\"G\n\x08PacketId\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04:\x04\x88\xa0\x1f\x00\"@\n\x0f\x41\x63knowledgement\x12\x10\n\x06result\x18\x15 \x01(\x0cH\x00\x12\x0f\n\x05\x65rror\x18\x16 \x01(\tH\x00\x42\n\n\x08response\"N\n\x07Timeout\x12\x30\n\x06height\x18\x01 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\"E\n\x06Params\x12;\n\x0fupgrade_timeout\x18\x01 \x01(\x0b\x32\x1c.ibc.core.channel.v1.TimeoutB\x04\xc8\xde\x1f\x00*\x85\x02\n\x05State\x12\x36\n\x1fSTATE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x11\x8a\x9d \rUNINITIALIZED\x12\x18\n\nSTATE_INIT\x10\x01\x1a\x08\x8a\x9d \x04INIT\x12\x1e\n\rSTATE_TRYOPEN\x10\x02\x1a\x0b\x8a\x9d \x07TRYOPEN\x12\x18\n\nSTATE_OPEN\x10\x03\x1a\x08\x8a\x9d \x04OPEN\x12\x1c\n\x0cSTATE_CLOSED\x10\x04\x1a\n\x8a\x9d \x06\x43LOSED\x12 \n\x0eSTATE_FLUSHING\x10\x05\x1a\x0c\x8a\x9d \x08\x46LUSHING\x12*\n\x13STATE_FLUSHCOMPLETE\x10\x06\x1a\x11\x8a\x9d \rFLUSHCOMPLETE\x1a\x04\x88\xa3\x1e\x00*w\n\x05Order\x12$\n\x16ORDER_NONE_UNSPECIFIED\x10\x00\x1a\x08\x8a\x9d \x04NONE\x12\"\n\x0fORDER_UNORDERED\x10\x01\x1a\r\x8a\x9d \tUNORDERED\x12\x1e\n\rORDER_ORDERED\x10\x02\x1a\x0b\x8a\x9d \x07ORDERED\x1a\x04\x88\xa3\x1e\x00\x42;Z9github.com/cosmos/ibc-go/v8/modules/core/04-channel/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.channel.v1.channel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/cosmos/ibc-go/v8/modules/core/04-channel/types'
  _globals['_STATE']._loaded_options = None
  _globals['_STATE']._serialized_options = b'\210\243\036\000'
  _globals['_STATE'].values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._loaded_options = None
  _globals['_STATE'].values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._serialized_options = b'\212\235 \rUNINITIALIZED'
  _globals['_STATE'].values_by_name["STATE_INIT"]._loaded_options = None
  _globals['_STATE'].values_by_name["STATE_INIT"]._serialized_options = b'\212\235 \004INIT'
  _globals['_STATE'].values_by_name["STATE_TRYOPEN"]._loaded_options = None
  _globals['_STATE'].values_by_name["STATE_TRYOPEN"]._serialized_options = b'\212\235 \007TRYOPEN'
  _globals['_STATE'].values_by_name["STATE_OPEN"]._loaded_options = None
  _globals['_STATE'].values_by_name["STATE_OPEN"]._serialized_options = b'\212\235 \004OPEN'
  _globals['_STATE'].values_by_name["STATE_CLOSED"]._loaded_options = None
  _globals['_STATE'].values_by_name["STATE_CLOSED"]._serialized_options = b'\212\235 \006CLOSED'
  _globals['_STATE'].values_by_name["STATE_FLUSHING"]._loaded_options = None
  _globals['_STATE'].values_by_name["STATE_FLUSHING"]._serialized_options = b'\212\235 \010FLUSHING'
  _globals['_STATE'].values_by_name["STATE_FLUSHCOMPLETE"]._loaded_options = None
  _globals['_STATE'].values_by_name["STATE_FLUSHCOMPLETE"]._serialized_options = b'\212\235 \rFLUSHCOMPLETE'
  _globals['_ORDER']._loaded_options = None
  _globals['_ORDER']._serialized_options = b'\210\243\036\000'
  _globals['_ORDER'].values_by_name["ORDER_NONE_UNSPECIFIED"]._loaded_options = None
  _globals['_ORDER'].values_by_name["ORDER_NONE_UNSPECIFIED"]._serialized_options = b'\212\235 \004NONE'
  _globals['_ORDER'].values_by_name["ORDER_UNORDERED"]._loaded_options = None
  _globals['_ORDER'].values_by_name["ORDER_UNORDERED"]._serialized_options = b'\212\235 \tUNORDERED'
  _globals['_ORDER'].values_by_name["ORDER_ORDERED"]._loaded_options = None
  _globals['_ORDER'].values_by_name["ORDER_ORDERED"]._serialized_options = b'\212\235 \007ORDERED'
  _globals['_CHANNEL'].fields_by_name['counterparty']._loaded_options = None
  _globals['_CHANNEL'].fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _globals['_CHANNEL']._loaded_options = None
  _globals['_CHANNEL']._serialized_options = b'\210\240\037\000'
  _globals['_IDENTIFIEDCHANNEL'].fields_by_name['counterparty']._loaded_options = None
  _globals['_IDENTIFIEDCHANNEL'].fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _globals['_IDENTIFIEDCHANNEL']._loaded_options = None
  _globals['_IDENTIFIEDCHANNEL']._serialized_options = b'\210\240\037\000'
  _globals['_COUNTERPARTY']._loaded_options = None
  _globals['_COUNTERPARTY']._serialized_options = b'\210\240\037\000'
  _globals['_PACKET'].fields_by_name['timeout_height']._loaded_options = None
  _globals['_PACKET'].fields_by_name['timeout_height']._serialized_options = b'\310\336\037\000'
  _globals['_PACKET']._loaded_options = None
  _globals['_PACKET']._serialized_options = b'\210\240\037\000'
  _globals['_PACKETSTATE']._loaded_options = None
  _globals['_PACKETSTATE']._serialized_options = b'\210\240\037\000'
  _globals['_PACKETID']._loaded_options = None
  _globals['_PACKETID']._serialized_options = b'\210\240\037\000'
  _globals['_TIMEOUT'].fields_by_name['height']._loaded_options = None
  _globals['_TIMEOUT'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_PARAMS'].fields_by_name['upgrade_timeout']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['upgrade_timeout']._serialized_options = b'\310\336\037\000'
  _globals['_STATE']._serialized_start=1310
  _globals['_STATE']._serialized_end=1571
  _globals['_ORDER']._serialized_start=1573
  _globals['_ORDER']._serialized_end=1692
  _globals['_CHANNEL']._serialized_start=114
  _globals['_CHANNEL']._serialized_end=349
  _globals['_IDENTIFIEDCHANNEL']._serialized_start=352
  _globals['_IDENTIFIEDCHANNEL']._serialized_end=634
  _globals['_COUNTERPARTY']._serialized_start=636
  _globals['_COUNTERPARTY']._serialized_end=693
  _globals['_PACKET']._serialized_start=696
  _globals['_PACKET']._serialized_end=927
  _globals['_PACKETSTATE']._serialized_start=929
  _globals['_PACKETSTATE']._serialized_end=1017
  _globals['_PACKETID']._serialized_start=1019
  _globals['_PACKETID']._serialized_end=1090
  _globals['_ACKNOWLEDGEMENT']._serialized_start=1092
  _globals['_ACKNOWLEDGEMENT']._serialized_end=1156
  _globals['_TIMEOUT']._serialized_start=1158
  _globals['_TIMEOUT']._serialized_end=1236
  _globals['_PARAMS']._serialized_start=1238
  _globals['_PARAMS']._serialized_end=1307
# @@protoc_insertion_point(module_scope)
