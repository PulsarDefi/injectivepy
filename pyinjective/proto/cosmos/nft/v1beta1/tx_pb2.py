from pyinjective.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/nft/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1b\x63osmos/nft/v1beta1/tx.proto\x12\x12\x63osmos.nft.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\"\xa9\x01\n\x07MsgSend\x12\x19\n\x08\x63lass_id\x18\x01 \x01(\tR\x07\x63lassId\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x30\n\x06sender\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x34\n\x08receiver\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08receiver:\x0b\x82\xe7\xb0*\x06sender\"\x11\n\x0fMsgSendResponse2V\n\x03Msg\x12H\n\x04Send\x12\x1b.cosmos.nft.v1beta1.MsgSend\x1a#.cosmos.nft.v1beta1.MsgSendResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x9f\x01\n\x16\x63om.cosmos.nft.v1beta1B\x07TxProtoP\x01Z\x12\x63osmossdk.io/x/nft\xa2\x02\x03\x43NX\xaa\x02\x12\x43osmos.Nft.V1beta1\xca\x02\x12\x43osmos\\Nft\\V1beta1\xe2\x02\x1e\x43osmos\\Nft\\V1beta1\\GPBMetadata\xea\x02\x14\x43osmos::Nft::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.nft.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.cosmos.nft.v1beta1B\007TxProtoP\001Z\022cosmossdk.io/x/nft\242\002\003CNX\252\002\022Cosmos.Nft.V1beta1\312\002\022Cosmos\\Nft\\V1beta1\342\002\036Cosmos\\Nft\\V1beta1\\GPBMetadata\352\002\024Cosmos::Nft::V1beta1'
  _globals['_MSGSEND'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGSEND'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSEND'].fields_by_name['receiver']._loaded_options = None
  _globals['_MSGSEND'].fields_by_name['receiver']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSEND']._loaded_options = None
  _globals['_MSGSEND']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSEND']._serialized_start=104
  _globals['_MSGSEND']._serialized_end=273
  _globals['_MSGSENDRESPONSE']._serialized_start=275
  _globals['_MSGSENDRESPONSE']._serialized_end=292
  _globals['_MSG']._serialized_start=294
  _globals['_MSG']._serialized_end=380
# @@protoc_insertion_point(module_scope)
