from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/channel/v1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n!ibc/core/channel/v1/genesis.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/core/channel/v1/channel.proto\"\xb2\x05\n\x0cGenesisState\x12]\n\x08\x63hannels\x18\x01 \x03(\x0b\x32&.ibc.core.channel.v1.IdentifiedChannelB\x19\xc8\xde\x1f\x00\xfa\xde\x1f\x11IdentifiedChannelR\x08\x63hannels\x12R\n\x10\x61\x63knowledgements\x18\x02 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00R\x10\x61\x63knowledgements\x12H\n\x0b\x63ommitments\x18\x03 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00R\x0b\x63ommitments\x12\x42\n\x08receipts\x18\x04 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00R\x08receipts\x12P\n\x0esend_sequences\x18\x05 \x03(\x0b\x32#.ibc.core.channel.v1.PacketSequenceB\x04\xc8\xde\x1f\x00R\rsendSequences\x12P\n\x0erecv_sequences\x18\x06 \x03(\x0b\x32#.ibc.core.channel.v1.PacketSequenceB\x04\xc8\xde\x1f\x00R\rrecvSequences\x12N\n\rack_sequences\x18\x07 \x03(\x0b\x32#.ibc.core.channel.v1.PacketSequenceB\x04\xc8\xde\x1f\x00R\x0c\x61\x63kSequences\x12\x32\n\x15next_channel_sequence\x18\x08 \x01(\x04R\x13nextChannelSequence\x12\x39\n\x06params\x18\t \x01(\x0b\x32\x1b.ibc.core.channel.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\"d\n\x0ePacketSequence\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequenceB\xd1\x01\n\x17\x63om.ibc.core.channel.v1B\x0cGenesisProtoP\x01Z9github.com/cosmos/ibc-go/v8/modules/core/04-channel/types\xa2\x02\x03ICC\xaa\x02\x13Ibc.Core.Channel.V1\xca\x02\x13Ibc\\Core\\Channel\\V1\xe2\x02\x1fIbc\\Core\\Channel\\V1\\GPBMetadata\xea\x02\x16Ibc::Core::Channel::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.channel.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ibc.core.channel.v1B\014GenesisProtoP\001Z9github.com/cosmos/ibc-go/v8/modules/core/04-channel/types\242\002\003ICC\252\002\023Ibc.Core.Channel.V1\312\002\023Ibc\\Core\\Channel\\V1\342\002\037Ibc\\Core\\Channel\\V1\\GPBMetadata\352\002\026Ibc::Core::Channel::V1'
  _globals['_GENESISSTATE'].fields_by_name['channels']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['channels']._serialized_options = b'\310\336\037\000\372\336\037\021IdentifiedChannel'
  _globals['_GENESISSTATE'].fields_by_name['acknowledgements']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['acknowledgements']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['commitments']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['commitments']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['receipts']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['receipts']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['send_sequences']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['send_sequences']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['recv_sequences']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['recv_sequences']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['ack_sequences']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['ack_sequences']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=116
  _globals['_GENESISSTATE']._serialized_end=806
  _globals['_PACKETSEQUENCE']._serialized_start=808
  _globals['_PACKETSEQUENCE']._serialized_end=908
# @@protoc_insertion_point(module_scope)
