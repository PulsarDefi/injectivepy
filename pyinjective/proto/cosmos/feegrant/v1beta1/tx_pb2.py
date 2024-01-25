# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/feegrant/v1beta1/tx.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/feegrant/v1beta1/tx.proto\x12\x17\x63osmos.feegrant.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\xec\x01\n\x11MsgGrantAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12R\n\tallowance\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB)\xca\xb4-%cosmos.feegrant.v1beta1.FeeAllowanceI:-\x82\xe7\xb0*\x07granter\x8a\xe7\xb0*\x1c\x63osmos-sdk/MsgGrantAllowance\"\x1b\n\x19MsgGrantAllowanceResponse\"\x9a\x01\n\x12MsgRevokeAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:.\x82\xe7\xb0*\x07granter\x8a\xe7\xb0*\x1d\x63osmos-sdk/MsgRevokeAllowance\"\x1c\n\x1aMsgRevokeAllowanceResponse2\xf3\x01\n\x03Msg\x12p\n\x0eGrantAllowance\x12*.cosmos.feegrant.v1beta1.MsgGrantAllowance\x1a\x32.cosmos.feegrant.v1beta1.MsgGrantAllowanceResponse\x12s\n\x0fRevokeAllowance\x12+.cosmos.feegrant.v1beta1.MsgRevokeAllowance\x1a\x33.cosmos.feegrant.v1beta1.MsgRevokeAllowanceResponse\x1a\x05\x80\xe7\xb0*\x01\x42)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.feegrant.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/cosmos/cosmos-sdk/x/feegrant'
  _globals['_MSGGRANTALLOWANCE'].fields_by_name['granter']._options = None
  _globals['_MSGGRANTALLOWANCE'].fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGGRANTALLOWANCE'].fields_by_name['grantee']._options = None
  _globals['_MSGGRANTALLOWANCE'].fields_by_name['grantee']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGGRANTALLOWANCE'].fields_by_name['allowance']._options = None
  _globals['_MSGGRANTALLOWANCE'].fields_by_name['allowance']._serialized_options = b'\312\264-%cosmos.feegrant.v1beta1.FeeAllowanceI'
  _globals['_MSGGRANTALLOWANCE']._options = None
  _globals['_MSGGRANTALLOWANCE']._serialized_options = b'\202\347\260*\007granter\212\347\260*\034cosmos-sdk/MsgGrantAllowance'
  _globals['_MSGREVOKEALLOWANCE'].fields_by_name['granter']._options = None
  _globals['_MSGREVOKEALLOWANCE'].fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGREVOKEALLOWANCE'].fields_by_name['grantee']._options = None
  _globals['_MSGREVOKEALLOWANCE'].fields_by_name['grantee']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGREVOKEALLOWANCE']._options = None
  _globals['_MSGREVOKEALLOWANCE']._serialized_options = b'\202\347\260*\007granter\212\347\260*\035cosmos-sdk/MsgRevokeAllowance'
  _globals['_MSG']._options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGGRANTALLOWANCE']._serialized_start=160
  _globals['_MSGGRANTALLOWANCE']._serialized_end=396
  _globals['_MSGGRANTALLOWANCERESPONSE']._serialized_start=398
  _globals['_MSGGRANTALLOWANCERESPONSE']._serialized_end=425
  _globals['_MSGREVOKEALLOWANCE']._serialized_start=428
  _globals['_MSGREVOKEALLOWANCE']._serialized_end=582
  _globals['_MSGREVOKEALLOWANCERESPONSE']._serialized_start=584
  _globals['_MSGREVOKEALLOWANCERESPONSE']._serialized_end=612
  _globals['_MSG']._serialized_start=615
  _globals['_MSG']._serialized_end=858
# @@protoc_insertion_point(module_scope)
